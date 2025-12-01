import os
import psycopg2
from psycopg2.extras import RealDictCursor

class CarroRepository:
    def __init__(self):
        # Pega a URL do banco das Variáveis de Ambiente (Configuraremos no Render)
        self.db_url = os.getenv('DATABASE_URL')
        self._criar_tabela()

    def _get_connection(self):
        return psycopg2.connect(self.db_url, cursor_factory=RealDictCursor)

    def _criar_tabela(self):
        # SQL para criar a tabela se ela não existir
        sql = """
        CREATE TABLE IF NOT EXISTS carros (
            id VARCHAR(255) PRIMARY KEY,
            modelo VARCHAR(255) NOT NULL,
            ano VARCHAR(4) NOT NULL,
            placa VARCHAR(20) NOT NULL,
            imagem TEXT
        );
        """
        try:
            conn = self._get_connection()
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")

    def salvar(self, carro):
        sql = "INSERT INTO carros (id, modelo, ano, placa, imagem) VALUES (%s, %s, %s, %s, %s)"
        conn = self._get_connection()
        cur = conn.cursor()
        cur.execute(sql, (carro['id'], carro['modelo'], carro['ano'], carro['placa'], carro['imagem']))
        conn.commit()
        cur.close()
        conn.close()
        return carro

    def listar_todos(self):
        sql = "SELECT * FROM carros"
        conn = self._get_connection()
        cur = conn.cursor()
        cur.execute(sql)
        carros = cur.fetchall() # Retorna uma lista de dicionários reais do banco
        cur.close()
        conn.close()
        return carros

    def filtrar(self, termo):
        termo = f"%{termo}%" # Formato para o LIKE do SQL
        sql = "SELECT * FROM carros WHERE LOWER(modelo) LIKE LOWER(%s) OR LOWER(placa) LIKE LOWER(%s)"
        conn = self._get_connection()
        cur = conn.cursor()
        cur.execute(sql, (termo, termo))
        carros = cur.fetchall()
        cur.close()
        conn.close()
        return carros

    def atualizar(self, id_carro, novos_dados):
        # Primeiro verificamos se precisa atualizar a imagem ou mantemos a antiga
        sql_check = "SELECT imagem FROM carros WHERE id = %s"
        
        conn = self._get_connection()
        cur = conn.cursor()
        
        # Pega imagem atual
        cur.execute(sql_check, (id_carro,))
        resultado = cur.fetchone()
        
        if not resultado:
            return None # Carro não existe

        # Define qual imagem usar (a nova ou a antiga)
        imagem_final = novos_dados.get('imagem')
        if not imagem_final:
            imagem_final = resultado['imagem']

        # Atualiza
        sql_update = """
            UPDATE carros 
            SET modelo = %s, ano = %s, placa = %s, imagem = %s 
            WHERE id = %s
        """
        cur.execute(sql_update, (novos_dados['modelo'], novos_dados['ano'], novos_dados['placa'], imagem_final, id_carro))
        conn.commit()
        
        # Retorna o objeto atualizado
        carro_atualizado = {
            "id": id_carro,
            "modelo": novos_dados['modelo'],
            "ano": novos_dados['ano'],
            "placa": novos_dados['placa'],
            "imagem": imagem_final
        }
        
        cur.close()
        conn.close()
        return carro_atualizado

    def excluir(self, id_carro):
        sql = "DELETE FROM carros WHERE id = %s"
        conn = self._get_connection()
        cur = conn.cursor()
        cur.execute(sql, (id_carro,))
        conn.commit()
        cur.close()
        conn.close()
        return True