__author__ = 'Jeannette'

#### conexion a la DB
import psycopg2
import json

datosPanelC1 = {}
datosPanelC2 = {}
datosPanelC3 = {}
datosPanelC4 = {}


def connect():
    conn = psycopg2.connect(" \
        dbname=BotPanelesFotovoltaicos \
        user=postgres \
        password=12345")
    return conn

def consultaB1(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT energia FROM datosPaneles WHERE id = %s', (id, ))
    #datos = cursor.fetchone()
    datos=cursor.fetchall()
    print (datos)
    datosPanelC1['energia'] = datos
    print(datosPanelC1)
    conn.close()
    return datos


def consultaB2(id,fecha):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT energia FROM datosPaneles WHERE id = %s and fecha = %s', (id,fecha ))
    #datos = cursor.fetchone()
    datos=cursor.fetchall()
    print (datos)
    datosPanelC2['energia'] = datos
    print(datosPanelC2)
    conn.close()
    return datos


def consultaB3(id,fechaI, fechaF):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT energia FROM datosPaneles WHERE id = %s and fecha between %s and %s', (id,fechaI, fechaF ))
    #datos = cursor.fetchone()
    datos=cursor.fetchall()
    print (datos)
    datosPanelC3['energia'] = datos
    print(datosPanelC3)
    conn.close()
    return datos

def consultaB4(id,fechaI, fechaF):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT AVG(energia) FROM datosPaneles WHERE id = %s and fecha between %s and %s', (id,fechaI, fechaF ))
    #datos = cursor.fetchone()
    datos=cursor.fetchall()
    print (datos)
    datosPanelC4['energia'] = str(datos)
    json.dumps(datosPanelC4 )
    print(datosPanelC4)
    conn.close()
    return datos

