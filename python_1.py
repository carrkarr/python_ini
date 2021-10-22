# -*- coding: utf-8 -*-

""""
El intérprete y su entorno Codiﬁcación del código fuente Por default, 
los archivos fuente de Python son tratados como codificados en UTF-8. 
En esa codificación, los caracteres de la mayoría de los lenguajes 
del mundo pueden ser usados simultáneamente en literales, identificadores 
y comentarios, a pesar de que la biblioteca estándar usa solamente 
caracteres ASCII para los identificadores, una convención que debería 
seguir cualquier código que sea portable. Para mostrar estos caracteres 
correctamente, tu editor debe reconocer que el archivo está en UTF-8 y 
usar una tipografía que soporte todos los careacteres del archivo. 
También es posible especificar una codificación distinta para los archivos 
fuente. Para hacer esto, poné una o más lineas de comentarios especiales 
luego de la linea del 
#! para definir la codificación del archivo fuente: 
# -*- coding: encoding -*-

Con esa declaración, todo en el archivo fuente será tratado utilizando la 
codificación encoding en lugar de UTF-8. La lista de posibles codificaciones
se puede encontrar en la Referencia de la Biblioteca de Python, en la 
sección sobre codecs. Por ejemplo, si tu editor no soporta la codificación 
UTF-8 e insiste en usar alguna otra, digamos Windows-1252, podés escribir: 
# -*- coding: cp-1252 -*-
"""

"""
Para documentar un programa se utiliza triple comilla  como en el caso que lo estamos haciendo 
(); no se debe de exagerar con la documentación en los programas; en este caso
se exagerra por que es didáctico; otra forna de comentar es con con  un
# .....texto 
"""

# hagamos nuestro hola mundo
print('Hola mundo')







