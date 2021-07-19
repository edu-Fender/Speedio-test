import pandas as pd
import numpy as np
import json

file = "raw\\K3241.K03200Y0.D10612.ESTABELE"

headers = ["cnpj_basico", "cnpj_ordem", "cnpj_dv", "id_matriz_filial", "nome_fantasia","situacao_cadastral",
           "data_situacao_cadastral", "motivo_situacao_cadastral", "nome_cidade_exterior", "pais",
           "data_inicio_atividade", "cnae_principal", "cnae_secundaria", "tipo_logradouro", "logradouro", "numero",
           "complemento", "bairro", "cep", "uf", "municipio", "ddd_1", "telefone_1", "ddd_2", "telefone_2", "ddd_fax",
           "fax", "correio_eletronico", "situacao_especial", "data_situacao_especial"]

types = {
    "cnpj_basico": 'Int64', "cnpj_ordem": 'Int64', "cnpj_dv": 'Int64', "id_matriz_filial": 'Int64', "nome_fantasia": object,
    "situacao_cadastral": 'Int64', "data_situacao_cadastral": 'Int64', "motivo_situacao_cadastral": 'Int64', "nome_cidade_exterior":
    object, "pais": 'Int64', "data_inicio_atividade": 'Int64', "cnae_principal": 'Int64', "cnae_secundaria": object,
    "tipo_logradouro": object, "logradouro": object, "numero": object, "complemento": object, "bairro": object, "cep": object,
    "uf": object, "municipio": 'Int64', "ddd_1": object, "telefone_1": object, "ddd_2": object, "telefone_2": object, "ddd_fax": object,
    "fax": object, "correio_eletronico": object, "situacao_especial": object, "data_situacao_especial": 'Int64'
}


df = pd.read_csv(file, names=headers, dtype=types, header=None, sep=';')
df = df.replace(np.nan, '')

df_json = df.to_json(orient='index')
df_json = json.loads(df_json)