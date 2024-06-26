# makelog.py

import os
import logging

# Define the full path to the log file
LOG_FILE = os.path.join(os.getcwd(), 'product_management.log')

# Configure logging to write to the specified log file
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_info(message):
    """
    Logs an information message to the log file.

    Args:
        message (str): The message to log.
    """
    logging.info(message)

def log_error(message):
    """
    Logs an error message to the log file.

    Args:
        message (str): The error message to log.
    """
    logging.error(message)
