Clasificador-de-Urls

# Documento de explicacion de proyecto:

  Este proyecto consiste en un clasificador de Urls con base a 3 categorias previamente establecidas por el equipo desarrollador. Se implementó el lenguaje de programación Python en el IDE de Visual Studio Code y la ejecución por hilos del proceso como tal para optimizar el análisis de 12000 Urls.

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
