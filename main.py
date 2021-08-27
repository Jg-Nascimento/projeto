from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
#from PIL import ImageTk, ImageTkimport
from datetime import date
from functions import Funcs
from cadastro import *
from nota import novaNota
from visitantes import novoVisitante

root = Tk()

#font das variaveis
font1 = ('verdana', 9, 'bold')
#font para titulos dos frames
font2=('verdana', 15, 'bold')

class App(Funcs, novoCadastros, novaNota, novoVisitante):
  #inicializa os componentes da janela
  def __init__(self):
    self.root = root
    self.Tela()
    self.Menus()
    self.entradaNotas()
    self.totalRecuperados()
    self.controleCarnes()
    #self.Botoes()
    
    root.mainloop()
 
  #configurações da tela
  def Tela(self):
    self.root.title("GESTÃO")
    #self.root.geometry('1366x768')
    self.root.geometry('1366x768')
    #self.root.configure(background='#2F4F4F')
    self.root.resizable(True, True)
    #self.root.maxsize(width=900, height=700)
    #self.root.minsize(width=500, height=300)

  def Login(self):
    self.login = Toplevel()
    self.login.title("CADASTRO DE FISCAL")
    self.login.configure(background='lightblue')
    self.login.geometry("400x350")
    self.login.resizable(False, False)
    self.login.transient(self.root)
    self.login.focus_force()#mantem a sobreposiçõa da janela
    self.login.grab_set()#não permite a troca entre janelas
    
    self.login.mainloop()

  #barra de menus
  def Menus(self):
    menubar = Menu(self.root)
    self.root.config(menu=menubar)
    filemenu = Menu(menubar)
    filemenu1 = Menu(menubar)

    def Quit(): self.root.destroy()

    #MENU 
    menubar.add_cascade(label='NOVO', menu=filemenu)
    filemenu.add_command(label='FISCAL', command=self.Cadastro)
    filemenu.add_command(label='VISITANTES', command=self.Visitante)
    
    #MENU1 LOGIN
    menubar.add_cascade(label='LOGIN', menu=filemenu1, )
    filemenu1.add_command(label='LOGIN', command=self.Login)
  
    #================================ aba1 ================================
    self.abas = ttk.Notebook(self.root)
    self.aba1 = Frame(self.abas)
        
    self.aba1.configure(background='gray')
    self.abas.add(self.aba1, text='ENTRADA DE NOTAS')# DE NOTAS')

    #frame para formulário de entrada de notas
    self.fr_entrada = Frame(self.aba1, bd=4, bg='#696969',
                        highlightbackground='#000', highlightthickness=2)
    self.fr_entrada.place(relx=0.01, rely=0.08,relwidth=0.25, relheight=0.45)

    #titulo do frame
    self.lb_titulo = Label(self.fr_entrada, text='NOTAS', bd=2, bg='#500', 
                            fg='white', font=(font2))
    self.lb_titulo.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.09)

    #formulario para entrada das notas
    self.lb_nota= Label(self.fr_entrada, text='NOTA', bd=2, bg='#000', 
                       fg='white', font=(font1))
    self.lb_nota.place(relx=0.0, rely=0.10, relwidth=0.30, relheight=0.09)
    self.nota_entry = Entry(self.fr_entrada)
    self.nota_entry.place(relx=0.32, rely=0.10, relwidth=0.68, relheight=0.09)

    self.lb_fornecedor = Label(self.fr_entrada, text='FORNECEDOR', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_fornecedor.place(relx=0.0, rely=0.20, relwidth=0.30, relheight=0.09)
    self.fornecedor_entry = Entry(self.fr_entrada)
    self.fornecedor_entry.place(relx=0.32, rely=0.20, relwidth=0.68, relheight=0.09)

    self.lb_volume = Label(self.fr_entrada, text='VOLUME', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_volume.place(relx=0.0, rely=0.30, relwidth=0.30, relheight=0.09)
    self.volume_entry = Entry(self.fr_entrada)
    self.volume_entry.place(relx=0.32, rely=0.30, relwidth=0.68, relheight=0.09)

    self.lb_peso = Label(self.fr_entrada, text='PESO', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_peso.place(relx=0.0, rely=0.40, relwidth=0.30, relheight=0.09)
    self.peso_entry = Entry(self.fr_entrada)
    self.peso_entry.place(relx=0.32, rely=0.40, relwidth=0.68, relheight=0.09)

    self.lb_emissao = Label(self.fr_entrada, text='EMISSAO', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_emissao.place(relx=0.0, rely=0.50, relwidth=0.30, relheight=0.09)
    self.emissao_entry = Entry(self.fr_entrada)
    self.emissao_entry.place(relx=0.32, rely=0.50, relwidth=0.68, relheight=0.09)

    #botao salvar
    self.btn_salvar = Button(self.fr_entrada, text="SALVAR", bd=2, bg='#000', fg='white',
                            font=(font1), command=self.add_nota)
    self.btn_salvar.place(relx=0.65, rely=0.60, relwidth=0.35, relheight=0.09)

    #total de entradad e notas 
    self.fr_total = Frame(self.aba1, bd=4, bg='#696969', 
                          highlightbackground='#000', highlightthickness=2)
    self.fr_total.place(relx=0.01, rely=0.54,relwidth=0.25, relheight=0.29)

    self.lb_total_notas = Label(self.fr_total, text='TOTAL DE ENTRADAS', bd=4, bg='#500', fg='white',
                                font=(font2))
    self.lb_total_notas.place(relx=0.0, rely=0.01, relwidth=1, relheight=0.15)

    self.lb_nota= Label(self.fr_total, text='NOTAS', bd=2, bg='#000', 
                       fg='white', font=(font1))
    self.lb_nota.place(relx=0.0, rely=0.19, relwidth=0.30, relheight=0.1)
    self.nota_entry = Entry(self.fr_total)
    self.nota_entry.place(relx=0.32, rely=0.19, relwidth=0.68, relheight=0.1)

    self.lb_peso = Label(self.fr_total, text='PESO', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_peso.place(relx=0.0, rely=0.31, relwidth=0.30, relheight=0.1)
    self.peso_entry = Entry(self.fr_total)
    self.peso_entry.place(relx=0.32, rely=0.31, relwidth=0.68, relheight=0.1)


    #frame  historico das entradas de notas
    self.fr_registro = Frame(self.aba1, bd=4, bg='#000', 
                        highlightbackground='#aaa', highlightthickness=2)
    self.fr_registro.place(relx=0.28, rely=0.08,relwidth=0.70, relheight=0.75)
    
  def entradaNotas(self):
    self.lb_total_notas = Label(self.fr_registro, text='ENTRADA DE NOTAS', bd=4, bg='#696969', 
                                fg='white', font=(font2))
    self.lb_total_notas.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.07)

    self.listaNota = ttk.Treeview(self.fr_registro, height=3,
                                column=('col0', 'col1', 
                                'col2', 'col3', 'col4'))
    self.listaNota.heading('#0', text='DATA')
    self.listaNota.heading('#1', text='NOTA')
    self.listaNota.heading('#2', text='FORNECEDOR')
    self.listaNota.heading('#3', text='VOLUME')
    self.listaNota.heading('#4', text='PESO')
    self.listaNota.heading('#5', text='EMISSAO')
        
    self.listaNota.column('#0', width=50)
    self.listaNota.column('#1', width=50)
    self.listaNota.column('#2', width=100)
    self.listaNota.column('#3', width=50)
    self.listaNota.column('#4', width=50)
    self.listaNota.column('#5', width=50)
                
    self.listaNota.place(relx=0.0, rely=0.08, relwidth=0.98, relheight=0.92)
   
    #barra de rolagem
    self.scroolLista = Scrollbar(self.fr_registro, orient='vertical')
    self.listaNota.configure(yscroll=self.scroolLista.set)
    self.scroolLista.place(relx=0.98,rely=0.08, relwidth=0.02, relheight=0.92)
    #self.listaNota.bind("<Double-1>", self.OnDoubleClick)
  
    #================================ aba2 ================================
    self.aba2 = Frame(self.abas)
    self.aba2.configure(background='gray')
    self.abas.add(self.aba2, text='RECUPERADOS')

    #self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame para controle de recuperados
    self.fr_entrada = Frame(self.aba2, bd=2, bg='#696969', 
                        highlightbackground='#000', highlightthickness=2)
    self.fr_entrada.place(relx=0.01, rely=0.08,relwidth=0.25, relheight=0.45)

    #titulo do frame
    self.lb_titulo = Label(self.fr_entrada, text='VALOR RECUPERADO', bd=2, bg='#500', 
                            fg='white', font=(font2))
    self.lb_titulo.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.09)

    #formulario para contrle de recuperados
    self.lb_prevencao= Label(self.fr_entrada, text='PREVENCAO', bd=2, bg='#000', 
                       fg='white', font=(font1))
    self.lb_prevencao.place(relx=0.0, rely=0.10, relwidth=0.35, relheight=0.09)
    self.prevencao_entry = Entry(self.fr_entrada)
    self.prevencao_entry.place(relx=0.37, rely=0.10, relwidth=0.63, relheight=0.09)

    self.lb_departamento = Label(self.fr_entrada, text='DEPARTAMENTO', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_departamento.place(relx=0.0, rely=0.20, relwidth=0.35, relheight=0.09)
    self.departamento_entry = Entry(self.fr_entrada)
    self.departamento_entry.place(relx=0.37, rely=0.20, relwidth=0.63, relheight=0.09)

    self.lb_fornecedor = Label(self.fr_entrada, text='FORNECEDOR', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_fornecedor.place(relx=0.0, rely=0.30, relwidth=0.35, relheight=0.09)
    self.fornecedor_entry = Entry(self.fr_entrada)
    self.fornecedor_entry.place(relx=0.37, rely=0.30, relwidth=0.63, relheight=0.09)

    self.lb_valor = Label(self.fr_entrada, text='VALOR', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_valor.place(relx=0.0, rely=0.40, relwidth=0.35, relheight=0.09)
    self.valor_entry = Entry(self.fr_entrada)
    self.valor_entry.place(relx=0.37, rely=0.40, relwidth=0.63, relheight=0.09)
  
    #radio button   
    Radiobutton(self.fr_entrada, text='DESCONTO EM NOTA', value=1, command=lambda:clicked()).place(relx=0.0, rely=0.50)
    Radiobutton(self.fr_entrada, text='NOTA FISCAL', value=1,command=lambda:clicked()).place(relx=0.0, rely=0.60)
    Radiobutton(self.fr_entrada, text='TROCA', value=1,command=lambda:clicked()).place(relx=0.0, rely=0.70)

    #botao salvar
    self.btn_salvar = Button(self.fr_entrada, text="SALVAR", bd=2, bg='#000', fg='white',
                            font=(font1), command=self.add_nota)
    self.btn_salvar.place(relx=0.65, rely=0.80, relwidth=0.35, relheight=0.09)

    #total de valores recuperados 
    self.fr_total = Frame(self.aba2, bd=4, bg='#696969', 
                          highlightbackground='#000', highlightthickness=2)
    self.fr_total.place(relx=0.01, rely=0.54,relwidth=0.25, relheight=0.29)
    
    #frame  historico de recuperados
    self.lb_titulo = Label(self.fr_total, text='TOTAL RECUPERADO',bd=2, bg='#500', 
                            fg='white', font=(font2))
    self.lb_titulo.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.15)

    self.lb_nf= Label(self.fr_total, text='NOTAS', bd=2, bg='#000', 
                       fg='white', font=(font1))
    self.lb_nf.place(relx=0.0, rely=0.17, relwidth=0.30, relheight=0.1)
    self.nf_entry = Entry(self.fr_total)
    self.nf_entry.place(relx=0.32, rely=0.17, relwidth=0.68, relheight=0.1)

    self.lb_peso = Label(self.fr_total, text='DESCONTO', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_peso.place(relx=0.0, rely=0.29, relwidth=0.30, relheight=0.1)
    self.peso_entry = Entry(self.fr_total)
    self.peso_entry.place(relx=0.32, rely=0.29, relwidth=0.68, relheight=0.1)

    self.lb_valor = Label(self.fr_total, text='VALOR', bd=2,
                               bg='#000', fg='white', font=('verdana', 9, 'bold'))
    self.lb_valor.place(relx=0.0, rely=0.41, relwidth=0.30, relheight=0.1)
    self.valor_entry = Entry(self.fr_total)
    self.valor_entry.place(relx=0.32, rely=0.41, relwidth=0.68, relheight=0.1)

    self.lb_valor = Label(self.fr_total, text='TROCA', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_valor.place(relx=0.0, rely=0.53, relwidth=0.30, relheight=0.1)
    self.valor_entry = Entry(self.fr_total)
    self.valor_entry.place(relx=0.32, rely=0.53, relwidth=0.68, relheight=0.1)

    self.lb_valor = Label(self.fr_total, text='VALOR TOTAL', bd=2,
                               bg='#000', fg='white', font=(font1))
    self.lb_valor.place(relx=0.0, rely=0.65, relwidth=0.30, relheight=0.1)
    self.valor_entry = Entry(self.fr_total)
    self.valor_entry.place(relx=0.32, rely=0.65, relwidth=0.68, relheight=0.1)

    self.fr_registro = Frame(self.aba2, bd=4, bg='#000', 
                        highlightbackground='#aaa', highlightthickness=2)
    self.fr_registro.place(relx=0.28, rely=0.08,relwidth=0.70, relheight=0.75)

  def totalRecuperados(self):
    self.lb_total_notas = Label(self.fr_registro, text='VALORES RECUPERADOS', bd=4, 
                              bg='#696969', fg='white', font=(font2))
    self.lb_total_notas.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.07)

    self.listaValores = ttk.Treeview(self.fr_registro, height=3,
                                column=('col0', 'col1', 'col2', 'col3', 'col4'))
    self.listaValores.heading('#0', text='DATA')
    self.listaValores.heading('#1', text='PREVENCAO')
    self.listaValores.heading('#2', text='DEPARTAMENTO')
    self.listaValores.heading('#3', text='FORNECEDOR')
    self.listaValores.heading('#4', text='VALOR')
    self.listaValores.heading('#5', text='TIPO DE TROCA')
        
    self.listaValores.column('#0', width=50)
    self.listaValores.column('#1', width=50)
    self.listaValores.column('#2', width=100)
    self.listaValores.column('#3', width=50)
    self.listaValores.column('#4', width=50)
    self.listaValores.column('#5', width=50)
                
    self.listaValores.place(relx=0.0, rely=0.08, relwidth=0.98, relheight=0.92)
   
    #barra de rolagem
    self.scroolLista = Scrollbar(self.fr_registro, orient='vertical')
    self.listaNota.configure(yscroll=self.scroolLista.set)
    self.scroolLista.place(relx=0.98,rely=0.08, relwidth=0.02, relheight=0.92)
    #self.listaValor.bind("<Double-1>", self.OnDoubleClick)  

    #================================ aba3 ================================
    self.aba3 = Frame(self.abas)
    self.aba3.configure(background='gray')
    self.abas.add(self.aba3, text='CONTROLE DE CARNES')

    self.abas.place(relx=0, rely=0, relwidth=1, relheight=1)

    #frame para controle de CARNES
    self.fr_entrada = Frame(self.aba3, bd=2, bg='#696969', 
                        highlightbackground='#000', highlightthickness=2)
    self.fr_entrada.place(relx=0.01, rely=0.08,relwidth=0.25, relheight=0.45)

    #titulo do frame
    self.lb_titulo = Label(self.fr_entrada, text='ENTRADA DE CARNES', bd=2, bg='#500', 
                            fg='white', font=(font2))
    self.lb_titulo.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.09)
    
    self.lb_cod= Label(self.fr_entrada, text='CÓDIGO', bd=2, bg='#000', 
                       fg='white', font=(font1))
    self.lb_cod.place(relx=0.0, rely=0.10, relwidth=0.30, relheight=0.1)
    self.cod_entry = Entry(self.fr_entrada)
    self.cod_entry.place(relx=0.32, rely=0.10, relwidth=0.68, relheight=0.1)

    self.lb_volume = Label(self.fr_entrada, text='VOLUME', bd=2, bg='#000',
                          fg='white', font=(font1))   
    self.lb_volume.place(relx=0.0, rely=0.21, relwidth=0.30, relheight=0.1)
    self.volume_entry = Entry(self.fr_entrada)
    self.volume_entry.place(relx=0.32, rely=0.21, relwidth=0.68, relheight=0.1)

    self.lb_descricao = Label(self.fr_entrada, text='DESCRIÇÃO', bd=2, bg='#000', 
                            fg='white', font=(font1))
    self.lb_descricao.place(relx=0.0, rely=0.32, relwidth=0.30, relheight=0.1)

    self.fr_registro = Frame(self.aba3, bd=4, bg='#000', 
                        highlightbackground='#aaa', highlightthickness=2)
    self.fr_registro.place(relx=0.28, rely=0.08,relwidth=0.70, relheight=0.75)

  def controleCarnes(self):
    self.lb_carnes = Label(self.fr_registro, text='CONTROLE DE CARNES', bd=4, bg='#696969', 
                                fg='white', font=(font2))
    self.lb_carnes.place(relx=0.0, rely=0.0, relwidth=1, relheight=0.07)

    self.listaNota = ttk.Treeview(self.fr_registro, height=3,
                                column=('col0', 'col1', 
                                'col2', 'col3', 'col4'))
    self.listaNota.heading('#0', text='DATA')
    self.listaNota.heading('#1', text='NOTA')
    self.listaNota.heading('#2', text='FORNECEDOR')
    self.listaNota.heading('#3', text='VOLUME')
    self.listaNota.heading('#4', text='PESO')
    self.listaNota.heading('#5', text='EMISSAO')
        
    self.listaNota.column('#0', width=50)
    self.listaNota.column('#1', width=50)
    self.listaNota.column('#2', width=100)
    self.listaNota.column('#3', width=50)
    self.listaNota.column('#4', width=50)
    self.listaNota.column('#5', width=50)
                
    self.listaNota.place(relx=0.0, rely=0.08, relwidth=0.98, relheight=0.92)
   
    #barra de rolagem
    self.scroolLista = Scrollbar(self.fr_registro, orient='vertical')
    self.listaNota.configure(yscroll=self.scroolLista.set)
    self.scroolLista.place(relx=0.98,rely=0.08, relwidth=0.02, relheight=0.92)
    #self.listaNota.bind("<Double-1>", self.OnDoubleClick)
      
    
App()