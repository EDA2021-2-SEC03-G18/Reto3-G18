"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def init_catalog():
    """
    Inicializa el catálogo de informacion sobre UFOs.
    """
    catalog = {'UFOs':lt.newList(),'city_index':None, 'date_index':None, 'coord_index':None, 'time_index':None}
    return catalog
# Funciones para agregar informacion al catalogo
def add_ufo(catalog,ufo_data):
    lt.addLast(catalog['UFOs'],ufo_data)

# Funciones para creacion de datos
def create_city_index(catalog):
    catalog['city_index'] = om.newMap(omaptype='RBT', comparefunction=compareNames)
    city_index = catalog['city_index']
    for ufo_data in lt.iterator(catalog['UFOs']):
        city_info = ufo_data['city']
        date_info = ufo_data['datetime']
        if om.contains(city_index,city_info):
            date_index = om.get(city_index,city_info)['value']
            if om.contains(date_index,date_info):
                list_UFOs = om.get(date_index,date_info)['value'] 
                lt.addLast(list_UFOs, ufo_data)
            else:
                list_UFOs = lt.newList()
                lt.addLast(list_UFOs,ufo_data)
                om.put(date_index,date_info,list_UFOs)
        else:
            date_index = om.newMap(omaptype='RBT', comparefunction=compareDates)
            list_UFOs = lt.newList()
            lt.addLast(list_UFOs,ufo_data)
            om.put(date_index,date_info,list_UFOs)
            om.put(city_index,city_info,date_index)

def create_time_index(catalog):
    catalog['time_index'] = om.newMap(omaptype='RBT', comparefunction=compareTime)
    time_index = catalog['time_index']
    for ufo_data in lt.iterator(catalog['UFOs']):
        time_info = ufo_data['datetime'][11:19]
        date_info = ufo_data['datetime'][0:10]
        if om.contains(time_index,time_info):
            date_index = om.get(time_index,time_info)['value']
            if om.contains(date_index,date_info):
                list_UFOs = om.get(date_index,date_info)['value'] 
                lt.addLast(list_UFOs, ufo_data)
            else:
                list_UFOs = lt.newList()
                lt.addLast(list_UFOs,ufo_data)
                om.put(date_index,date_info,list_UFOs)
        else:
            date_index = om.newMap(omaptype='RBT', comparefunction=compareTime)
            list_UFOs = lt.newList()
            lt.addLast(list_UFOs,ufo_data)
            om.put(date_index,date_info,list_UFOs)
            om.put(time_index,time_info,date_index)

def create_date_index(catalog):
    catalog['date_index'] = om.newMap(omaptype='RBT', comparefunction=compareDates)
    date_index = catalog['date_index']
    for ufo_data in lt.iterator(catalog['UFOs']):
        date_info = ufo_data['datetime']
        if om.contains(date_index,date_info):
            list_UFOs = om.get(date_index,date_info)['value'] 
            lt.addLast(list_UFOs, ufo_data)
        else:
            list_UFOs = lt.newList()
            lt.addLast(list_UFOs,ufo_data)
            om.put(date_index,date_info,list_UFOs)

def create_coord_index(catalog):
    catalog['coord_index'] = om.newMap(omaptype='RBT', comparefunction=compareCoord)
    coord_index = catalog['coord_index']
    for ufo_data in lt.iterator(catalog['UFOs']):
        latitude_info = str(round(float(ufo_data['latitude']),2))
        longitude_info = str(round(float(ufo_data['longitude']),2))
        if om.contains(coord_index,latitude_info):
            longitude_index = om.get(coord_index,latitude_info)['value']
            if om.contains(longitude_index,longitude_info):
                list_UFOs = om.get(longitude_index,longitude_info)['value'] 
                lt.addLast(list_UFOs, ufo_data)
            else:
                list_UFOs = lt.newList()
                lt.addLast(list_UFOs,ufo_data)
                om.put(longitude_index,longitude_info,list_UFOs)
        else:
            longitude_index = om.newMap(omaptype='RBT', comparefunction=compareCoord)
            list_UFOs = lt.newList()
            lt.addLast(list_UFOs,ufo_data)
            om.put(longitude_index,longitude_info,list_UFOs)
            om.put(coord_index,latitude_info,longitude_index)

# Funciones de consulta
def UFOsSize(catalog):
    """
    Número de crimenes
    """
    return lt.size(catalog['UFOs'])


def indexHeight(catalog,index):
    """
    Altura del arbol
    """
    return om.height(catalog[index])


def indexSize(catalog,index):
    """
    Numero de elementos en el indice
    """
    return om.size(catalog[index])


def minKey(catalog,index):
    """
    Llave mas pequena
    """
    return om.minKey(catalog[index])


def maxKey(catalog,index):
    """
    Llave mas grande
    """
    return om.maxKey(catalog[index])

def getSightingsByCity(catalog, city):
    city_index = catalog['city_index']
    date_index = om.get(city_index,city)['value']
    return om.size(city_index), date_index

def getSightingsByTime(catalog,time_min,time_max):
    time_index = catalog['time_index']
    ufo_list = lt.newList()
    latest_time = om.maxKey(time_index)
    latest_dates = om.get(time_index,latest_time)['value']
    latest_sightings = 0
    for date in lt.iterator(om.keySet(latest_dates)):
        latest_sightings += lt.size(om.get(latest_dates,date))
    keys_time = om.keys(time_index,time_min,time_max)
    for key_time in lt.iterator(keys_time):
        date_index = om.get(time_index,key_time)['value']
        for key_date in lt.iterator(om.keySet(date_index)):
            ufo_info = om.get(date_index,key_date)['value']
            for ufo in lt.iterator(ufo_info):
                lt.addLast(ufo_list,ufo)
    return latest_time, latest_sightings, ufo_list

def getSightingsByDate(catalog,initial_date,final_date):
    date_index = catalog['date_index']
    dates = lt.newList()
    keyMax = om.floor(date_index,final_date)
    final_dates = om.get(date_index,keyMax)['value']
    for date_list in lt.iterator(om.values(date_index,initial_date,final_date)):
        for date_info in lt.iterator(date_list):
            lt.addLast(dates,date_info)
    return dates, final_dates


def getSightingsByGeography(catalog,longitude_min,longitude_max,latitude_min,latitude_max):
    coord_index = catalog['coord_index']
    ufo_list = lt.newList()
    keys_latitude = om.keys(coord_index,latitude_min,latitude_max)
    for key_latitude in lt.iterator(keys_latitude):
        latitude_index = om.get(coord_index,key_latitude)['value']
        keys_longitude = om.keys(latitude_index,longitude_min,longitude_max)
        for key_longitude in lt.iterator(keys_longitude):
            ufo_info = om.get(latitude_index,key_longitude)['value']
            for ufo in lt.iterator(ufo_info):
                lt.addLast(ufo_list,ufo)
    return ufo_list


# Funciones utilizadas para comparar elementos dentro de una lista
def compareNames(name1, name2):
    """
    Compara dos fechas
    """
    if (name1 == name2):
        return 0
    elif (name1 > name2):
        return 1
    else:
        return -1

def compareTime(time1, time2):
    """
    Compara dos coordenadas
    """
    if (time1 == time2):
        return 0
    elif (time1 > time2):
        return 1
    else:
        return -1

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compareCoord(coord1, coord2):
    """
    Compara dos coordenadas
    """
    if (coord1 == coord2):
        return 0
    elif (coord1 > coord2):
        return 1
    else:
        return -1

# Funciones de ordenamiento
