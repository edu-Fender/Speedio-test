# ----------------------------------------------------------------------------
# This script is responsible for reading and retrieving MongoDB desired data.
# ----------------------------------------------------------------------------
from connection import connect
import collections
import pandas as pd


# TODO: 4. Ler os dados do db e obter as seguintes informações:
def read_mongo():

    db = connect("speedio")
    col = db["estabelecimentos"]

    # TODO: 4.a. qual % das empresas estão ativas (SITUAÇÃO CADASTRAL)
    # Counts every mongodb documents, then counts only the ones where "situacao_cadastral" is 2
    query1 = col.count_documents({})
    query2 = col.count_documents({"situacao_cadastral": 2})

    percentage = round((query2 / query1) * 100)  # Percentage formula

    # Creates Pandas DataFrame with data to be entered into excel file later
    df1 = pd.DataFrame([f"{percentage}%"], columns=["Porcentagem das Empresas em Atividade"])

    # TODO: 4.b. Quantas empresas do setor de restaurantes foram abertas em cada ano ?
    # Returns only the first 4 digits of data_inicio_atividade for all the fields where cnae_principal starts with 561
    query3 = col.aggregate([
        {"$match": {"cnae_principal":
                        {"$gte": 5610000, "$lte": 5619999}}},
        {"$project": {"_id": 0, "data_inicio_atividade":
            {"$toInt":
                {"$divide": [
                    "$data_inicio_atividade", 10000]}}}},
        {"$sort": {"data_inicio_atividade": 1}}
    ], allowDiskUse=True)  # If aggregation buffer exceeds the 100MB threshold, you need to allow disk memory usage

    results = []

    # Retrieves all the matches (years) from 'query3' and appends it into 'result' list
    for i in query3:
        temp = list(i.values())[0]
        results.append(temp)

    # Counts the number of occurrences of each item (year) in the list
    count = collections.Counter(results)
    count = (count.items())

    df2 = pd.DataFrame(count, columns=["Ano", "Restaurantes Abertos"])

    # TODO: 5. Exportar os dados do ponto 4 para um CSV (BONUS POINTS: exportar para formato excel)
    try:
        writer = pd.ExcelWriter('excel/empresas.xlsx', engine='openpyxl')
    except PermissionError as e:
        print(f"\nERROR: Please close Excel and try again ({e}).")
        return

    # Converts data from Pandas DataFrame to Excel file
    df2.to_excel(writer, sheet_name="sheet1", index=False)
    df1.to_excel(writer, sheet_name="sheet1", startcol=3, index=False)

    # Adjust columns width to fit the content
    writer.sheets['sheet1'].column_dimensions['A'].width = 24
    writer.sheets['sheet1'].column_dimensions['B'].width = 24
    writer.sheets['sheet1'].column_dimensions['D'].width = 42
    writer.save()

    return True  # If everything went good, returns True
