from flask import Blueprint, request, flash, redirect, url_for, render_template

from backend.models.usuarios import Usuario

from backend.validadores.validador_cadastro import validar_cadastro

cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    if request.method == "POST":

        nome_completo = request.form.get("nome_completo").rstrip()
        senha = request.form.get("senha").rstrip()

        valido, mensagem = validar_cadastro(nome_completo, senha)
        if not valido:
            flash(mensagem, "erro")
            return render_template("cadastro.html")

        else:
            
            novo_usuario = Usuario(nome_completo, senha)

            novo_usuario.inserir_usuario()

            return redirect(url_for("picking.picking"))

    return render_template("cadastro.html")