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
from datetime import datetime
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inizializa el modelo

    crea una lista vacia para guardad los avistamientos y se crean mapas
    (RBT) con los siguientes criterios:

        - Ciudad de avistamiento (city)
        - Duracion del avistamiento (duration (seconds))
        - Hora/Minuto del avistamiento (datetime)
        - Fecha del avistamiento (datetime)
        - Zona geografica del avistamiento (latitude, longitude)

    Retorna el analizador

    """

    catalog = {"Avistamientos": None,
               "Ciudad": None,
               "Duration": None,
               "HoraMin": None,
               "Fecha": None,
               "Zona": None}

    catalog["Avistamientos"] = lt.newList("ARRAY_LIST")
    catalog["Ciudad"] = om.newMap(omaptype= "RBT")
    catalog["Duration"] = om.newMap(omaptype= "RBT")
    catalog["HoraMin"] = om.newMap(omaptype= "RBT")
    catalog["Fecha"] = om.newMap(omaptype= "RBT")
    catalog["Zona"] = om.newMap(omaptype= "RBT")

    return catalog

# Funciones para agregar informacion al catalogo

def addAvista(catalog, avistamiento):
    """
    Carga los datos al catalogo
    """
    lt.addLast(catalog["Avistamientos"], avistamiento)
    addCity(catalog, avistamiento)

def addCity(catalog, avistamiento):
    """
    Anade una ciudad al mapa si no existe ya 
    """
    ciudades = catalog["Ciudad"]

    city = avistamiento["city"]

    existe = om.contains(ciudades,city)

    if existe:
        ci = om.get(ciudades, city)
        ci = me.getValue(ci)

    else:
        ci = lt.newList("ARRAY_LIST")
        om.put(ciudades, city, ci)

    lt.addLast(ci, avistamiento)

# Funciones para creacion de datos

def reqUno(catalog, ciudad):

    ciudades = catalog["Ciudad"]

    resp = om.get(ciudades, ciudad)
    resp = me.getValue(resp)
    resp = merge.sort(resp, cmpcronologico)

    return resp

# Funciones de consulta

def Altura(catalog, mapa):
    return om.height(catalog[mapa])

def Size(catalog, mapa):
    return om.size(catalog[mapa])

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def cmpcronologico(avista1, avista2):
    d1 = datetime.strptime(avista1["datetime"], '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime(avista2["datetime"], '%Y-%m-%d %H:%M:%S')
    return (d1<d2)

