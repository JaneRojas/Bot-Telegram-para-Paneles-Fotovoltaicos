__author__ = 'Jeannette'
import sys
import time
import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent

import datetime
#from datetime import datetime, date, time, timedelta  #operaciones con hora y tiempo
#from datetime import datetime, date, time, timedelta
#import calendar
import datetime

import conexion
from conexion import consultaB1, consultaB2, consultaB3, consultaB4
from conexion import datosPanelC1, datosPanelC2, datosPanelC3, datosPanelC4



#menu principal
def menuPrincipal(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print("Menu principal")

    markup = ReplyKeyboardMarkup(keyboard=[
            ['Energia producida por un panel'],
            ['Energia producida por panel por fecha'],
            ['Energia producida por panel por rango de fecha'],
            ['Promedio de la energia producida por panel por rango de fecha']
             ])

    bot.sendMessage(chat_id, 'Seleccione la opción deseada', reply_markup=markup)

    ##consulta 1
    if msg['text'] == 'Panel 1':
        bot.sendMessage(chat_id, 'Los datos del panel son:')
        consultaB1(1)
        imprimir(datosPanelC1.values(),msg)
    if msg['text'] == 'Panel 2':
        bot.sendMessage(chat_id, 'Los datos del panel son:')
        consultaB1(2)
        imprimir(datosPanelC1.values(),msg)
    if msg['text'] == 'Panel 3':
        bot.sendMessage(chat_id, 'Los datos del panel son:')
        consultaB1(3)
        imprimir(datosPanelC1.values(),msg)
    if msg['text'] == 'Panel 4':
        bot.sendMessage(chat_id, 'Los datos del panel son:')
        consultaB1(4)
        imprimir(datosPanelC1.values(),msg)

    ##consulta2
    if msg['text'] == 'Panel F.1':
        bot.sendMessage(chat_id, 'La energia producida del panel el dia: xx es: ')
        consultaB2(1, '2017-03-23')
        imprimir(datosPanelC2.values(),msg)
    if msg['text'] == 'Panel F.2':
        bot.sendMessage(chat_id, 'La energia producida del panel el dia: xx es: ')
        consultaB2(2, '2017-03-23')
        imprimir(datosPanelC2.values(),msg)
    if msg['text'] == 'Panel F.3':
        bot.sendMessage(chat_id, 'La energia producida del panel el dia: xx es: ')
        consultaB2(3, '2017-03-23')
        imprimir(datosPanelC2.values(),msg)
    if msg['text'] == 'Panel F.4':
        bot.sendMessage(chat_id, 'La energia producida del panel el dia: xx es: ')
        consultaB2(4, '2017-03-23')
        imprimir(datosPanelC2.values(),msg)

    ##consulta3
    if msg['text'] == 'Panel F 1':
        bot.sendMessage(chat_id, 'La energia producida del panel desde el inicio hasta la fecha actual: ')
        consultaB3(1, '2017-03-21',time.strftime('%d %b %y'))
        imprimir(datosPanelC3.values(),msg)
    if msg['text'] == 'Panel F 2':
        bot.sendMessage(chat_id, 'La energia producida del panel desde el inicio hasta la fecha actual: ')
        consultaB3(2, '2017-03-21',time.strftime('%d %b %y'))
        imprimir(datosPanelC3.values(),msg)
    if msg['text'] == 'Panel F 3':
        bot.sendMessage(chat_id, 'La energia producida del panel desde el inicio hasta la fecha actual: ')
        consultaB3(3, '2017-03-21',time.strftime('%d %b %y'))
        imprimir(datosPanelC3.values(),msg)
    if msg['text'] == 'Panel F 4':
        bot.sendMessage(chat_id, 'La energia producida del panel desde el inicio hasta la fecha actual: ')
        consultaB3(4, '2017-03-21',time.strftime('%d %b %y'))
        imprimir(datosPanelC3.values(),msg)

    ##consulta4
    if msg['text'] == 'Panel F - 1':
        bot.sendMessage(chat_id, 'El promedio de energia producida del panel desde el inicio hasta la fecha actual: ')
        consultaB4(1, '2017-03-21',time.strftime('%d %b %y'))
        imprimir(datosPanelC4.values(),msg)
    if msg['text'] == 'Panel F - 2':
        bot.sendMessage(chat_id, 'El promedio de energia producida del panel desde el inicio hasta la fecha actual: ')
        consultaB4(2, '2017-03-21',time.strftime('%d %b %y'))
        imprimir(datosPanelC4.values(),msg)
    if msg['text'] == 'Panel F - 3':
        bot.sendMessage(chat_id, 'El promedio de energia producida del panel desde el inicio hasta la fecha actual: ')
        consultaB4(3, '2017-03-21',time.strftime('%d %b %y'))
        imprimir(datosPanelC4.values(),msg)
    if msg['text'] == 'Panel F - 4':
        bot.sendMessage(chat_id, 'El promedio de energia producida del panel desde el inicio hasta la fecha actual: ')
        consultaB4(4, '2017-03-21',time.strftime('%d %b %y'))
        imprimir(datosPanelC4.values(),msg)


    ##opciones de menu principal
    if msg['text'] == 'Energia producida por un panel':
        consulta1(msg)

    if msg['text'] == 'Energia producida por panel por fecha':
        consulta2(msg)

    if msg['text'] == 'Energia producida por panel por rango de fecha':
        consulta3(msg)

    if msg['text'] == 'Promedio de la energia producida por panel por rango de fecha':
        consulta4(msg)


#subs menus de consultas
def consulta1(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id,"- " + msg['text'] + " -")
    markupConsulta1 = ReplyKeyboardMarkup(keyboard=[
            ['Panel 1'],
            ['Panel 2'],
            ['Panel 3'],
            ['Panel 4']
             ])

    bot.sendMessage(chat_id, 'Seleccione el id del panel fotovoltaico', reply_markup=markupConsulta1)

def consulta2(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id,"- " + msg['text'] + " -")
    markupConsulta2 = ReplyKeyboardMarkup(keyboard=[
            ['Panel F.1'],
            ['Panel F.2'],
            ['Panel F.3'],
            ['Panel F.4']
             ])

    bot.sendMessage(chat_id, 'Seleccione el id del panel fotovoltaico', reply_markup=markupConsulta2)

def consulta3(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id,"- " + msg['text'] + " -")
    markupConsulta3 = ReplyKeyboardMarkup(keyboard=[
            ['Panel F 1'],
            ['Panel F 2'],
            ['Panel F 3'],
            ['Panel F 4']
             ])

    bot.sendMessage(chat_id, 'Seleccione el id del panel fotovoltaico', reply_markup=markupConsulta3)

def consulta4(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id,"- " + msg['text'] + " -")
    markupConsulta4 = ReplyKeyboardMarkup(keyboard=[
            ['Panel F - 1'],
            ['Panel F - 2'],
            ['Panel F - 3'],
            ['Panel F - 4']
             ])

    bot.sendMessage(chat_id, 'Seleccione el id del panel fotovoltaico', reply_markup=markupConsulta4)


#metodo para imprimir datos
def imprimir(lista, msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    for element in lista:
        bot.sendMessage(chat_id, element)


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(telepot.glance(msg))
    print(content_type, chat_type, chat_id)
    print("----")
    print(msg)
    print("----")


#restringe comandos enviados

    informacionEmisor = msg['from'] #diccionario que contiene informacion personal del emisor
    emisor= informacionEmisor['first_name'] #nombre de quien envia el mensaje

    if (content_type == 'text'):
        command = msg['text']
        print('Got command: %s' % command)
        menuPrincipal(msg)

    if (content_type == 'audio'):
        print('Got AUDIO: ')

        bot.sendMessage(chat_id, "Lo sentimos "+ emisor + " aun no implementamos el servicio de AUDIO. Si tienes alguna idea de como "
                                                 "implementar el servicio podes escribirnos y hacer la recomendación")

    if (content_type == 'voice'):
        print('Got voice: ')

        bot.sendMessage(chat_id, "Lo sentimos "+ emisor + " aun no implementamos el servicio de VOZ. Si tienes una idea de como "
                                                 "implementar el servicio podes escribirnos y hacer la recomendación")


    #agregar otras restricciones a comandos enviados




#token
bot = telepot.Bot('478316324:AAF1TBgzsBDXyyjeH0UQs35OoD0gW_zm_IQ')
bot.message_loop(handle)
print ('Listening ...')


if (time.strftime("%H:%M") ==  "18:05"):
    print("hola mundo")

    #time.strftime('%d %b %y')


# Keep the program running.
while 1:
    time.sleep(10)