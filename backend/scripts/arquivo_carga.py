import pandas as pd

def agrupar_produtos_por_caminhao(caminho_arquivo):
  df = pd.read_csv(caminho_arquivo, sep=";", encoding="latin1", index_col=False)

  df.columns = df.columns.str.strip()

  # NORMALIZA COLUNAS IMPORTANTES
  df["MAPA"] = df["MAPA"].astype(str).str.strip()
  df["BAIA"] = df["BAIA"].astype(str).str.strip()
  df["PRODUTO"] = df["PRODUTO"].astype(str).str.strip()
  df["QUANTIDADE"] = df["QUANTIDADE"].astype(str).str.strip()

  df["QUANTIDADE"] = pd.to_numeric(df["QUANTIDADE"], errors="coerce")

  # AGRUPA POR CAMINHÃO (MAPA, BAIA E PRODUTO)
  agrupado = (
      df.groupby(["MAPA", "BAIA", "PRODUTO"], as_index=False)
        .agg({"QUANTIDADE": "sum"})
  )


  agrupado = agrupado.sort_values(["MAPA", "BAIA"])

  return agrupado