from modules import *
#import teste

class novoCadastros():
    def Cadastro(self):
        self.cadastro = Toplevel()
        self.cadastro.title("CADASTRO DE FISCAL")
        self.cadastro.configure(background='lightblue')
        self.cadastro.geometry("400x350")
        self.cadastro.resizable(False, False)
        self.cadastro.transient(self.root)
        self.cadastro.focus_force()#mantem a sobreposiçõa da janela
        self.cadastro.grab_set()#não permite a troca entre janelas
        
        self.lb_nome = Label(self.cadastro, text='NOME', bd=2, bg='#000', 
                            fg='white', font=('verdana', 10, 'bold'))
        self.lb_nome.place(relx=0.1, rely=0.07, relwidth=0.17, relheight=0.07)

        self.nome_entry = Entry(self.cadastro).place(relx=0.28, rely=0.07, 
                                relwidth=0.40, relheight=0.07)
        
        self.lb_loja = Label(self.cadastro, text='LOJA', bd=2, bg='#000', 
                            fg='white', font=('verdana', 10, 'bold'))
        self.lb_loja.place(relx=0.1, rely=0.15, relwidth=0.17, relheight=0.07)

        self.loja_entry = Entry(self.cadastro).place(relx=0.28, rely=0.15, 
                                relwidth=0.40, relheight=0.07)

        self.lb_senha = Label(self.cadastro, text='SENHA', bd=2, bg='#000', 
                              fg='white', font=('verdana', 9, 'bold'))
        self.lb_senha.place(relx=0.1, rely=0.23, relwidth=0.17, relheight=0.07)

        self.senha_entry = Entry(self.cadastro).place(relx=0.28, rely=0.23,
                                 relwidth=0.40, relheight=0.07)

        self.cadastro.mainloop()
