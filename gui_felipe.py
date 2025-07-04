from tkinter import * # type: ignore
from Produtos import Produto
from funcoes_felipe import label
from funcoes_felipe import label_entry

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
frame2.place(relx=0.02, rely=0.56, relwidth=0.96, relheight=0.40)

#///Label do Frame1///
label(janela, "Produtos:", "Arial Bold", "#141F81", "White", 30, "10", "14")

#///Label, E as entradas do frame2///
label_produto = label(janela, "Produto:", "Arial Bold", "#141F81", "White", 15, "10", "280")
Label_produto_entry = label_entry("10", "310", "20", "300")

label_preco = label(janela, "Preço:", "Arial Bold", "#141F81", "White", 15, "10", "330")
Label_preco_entry = label_entry("10", "360", "20", "300")

Label_quantidade = label(janela, "Quantidade:", "Arial Bold", "#141F81", "White", 15, "10", "380")
Label_quantidade_entry = label_entry("10", "410", "20", "300")

Label_categoria = label(janela, "Categoria:", "Arial Bold", "#141F81", "White", 15, "10", "430")
Label_categoria_entry = label_entry("10", "460", "20", "300")

#///botão de adicionar Produto///
botao = Button(janela, text="Adicionar Produto", width="15", height="3", fg="White")
botao.place(x="375", y="425")
botao.configure(background="#260033")

janela.mainloop()


