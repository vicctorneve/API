from flask import Blueprint
from controllers.cliente_controller import (
    get_clientes,
    get_cliente_by_id,
    add_cliente,
    edite_cliente,
    delete_cliente,
    delete_clientes
)

cliente_bp = Blueprint("cliente", __name__)

cliente_bp.route("/clientes", methods=["GET"])(get_clientes)
cliente_bp.route("/cliente/<int:id>", methods=["GET"])(get_cliente_by_id)
cliente_bp.route("/cliente/<int:id>", methods=["DELETE"])(delete_cliente)
cliente_bp.route("/clientes", methods=["DELETE"])(delete_clientes)
cliente_bp.route("/cliente", methods=["POST"])(add_cliente)
cliente_bp.route("/cliente/<int:id>", methods=["PUT"])(edite_cliente)
