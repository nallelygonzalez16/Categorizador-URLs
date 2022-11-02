from distutils.log import debug
from turtle import delay
from flask import Flask
from random import random
from bs4 import BeautifulSoup
import csv
import re
import time
import random
from threading import Thread
import requests

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
"engineering","communication","machine","learning","projects","sensor","images","developer","robot",
"technology",
"electrical","security","database","mathematics","simulation","statistics","discrete"]

pageNotFound=[] #this is the array to get all no found pages in a s
info=[]
ContSociedad = []
ContComputadores= []
ContArte = []
ContSinRespuesta = []
ContSinCategoria = []
group=[]

with open('URLS2.csv') as file:
    lector = csv.reader(file)
    for row in lector:
        group.append(row[1])

def connectionToPage(url):
    try:
        page = requests.get(url)
    except:
        
        datos = {"link":url, "categoria":"Sin respuesta", "palabras": "No existen"}
        info.append(datos)
        ContSinRespuesta.append(1)
        
        return 
    if page:
        soup = BeautifulSoup(page.content,"html.parser")
        return soup
    else:
        datos = {"link":url, "categoria":"Sin respuesta", "palabras": "No existen"}
        info.append(datos)
        ContSinRespuesta.append(1)
        return 

def probability(lista, url):
    #[0]= arte, [1]=computadores, [2]= sociedad
    probArte = len(lista[0]) / len(arte)
    probComputadores = len(lista[1]) / len(computadores)
    probSociedad = len(lista[2]) / len(sociedad)
    totalArte = probArte * (len(arte)/182)
    totalComputadores = probComputadores * (len(computadores)/182)
    totalSociedad = probSociedad* (len(sociedad)/182)
    if (totalArte > totalComputadores) and (totalArte > totalSociedad):
        categoria = "Arte"
    elif (totalComputadores > totalArte) and (totalComputadores > totalSociedad):
        categoria = "Computadores"
    elif (totalSociedad > totalArte) and (totalSociedad > totalComputadores):
        categoria = "Sociedad"
    if (totalSociedad == totalArte) and (totalSociedad == totalComputadores):
        categoria = (random.choice(["Sociedad", "Arte", "Computadores"]))
    elif (totalSociedad == totalArte):
        categoria = (random.choice(["Sociedad", "Arte"]))
    elif (totalSociedad == totalComputadores): 
        categoria = (random.choice(["Sociedad", "Computadores"]))
    elif (totalArte == totalComputadores):
        categoria = (random.choice(["Computadores", "Arte"]))
    if categoria == "Arte":
        ContArte.append(1)
        listaElegida = lista[0]
    elif categoria == "Computadores":
        ContComputadores.append(1)
        listaElegida = lista[1]
    elif categoria == "Sociedad":
        ContSociedad.append(1)
        listaElegida = lista[2]
    datos = {"link":url, "categoria":categoria, "palabras": listaElegida}
    info.append(datos)

#check if a word is inside a page and how many times appears 
def checkForKeyWords(allWords, url):
    #[0]= arte, [1]=computadores, [2]= sociedad
    lista = [[],[],[]]
    for keyWord in arte:
        if keyWord in allWords:
            lista[0].append(keyWord)  
    for keyWord in computadores:
        if keyWord in allWords:  
            lista[1].append(keyWord)      
    for keyWord in sociedad:
        if keyWord in allWords: 
            lista[2].append(keyWord)             
    pageNotFound.clear()
    if (len(lista[0]) == 0 ) and (len(lista[1]) == 0 ) and (len(lista[2]) == 0 ):
        datos = {"link":url, "categoria":"Sin Categoría", "palabras": "No existen"}
        info.append(datos)
        ContSinCategoria.append(1)
        #ContSinCategoria = ContSinCategoria + 1
    else:
        probability(lista, url)
    return lista

#Here's begin the process to get all words in the specified tags and append it to a global array called allWords
def ObtainWordsInPage(url):
    allWords=[]  #this is the array to get all words in a page
    soup = connectionToPage(url)
    if soup:
        textP = soup.find_all("p")
        textH1 = soup.find_all("h1")
        textH2 = soup.find_all("h2")
        textSpan = soup.find_all("span")
        textA= soup.find_all("a")

#These for loops iterate in each of the texts founded and separate them based on the criteria if they are letters, numbers, or _  
        for data in textP:
            splitWords = re.findall(r"[\w']+", str(data.get_text()))
            for word in splitWords:
                allWords.append(word)
        for data in textH1:
            splitWords = re.findall(r"[\w']+", str(data.get_text()))
            for word in splitWords:
                allWords.append(word)
        for data in textH2:
            splitWords = re.findall(r"[\w']+", str(data.get_text()))
            for word in splitWords:
                allWords.append(word)
        for data in textSpan:
            splitWords = re.findall(r"[\w']+", str(data.get_text()))
            for word in splitWords:
                allWords.append(word)
        for data in textA:
            splitWords = re.findall(r"[\w']+", str(data.get_text()))
            for word in splitWords:
                allWords.append(word)
        checkForKeyWords(allWords, url)
        allWords.clear()

def get_characters_parallel():
    request_threads = {}
    for page in range(0, (len(group))):
        request_threads[page] = Thread(target=ObtainWordsInPage, kwargs={'url':group[page]})
        request_threads[page].start()
    while(True):
        for key, value in request_threads.copy().items():
            if not value.is_alive():
                del request_threads[key]
        if len(request_threads) < 1:
            break

#Iterates the group number 1 and gets all words that matches with keyWords with each of the websites visited
app = Flask(__name__)

@app.route("/categorizador")
def categorizador():
    return info

@app.route("/porcentajes")
def porcentajes():
    total = 300
    totalSociedad = round(((len(ContSociedad )* 100) / total),2)
    totalComputadores = round(((len(ContComputadores) * 100) / total),2)
    totalArte = round(((len(ContArte) * 100) / total),2)
    totalSinRespuesta = round(((len(ContSinRespuesta) * 100) / total),2)
    totalSinCategoria = round(((len(ContSinCategoria) * 100) / total),2)
    TotalPorcentajes = [{'name':'Sociedad', 'total': totalSociedad},
                        {'name':'Arte' , 'total':totalArte},
                        {'name':'Computadores','total': totalComputadores},
                        {'name':'Sin respuesta', 'total':totalSinRespuesta},
                        {'name':'Sin categoría', 'total':totalSinCategoria},
]
    return TotalPorcentajes


if __name__ == "__main__":
    init = time.time()
    get_characters_parallel()
    print('Time ' + str(time.time() - init))
    app.run(debug=True)