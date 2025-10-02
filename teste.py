import pandas as pd


arquivo_cargas = pd.read_csv("CARGA.csv", index_col=False, sep=";")

arquivo_cargas = arquivo_cargas[["DATA MONTAGEM", "MAPA", "VEICULO", "BAIA", "PRODUTO", "QUANTIDADE",
       "UNIDADE", "LASTRO", "CODIGO DE BARRAS"]]

arquivo_cargas["MAPA"] = arquivo_cargas["MAPA"].astype(str)

arquivo_cargas["MAPA"].str.strip()

caminhao_17 = arquivo_cargas[arquivo_cargas["MAPA"] == "7170101"]

caminhao_17_baias_agrupadas = caminhao_17.groupby(["BAIA", "PRODUTO"])["QUANTIDADE"].sum()


teste = pd.concat([caminhao_17, caminhao_17_baias_agrupadas], axis=1)

print(caminhao_17_baias_agrupadas)