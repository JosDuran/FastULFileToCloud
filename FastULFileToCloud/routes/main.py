from flask import Blueprint, render_template, request, send_file
import psycopg2
import psycopg2.extras
import os


from FastULFileToCloud.extensions import getcon
from FastULFileToCloud.settings import MEDIA_DIR
from FastULFileToCloud.settings import ENVIROMENT


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
    aconn = getcon()
    try:
        cursor = aconn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
        cursor.execute("SELECT * from filegen")
        # Fetch result
        row = cursor.fetchone()
        fileArray = []  # listado o array vacio

        while row is not None:
            fileObj = dict()    # diccionario vacio
            fileObj['file'] = row['file']
            fileObj['descripcion'] = row['file_description']
            fileArray.append(fileObj)
            row = cursor.fetchone()
        return render_template('index.html', filelist=fileArray)
    except (Exception, psycopg2.DatabaseError) as error: 
        print("a ocurrido un error", error) 
        return 'a ocurrido un error en la consulta'
    finally: 
        if aconn is not None: 
            aconn.close()
         




@main.route('/filter', methods=['POST'])
def filter():
    aconn = getcon()
    if ENVIROMENT == 'development-fulllocal':
        cursor = aconn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    else:
        cursor = aconn.cursor()
    # execute sql
    deffilter = request.form['textfilter']
    if ((deffilter == '') or (deffilter == None)):
        deffilter = 'all'
        cursor.execute("SELECT * from filegen")
    else:
        sqlstr = 'SELECT * FROM filegen WHERE UPPER(file_description) LIKE '
        # args=[deffilter+'%']
        sqlstr = sqlstr + '\'' +'%'+ deffilter.upper() + '%' + '\'' 

        print(sqlstr)
        cursor.execute(sqlstr)

    # Fetch result
    row = cursor.fetchone()
    fileArray = []  # listado o array vacio

    while row is not None:
        fileObj = dict()    # diccionario vacio
        fileObj['file'] = row['file']
        fileObj['descripcion'] = row['file_description']
        fileObj['pagina'] = row['pagi']
        fileArray.append(fileObj)
        row = cursor.fetchone()

    return render_template('index.html', filelist=fileArray)


@main.route('/media/<path:filename>')
def media_file(filename):
    file_path = os.path.join(MEDIA_DIR, filename)
    return send_file(file_path)


