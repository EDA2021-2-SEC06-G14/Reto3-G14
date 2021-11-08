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
import folium
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
               "Zona": None,
               "Longitud": None}

    catalog["Avistamientos"] = lt.newList("ARRAY_LIST")
    catalog["Ciudad"] = om.newMap(omaptype= "RBT")
    catalog["Duration"] = om.newMap(omaptype= "RBT")
    catalog["HoraMin"] = om.newMap(omaptype= "RBT")
    catalog["Fecha"] = om.newMap(omaptype= "RBT")
    catalog["Hora"] = om.newMap(omaptype= "RBT")
    catalog["Longitud"] = om.newMap(omaptype= "RBT")

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
    addHora(catalog, avistamiento)
    addLongitud(catalog, avistamiento)

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

def addLongitud(catalog, avistamiento):
    """
    Anade una longitud al mapa si no existe ya 
    """
    longitudes = catalog["Longitud"]

    longitud = float(avistamiento["longitude"])
    latitud = float(avistamiento["latitude"])

    existe = om.contains(longitudes,longitud)

    if existe:
        lon = om.get(longitudes, longitud)
        lon = me.getValue(lon)
        existex2=om.contains(lon,latitud)
        if existex2:
            lat = om.get(lon,latitud)
            lat = me.getValue(lat)
        else:
            lat=lt.newList("ARRAY_LIST")
            om.put(lon,latitud,lat)

        lt.addLast(lat,avistamiento)

    else:
        lon = om.newMap(omaptype= "RBT")
        lat=lt.newList("ARRAY_LIST")
        lt.addLast(lat,avistamiento)
        om.put(lon, latitud,lat)
        om.put(longitudes, longitud, lon)

    #lt.addLast(ci, avistamiento)

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

def addHora(catalog, avistamiento):
    """
    Anade un avistamiento en cuanto a su hora 
    """
    horas = catalog["Hora"]

    hora = datetime.strptime(avistamiento["datetime"][11:], '%H:%M:%S')

    existe = om.contains(horas, hora)

    if existe:
        sec = om.get(horas, hora)
        sec = me.getValue(sec)

    else:
        sec = lt.newList("ARRAY_LIST")
        om.put(horas, hora, sec)

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

def reqTres(catalog, inferior, superior):
    horas = catalog["Hora"]
    primerprint=om.size(horas)
    rta = lt.newList("ARRAY_LIST")
    rtamin=lt.newList("ARRAY_LIST")
    #inf=inferior+":00"
    #sup=superior+":00"
    resp = om.values(horas, inferior, superior)
    resp = lt.iterator(resp)
    minimo= om.maxKey(horas)
    minimos= om.get(horas, minimo)
    conteo= me.getValue(minimos)
    conteoo=lt.size(conteo)
    elemento={"time":minimo, "conteo":conteoo}
    lt.addLast(rtamin, elemento)
    for i in resp:
        re = lt.iterator(i)
        for j in re:
            lt.addLast(rta, j)

    rta = merge.sort(rta, cmpcronolotemp)
    return rta, rtamin,primerprint


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


def reqCin(catalog, loninferior, lonsuperior,latinferior,latsuperior):
    longitudes = catalog["Longitud"]
    rta = lt.newList("ARRAY_LIST")

    resp = om.values(longitudes, loninferior, lonsuperior)
    resp = lt.iterator(resp)
    for i in resp:
        respuesta= om.values(i,latinferior,latsuperior)
        respuesta = lt.iterator(respuesta)
        for j in respuesta:
            re = lt.iterator(j)
            for k in re:
                lt.addLast(rta,k)

    rta = merge.sort(rta, cmplatitud)
    return rta

def reqSeis(catalog, loninferior, lonsuperior, latinferior, latsuperior):
    avista = reqCin(catalog, loninferior, lonsuperior,latinferior,latsuperior)

    avistamientos = lt.iterator(avista)
 
    m = folium.Map(location=[(latinferior+latsuperior)/2, (loninferior+lonsuperior)/2], tiles="Stamen Terrain", zoom_start=7)

    for i in avistamientos:

        latitud = i["latitude"]
        longitud = i["longitude"]


        iframe = folium.IFrame("Duracion: " + str(i["duration (seconds)"]) + "\n"+ 
                            "Fecha: " + str(i["datetime"]) + "\n"
                            "Forma: " + str(i["shape"]))
        popup = folium.Popup(iframe,
                     min_width=150,
                     max_width=150)

        folium.Marker(location=[latitud, longitud],
                      popup=popup,
                      icon=folium.Icon(color="blue")
        ).add_to(m)

    m.save("mapa_avistamientos.html")

    return avista
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

def cmpcronolotemp(avista1, avista2):
    d1 = datetime.strptime(avista1["datetime"][11:], '%H:%M:%S')
    d2 = datetime.strptime(avista2["datetime"][11:], '%H:%M:%S')
    if d1==d2:
        d3 = datetime.strptime(avista1["datetime"], '%Y-%m-%d %H:%M:%S')
        d4 = datetime.strptime(avista2["datetime"], '%Y-%m-%d %H:%M:%S')
        return (d3<d4) 
    else:
        return (d1<d2)

def cmpduration(avista1, avista2):
    d1 = float(avista1["duration (seconds)"])
    d2 = float(avista2["duration (seconds)"])

    if d1==d2:
        d1 = (avista1["country"] + avista1["city"]).replace(" ","")
        d2 = (avista2["country"] + avista2["city"]).replace(" ","")

    return (d1<d2)

def cmplatitud(avista1, avista2):
    l1 = float(avista1["latitude"])
    l2 = float(avista2["latitude"])
    if l1==l2:
        lo1 = float(avista1["longitude"])
        lo2 = float(avista2["longitude"])
        return (lo1<lo2)
    else:
        return (l1<l2)