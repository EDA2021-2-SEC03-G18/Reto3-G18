"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
assert cf
from prettytable import PrettyTable

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printSightingsByCity(total, city):
    num_cities,date_index = total
    print('Hay un total de',num_cities,'donde se presentaron avistamientos de OVNIs.')
    print('-'*80,'\n')
    sightings = om.size(date_index)
    print('-'*80)
    print('Para la ciudad de',city,'se han presentado un total de',sightings,'avistamientos.\n')
    print('-'*80)

    if sightings > 6:
        dates = om.keySet(date_index)
        first_dates = lt.subList(dates,1,3)
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','country','duration (seconds)','shape']
        for date in lt.iterator(first_dates):
            ufo_list = om.get(date_index,date)['value']
            for ufo_data in lt.iterator(ufo_list):
                imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['country'],
                                ufo_data['duration (seconds)'],ufo_data['shape']])
        
                
                
        last_dates = lt.subList(dates,lt.size(dates)-2,3)
        for date in lt.iterator(last_dates):
            ufo_list = om.get(date_index,date)['value']
            for ufo_data in lt.iterator(ufo_list):
                imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['country'],
                                ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)
    else:
        dates = om.keySet(date_index)
        imprimir= PrettyTable()
        imprimir.field_names=['datetime', 'city','country','duration (seconds)','shape']
        for date in lt.iterator(dates):
            ufo_list = om.get(date_index,date)['value']
            for ufo_data in lt.iterator(ufo_list):
                imprimir.add_row([ ufo_data['datetime'], ufo_data['city'],ufo_data['country'],
                                ufo_data['duration (seconds)'],ufo_data['shape']])
        print(imprimir)


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información en el catálogo")
    print("3- Contar los avistamientos en una ciudad")
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.init_catalog()
    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos de ovnis ....")
        controller.load_UFOs(cont)
        print('Avistamientos de ovnis cargados: ' + str(controller.UFOsSize(cont)))
        input('Presione "Enter" para continuar.')
    elif int(inputs[0]) == 3:
        print("\nBuscando y listando cronológicamente los avistamientos en una ciudad")
        city = input("Nombre de la ciudad a consultar: ")
        controller.create_city_index(cont)
        total = controller.getSightingsByCity(cont, city)
        print('-'*80)
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
        print('-'*80,'\n')
        print('-'*80)
        printSightingsByCity(total, city)
        input('Presione "Enter" para continuar.')

    else:
        sys.exit(0)
sys.exit(0)
