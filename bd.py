 # Importa o modulo Python que interfaceia com o gerenciador sqlite
import sqlite3  
import sys
 
 
def main():
    try:
        # Criamos a base de dados, a conexao para ela e um cursor
        conexao = sqlite3.connect('notas_fiscais.db')
        cursor = conexao.cursor()

        # Executa a sentenca SQlite para criar as tabelas
        #tabela nota
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tbl_notas(
            data date
            nota INTEGER,
            fornecedor CHAR(40) NOT NULL,
            volume INTEGER(6),
            peso FLOAT(7),
            emissao DATE
            )""")

        # Insere dados nas tabelas
        #tb_nota
        cursor.execute("INSERT INTO tbl_notas VALUES (null,'data', 'nota', 'fornecedor', 'volume', 'peso', 'emissao')")
        '''cursor.execute("INSERT INTO tbl_notas VALUES (null,'cameras fotograficas analogicas', 'G002','5')")
                                     cursor.execute("INSERT INTO tbl_notas VALUES (null,'placas circuitos não populadas', 'H001','500')")
                                     cursor.execute("INSERT INTO tbl_notas VALUES (null,'descricao falsa', '1234','999')")'''     
     
        # Realiza a transacao e fecha a conexao
        conexao.commit()
        cursor.close()
        conexao.close()
        return 0
     
    except sqlite3.Error:
     
        print ("Erro  %s:" % e.args[0])
        sys.exit(1)
   
 
if __name__ == '__main__':
    main()