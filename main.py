# ----------------------------------------------------------------------------------------------------------------
# ADVISE: This program demands heavy memory and CPU usage, so it may take a while to finish running.
# It is highly recommended to close all the applications and not essential background processes before running this
# script. It is also highly recommended not to use the computer during the runtime.
# ----------------------------------------------------------------------------------------------------------------
from writer import write_mongo
from reader import read_mongo
import datetime
import time

if __name__ == "__main__":

    time1 = time.time()
    print("\nADVISE: This program demands heavy memory and CPU usage, so it may take a while to finish running")
    print("Running...")

    if write_mongo():
        print("\nInsertion finished! Now parsing data from MongoDB...")

    if read_mongo():
        print("Excel file created with success! Please check: Speedio-test/excel folder.")

    # Tracking code performance
    time2 = time.time()
    run_time = time2 - time1
    run_time = datetime.timedelta(seconds=run_time)
    print(f"\nRuntime: {run_time}")
