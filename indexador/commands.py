from telnetlib import theNULL
import click
import psycopg2
import os
from flask.cli import with_appcontext
from .extensions import getcon
from .settings import ENVIROMENT
from .settings import MEDIA_DIR

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

@click.command( name = 'create_database')
@with_appcontext
def create_database():
    aconn = getcon()
    if (ENVIROMENT == 'development') or (ENVIROMENT == 'development-fulllocal'):
        screate = f"CREATE DATABASE docker"
        commands = (
        screate ,
        )
    try:
        cur = aconn.cursor()
        for command in commands:
            if command:
                cur.execute(command) 
        cur.close()
        
        
        aconn.commit() 
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error) 
    finally: 
        if aconn is not None: 
            aconn.close() 

        

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    aconn = getcon()
    if (ENVIROMENT == 'development') or (ENVIROMENT == 'development-fulllocal'):
        screate = ' CREATE TABLE filegen ( RECID  VARCHAR(255) NOT NULL,  FILE VARCHAR(255) NOT NULL,  FILE_DESCRIPTION VARCHAR(255) NOT NULL,' \
                ' PAGI INTEGER NOT NULL CHECK (PAGI >0) )'
    
        commands = (
        screate ,
        )
 
    try:         
         
        cur = aconn.cursor() 
        
        for command in commands:
            if command:
                cur.execute(command) 
        cur.close()
        
        
        aconn.commit() 
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error) 
    finally: 
        if aconn is not None: 
            aconn.close() 


@click.command(name='insert_data')
@with_appcontext
def insert_data():
    fileArray = []  # listado o array vacio
    apath = os.getcwd()
    afullpath = apath + "/indexador/database.MD"
    f = open(afullpath, "r")
  

    """"
    # RECID
    file001
    # FILE
    Manual de Electronica Basica.pdf
    # FILE_DESCRIPTION
    ninguna
    # TAG
    Electronica, libro
    ***

    """
    lista = f.readlines()
    listaobjs = []
    aRecid = ''
    aFile = ''
    aFileDesc = ''
    

    numlineass = len(lista)
    esmult9 = False
    resto = 0
    resto = (numlineass % 9 )
    esmult = (  resto == 0)
    if not esmult:
        raise 'El archivo de entrada debe tener un numero de lineas multiplo de 9'
    
    numiter = ( len(lista) // 9 )

    for i in range(numiter):
        #print( 'elnumero de iteraciones es ', numiter)
        numlinearecid = i*9+1
        linearecid = str(lista[numlinearecid]).strip()
        aRecid = linearecid
        numlineafile = i*9+3
        lineafile = str(lista[numlineafile]).strip()
        aFile = lineafile
        numlineafiledesc = i*9+ +5
        lineafiledesc = str(lista[numlineafiledesc]).strip()
        aFileDesc = lineafiledesc
        numlineapag = i*9+7
        lineanropag = str(lista[numlineapag]).strip()
        aPag = lineanropag

                
        fileobj = dict()
        fileobj['RECID'] = aRecid
        fileobj['FILE'] = aFile
        fileobj['FILE_DESCRIPTION'] = aFileDesc
        fileobj['PAGINA'] = aPag

        aTupla = (aRecid, aFile,aFileDesc,)
        fileobj['TUPLAS'] = aTupla
        listaobjs.append(fileobj)
    print (fileobj.values())
    aconn = getcon()
    aconn.autocommit = True
    listtuples = [(d['RECID'], d['FILE'], d['FILE_DESCRIPTION'], d['PAGINA']) for d in listaobjs]
    print(listtuples)
    try:
        cursor = aconn.cursor()
        query = "INSERT INTO filegen (RECID, FILE, FILE_DESCRIPTION, PAGI ) VALUES(%s,%s,%s,%s)"
        print(query)
        cursor.executemany(query,listtuples)
    finally:
        aconn.commit()           
        aconn.close()
    return 'ok'
        
@click.command(name='empty_table')
@with_appcontext
def empty_table():
    aconn = getcon()
    if (ENVIROMENT == 'development') or (ENVIROMENT == 'development-fulllocal'):
        screate = ' DELETE FROM FILEGEN '
    
        commands = (
        screate ,
        )
 
    try:         
         
        cur = aconn.cursor() 
        
        for command in commands:
            if command:
                cur.execute(command) 
        cur.close()
        
        
        aconn.commit() 
    except (Exception, psycopg2.DatabaseError) as error: 
        print(error) 
    finally: 
        if aconn is not None: 
            aconn.close() 




    