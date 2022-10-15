# Proyecto del Primer Cuatrimestre Fundamentos de Programaci�n (Curso  \<21\>/\<22\>)
Autor/a: \<Carlos Santos Exp�sito\>   uvus:\<carsanexp\>

Este proyecto entregable est� formado por 2 m�dulos, el "EsperanzaVida" y "EsperanzaVidaTest" y conformado por 12 funciones, "leer_esperanza_vida", "test_leer_esperanza_vida", "filtrar_por_a�o","test_filtrar_por_a�o",
"esperanza_vida_media_seg�n_a�o_genero","test_esperanza_vida_media_seg�n_a�o_genero","n_paises_mayor_esperanza_vida_total_ordenada_segun_a�o","test_n_paises_mayor_esperanza_vida_total_ordenada_segun_a�o","esperanza_vida_maxima","test_esperanza_vida_maxima"," lista_paises_datos","test_lista_paises_datos".


## Estructura de las carpetas del proyecto

* **/src**: Contiene los diferentes m�dulos de Python que conforman el proyecto.
  * **\<EsperanzaVida.py\>**: Este m�dulo contiene las 6 funciones principales del proyecto encargadas de llevar a cabo los principales procesos como los de ordenaci�n, filtrado y generaci�n de lista de tuplas y "named tuples".
  * **\<EsperanzaVidaTest.py\>**: El m�dulo de pruebas est� conformado por 6 funciones cuyo objetivo es la invocaci�n de las 6 funciones principales con los valores de variables necesarios para su ejecuci�n. 

   
* **/data**: Contiene el dataset o datasets del proyecto
    * **\<esperanza_vida.csv\>**: Este dataset contiene datos de esperanza de vida general, de la esperanza de vida de los hombres y de la esperanza de vida de las mujeres en distintos pa�ses desde el a�o 2017.
 
    
## Estructura del *dataset*

Aqu� debes describir la estructura del dataset explicando qu� representan los datos que contiene y la descripci�n de cada una de las columnas.

El dataset est� compuesto por \<5\> columnas, con la siguiente descripci�n:

* **\<columna 1>**: de tipo \<int\>, representa el a�o del cual se han sacado los datos.
* **\<columna 2>**: de tipo \<float\>, representa la esperanza de vida del pa�s entero.
* **\<columna 3>**: de tipo \<float\>, representa la esperanza de vida de los varones del pa�s.
* **\<columna 4>**: de tipo \<float\>, representa la esperanza de vida de las mujeres del pa�s.
* **\<columna 5>**: de tipo \<str\>, determina el pa�s del cual son los datos.


## Tipos implementados

En este proyecto solo se ha integrado una namedtuple, con nombre "esperanzaVida". Esta cuenta con los datos anteriormente descritos; a�o, esperanza vida media, esperanza vida hombres, esperanza vida mujeres y el pa�s. 

## Funciones implementadas
Se han implementado 26 funciones; llamadas "leer_esperanza_vida", "test_leer_esperanza_vida", "filtrar_por_a�o","test_filtrar_por_a�o","esperanza_vida_media_seg�n_a�o_genero","test_esperanza_vida_media_seg�n_a�o_genero","n_paises_mayor_esperanza_vida_total_ordenada_segun_a�o","test_n_paises_mayor_esperanza_vida_total_ordenada_segun_a�o","esperanza_vida_maxima","test_esperanza_vida_maxima"," lista_paises_datos","test_lista_paises_datos".
Todas las funciones con "test" en su nombre sirven para llamar a la funci�n que lleva su nombre. Luego, "leer_esperanza_vida" recoge los datos del fichero y los coloca en una lista de tuplas. La funci�n "filtrar_por_a�o" filtra los datos de la lista de tuplas dependiendo del a�o a que pertenezcan. La funci�n "esperanza_vida_media_seg�n_a�o_genero" calcula la esperanza de vida media de un g�nero en un a�o dado. La funci�n "n_paises_mayor_esperanza_vida_total_ordenada_segun_a�o"
ordena de mayor a menor los 5 pa�ses con mayor esperanza de vida en un a�o dado. La funci�n "esperanza_vida_maxima" sirve para determinar el valor m�ximo de esperanza de vida de todos los datos del fichero. La funci�n "lista_paises_datos" genera una lista de tuplas cuyos elementos son los distintos pa�ses de los cuales se tiene datos. 
### \<modulo 1\>

* **<leer_esperanza_vida>**: Este m�dulo se encarga de realizar la funci�n principal. Al entrar un fichero con datos separados por comas (csv), esta funci�n separa los valores y los plasma en una tupla, respondiendo estos al dato que entregan. Para ello se
emplea un with y la librer�a csv para general un lector de estos documentos. Luego, se crea la lista de tuplas con la variable "res". Finalmente, esta se muestra en pantalla. 

* **<filtrar_por_a�o>**: Este m�dulo se encarga de filtrar la lista de tuplas generada por la funcion 1 segun el a�o de los datos. Para ello se crea una variable "res" la cual es una lista a la que solo se a�aden los t�rminos que cumplen la condici�n del a�o. 

* **<esperanza_vida_media_seg�n_a�o_genero>**: Este m�dulo se encarga de obtener el valor de esperanza de vida media de un g�nero en un a�o determinado. Para ello se coloca un bloque "if" que dependiendo del valor de la variable "g�nero" genera la lista "lista_aux" filtrando por un g�nero u otro.
Luego se genera una variable "res" la cual es la suma de de los valores de "lista_aux" y los divide por la longitud de la lista.

* **<n_paises_mayor_esperanza_vida_total_ordenada_segun_a�o>**: Este m�dulo se encarga de ordenar de mayor a menor los n paises, en este caso 5, con mayor esperanza de vida en un determinado a�o. Para ello se genera una lista auxiliar filtrada por a�o y luego esa lista se ordena mediante slicing. Despu�s se genera una lista resultado
la cual contiene ordenados de mayor a menor los pa�ses. De estos solo se ense�an los 5 primeros.

* **<esperanza_vida_maxima>**: Este m�dulo se encarga de obtener el valor m�ximo de esperanza de vida total. Para ello se genera una lista auxiliar con los datos de "lista_tuplas". Esta lista luego se recorre y de la cual se extrae el valor m�ximo de la misma, la cual se presenta con una variable "res".

* **<lista_paises_datos>**: Este m�dulo se encarga de estampar en una lista todos los diferentes pa�ses que forman parte del fichero. Para ello se genera una lista auxiliar y con esta misma se genera otra lista solo con los paises en la variable "res". 

* **<diccionario_contador_a�os>**: Este m�dulo se encarga de encarga de contar la cantidad de paises que hay por a�os. Este m�dulo realiza el conteo mediante un diccionario, con claves los distintos a�os y luego va sumando la distinta cantidad de valores.

* **<diccionario_contador_a�os2>**: Este m�dulo se encarga de contar la cantidad de paises que hay por a�os. Este m�dulo lo realiza de manera directa con la opcion "counter", los cuales los cuenta por las distintas claves.

* **<paises_por_a�o>**: Este m�dulo se encarga de imprimir un diccionario en el cual se encuentran la lista de los paises que hay dependiendo de los a�os. Esto se lleva a cabo generando 3 listas auxiliares, las cuales se vuelcan en un diccionario con los a�os como claves y luego a�adiendo los valores (nombres) al diccionario.

* **<a�o_con_mas_datos>**: Este m�dulo se encarga de calcular cual es el a�o con el mayor n�mero de datos. Se realiza generando 3 listas auxiliares con cada a�o respectivo y luego generando una que incluye a cada longitud de cada auxiliar con su respectivo a�o. Luego esto se vuelca en un diccionario y se calcula el m�ximo con la funci�n procedente.

* **<a�o_con_menos_datos>**: Este m�dulo se encarga de calcular cual es el a�o con el menor n�mero de datos. Se realiza generando 3 listas auxiliares con cada a�o respectivo y luego generando una que incluye a cada longitud de cada auxiliar con su respectivo a�o. Luego esto se vuelca en un diccionario y se calcula el m�nimo con la funci�n procedente.

* **<esperanza_vida_media_de_los_n_top>**: Este m�dulo se encarga de calcular la esperanza de vida media de los n paises con mas esperanza de vida de un a�o dado. Se realiza generando una lista con los datos y luego generando otra siendo la misma que la anterior pero acotada a n valores. Luego se generan un diccionario auxiliar, constando de los distintos valores de esperanza de vida total de los paises.
Luego, se generan dos nuevas variables, una asignandole la suma de los valores del diccionario auxiliar y la segunda siendo el valor n. Luego estos dos valores se dividen para calcular la media.

* **<n_paises_mas_esperanza_vida_segun_genero_a�o>**: Este m�dulo se encarga de mostrar los n paises con mas esperanza de vida segun el genero y a�o. Primero se ordena una lista auxiliar dependiendo del genero proporcionado. Luego, se genera un diccionario al que se le a�aden los nombres de los paises provenientes de la lista ya ordenada, todos bajo la misma clave.

### \<test modulo 1\>

* **<test_leer_esperanza_vida>**: Este m�dulo se encarga de poner a prueba el m�dulo anterior. Para ello, se define la funci�n; determinando el directorio y fichero del cual el lector debe sacar los datos y determinando la variable resultado al resultado de
la lectura del csv. Adem�s, se limita el mostrado de elementos a 6; los 3 primeros y los 3 �ltimos. 

* **<test_filtrar_por_a�o>**: Este m�dulo se encarga de invocar a la funcion "filtrar_por_a�o" con el a�adido de la variable "a�o" y generar la lista de tuplas con la funci�n primera, a lo que se genera una variable "res" la cual es el resultado de la funci�n. 

* **<test_esperanza_vida_media_seg�n_a�o_genero>**: Este m�dulo se encarga de invocar a la funcion "esperanza_vida_media_seg�n_a�o_genero" a�adiendo el valor de la variable "a�o" y "genero" generando la lista de tuplas con la funci�n primera, a lo que se genera una variable "res" la cual es el resultado de la funci�n. 

* **<test_n_paises_mayor_esperanza_vida_total_ordenada_segun_a�o>**: Este m�dulo se encarga de invocar a la funcion "paises_mayor_esperanza_vida_total_ordenada_segun_a�o" a�adiendo el valor de la variable "a�o" generando la lista de tuplas con la funci�n primera, a lo que se genera una variable "res" la cual es el resultado de la funci�n. 

* **<test_esperanza_vida_maxima>**: Este m�dulo se encarga de invocar a la funcion "esperanza_vida_maxima" generando la lista de tuplas con la funci�n primera, a lo que se genera una variable "res" la cual es el valor del maximo de la funci�n. 

* **<test_lista_paises_datos>**: Este m�dulo se encarga de invocar a la funcion "lista_paises_datos" generando la lista de tuplas con la funcion primera, generando una variable "res" la cual es el resultado de la funci�n. A esto se le a�ade la variable "ndi" que es la longitud total de la lista generada, que indica la cantidad total de pa�ses que forman parte del fichero. 

* **<test_diccionario_contador_a�os>**: Este m�dulo se encarga de invocar a la funcion "diccionario_contador_a�os".

* **<test_diccionario_contador_a�os2>**: Este m�dulo se encarga de invocar a la funcion "diccionario_contador_a�os2".

* **<test_paises_por_a�o>**: Este m�dulo se encarga de invocar a la funcion "paises_por_a�o".

* **<test_a�o_con_mas_datos>**: Este m�dulo se encarga de invocar a la funcion "a�o_con_mas_datos".

* **<test_a�o_con_menos_datos>**: Este m�dulo se encarga de invocar a la funcion "a�o_con_menos_datos".

* **<test_esperanza_vida_media_de_los_n_top>**: Este m�dulo se encarga de invocar a la funcion "esperanza_vida_media_de_los_n_top".

* **<test_n_paises_mas_esperanza_vida_segun_genero_a�o>**: Este m�dulo se encarga de invocar a la funcion "n_paises_mas_esperanza_vida_segun_genero_a�o".

