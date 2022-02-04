from flask import Blueprint, render_template, request, send_file
import psycopg2
import psycopg2.extras
import os


from indexador.extensions import conn
from indexador.settings import IMAGE_PATH
from indexador.settings import ENVIROMENT


main = Blueprint('main', __name__)

""""

# RECID
file001
# FILE
Manual de Electronica Basica.pdf
# FILE_DESCRIPTION
Manual de electronica basica
# TAG
Electronica, libro
# ***

"""


@main.route('/')
def index():
    if ENVIROMENT == 'development-fulllocal':
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    else:
        cursor = conn.cursor()

    # execute sql

    try:
        cursor.execute("SELECT * from ffiles")
        # Fetch result
        row = cursor.fetchone()
        fileArray = []  # listado o array vacio

        while row is not None:
            fileObj = dict()    # diccionario vacio
            fileObj['file'] = row['file']
            fileObj['descripcion'] = row['file_description']
            fileObj['tag'] = row['file_tag']
            fileObj['fileurl'] = row['fileurl']
            fileArray.append(fileObj)
            row = cursor.fetchone()
        return render_template('index.html', filelist=fileArray)
    except (Exception, psycopg2.DatabaseError) as error: 
        print("a ocurrido un error", error) 
        return 'a ocurrido un error en la consulta'
    finally: 
        if conn is not None: 
            conn.close()
         




@main.route('/filter', methods=['POST'])
def filter():
    if ENVIROMENT != 'development-fulllocal':
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    else:
        cursor = conn.cursor()
    # execute sql
    deffilter = request.form['textfilter']
    if ((deffilter == '') or (deffilter == None)):
        deffilter = 'all'
        cursor.execute("SELECT * from ffiles")
    else:
        sqlstr = 'SELECT * FROM ffiles WHERE file_description LIKE '
        # args=[deffilter+'%']
        sqlstr = sqlstr + '\'' +'%'+ deffilter + '%' + '\''
        print(sqlstr)
        cursor.execute(sqlstr)

    # Fetch result
    row = cursor.fetchone()
    fileArray = []  # listado o array vacio

    while row is not None:
        fileObj = dict()    # diccionario vacio
        fileObj['file'] = row['file']
        fileObj['descripcion'] = row['FILE_description']
        fileObj['tag'] = row['FILE_TAG']
        fileObj['fileurl'] = row['fileurl']
        fileArray.append(fileObj)
        row = cursor.fetchone()

    return render_template('index.html', filelist=fileArray)


@main.route('/media/<path:filename>')
def media_file(filename):
    file_path = os.path.join(app.config['MEDIA_DIR'], filename)
    return send_file(file_path)


