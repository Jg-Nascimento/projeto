from modules import *
from notas import *

class Funcs():
    
    #limpa tela
    def limpa_tela(self):
        self.nota_entry.delete(0, END)
        
    #funcao que conecta ao db
    def conecta_db(self):
        self.conn = sqlite3.connect('notas_fiscais.db');
        self.cursor = self.conn.cursor()
                
    #funcao que deconecta do db
    def desconecta_db(self):
        self.conn.close(); 
    
    def montarTabela(self):
        #conecta a bd
        self.conecta_db();
        
       #cria as tabelas
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_notas(
        nota INTEGER PRIMARY KEY NOT NULL,
        fornecedor TEXT (40) NOT NULL,
        volume INTEGER(6),
        peso VARCHAR(10),
        emissao DATE (8)
        );
        """)
        #validando as informacoes
        self.conn.commit(); 

        #desconecta do bd
        self.desconecta_db(); 
        
    def variaveis(self):
        #col1, col2, col3, col4 = self.listaLink.item(n, 'values')
        #self.data = #pegar data do os
        self.nota =  self.nota_entry.get()
        self.fornecedor = self.fornecedor_entry.get()
        self.volume = self.volume_entry.get()
        self.peso = self.peso_entry.get()
        self.emissao = self.emissao_entry.get()

    #adiciona
    def add_nota(self):
        #self.data =  self.data_entry.get()
        self.nota =  self.nota_entry.get()
        self.fornecedor = self.fornecedor_entry.get()
        self.volume = self.volume_entry.get()
        self.peso = self.peso_entry.get()
        self.emissao = self.emissao_entry.get()

        self.conecta_db()

        try:
            #insere 
            self.cursor.execute("""
            INSERT INTO  tbl_notas (nota, fornecedor, volume, peso, emissao)
                VALUES (?, ?, ?, ?, ?)""", (self.nota, self.fornecedor, self.volume, self.peso, self.emissao))
        except Exception as error:
            print ("ERRO", error)
        
        self.conn.commit();
        self.desconecta_db()
        self.select_nota()
        self.limpa_tela()
    
    def select_nota(self):
        self.listaNota.delete(*self.listaNota.get_children())
        self.conecta_db()

        lista = self.cursor.execute(""" SELECT * FROM  tbl_notas
            ORDER BY nota ASC;  """)

        for i in lista:
            self.listaNota.insert("", END, values=i)
        self.desconecta_db()

    '''====================precisa de permissão para essa tarefa ============================'''
    #apagar registros
    '''def OnDoubleClick(self, event):
                    self.limpa_tela()
                    for n in self.listaNota.selection():
                        col1, col2, col3, col4, col5 = self.listaNota.item(n, 'values')
                        self.nota_entry.insert(END, col1)
                        self.fornecedor_entry.insert(END, col2)
                        self.peso_entry.insert(END, col3)
                        self.volume_entry.insert(END, col4)
                        self.emissao_entry.insert(END, col5)'''
            
    
    #deleta
    def deleta_nota(self):
        self.variaveis()
        self.conecta_db()
        self.cursor.execute("""DELETE FROM tbl_notas WHERE nota = ?""", (self.nota))
        self.conn.commit()
        self.desconecta_db()
        self.conn.commit()
        self.desconecta_db()
        self.limpa_tela()
        self.select_nota()