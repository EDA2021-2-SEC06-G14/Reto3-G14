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
    addDuration(catalog, avistamiento)
    addFecha(catalog, avistamiento)

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

def addDuration(catalog, avistamiento):
    """
    Anade un avistamiento en cuanto a su duracion 
    """
    Duration = catalog["Duration"]

    Dura = float(avistamiento["duration (seconds)"])

    existe = om.contains(Duration, Dura)

    if existe:
        sec = om.get(Duration, Dura)
        sec = me.getValue(sec)

    else:
        sec = lt.newList("ARRAY_LIST")
        om.put(Duration, Dura, sec)

    lt.addLast(sec, avistamiento)

def addFecha(catalog, avistamiento):
    """
    Anade un avistamiento en cuanto a su fecha 
    """
    fechas = catalog["Fecha"]

    fecha = datetime.strptime(avistamiento["datetime"][:10], '%Y-%m-%d')

    existe = om.contains(fechas, fecha)

    if existe:
        sec = om.get(fechas, fecha)
        sec = me.getValue(sec)

    else:
        sec = lt.newList("ARRAY_LIST")
        om.put(fechas, fecha, sec)

    lt.addLast(sec, avistamiento)

# Funciones para creacion de datos

def reqUno(catalog, ciudad):

    ciudades = catalog["Ciudad"]

    resp = om.get(ciudades, ciudad)
    resp = me.getValue(resp)
    resp = merge.sort(resp, cmpcronologico)

    return resp


def reqDos(catalog, inferior, superior):
    duracion = catalog["Duration"]
    data = lt.newList("ARRAY_LIST")

    resp = om.values(duracion, inferior, superior)
    resp = lt.iterator(resp)
    for i in resp:
        re = lt.iterator(i)
        for j in re:
            lt.addLast(data, j)

    data = merge.sort(data, cmpduration)

    return data

def reqCuatro(catalog, inferior, superior):
    fechas = catalog["Fecha"]
    data = lt.newList("ARRAY_LIST")

    resp = om.values(fechas, inferior, superior)
    resp = lt.iterator(resp)
    for i in resp:
        re = lt.iterator(i)
        for j in re:
            lt.addLast(data, j)

    data = merge.sort(data, cmpcronologico)

    return data

# Funciones de consulta

def Altura(catalog, mapa):
    return om.height(catalog[mapa])

def Size(catalog, mapa):
    return om.size(catalog[mapa])

def Max(catalog, mapa):
    duracion = catalog[mapa]
    key = om.maxKey(duracion)
    size = lt.size(me.getValue(om.get(duracion, key)))

    return [key, size]

def Min(catalog, mapa):
    fecha = catalog[mapa]
    key = om.minKey(fecha)
    size = lt.size(me.getValue(om.get(fecha, key)))

    return [key, size]

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

def cmpcronologico(avista1, avista2):
    d1 = datetime.strptime(avista1["datetime"], '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime(avista2["datetime"], '%Y-%m-%d %H:%M:%S')
    return (d1<d2)

def cmpduration(avista1, avista2):
    d1 = float(avista1["duration (seconds)"])
    d2 = float(avista2["duration (seconds)"])

    if d1==d2:
        d1 = (avista1["country"] + avista1["city"]).replace(" ","")
        d2 = (avista2["country"] + avista2["city"]).replace(" ","")

    return (d1<d2)

