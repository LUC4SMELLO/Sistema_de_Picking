from flask import Blueprint, request, flash, redirect, url_for, render_template


picking_bp = Blueprint("picking", __name__)

@picking_bp.route("/picking", methods=["GET", "POST"])
def picking():
    
    return render_template("picking.html")