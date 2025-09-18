from flask import Blueprint, request, flash, redirect, url_for, render_template

from database.banco_dados_usuarios import (
    buscar_usuario,
    inserir_usuario
)

cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome_completo = request.form.get("nome_completo")
        senha = request.form.get("senha")

        resultado = buscar_usuario(nome_completo, senha)

        if resultado:
            flash("Usuário Já Encontrado.", "erro")
            return render_template("cadastro.html")
        
        else:
            inserir_usuario(nome_completo, senha)
            
            flash("Cadastro Bem Sucedido!", "sucesso")
            return redirect(url_for("checklist.checklist", nome_usuario=nome_completo))

    return render_template("cadastro.html")