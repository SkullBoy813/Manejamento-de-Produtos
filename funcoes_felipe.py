from tkinter import * # type: ignore
import sqlite3

def label(aba, texto, fonte, background, cor_da_fonte, tamanho_da_fonte, x, y):
    Label_name = Label(aba, text=texto, font=(fonte, tamanho_da_fonte), bg=background, fg=cor_da_fonte)
    Label_name.place(x=x, y=y)
    
def label_entry(x, y, altura, largura):
    Label_name_entry = Entry()
    Label_name_entry.place(x=x, y=y, height=altura, width=largura)