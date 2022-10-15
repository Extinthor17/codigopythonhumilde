# -*- coding: utf-8 -*-
'''
Created on 25 oct. 2021

@author: carsanexp
'''
#---------------------------------Importaciones
from EsperanzaVida import *


#---------------------------------Funciones
def test_leer_esperanza_vida():
    nombre_fichero="./data/esperanza_vida.csv"
    resultado= leer_esperanza_vida(nombre_fichero)
    print(resultado[:3])
    print(resultado[-3:])
   
def test_filtrar_por_año():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res= filtrar_por_año(lista_tuplas, 2016)
    print(res)
    
    
def test_esperanza_vida_media_según_año_genero():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=esperanza_vida_media_según_año_genero(lista_tuplas,2016,"Mujeres")
    print(res)
    
def test_n_paises_mayor_esperanza_vida_total_ordenada_segun_año():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=n_paises_mayor_esperanza_vida_total_ordenada_segun_año(lista_tuplas,2017,)
    print(res)
    
def test_esperanza_vida_maxima():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res= esperanza_vida_maxima(lista_tuplas)
    print(res)

def test_lista_paises_datos():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=lista_paises_datos(lista_tuplas)
    ndi=len(res)
    print("Hay",ndi,"paises distintos.")
    print(res) 
    
def test_diccionario_contador():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=diccionario_contador_años(lista_tuplas)
    print(res)
    
def test_diccionario_contador2():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=diccionario_contador_años2(lista_tuplas)
    print(res)
    
def test_paises_por_año():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=paises_por_año(lista_tuplas)
    return res

def test_año_mas_datos():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=año_con_mas_datos(lista_tuplas)
    return res

def test_año_menos_datos():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=año_con_menos_datos(lista_tuplas)
    return res

def test_esperanza_vida_media_de_los_n_top():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=esperanza_vida_media_de_los_n_top(lista_tuplas,2017,5)
    return res 

def test_n_paises_mas_esperanza_vida_segun_genero_año():
    lista_tuplas=leer_esperanza_vida("./data/esperanza_vida.csv")
    res=n_paises_mas_esperanza_vida_segun_genero_año(lista_tuplas,2017,"Hombres",8)
    return res
#---------------------------------Modulo main
if __name__ == '__main__':
    test_filtrar_por_año()