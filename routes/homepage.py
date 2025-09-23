from flask import Blueprint, render_template

homepage_bp = Blueprint("/", __name__)

@homepage_bp.route("/", methods=["GET"])
def homepage():
    return render_template("homepage.html")