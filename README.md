# Categorizador-URLs
Python backend and react fronte categorizador URLs

Este proyecto consiste en un clasificador de Urls con base a 3 categorias previamente establecidas por el equipo desarrollador. Se implementó el lenguaje de programación Python en el IDE de Visual Studio Code y la ejecución por hilos del proceso como tal para optimizar el análisis de 7000 Urls.

#Backend

# Librerías necesarias 
Por medio de la consola se debe instalar la librería de requests
Comando:
npm install requests
Luego debe importarlo dentro del archivo Python
Import requests

De igual forma la librería Flask
Comando:
pip3 install flask
Luego debe importarlo dentro del archivo Python
from flask import Flask

# Categorias a utilizar para el clasificador y sus palabras claves: 

arte = ["Art","art","oil","liberal","artists","craft","painting","artwork","creative","creativity","design","gallery","crafts","crafting",
"music","dancing","dance","play","draw","drawing""history","designer","editing","colors","decorate","decorative","photography","photos",
"musicians","music","mosaics","picture","portray","poetry","philosophy","cartooning","masterpiece","modernist","performer","folklore",
"handmade","movies","sculture","composer","singer","talent","theater","books","skill","novel","cultural","film","performance","perform",
"actress","actors","director","culture","presentation","filmmaker","contemporary","photobooks","edition","talented","prints","participation",
"Copyright","Content","animation"]

sociedad = ["people", "economy", "social","socialize","political","Capitalism ","history","events","democracy","generation"
"institutions","money","public","information","organization","community","world","humanity","inhabitants","group"
"collectivity","generality","family","nation","citizenship","city","culture","society","Socialism","protesters"
"massive","police","millennial","countries","globalization","civil","rights","Educate","activists","business", 
"hospital", "discrimination","employees","Union","organizations","participation","town","progress","homeland","independence"
"representation","war","international","government","PLANET","celebration","human","justice","transnational","planet"
"health","water","climate","rebellion","fight","national","popular"] 

computadores = ["information","computational","algorithm","binary","optimization", "programming","geometry",
"computer","sciencie","web","course","design","paradigms","dynamic","software","data","applications",
"program","computation","structures","simulation","automathic","automata","graph","techniques","tree",
"proccessing","website","compression","code","system","analysis","coding","research","multimedia",
"engineering","communication","machine","learning","projects","sensor","images","developer","robot","technology",
"electrical","security","database","mathematics","simulation","statistics","discrete"]


# Repositorio con urls:

Como repositorio de las urls se utilizó un CSV obtenido de https://www.kaggle.com/code/shawon10/url-classification-by-naive-bayes/data y sobre el cual se acomodaron los primeros 12000 urls para que estos estuviesen dentro de las categorias escogidas.

Para poder acceder a la información de este CSV se utilizó la libreria csv de Python.

![image](https://user-images.githubusercontent.com/61404066/197903525-f16ba549-a43c-4c01-8b4f-ce150f089355.png)

# Web Scrapping:

Para este apartado del proyecto se utilizaron dos librerías: bs4 (BeautifulSoup) y Request.

Request es utilizada especificamente para realizar una conexión a una página web con base a un Url dado. Asimismo BeautifulSoup se utiliza para tomar el contenido html de las páginas. Todo esto se hace dentro de la funcion connectionToPage(url).

![image](https://user-images.githubusercontent.com/61404066/197903075-4a8c0f47-9a74-4750-8b4b-3fbd35f7796b.png)

Especificamente para este proyecto se revisaron algunas etiquetas html claves de las páginas y en donde se verifica si existe o no coincidencia con las palabras definidas en cada categoría dentro de estas. Por lo que una vez obtenidas las palabras que estan contenidas en esas etiquetas, se dividen en palabras completas utilizando expresiones regulares y se van agregando dentro de una lista local con la cual se pasa a ejecutar la funcion, ademas del url que se está revisando en ese momento, checkForKeyWords(list,url).

![image](https://user-images.githubusercontent.com/61404066/198919723-cbf36bd2-d240-431f-86a1-c799b3f8e95b.png)


Esta funcion checkForKeyWords(list,url) retorna una lista con 3 listas internas, cada una de estas listas representan las palabras claves encontradas para la categoria arte, computadoras o sociedad respectivamente con su índice dentro de dicha lista principal ([0] = arte, [1] = computadoras y [3] sociedad).


![image](https://user-images.githubusercontent.com/61404066/198919967-18e4002c-d7ca-49fd-a839-6b2635a8b162.png)


# Paralelismo:
Con fin de lograr resultados en menor tiempo al recorrer los 10000 links utilizados para ser clasificados se aplicó un nivel de paralelismo por medio de la librería Thread, específicamente la sección de threading. La cual debe ser importada del archivo Python de la siguiente manera.
from threading import Thread
Después de importar la librería se utiliza la siguiente función para realizar el paralelismo.

![image](https://user-images.githubusercontent.com/61396158/199614576-49773dc0-1349-40a0-9538-14328317b75f.png)

En esta función se crea una lista en la cual se van a almacenar todos los threads(hilos) que se están creando. Luego se realiza un for desde el numero 1 hasta el tamaño de que tenga la lista de los urls a utilizar. En cada iteración se va a crear un hilo que se agregará a la lista creada anteriormente en la posición que le corresponde. 
Los hilos se crean utilizando la función Thread la cual tiene 2 argumentos, los cuales son: target, en el cual se envía la función que se debe ejecutar de forma paralela y kwargs, el cual esta compuesto por los parámetros que debe recibir la función del argumento target.
Después de realizar esto se debe iniciar el hilo que se creó por medio del comando .start, cabe aclarar que si no se realiza este comando los hilos solo crearán pero no van a comenzar por lo cual no se realizará ningún procedimiento. 
Para finalizar, se realiza con ciclo que se ejecuta siempre al usar el true, dentro de este ciclo se realizar un for que recorre todos los elementos de la lista de hilos que se creó anteriormente y dentro de este se pregunta si el hilo no está vivo, lo cual se refiere a que si el hilo ya no se está ejecutando, si esto es cierto entonces se elimina el hilo de la lista de hilos. Luego de este for se pregunta si el tamaño de la lista de hilos es menor a 1 es decir que ya no hay más, entonces el ciclo se rompe por medio del comando break. 

# ¿Por qué utilizar la librería Threading?
La programación con hilos para realizar paralelismo ofrece varias ventajas una de ellas es que al crear varios hilos los cuales son subprocesos que se ejecutan dentro de un mismo espacio de datos, pueden tener el mismo acceso a los datos que el proceso principal por lo cual hace más rápida la comunicación entre ellos de ser necesario. 
Además, al realizar un mismo programa por medio de hilos requiere que se utilicen menos recursos del computador. 

 
# Probabilidad de bayes:
Para realizar el cálculo de Bayes para saber a que categoría pertenece cada URL se realizaron una serie de cálculos. 
Las primeras 3 variables se utilizan para calcular la probabilidad previa, al dividir la cantidad de palabras que tiene el url sobre una categoría y el total de palabras de la misma categoría.
Las siguientes 3 variables se utilizan para calcular la probabilidad final de que el url pertenezca a una u otra categoría lo cual se logra al multiplicar los resultados de las variables anteriores por categoría, por el resultado de la división de la cantidad de las palabras de una categoría entre el total de palabras.
  
![image](https://user-images.githubusercontent.com/61396158/199614769-666f63d5-ae1e-475e-b992-096425fe757a.png)  
  
Luego de estos cálculos se realizan una serie de condicionales para determinar cuál fue la mayor probabilidad y de esta forma asignarle al url la categoría a la que pertenece. 

# Server-Client
Para que nuestro archivo .py funcione como servidor, se debe crear un entorno virtual y posteriomente este se debe activar:
Comando para crear entorno virtual: python3 -m venv venv
Comando para activar entorno virtual: venv\Scripts\activate
*venv es el nombre que se le dio al entorno virtual.*

Luego de tener el entorno virtual activo, se procede a implementar la librería de Flask:

![image](https://user-images.githubusercontent.com/61506908/199640108-b30a6b67-5b16-422b-8dec-d050ce09726a.png)

*app* será nuestra variable que está utilizando la librería de Flask, de manera que luego con esa variable se crean las rutas para generar las APIs necesarias en el proyecto.

![image](https://user-images.githubusercontent.com/61506908/199640264-f5ef4ca9-ee86-43e3-b477-00cd265d4008.png)

Para cada ruta se debe crear una respectiva función, que lleve el mismo nombre de la ruta. Aquí es donde funciona y tiene sentido la librería de Flask, pues lo que retorne la función, quedará en la dirección que corresponde a la ruta, y luego podrá consumirse por medio de un GET.

![image](https://user-images.githubusercontent.com/61506908/199640590-ac6c99df-60b7-4161-9700-a07d128525fb.png)

Finalmente, se debe ejecutar la siguiente línea de código para correr la *app*

![image](https://user-images.githubusercontent.com/61506908/199640742-33c865ff-8a2d-4d3e-b1b9-dbf01bac83c2.png)

El Api generado puede verse la dirección local, del localhost , puerto 5000 y las rutas que asignamos:

 http://localhost:5000/categorizador o http://127.0.0.1:5000/categorizador

![image](https://user-images.githubusercontent.com/61506908/199641448-36ef459f-5c7e-4e00-a0ea-489fc1f55368.png)

 http://localhost:5000/porcentajes o http://127.0.0.1:5000/porcentajes

![image](https://user-images.githubusercontent.com/61506908/199641566-daf83f19-91e8-4253-bbb8-ba8afaf49e03.png)


# Frontend 

# Gráfico
Se ejecuta un GET para obtener los datos generados en el archivo de python, y se agregan esos datos a la variable *porcentajes*

![image](https://user-images.githubusercontent.com/61506908/199642216-a934620c-aa22-4db8-910c-37a57d373f6b.png)

Se renderiza un componente llamado Graph y se envían los datos por parámetro.

![image](https://user-images.githubusercontent.com/61506908/199642627-3813e1ea-b87d-475e-a2bc-662e3beb7a76.png)

# Graph

![image](https://user-images.githubusercontent.com/61506908/199642586-dc5b7363-6d76-4a6c-a687-7193c9a7eb35.png)

# Resultado Graph 

![image](https://user-images.githubusercontent.com/61506908/199645245-66eb12ac-5471-4247-bf96-dcf8b1ac337e.png)


# Tabla de resultados
Se ejecuta un GET para obtener los datos generados en el archivo de python, y se agregan esos datos a la variable *datos*

![image](https://user-images.githubusercontent.com/61506908/199642074-8e46c29f-e7c3-4abe-a15b-02a563b2234f.png)

Se renderiza un componente llamado TableDisplay y se envían los datos por parámetro.

![image](https://user-images.githubusercontent.com/61506908/199642264-d78725b6-724b-4a84-ab97-da616184f45d.png)

# TableDisplay

![image](https://user-images.githubusercontent.com/61506908/199642410-bd7d3b4f-b6f2-4aea-a000-c00ee128dbe2.png)

![image](https://user-images.githubusercontent.com/61506908/199642548-6ccfed01-a447-4dc3-91a0-4b4aad24a09d.png)

# Resultado TableDisplay 

![image](https://user-images.githubusercontent.com/61506908/199645277-17d76af3-e189-428c-bdb2-0c6f8f3eb6f6.png)

# Resultados de la ejecución utilizando hilos
Se ejecutó con 300 links, tardó 21 segundos en ejecutarse.

![image](https://user-images.githubusercontent.com/61506908/199617262-aee1107d-d9cc-44d9-a679-ad885dd9948c.png)

# Resultados de la ejecución secuencial

Se ejecutó con 300 links, tardó 99 segundos en ejecutarse.
![image](https://user-images.githubusercontent.com/61506908/199617078-df8546bd-f9e0-4fb2-af05-38dc6d34d8c5.png)

