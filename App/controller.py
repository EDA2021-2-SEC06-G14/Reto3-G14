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
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Lama la funcion de Inicialización del modelo
    """
    return model.newCatalog()

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los archivos del CSV en el modelo
    """

    avistamientos = cf.data_dir + "UFOS/UFOS-utf8-small.csv"
    input_file = csv.DictReader(open(avistamientos, encoding = "utf-8"))

    for avistamiento in input_file:
        model.addAvista(catalog, avistamiento)

def reqUno(catalog, ciudad):
    """
    Requerimiento 1
    """
    return model.reqUno(catalog, ciudad)


def reqDos(catalog, inferior, superior):
    """
    Segunda parte requerimiento 2
    """
    return model.reqDos(catalog, inferior, superior)

def reqTres(catalog, inferior, superior):
    """
    Requerimiento 3
    """
    return model.reqTres(catalog, inferior, superior)

def reqCuatro(catalog, inferior, superior):
    """
    Segunda parte requerimiento 4
    """
    return model.reqCuatro(catalog, inferior, superior)

# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def Altura(catalog, mapa):
    return model.Altura(catalog, mapa)

def Size(catalog, mapa):
    return model.Size(catalog, mapa)

def Max(catalog, mapa):
    return model.Max(catalog, mapa)

def Min(catalog, mapa):
    return model.Min(catalog, mapa)
