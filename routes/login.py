from flask import Blueprint, request, flash, redirect, url_for, render_template

from database.banco_dados_usuarios import buscar_usuario

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        nome_completo = request.form.get("nome_completo")
        senha = request.form.get("senha")

        resultado = buscar_usuario(nome_completo, senha)

        if resultado:
            return redirect(url_for("checklist.checklist", nome_usuario=nome_completo))
            
        else:
            flash("Usuário ou Senha Inválido.", "erro")
            return render_template("login.html")
        
    
    return render_template("login.html")
