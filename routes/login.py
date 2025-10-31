from flask import Blueprint, request, flash, redirect, url_for, render_template, session

from backend.models.usuarios import Usuario

from backend.validadores.validador_login import validar_login


login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        nome_completo = request.form.get("nome_completo").rstrip()
        senha = request.form.get("senha").rstrip()

        usuario_buscado = Usuario.buscar_usuario(nome_completo, senha)

        valido, mensagem = validar_login(nome_completo, senha)
        if not valido:
            flash(mensagem, "erro")
            return render_template("login.html")
        
        else:
            session["username"] = nome_completo
            session["user_id"] = usuario_buscado[0]
            return redirect(url_for("picking.picking"))
    
    return render_template("login.html")