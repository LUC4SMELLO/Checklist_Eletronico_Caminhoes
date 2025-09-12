from flask import Blueprint, request, redirect, url_for, render_template

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

        resultado = buscar_usuario(nome_completo)

        if resultado:
            erro = "Usuário Já Encontrado."

            return render_template("cadastro.html", erro=erro)
        
        else:

            inserir_usuario(nome_completo, senha)

            return redirect(url_for("checklist.checklist", nome_usuario=nome_completo))

    return render_template("cadastro.html")