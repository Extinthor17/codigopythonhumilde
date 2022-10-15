# -*- coding: utf-8 -*-

'''
Created on 25 oct. 2021

@author: carsanexp
'''

#---------------------Importaciones
import csv
from collections import Counter, namedtuple

#------------------------------Definición de la tupla

esperanzaVida= namedtuple ("esperanzaVida",'año, totalpoblacion, hombres, mujeres, pais')

#-------------------------Funciones

def leer_esperanza_vida(fichero):
    '''
    Entra una cadena con fichero
    Sale una lista de tuplas
    
    '''
    with open(fichero, 'r', encoding= 'utf-8') as f:
        lector= csv.reader(f)
        next(lector)
        res=[esperanzaVida(int(a),float(tp),float(h),float(m),p)for a,tp,h,m,p in lector]
    return res

def filtrar_por_año(lista_tuplas,año):
    '''
    Entra una lista de tuplas con un año
    Sale una lista de tuplas con los datos filtrados por el año dado
    
    '''
    res = [e.pais for e in lista_tuplas if e.año == año]
    return res

def esperanza_vida_media_según_año_genero(lista_tuplas,año,genero):
    '''
    Entra una lista de tuplas con un año y un genero
    Sale un numero que es la esperanza de vida media
    
    '''
    if genero=="Hombres":
        lista_aux=[e.hombres for e in lista_tuplas if (e.año == año)]
        res=sum(lista_aux)/len(lista_aux)
    else:
        lista_aux=[e.mujeres for e in lista_tuplas if (e.año == año)]
        res=sum(lista_aux)/len(lista_aux)
    return res
    

def n_paises_mayor_esperanza_vida_total_ordenada_segun_año(lista_tuplas,año):
    lista_aux=[e for e in lista_tuplas if (e.año == año)]
    lista_aux.sort(key= lambda x:x.totalpoblacion, reverse= True)
    res=[e.pais for e in lista_aux]
    return res[:5]
   
    '''
    Entra una lista de tuplas junto a un año y a una opcion para elegir los 5 paises con mayor o menor esperanza de vida(poner mayores para los que mas y menores para los que menos)
    Sale una lista de tuplas cuyo elementos son 
    
    '''

def esperanza_vida_maxima(lista_tuplas):
    lista_aux=[e for e in lista_tuplas]
    maximo=max(lista_aux, key= lambda x:x.totalpoblacion)
    res=maximo.totalpoblacion
    return res 
    '''
    Entra una lista de tuplas
    Sale el valor de esperanza de vida maxima
    
    '''

def lista_paises_datos(lista_tuplas):
    lista_aux=[e for e in lista_tuplas]
    res=[e.pais for e in lista_aux]
    return res

    '''
    Entra una lista de tuplas
    Sale una lista con todos los distintos paises que se encuentran además del numero de ellos 
    
    '''

def diccionario_contador_años(lista_tuplas):
    lista_aux=[e.año for e in lista_tuplas]
    dic1=dict()
    
    for año in lista_aux:
        clave=año
        
        if clave not in dic1.keys():
            dic1[clave]=1
        else:
            dic1[clave]= dic1[clave]+1
            
    return dic1

    '''
    Entra una lista de tuplas
    Sale un diccionario que contiene los años de los que hay datos y los paises de los que se tienen datos de respectivos años
    
    '''

def diccionario_contador_años2(lista_tuplas):
    lista_aux=[e for e in lista_tuplas]
    dic_aux=Counter(e.año for e in lista_aux)
    
    return dic_aux
    
    

def paises_por_año(lista_tuplas):
    lista_aux1=[e.pais for e in lista_tuplas if e.año == 2018]
    lista_aux2=[e.pais for e in lista_tuplas if e.año == 2017]
    lista_aux3=[e.pais for e in lista_tuplas if e.año == 2016]
    
    lista1=[(lista_aux1,"2018"),(lista_aux2,"2017"),(lista_aux3,"2016")]
    
    
    d1=dict()
    for e in lista1:
        clave=e[1]
        if clave not in d1.keys():
            d1[clave]=[e[0]]
        else:
            d1[clave].append(e[0])
            
    
    
    print(d1)
    
    '''
    Entra una lista de tuplas
    Sale un diccionario que contiene los años de los que hay datos y los paises de los que se tienen datos de respectivos años
    
    '''

    
    
    
def año_con_mas_datos(lista_tuplas):
    lista_aux1=[e.pais for e in lista_tuplas if e.año == 2018]
    lista_aux2=[e.pais for e in lista_tuplas if e.año == 2017]
    lista_aux3=[e.pais for e in lista_tuplas if e.año == 2016]
    
    lista1=[(len(lista_aux1),"2018"),(len(lista_aux2),"2017"),(len(lista_aux3),"2016")]
    
    d1=dict()
    for e in lista1:
        clave=e[1]
        if clave not in d1.keys():
            d1[clave]=[e[0]]
        else:
            d1[clave].append(e[0])
            
    
    
    aux = list(d1.items())
    maximo = max(aux, key = lambda x:x[1])
    print(maximo[0])
    
def año_con_menos_datos(lista_tuplas):
    lista_aux1=[e.pais for e in lista_tuplas if e.año == 2018]
    lista_aux2=[e.pais for e in lista_tuplas if e.año == 2017]
    lista_aux3=[e.pais for e in lista_tuplas if e.año == 2016]
    
    lista1=[(len(lista_aux1),"2018"),(len(lista_aux2),"2017"),(len(lista_aux3),"2016")]
    
    d1=dict()
    for e in lista1:
        clave=e[1]
        if clave not in d1.keys():
            d1[clave]=[e[0]]
        else:
            d1[clave].append(e[0])
            
    
    
    aux = list(d1.items())
    minimo = min(aux, key = lambda x:x[1])
    print(minimo[0])
 
def esperanza_vida_media_de_los_n_top(lista_tuplas,año,n):
    lista_aux=[e for e in lista_tuplas if (e.año == año)]
    lista_aux.sort(key= lambda x:x.totalpoblacion, reverse= True)
    res1=[e for e in lista_aux]
    resaux=res1[:n]
    
    dicaux1=dict()
    for e in resaux:
        clave=e.pais
        if clave not in dicaux1.keys():
            dicaux1[clave]=e.totalpoblacion
    
    
    varux1=sum(dicaux1.values())
    
    varux2=n
    
    res2=varux1/varux2
    print('La esperanza de vida media de los 5 mejores paises es',res2)
    
def n_paises_mas_esperanza_vida_segun_genero_año(lista_tuplas,año,genero,n):
    lista_aux=[e for e in lista_tuplas if (e.año == año)]
    if genero=="Hombres":
        lista_aux.sort(key= lambda x:x.hombres, reverse= True)
        res=[e for e in lista_aux]
        res1=res[:n]
        
    else:
        lista_aux.sort(key= lambda x:x.mujeres, reverse= True)
        res=[e for e in lista_aux]
        res1=res[:n]
    
    d1=dict()
    
    
    
    for e in res1:
        clave= 'N paises con mas esperanza de vida segun el año y género elegido'
        if clave not in d1.keys():
            d1[clave]=[e[4]]
        else:
            d1[clave].append(e[4])
            
    
    
    print(d1)
        
    
    
    
    
    
    