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
assert cf
from time import process_time
from prettytable import PrettyTable, ALL


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Contar avistamientos en una ciudad")
    print("3- Contar los avistamientos por duración")
    print("4- Contar avistamientos por Hora/Minutos del día")
    print("5- Contar los avistamientos en un rango de fechas")
    print("6- Contar los avistamientos de una Zona Geográfica")
    print("7- Visualizar los avistamientos de una zona geográfica.")
    print("0- Salir")

catalog = None


def reqUno(catalog, ciudad):
    data = controller.reqUno(catalog, ciudad)
    print("Se registraron " + str(lt.size(data)) + " avistamientos en " + str(ciudad) + "\n")

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos .... \n")

        catalog = controller.init()
        controller.loadData(catalog)
        print("Avistamientos cargados: " + str(lt.size(catalog["Avistamientos"])) + "\n")

    elif int(inputs[0]) == 2:
        print("Altura de arbol por ciudad: " + str(controller.Altura(catalog, "Ciudad")) + "\n")
        print("Numero de ciudades en el arbol: " + str(controller.Size(catalog, "Ciudad")) + "\n")

        ciudad = input("Ciudad en la que quiere consultar avistamientos: \n >")
        t1 = process_time()
        reqUno(catalog, ciudad)
        t2 = process_time()
        print("Time = " + str(t2-t1) + "seg \n")

    elif int(inputs[0]) == 3:
        print("Funcion en desarrollo")

    elif int(inputs[0]) == 4:
        print("Funcion en desarrollo")

    elif int(inputs[0]) == 5:
        print("Funcion en desarrollo")

    elif int(inputs[0]) == 6:
        print("Funcion en desarrollo")

    elif int(inputs[0]) == 7:
        print("Funcion en desarrollo")

    else:
        sys.exit(0)
sys.exit(0)
