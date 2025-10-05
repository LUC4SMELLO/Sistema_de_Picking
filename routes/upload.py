from flask import Blueprint, request, render_template
import os

upload_bp = Blueprint("upload", __name__)

UPLOAD_FOLDER = 'uploads'

@upload_bp.route('/upload', methods=['POST'])
def upload():

    foto = request.files['foto']

    if foto:
        caminho = os.path.join(UPLOAD_FOLDER, foto.filename)
        foto.save(caminho)
        return f"Foto recebida e salva em: {caminho}"
    
    else:
        return "Nenhum arquivo enviado"
