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
 """

import config as cf
import model
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init_catalog():
    return model.init_catalog()

# Funciones para la carga de datos
def load_UFOs(catalog):
    filename = cf.data_dir + 'UFOS/UFOS-utf8-small.csv'
    input_file = csv.DictReader(open(filename, encoding='utf-8'))
    for ufo_data in input_file:
        model.add_ufo(catalog, ufo_data)

def create_city_index(catalog):
    model.create_city_index(catalog)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def UFOsSize(catalog):
    return model.UFOsSize(catalog)

def indexHeight(catalog):
    return model.indexHeight(catalog)


def indexSize(catalog):
    return model.indexSize(catalog)


def minKey(catalog):
    return model.minKey(catalog)

def maxKey(catalog):
    return model.maxKey(catalog)


def getSightingsByCity(catalog, city):
    return model.getSightingsByCity(catalog, city)