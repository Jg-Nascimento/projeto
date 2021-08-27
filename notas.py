from modules import *

class novaNota():
    def Notas(self):
        
        self.nota = Toplevel()
        self.nota.title("ENTRADA DE NOTAS")
        self.nota.configure(background='lightblue')
        self.nota.geometry("400x350")
        self.nota.resizable(False, False)
        self.nota.transient(self.aba1)
        self.nota.focus_force()#mantem a sobreposiçõa da janela
        self.nota.grab_set()#não permite a troca entre janelas
        
        #número da nota
        self.lb_nota= Label(self.fr_entrada, text='NOTA', bd=2, bg='#000', 
                            fg='white', font=('verdana', 9, 'bold'))
        self.lb_nota.place(relx=0.01, rely=0.3, relwidth=0.35, relheight=0.07)

        self.nota_entry = Entry(self.nota)
        self.nota_entry.place(relx=0.5, rely=0.07, relwidth=0.40, relheight=0.07)
        
        #fornecedorfrom notas import *
        self.lb_fornecedor = Label(self.nota, text='FORNECEDOR', bd=2, bg='#000', 
                            fg='white', font=('verdana', 10, 'bold'))
        self.lb_fornecedor.place(relx=0.1, rely=0.15, relwidth=0.35, relheight=0.07)

        self.fornecedor_entry = Entry(self.nota)
        self.fornecedor_entry.place(relx=0.5, rely=0.15, relwidth=0.40, relheight=0.07)
 
        #volume
        self.lb_volume = Label(self.nota, text='VOLUME', bd=2, bg='#000',
                              fg='white', font=('verdana', 10, 'bold'))
        self.lb_volume.place(relx=0.1, rely=0.23, relwidth=0.35, relheight=0.07)

        self.volume_entry = Entry(self.nota)
        self.volume_entry.place(relx=0.5, rely=0.23, relwidth=0.40, relheight=0.07)
      
        # peso
        self.lb_peso = Label(self.nota, text='PESO',  bd=2, bg='#000',
                              fg='white', font=('verdana', 10, 'bold'))
        self.lb_peso.place(relx=0.1, rely=0.31, relwidth=0.35, relheight=0.07)
        self.peso_entry = Entry(self.nota)
        self.peso_entry.place(relx=0.5, rely=0.31, relwidth=0.40, relheight=0.07)

        # emissao    
        self.lb_emissao = Label(self.nota, text='EMISSAO', bd=2, bg='#000',
                              fg='white', font=('verdana', 10, 'bold'))
        self.lb_emissao.place(relx=0.1, rely=0.39, relwidth=0.35, relheight=0.07)    
        self.emissao_entry = Entry(self.nota)
        self.emissao_entry.place(relx=0.5, rely=0.39, relwidth=0.40, relheight=0.07)                      
        
        #botao salvar
        self.btn_salvar = Button(self.nota, text="SALVAR", bd=2, bg='#000', fg='white',
                              font=('verdana', 10, 'bold'), command=self.add_nota)
        self.btn_salvar.place(relx=0.55, rely=0.50, relwidth=0.35, relheight=0.07)

        self.nota.mainloop()


