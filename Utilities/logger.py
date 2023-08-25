# logging imports
import os
import csv
import time
import datetime
import System.Environment as env


def log_function(script_name, csv_path):
    """Decorator function to log script runtime and errors to a csv file.

    Args:
        script_name (str): name of function/script to be logged
        csv_path (str): path to csv file
    """
    def decorator(func):
        def wrapper(*args, **kwargs):

            # start timer
            start_time = time.time()

            # declare variables
            result = None
            error_message = None

            try:
                result = func(*args, **kwargs)
            except Exception as e:
                error_message = str(e)
            end_time = time.time()

            # calculate runtime
            runtime = end_time - start_time

            # get current time, username
            current_time = datetime.datetime.now()

            # get username
            username = env.UserName

            # write to csv
            # check if file exists first
            file_exists = os.path.exists(csv_path)

            # open file as append binary
            with open(csv_path, mode='ab') as csv_file:
                csv_writer = csv.writer(csv_file)
                if not file_exists:
                    print(error_message)
                    csv_writer.writerow(["Script Name", "Timestamp", "Runtime", "Username", "Error"])
                csv_writer.writerow([script_name, current_time, runtime, username, error_message])

            # close file
            csv_file.close()

            return result
        return wrapper
    return decorator
