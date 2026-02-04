import logging

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def log_info(msg):
    logging.info(msg)

def log_error(msg):
    logging.error(msg)