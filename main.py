import pymongo
import pandas as pd
import gridfs

# Connection with MongoDB client via PyMongo
connection = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

file = "raw\\K3241.K03200Y0.D10612.csv"

# The CSV file doesn't has headers, so we need to add them
headers = ["cnpj_basico", "cnpj_ordem", "cnpj_dv", "id_matriz_filial", "nome_fantasia","situacao_cadastral",
           "data_situacao_cadastral", "motivo_situacao_cadastral", "nome_cidade_exterior", "pais",
           "data_inicio_atividade", "cnae_principal", "cnae_secundaria", "tipo_logradouro", "logradouro", "numero",
           "complemento", "bairro", "cep", "uf", "municipio", "ddd_1", "telefone_1", "ddd_2", "telefone_2", "ddd_fax",
           "fax", "correio_eletronico", "situacao_especial", "data_situacao_especial"]

# Those are the Pandas types of each column of the CSV
types = {
    "cnpj_basico": 'Int64', "cnpj_ordem": 'Int64', "cnpj_dv": 'Int64', "id_matriz_filial": 'Int64', "nome_fantasia": object,
    "situacao_cadastral": 'Int64', "data_situacao_cadastral": 'Int64', "motivo_situacao_cadastral": 'Int64', "nome_cidade_exterior":
    object, "pais": 'Int64', "data_inicio_atividade": 'Int64', "cnae_principal": 'Int64', "cnae_secundaria": object,
    "tipo_logradouro": object, "logradouro": object, "numero": object, "complemento": object, "bairro": object, "cep": object,
    "uf": object, "municipio": 'Int64', "ddd_1": object, "telefone_1": object, "ddd_2": object, "telefone_2": object, "ddd_fax": object,
    "fax": object, "correio_eletronico": object, "situacao_especial": object, "data_situacao_especial": 'Int64'
}

# Specifying dtypes is crucial to make large data processing faster, as Pandas can only determine dtypes after
# reading the whole DataFrame
df = pd.read_csv(file, names=headers, dtype=types, header=None, sep=';')
df_json = df.to_json(orient='index')

db = connection["speedio"]

# As the maximum size of document insertion on MongoDB is 16MB (and our file is way too big), we need to use GridFS to
# divide the whole document into chunks of data to make in more manageable
fs = gridfs.GridFS(db, collection='estabelecimentos2')

# GridFS only accepts binary data insertion, so we need to convert it
x = fs.put(df_json.encode('ascii'))
