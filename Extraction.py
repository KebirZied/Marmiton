# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 14:39:38 2022

@author: Daniel
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

import pandas as pd 
import numpy as np
######################
from tkinter import *
from tkinter.ttk import *
import sqlite3
import sys
import traceback
######################

def quit(fen):
    """ Récupérer ce qui a été saisi par l'utilisateur"""
    #message.configure(text=nom.get())
    plat=nom.get()
    fen.quit()
    return plat



#################### CREATION DE L'INTERFACE ####################
fen = Tk()

image = PhotoImage(file='Image.png', master=fen) #Importation de l'image
can = Canvas(fen, width =500, height =400, bg ='pink')
can.grid(column=0,row=0,columnspan=3,padx=10, pady=10)
can.create_image((150, 200), image=image)

libelle = Label(can, text='Alors que vous voulez vous préparer aujourdhui :')
libelle.pack()
nom = Entry(can)
nom.pack(pady=180,padx=180)
message = Label(can, text='')
message.pack(padx=10, pady=(0, 10))


b1 = Button(fen, text ='Valider votre choix' ,command=lambda root=fen:quit(fen))
b1.grid(column=0,row=1,padx=200, pady=10)


fen.mainloop()#


driver = webdriver.Chrome()


plat = quit(fen)
print("on fait un test de notre plat",plat)
url = 'https://www.marmiton.org/recettes/recherche.aspx?aqt='+plat
driver.get(url)
button = driver.find_element_by_id('didomi-notice-agree-button')
button.click()
html=driver.page_source
bs = BeautifulSoup(html, "html.parser")


def extract(bs): ## cette fonction permet d'extraire l'ensemble des infos ci-dessous liées au plat choisit (!!! retourne seulement les 3 premières recettes)
    nom=list() ## le nom du plat
    lien = list() ## le lien vers la recette 
    note =list() # la note de la recette 
    review = list() #le nbr de personnes qui ont mis une remarque 
    nom=list(map(lambda i: i.get_text(),bs.find_all('h4',{'class':'MRTN__sc-30rwkm-0 dJvfhM'})))[:3]
    lien = list(map(lambda i: "https://www.marmiton.org"+i.attrs['href'],bs.find_all('a',{'class':'MRTN__sc-1gofnyi-2 gACiYG'})))[:3]
    note = list(map(lambda i: i.get_text(),bs.find_all('span',{'class':'SHRD__sc-10plygc-0 jHwZwD'})))[:3]
    review = list(map(lambda i: i.get_text(),bs.find_all('div',{'class':'MRTN__sc-30rwkm-3 fyhZvB'})))[:3]
    df = pd.DataFrame(np.column_stack([nom,lien,note,review]), columns=['nom','lien','note','review'])
    return df

df=extract(bs)
len(df)

print(df)

def extract_inf(df): ## this function extracts the time, difficulty, and price(budget) and takes the output of the preivous function
    time=list()
    diff = list()
    cout = list()
    for i in range(0,len(df)):
        url = df['lien'][i]
        driver.get(url)
        html=driver.page_source
        bs = BeautifulSoup(html, "html.parser")
        time.append(bs.find_all('p',{'class':'RCP__sc-1qnswg8-1 iDYkZP'})[0].get_text())
        diff.append(bs.find_all('p',{'class':'RCP__sc-1qnswg8-1 iDYkZP'})[1].get_text())
        cout.append(bs.find_all('p',{'class':'RCP__sc-1qnswg8-1 iDYkZP'})[2].get_text())
    df = pd.DataFrame(np.column_stack([time,diff,cout]), columns=['Temps de préparation','difficulté','cout'])
    return df

df
df_2=extract_inf(df)
df_2

## merging the dataframes given by the two previous function
import pandas as pd 
df_f=pd.concat([df, df_2], axis=1)
df_f ## the user should select a reciepe by giving the name the next function will extract the ingrendients

def extract_ing(df_f,i):
    dic = {}
    url = df_f['lien'][i]
    driver.get(url)
    html=driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    poid = bs.find_all('div',{'class':'RCP__sc-8cqrvd-0 hSorOY'})
    
    ing = bs.find_all('span',{'class':'SHRD__sc-10plygc-0 kWuxfa'})
    for i in range(0,len(poid)):
        dic[poid[i].get_text().replace('\xa0g','').replace('\xa0','')] = ing[i].get_text()
        ## sometimes get_text() returns '\xa0' and '\xa0g'
    return dic

extract_ing(df_f,0)

## Display the reciept
def extract_rec (df_f,i): ## extraire la recette 
    url = df_f['lien'][i]
    driver.get(url)
    html=driver.page_source
    bs = BeautifulSoup(html, "html.parser")
    nbr_steps = len(bs.find_all('h3',{'class':'RCP__sc-1wtzf9a-1 ikYBNp'}))
    for i in range(0,nbr_steps):
        print(bs.find_all('h3',{'class':'RCP__sc-1wtzf9a-1 ikYBNp'})[i].get_text())
        print(bs.find_all('p',{'class':'RCP__sc-1wtzf9a-3 jFIVDw'})[i].get_text())
        

extract_rec(df_f,0)
## Steps left commander sur auchan drive 
"""
url = "https://www.auchan.fr/recherche?text=de+poudre+d%27amandes"
driver.get(url)
html=driver.page_source
bs = BeautifulSoup(html, "html.parser")
"""



