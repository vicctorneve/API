from flask import jsonify

def cliente_to_dict(cliente):
    """Converte um objeto Cliente para um dicionário."""
    return {
        'id': cliente.id,
        'nomeCompleto': cliente.nomeCompleto,
        'cpf': cliente.cpf,
        'endereco': cliente.endereco
    }

def clientes_to_json(clientes):
    """Converte uma lista de clientes para JSON."""
    return jsonify([cliente_to_dict(cliente) for cliente in clientes])

def cliente_to_json(cliente):
    """Converte um único cliente para JSON."""
    return jsonify(cliente_to_dict(cliente))