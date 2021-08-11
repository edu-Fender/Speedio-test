from pymongo import MongoClient


def connect(database_name):

    # FIXME: Check this connection string!!
    client = MongoClient("mongodb://127.0.0.1:27017/")

    # Small connection test
    try:
        client.server_info()
    except Exception as e:
        print(f"\nERROR: Please check your connection string and make sure mongod process is running properly. "
              f"\n\nError Details: {e}.")
        quit()

    # Opens or creates database if it doesn't exist
    db = client[database_name]

    return db
