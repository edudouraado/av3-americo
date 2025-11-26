from repositories.carro_repo import CarroRepository
import uuid

class CarroService:
    def __init__(self):
        self.repo = CarroRepository()

    def registrar_carro(self, modelo, ano, placa):
        if int(ano) > 2025:
            raise Exception("Ano inválido!")
        
        novo_carro = {
            "id": str(uuid.uuid4()),
            "modelo": modelo,
            "ano": ano,
            "placa": placa
        }
        return self.repo.salvar(novo_carro)

    # ATUALIZADO: Aceita termo de busca opcional
    def buscar_carros(self, termo=None):
        if termo:
            return self.repo.filtrar(termo)
        return self.repo.listar_todos()

    # NOVO
    def atualizar_carro(self, id_carro, modelo, ano, placa):
        if int(ano) > 2027:
            raise Exception("Ano inválido!")
        
        dados = {"modelo": modelo, "ano": ano, "placa": placa}
        return self.repo.atualizar(id_carro, dados)

    def excluir_carro(self, id_carro):
        return self.repo.excluir(id_carro)