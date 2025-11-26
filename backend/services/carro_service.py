from repositories.carro_repo import CarroRepository
import uuid

class CarroService:
    def __init__(self):
        self.repo = CarroRepository()

    def registrar_carro(self, modelo, ano, placa, imagem):
        if int(ano) > 2025:
            raise Exception("Ano inválido! Não aceitamos carros do futuro.")
        
        # Imagem padrão caso não seja informada
        if not imagem:
            imagem = "https://images.unsplash.com/photo-1533473359331-0135ef1b58bf?auto=format&fit=crop&w=500&q=60"

        novo_carro = {
            "id": str(uuid.uuid4()),
            "modelo": modelo,
            "ano": ano,
            "placa": placa,
            "imagem": imagem
        }
        return self.repo.salvar(novo_carro)

    def buscar_carros(self, termo=None):
        if termo:
            return self.repo.filtrar(termo)
        return self.repo.listar_todos()

    def atualizar_carro(self, id_carro, modelo, ano, placa, imagem):
        if int(ano) > 2025:
            raise Exception("Ano inválido!")
        
        dados = {"modelo": modelo, "ano": ano, "placa": placa, "imagem": imagem}
        return self.repo.atualizar(id_carro, dados)

    def excluir_carro(self, id_carro):
        return self.repo.excluir(id_carro)