from flask import request
from app import app
from models import carrinho
from routes_produto import *
from utils import procurar_por_id

#Mostrar carrinho
@app.route("/carrinho", methods=["GET"])
def get_carrinho():
    return {"Seu carrinho": carrinho}

@app.route("/carrinho/addProduto/<int:id>", methods=["POST"])
def adicionar_produto_carrinho(id):

    #pegar dados query da url ?quantidade=x
    qnt = request.args.get("qnt", default = 1, type=int)
    produto = procurar_por_id(id)
    if not produto:
        return {"erro": "Produto não encontrado"}, 404
    
    #adicionar ao carrinho
    carrinho.append({
        "produto": produto,
        "quantidade": qnt
        })
    return produto

@app.route("/carrinho/limpar", methods=["DELETE"])
def limpar_carrinho():
    carrinho.clear()
    return {"mensagem": "Carrinho limpo"}, 200