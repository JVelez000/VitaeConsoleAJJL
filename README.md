Nombre del proyecto: Curriculum Vitae

Nombre de los integrantes:
 - Angelica Maria Cuervo (Ritchie)
 - Luna Valdelamar (Berners Lee)
 - Jeims Velez Echavarria (Van Rossum)
 - Juan Andres Aristizabal Vallejo (Van Rossum)

Descripcion general:

Nuestro programa permite la creacion, actualizacion, exportacion y busqueda de hojas de vida. Los datos son almacenados en un archivo JSON para asegurar que queden como una base de datos. 

El archivo madre es "hojasdevida" donde almacenamos todas las funciones, las condicionales y criterios de aceptacion. 

El archivo en el cual el usuario ejecutara el programa se llama "main" donde llamamos las funciones y se ejecutan en el orden que el cliente desee, siempre y cuando ingrese los datos dentro del margen de aceptacion. Adicional se otorga una base de datos ya creada para testear la funcionalidad del programa.

Instrucciones de uso:

Al ejecutar el programa nos encontraremos con un menu de seleccion multiple con el que el usuario puede interactuar:

 - Agregar usuario:

En este apartado, el cliente puede registrar desde cero una hoja de vida con un pin unico por cada usuario. Es obligatorio ingresar un pin unico, nombre, contacto, direccion, email y fecha de nacimiento (lo minimo que debe de contener una CV). 

Los otros datos son opcionales ya que van a haber usuarios que pueden o no tener ciertos criterios.

Una vez finalizada la creacion del usuario, toda la informacion se almacena en el archivo JSON.

 - Consultar CV

En este apartado, el usuario tiene la posibilidad de consultar cv's YA EXISTENTES en la base de datos con criterios de aceptacion. Se retornaran en pantalla SOLO los candidatos que apliquen con dichos criterios, las otras cv seran descartadas.

 - Actualizar Datos

Para este submenu, se le permite al usuario modificar a gusto ciertos parametros de las hojas de vida ya registradas. Esto es debido a que no se puede modificar ningun dato principal del usuario (pin unico, nombre y fecha de nacimiento). 

Al momento de actualizar los datos, estos se veran reflejados en el archivo JSON.

 - Exportar CV

Como final del menu, tenemos la opcion de exportar toda la informacion que esta almacenada en el archivo JSON transformado a PDF para una mejor lectura de las hojas de vida. Recordemos que esta funcion es unica y si ya tenemos un PDF y hacemos una modificacion de alguna CV, tendremos que descargar nuevamente el PDF para ver el archivo actualizado.

Librerias utilizadas:

 - import re
 - import json

Estas no requieren instalacion previa ya que estamos invocando archivos que ya se crearon anteriormente.

 -

 Por cierto, el .json se crea cuando se ejecuta el archivo al anadir nuevos usuarios, ya que si no se hace asi se sobreescriben datos si se pasa un json a modificado
Ejemplos de uso:
