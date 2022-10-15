# Proyecto del Primer Cuatrimestre Fundamentos de Programación (Curso  \<21\>/\<22\>)
Autor/a: \<Carlos Santos Expósito\>   uvus:\<carsanexp\>

Este proyecto entregable está formado por 2 módulos, el "EsperanzaVida" y "EsperanzaVidaTest" y conformado por 12 funciones, "leer_esperanza_vida", "test_leer_esperanza_vida", "filtrar_por_año","test_filtrar_por_año",
"esperanza_vida_media_según_año_genero","test_esperanza_vida_media_según_año_genero","n_paises_mayor_esperanza_vida_total_ordenada_segun_año","test_n_paises_mayor_esperanza_vida_total_ordenada_segun_año","esperanza_vida_maxima","test_esperanza_vida_maxima"," lista_paises_datos","test_lista_paises_datos".


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes módulos de Python que conforman el proyecto.
  * **\<EsperanzaVida.py\>**: Este módulo contiene las 6 funciones principales del proyecto encargadas de llevar a cabo los principales procesos como los de ordenación, filtrado y generación de lista de tuplas y "named tuples".
  * **\<EsperanzaVidaTest.py\>**: El módulo de pruebas está conformado por 6 funciones cuyo objetivo es la invocación de las 6 funciones principales con los valores de variables necesarios para su ejecución. 

   
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<esperanza_vida.csv\>**: Este dataset contiene datos de esperanza de vida general, de la esperanza de vida de los hombres y de la esperanza de vida de las mujeres en distintos países desde el año 2017.
 
    
## Estructura del *dataset*

Aquí debes describir la estructura del dataset explicando qué representan los datos que contiene y la descripción de cada una de las columnas.

El dataset está compuesto por \<5\> columnas, con la siguiente descripción:

* **\<columna 1>**: de tipo \<int\>, representa el año del cual se han sacado los datos.
* **\<columna 2>**: de tipo \<float\>, representa la esperanza de vida del país entero.
* **\<columna 3>**: de tipo \<float\>, representa la esperanza de vida de los varones del país.
* **\<columna 4>**: de tipo \<float\>, representa la esperanza de vida de las mujeres del país.
* **\<columna 5>**: de tipo \<str\>, determina el país del cual son los datos.


## Tipos implementados

En este proyecto solo se ha integrado una namedtuple, con nombre "esperanzaVida". Esta cuenta con los datos anteriormente descritos; año, esperanza vida media, esperanza vida hombres, esperanza vida mujeres y el país. 

## Funciones implementadas
Se han implementado 26 funciones; llamadas "leer_esperanza_vida", "test_leer_esperanza_vida", "filtrar_por_año","test_filtrar_por_año","esperanza_vida_media_según_año_genero","test_esperanza_vida_media_según_año_genero","n_paises_mayor_esperanza_vida_total_ordenada_segun_año","test_n_paises_mayor_esperanza_vida_total_ordenada_segun_año","esperanza_vida_maxima","test_esperanza_vida_maxima"," lista_paises_datos","test_lista_paises_datos".
Todas las funciones con "test" en su nombre sirven para llamar a la función que lleva su nombre. Luego, "leer_esperanza_vida" recoge los datos del fichero y los coloca en una lista de tuplas. La función "filtrar_por_año" filtra los datos de la lista de tuplas dependiendo del año a que pertenezcan. La función "esperanza_vida_media_según_año_genero" calcula la esperanza de vida media de un género en un año dado. La función "n_paises_mayor_esperanza_vida_total_ordenada_segun_año"
ordena de mayor a menor los 5 países con mayor esperanza de vida en un año dado. La función "esperanza_vida_maxima" sirve para determinar el valor máximo de esperanza de vida de todos los datos del fichero. La función "lista_paises_datos" genera una lista de tuplas cuyos elementos son los distintos países de los cuales se tiene datos. 
### \<modulo 1\>

* **<leer_esperanza_vida>**: Este módulo se encarga de realizar la función principal. Al entrar un fichero con datos separados por comas (csv), esta función separa los valores y los plasma en una tupla, respondiendo estos al dato que entregan. Para ello se
emplea un with y la librería csv para general un lector de estos documentos. Luego, se crea la lista de tuplas con la variable "res". Finalmente, esta se muestra en pantalla. 

* **<filtrar_por_año>**: Este módulo se encarga de filtrar la lista de tuplas generada por la funcion 1 segun el año de los datos. Para ello se crea una variable "res" la cual es una lista a la que solo se añaden los términos que cumplen la condición del año. 

* **<esperanza_vida_media_según_año_genero>**: Este módulo se encarga de obtener el valor de esperanza de vida media de un género en un año determinado. Para ello se coloca un bloque "if" que dependiendo del valor de la variable "género" genera la lista "lista_aux" filtrando por un género u otro.
Luego se genera una variable "res" la cual es la suma de de los valores de "lista_aux" y los divide por la longitud de la lista.

* **<n_paises_mayor_esperanza_vida_total_ordenada_segun_año>**: Este módulo se encarga de ordenar de mayor a menor los n paises, en este caso 5, con mayor esperanza de vida en un determinado año. Para ello se genera una lista auxiliar filtrada por año y luego esa lista se ordena mediante slicing. Después se genera una lista resultado
la cual contiene ordenados de mayor a menor los países. De estos solo se enseñan los 5 primeros.

* **<esperanza_vida_maxima>**: Este módulo se encarga de obtener el valor máximo de esperanza de vida total. Para ello se genera una lista auxiliar con los datos de "lista_tuplas". Esta lista luego se recorre y de la cual se extrae el valor máximo de la misma, la cual se presenta con una variable "res".

* **<lista_paises_datos>**: Este módulo se encarga de estampar en una lista todos los diferentes países que forman parte del fichero. Para ello se genera una lista auxiliar y con esta misma se genera otra lista solo con los paises en la variable "res". 

* **<diccionario_contador_años>**: Este módulo se encarga de encarga de contar la cantidad de paises que hay por años. Este módulo realiza el conteo mediante un diccionario, con claves los distintos años y luego va sumando la distinta cantidad de valores.

* **<diccionario_contador_años2>**: Este módulo se encarga de contar la cantidad de paises que hay por años. Este módulo lo realiza de manera directa con la opcion "counter", los cuales los cuenta por las distintas claves.

* **<paises_por_año>**: Este módulo se encarga de imprimir un diccionario en el cual se encuentran la lista de los paises que hay dependiendo de los años. Esto se lleva a cabo generando 3 listas auxiliares, las cuales se vuelcan en un diccionario con los años como claves y luego añadiendo los valores (nombres) al diccionario.

* **<año_con_mas_datos>**: Este módulo se encarga de calcular cual es el año con el mayor número de datos. Se realiza generando 3 listas auxiliares con cada año respectivo y luego generando una que incluye a cada longitud de cada auxiliar con su respectivo año. Luego esto se vuelca en un diccionario y se calcula el máximo con la función procedente.

* **<año_con_menos_datos>**: Este módulo se encarga de calcular cual es el año con el menor número de datos. Se realiza generando 3 listas auxiliares con cada año respectivo y luego generando una que incluye a cada longitud de cada auxiliar con su respectivo año. Luego esto se vuelca en un diccionario y se calcula el mínimo con la función procedente.

* **<esperanza_vida_media_de_los_n_top>**: Este módulo se encarga de calcular la esperanza de vida media de los n paises con mas esperanza de vida de un año dado. Se realiza generando una lista con los datos y luego generando otra siendo la misma que la anterior pero acotada a n valores. Luego se generan un diccionario auxiliar, constando de los distintos valores de esperanza de vida total de los paises.
Luego, se generan dos nuevas variables, una asignandole la suma de los valores del diccionario auxiliar y la segunda siendo el valor n. Luego estos dos valores se dividen para calcular la media.

* **<n_paises_mas_esperanza_vida_segun_genero_año>**: Este módulo se encarga de mostrar los n paises con mas esperanza de vida segun el genero y año. Primero se ordena una lista auxiliar dependiendo del genero proporcionado. Luego, se genera un diccionario al que se le añaden los nombres de los paises provenientes de la lista ya ordenada, todos bajo la misma clave.

### \<test modulo 1\>

* **<test_leer_esperanza_vida>**: Este módulo se encarga de poner a prueba el módulo anterior. Para ello, se define la función; determinando el directorio y fichero del cual el lector debe sacar los datos y determinando la variable resultado al resultado de
la lectura del csv. Además, se limita el mostrado de elementos a 6; los 3 primeros y los 3 últimos. 

* **<test_filtrar_por_año>**: Este módulo se encarga de invocar a la funcion "filtrar_por_año" con el añadido de la variable "año" y generar la lista de tuplas con la función primera, a lo que se genera una variable "res" la cual es el resultado de la función. 

* **<test_esperanza_vida_media_según_año_genero>**: Este módulo se encarga de invocar a la funcion "esperanza_vida_media_según_año_genero" añadiendo el valor de la variable "año" y "genero" generando la lista de tuplas con la función primera, a lo que se genera una variable "res" la cual es el resultado de la función. 

* **<test_n_paises_mayor_esperanza_vida_total_ordenada_segun_año>**: Este módulo se encarga de invocar a la funcion "paises_mayor_esperanza_vida_total_ordenada_segun_año" añadiendo el valor de la variable "año" generando la lista de tuplas con la función primera, a lo que se genera una variable "res" la cual es el resultado de la función. 

* **<test_esperanza_vida_maxima>**: Este módulo se encarga de invocar a la funcion "esperanza_vida_maxima" generando la lista de tuplas con la función primera, a lo que se genera una variable "res" la cual es el valor del maximo de la función. 

* **<test_lista_paises_datos>**: Este módulo se encarga de invocar a la funcion "lista_paises_datos" generando la lista de tuplas con la funcion primera, generando una variable "res" la cual es el resultado de la función. A esto se le añade la variable "ndi" que es la longitud total de la lista generada, que indica la cantidad total de países que forman parte del fichero. 

* **<test_diccionario_contador_años>**: Este módulo se encarga de invocar a la funcion "diccionario_contador_años".

* **<test_diccionario_contador_años2>**: Este módulo se encarga de invocar a la funcion "diccionario_contador_años2".

* **<test_paises_por_año>**: Este módulo se encarga de invocar a la funcion "paises_por_año".

* **<test_año_con_mas_datos>**: Este módulo se encarga de invocar a la funcion "año_con_mas_datos".

* **<test_año_con_menos_datos>**: Este módulo se encarga de invocar a la funcion "año_con_menos_datos".

* **<test_esperanza_vida_media_de_los_n_top>**: Este módulo se encarga de invocar a la funcion "esperanza_vida_media_de_los_n_top".

* **<test_n_paises_mas_esperanza_vida_segun_genero_año>**: Este módulo se encarga de invocar a la funcion "n_paises_mas_esperanza_vida_segun_genero_año".

