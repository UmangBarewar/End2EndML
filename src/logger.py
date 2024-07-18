import logging
import os
from datetime import datetime

# Define log file path and directory
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s\n%(levelname)s\n%(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info("This is an info message.")

# this is the testing code

# NOTES:
# 1.logging: This module is used to write log messages to a file or console.
# os: This module provides a way of using operating system-dependent functionality, such as file paths.
# datetime: This module supplies classes for manipulating dates and times.

# 2.LOG_FILE: A string that represents the log file's name, which includes the current date and time. This ensures a unique log file for each run of the script.

# 3.Creating the Logs Directory Path
# python
# Copy code
# logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
# os.makedirs(logs_path, exist_ok=True)
# logs_path: Constructs the path to the directory where logs will be stored. It uses the current working directory and adds a "logs" folder.
# os.makedirs(logs_path, exist_ok=True): Creates the "logs" directory if it doesn't exist. The exist_ok=True parameter prevents an error if the directory already exists.

# Defining the Full Log File Path
# python
# Copy code
# LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
# LOG_FILE_PATH: Constructs the full path to the log file, including the directory and file name.

# 4. Configuring the logging
# filename=LOG_FILE_PATH: Specifies the file to which logs will be written.
# format: Defines the format of log messages. It includes:
# [ %(asctime)s ]: Timestamp of the log entry.
# %(lineno)d: Line number where the logging call was made.
# %(name)s: Name of the logger.
# %(levelname)s: Log level (e.g., INFO, ERROR).
# %(message)s: The actual log message.
# level=logging.INFO: Sets the logging level to INFO, which means all messages at this level and higher (e.g., WARNING, ERROR, CRITICAL) will be logged.