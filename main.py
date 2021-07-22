# ------------------------------------------------------------------------------------------------
# ATTENTION: This is a very hardware demanding program, so it may take a while to finish running.
# ------------------------------------------------------------------------------------------------
import insert_mongodb
import read_mongodb
import datetime
import time

if __name__ == "__main__":

    time1 = time.time()
    print("\nADVISE: This is a very hardware demanding program, so it may take up to 1 hour to finish running"
          " depending on your system specs.")
    print("\nRunning...")

    # Main script, inserts the data
    insert_mongodb.insert_mongodb()

    # Also main script, reads the data
    read_mongodb.read_mongodb()

    # Tracking code performance
    time2 = time.time()
    run_time = time2 - time1
    run_time = datetime.timedelta(seconds=run_time)
    print(f"\n Runtime: {run_time}")
