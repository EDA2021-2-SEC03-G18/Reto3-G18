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
    catalog = {'UFOs':lt.newList(),'city_index':None}
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

# Funciones de consulta
def UFOsSize(catalog):
    """
    Número de crimenes
    """
    return lt.size(catalog['UFOs'])


def indexHeight(catalog):
    """
    Altura del arbol
    """
    return om.height(catalog['city_index'])


def indexSize(catalog):
    """
    Numero de elementos en el indice
    """
    return om.size(catalog['city_index'])


def minKey(catalog):
    """
    Llave mas pequena
    """
    return om.minKey(catalog['city_index'])


def maxKey(catalog):
    """
    Llave mas grande
    """
    return om.maxKey(catalog['city_index'])

def getSightingsByCity(catalog, city):
    city_index = catalog['city_index']
    date_index = om.get(city_index,city)['value']
    return om.size(city_index), date_index
        

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

# Funciones de ordenamiento
