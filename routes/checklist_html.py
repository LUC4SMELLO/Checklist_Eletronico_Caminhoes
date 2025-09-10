from flask import Blueprint, render_template

checklist_bp = Blueprint("checklist", __name__)

@checklist_bp.route("/checklist/<nome_usuario>")
def checklist(nome_usuario):
    return render_template("checklist.html", nome_usuario=nome_usuario)