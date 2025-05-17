# mlProject/logger.py
import logging

# Set up the logger
def setup_logger():
    logger = logging.getLogger(__name__)  # Create a logger for this module
    handler = logging.StreamHandler()  # Create a stream handler to log to console
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Log format
    handler.setFormatter(formatter)  # Set the formatter to the handler
    logger.addHandler(handler)  # Add handler to the logger
    logger.setLevel(logging.INFO)  # Set the logging level to INFO
    return logger

# Create and configure the logger
logger = setup_logger()
