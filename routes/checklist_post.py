from flask import Blueprint, request, render_template
from database.banco_dados_checklist import inserir_checklist

checklist_post_bp = Blueprint("checklist_post", __name__)

@checklist_post_bp.route("/resultado_checklist", methods=["POST"])
def resultado_checklist():

    data = request.form.get("data", "vazio")
    usuario = request.form.get("usuario", "vazio")
    caminhao = request.form.get("numero_caminhao", "vazio")
    pneu = request.form.get("pneu", "vazio")
    estepe = request.form.get("estepe", "vazio")
    adesivos_refletivos = request.form.get("adesivos_refletivos", "vazio")
    cinto_seguranca = request.form.get("cinto_seguranca", "vazio")
    freio = request.form.get("freio", "vazio")
    tacografo = request.form.get("tacografo", "vazio")
    luzes = request.form.get("luzes", "vazio")
    farois = request.form.get("farois", "vazio")
    indicadores = request.form.get("indicadores", "vazio")
    documentos = request.form.get("documento", "vazio")
    observacao = request.form.get("observacao", "vazio")

    inserir_checklist(
        data,
        usuario,
        caminhao,
        pneu,
        estepe,
        adesivos_refletivos,
        cinto_seguranca,
        freio,
        tacografo,
        luzes,
        farois,
        indicadores,
        documentos,
        observacao,
        )

    return render_template(
        "resultado.html",
        data=data,
        usuario=usuario,
        caminhao=caminhao,
        pneu=pneu,
        estepe=estepe,
        adesivos_refletivos=adesivos_refletivos,
        cinto_seguranca=cinto_seguranca,
        freio=freio,
        tacografo=tacografo,
        luzes=luzes,
        farois=farois,
        indicadores=indicadores,
        documentos_veiculo=documentos,
        observacao=observacao,
        )