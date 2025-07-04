from tkinter import * # type: ignore
from Produtos import Produto


#///janela///
janela = Tk()
janela.title("FELIPE PRODUTOS")
janela.geometry("500x500")
janela.resizable(False, False)
janela.configure(background="#050A30")

#///Frame///
frame1 = Frame(background="#000C66")
frame1.place(relx= 0.02 , rely=0.13, relwidth= 0.96,relheight= 0.41)

frame2 = Frame(background="#000C66")
frame2.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.41)

#///Label///
label_titulo = Label(janela, text="Produtos:", font=("Arial Bold", 30), bg="#260033", fg="White")
label_titulo.place(x="8", y="10")
#///Label, E as entradas do frame2 

Label_produto = Label(janela, text="Produto:", font=("Arial Bold", 15), bg="#260033", fg="White")
Label_produto.place(x="10", y="280")
Label_produto_entry = Entry()
Label_produto_entry.place(x="10", y="310", width="300")

Label_preco = Label(janela, text="Preço:", font=("Arial Bold", 15), bg="#260033", fg="White")
Label_preco.place(x="10", y="330")
Label_preco_entry = Entry()
Label_preco_entry.place(x="10", y="360", width="300")

Label_quantidade = Label(janela, text="Preço:", font=("Arial Bold", 15), bg="#260033", fg="White")
Label_quantidade.place(x="10", y="330")
Label_quantidade_entry = Entry()
Label_quantidade_entry.place(x="10", y="360", width="300")
#///botão///
botao = Button(janela, text="Adicionar Produto", width="15", height="3", fg="White")
botao.place(x="373", y="426")
botao.configure(background="#260033")










janela.mainloop()


