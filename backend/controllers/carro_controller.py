from flask import Blueprint, request, jsonify
from services.carro_service import CarroService

carro_bp = Blueprint('carro', __name__)
service = CarroService()

@carro_bp.route('/carros', methods=['POST'])
def criar():
    dados = request.json
    try:
        img = dados.get('imagem')
        carro = service.registrar_carro(dados['modelo'], dados['ano'], dados['placa'], img)
        return jsonify(carro), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@carro_bp.route('/carros', methods=['GET'])
def listar():
    termo = request.args.get('termo')
    return jsonify(service.buscar_carros(termo))

@carro_bp.route('/carros/<id_carro>', methods=['PUT'])
def editar(id_carro):
    dados = request.json
    try:
        img = dados.get('imagem')
        carro = service.atualizar_carro(id_carro, dados['modelo'], dados['ano'], dados['placa'], img)
        if carro:
            return jsonify(carro), 200
        return jsonify({"erro": "Carro não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@carro_bp.route('/carros/<id_carro>', methods=['DELETE'])
def deletar(id_carro):
    service.excluir_carro(id_carro)
    return jsonify({"mensagem": "Carro removido"}), 200