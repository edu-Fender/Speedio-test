# ----------------------------------------------------------------------------------
# This script is responsible for inserting the CSV data into the MongoDB database.
# ATTENTION: This is a very hardware demanding script, so it may run for a while.
# ----------------------------------------------------------------------------------

import pandas as pd
import subprocess
import tempfile
import time
import datetime

csv_file = "raw\\K3241.K03200Y0.D10612.csv"


def insert_data_mongodb():

    time1 = time.time()

    # The CSV file doesn't has headers, so we need to add them
    headers = ["cnpj_basico", "cnpj_ordem", "cnpj_dv", "id_matriz_filial", "nome_fantasia", "situacao_cadastral",
               "data_situacao_cadastral", "motivo_situacao_cadastral", "nome_cidade_exterior", "pais",
               "data_inicio_atividade", "cnae_principal", "cnae_secundaria", "tipo_logradouro", "logradouro", "numero",
               "complemento", "bairro", "cep", "uf", "municipio", "ddd_1", "telefone_1", "ddd_2", "telefone_2", "ddd_fax",
               "fax", "correio_eletronico", "situacao_especial", "data_situacao_especial"]

    # Those are the Pandas types of each column of the CSV
    types = {
        "cnpj_basico": 'Int64', "cnpj_ordem": 'Int64', "cnpj_dv": 'Int64', "id_matriz_filial": 'Int64',
        "nome_fantasia": object, "situacao_cadastral": 'Int64', "data_situacao_cadastral": 'Int64',
        "motivo_situacao_cadastral": 'Int64', "nome_cidade_exterior": object, "pais": 'Int64',
        "data_inicio_atividade": 'Int64', "cnae_principal": 'Int64', "cnae_secundaria": object, "tipo_logradouro": object,
        "logradouro": object, "numero": object, "complemento": object, "bairro": object, "cep": object, "uf": object,
        "municipio": 'Int64', "ddd_1": object, "telefone_1": object, "ddd_2": object, "telefone_2": object, "ddd_fax": object,
        "fax": object, "correio_eletronico": object, "situacao_especial": object, "data_situacao_especial": 'Int64'
    }

    # Specifying dtypes is crucial to make large data processing faster, as Pandas can only determine dtypes after
    # reading the whole DataFrame
    df = pd.read_csv(csv_file, names=headers, dtype=types, header=None, sep=';')
    df_json = df.to_json(orient='records')

    # Creates temporary buffer file to store the json data
    with tempfile.NamedTemporaryFile("w+", buffering=8192, delete=False) as tf:
        tf.write(df_json)
        tf.flush()
        # subprocess.run() method is used to call the OS Terminal and run the mongoimport command line tool.
        # numInsertionWorkers => number of threads working on the task. Increase it depending on your processor performance.
        subprocess.run(f"mongoimport -d speedio -c estabelecimentos --drop --file {tf.name} --jsonArray "
                       f"--numInsertionWorkers 4 ", shell=True)

    # Tracking code performance
    time2 = time.time()
    run_time = time2 - time1
    run_time = datetime.timedelta(seconds=run_time)
    print(f"\n Runtime: {run_time}")