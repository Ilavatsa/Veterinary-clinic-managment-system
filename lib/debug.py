import logging
import sys

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

def log_debug(message):
    """Log a debug message."""
    logging.debug(message)

def log_info(message):
    """Log an info message."""
    logging.info(message)

def log_warning(message):
    """Log a warning message."""
    logging.warning(message)

def log_error(message):
    """Log an error message."""
    logging.error(message)

def log_critical(message):
    """Log a critical message."""
    logging.critical(message)

# Example usage of logging
if __name__ == "__main__":
    log_debug("This is a debug message.")
    log_info("This is an info message.")
    log_warning("This is a warning message.")
    log_error("This is an error message.")
    log_critical("This is a critical message.")

