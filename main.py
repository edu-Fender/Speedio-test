# ----------------------------------------------------------------------------------------------------------------
# ADVISE: This program demands heavy memory and CPU usage, so it may take a while to finish running.
# It is highly recommended to close all the applications and not essential background processes before running this
# script. It is also highly recommended not to use the computer during the runtime.
# ----------------------------------------------------------------------------------------------------------------
import insert_mongodb
import read_mongodb
import datetime
import time

if __name__ == "__main__":

    time1 = time.time()
    print("\nADVISE: This program demands heavy memory and CPU usage, so it may take a while to finish running")
    print("Running...\n")

    if insert_mongodb.insert_mongodb():
        print("\nInsertion finished! Now parsing the data from MongoDB...")

    if read_mongodb.read_mongodb():
        print("Excel file created with success! Please check: Speedio-test/excel folder.")

    # Tracking code performance
    time2 = time.time()
    run_time = time2 - time1
    run_time = datetime.timedelta(seconds=run_time)
    print(f"\nRuntime: {run_time}")
