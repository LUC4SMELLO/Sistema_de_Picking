from flask import Flask, Blueprint, render_template

from backend.scripts.arquivo_carga import agrupar_produtos_por_caminhao


caminhoes_bp = Blueprint("caminhoes", __name__)

@caminhoes_bp.route("/caminhoes")
def caminhoes():
    
    caminho_csv = "CARGA.csv"
    df = agrupar_produtos_por_caminhao(caminho_csv)

    caminhoes_dict = {}

    #CONVERTE O DATAFRAME EM UMA ESTRUTURA DE DICIONÁRIO HIERARQUICA
    for _, linha in df.iterrows():
        mapa = linha["MAPA"]
        baia = linha["BAIA"]
        produto = linha["PRODUTO"]
        qtd = int(linha["QUANTIDADE"])

        if mapa not in caminhoes_dict:
            caminhoes_dict[mapa] = {}
        if baia not in caminhoes_dict[mapa]:
            caminhoes_dict[mapa][baia] = []
        caminhoes_dict[mapa][baia].append({"produto": produto, "quantidade": qtd})


    return render_template("caminhoes.html", caminhoes=caminhoes_dict)
