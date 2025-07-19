from flask import jsonify, request
from models.cliente import db, Cliente
from views.cliente_view import clientes_to_json, cliente_to_json
from utils.validador import validar_cpf

def add_cliente():
    dados = request.get_json()
    cpf = dados.get("cpf")
    try:
        cpf_existente = Cliente.query.filter_by(cpf=cpf).first()

        if cpf_existente:
            return jsonify({"erro": "CPF já cadastrado"}), 400
        

        if not validar_cpf(cpf):
            return jsonify({"erro": "CPF invalido"}), 400
        

        cliente =  Cliente(dados['nomeCompleto'], dados['cpf'], dados['endereco'])
        db.session.add(cliente)
        db.session.commit()
        return cliente_to_json(cliente), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

def get_clientes():
    clientes = Cliente.query.all()
    return clientes_to_json(clientes)

def get_cliente_by_id(id):
    cliente = Cliente.query.get(id)
    if cliente:
        return cliente_to_json(cliente)
    return jsonify({'erro': 'Cliente não encontrado'}), 404


def edite_cliente(id):
    dados = request.get_json()
    try:
        cliente = Cliente.query.get(id)
        cpf = dados.get("cpf", "")

        if cpf != "" and not validar_cpf(cpf=cpf):
            return jsonify({"erro": "CPF invalido"}), 400

        if not cliente:
            raise ValueError(f"Cliente com ID {id} não encontrado.")
        
        for key, value in dados.items():
            if key != 'id':
                setattr(cliente, key, value)

        db.session.commit()
        if cliente:
            return cliente_to_json(cliente)
        
    except ValueError as e:
        return jsonify({"erro": str(e)}), 404

def delete_cliente(id):
    try:
        cliente = Cliente.query.get(id)
        if not cliente:
            return jsonify({"erro": "Cliente não encontrado"}), 404
        
        db.session.delete(cliente)
        db.session.commit()
        
        return cliente_to_json(cliente)
    except ValueError as e:
        return jsonify({"error": str(e)}), 404
    

def delete_clientes():
    try:
        qtd_clientes_deletado = db.session.query(Cliente).delete()
        db.session.commit()
        return jsonify({"mensagem": f"{qtd_clientes_deletado} cliente(s) deletado(s) com sucesso."}), 200
    except ValueError as e:
        db.session.rollback()
        return jsonify({"erro": str(e)}), 500