# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:29:46 2022

@author: Daniel
"""

from tkinter import *
from tkinter.ttk import *
import sqlite3
import sys
import traceback




def liste():
    tableau = Treeview(can, columns=('Id','Plats', 'Lien', 'Recette'))
    tableau.heading('Id', text='Id')
    tableau.heading('Plats', text='Plats')
    tableau.heading('Lien', text='Lien')
    tableau.heading('Recette', text='Recette')
    tableau['show'] = 'headings' # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert
    tableau.pack(padx = 10, pady = (0, 10))
    tableau.insert('', 'end', iid=0, values=(0,5, 4, 9))




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


b1 = Button(fen, text ='Valider votre choix' ,command=soumettre_click)
b1.grid(column=0,row=1,padx=200, pady=10)


fen.mainloop()#
