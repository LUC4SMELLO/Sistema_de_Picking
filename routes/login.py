from flask import Blueprint, request, flash, redirect, url_for, render_template

from backend.validadores.validador_login import validar_login

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        nome_completo = request.form.get("nome_completo")
        senha = request.form.get("senha")

        valido, mensagem = validar_login(nome_completo, senha)
        if not valido:
            flash(mensagem, "erro")
            return render_template("login.html")
    
    return render_template("login.html")