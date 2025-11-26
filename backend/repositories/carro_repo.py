# Simulando um banco de dados em memória
banco_de_dados = []

class CarroRepository:
    def salvar(self, carro):
        banco_de_dados.append(carro)
        return carro

    def listar_todos(self):
        return banco_de_dados

    def filtrar(self, termo):
        termo = termo.lower()
        return [c for c in banco_de_dados if termo in c['modelo'].lower() or termo in c['placa'].lower()]

    def atualizar(self, id_carro, novos_dados):
        for carro in banco_de_dados:
            if carro['id'] == id_carro:
                carro['modelo'] = novos_dados['modelo']
                carro['ano'] = novos_dados['ano']
                carro['placa'] = novos_dados['placa']
                # Só atualiza a imagem se o usuário mandou uma nova
                if novos_dados.get('imagem'):
                    carro['imagem'] = novos_dados['imagem']
                return carro
        return None

    def excluir(self, id_carro):
        global banco_de_dados
        banco_de_dados = [c for c in banco_de_dados if c['id'] != id_carro]
        return True