import logging
from colorlog import ColoredFormatter

color_formatter = ColoredFormatter(
    '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'bold_red',
    }
)

def getLogger():
    logger = logging.getLogger('video_logger')
    logger.setLevel(logging.INFO)

    logger.log(logging.INFO,"Testing1")

    # Create a formatter to define the log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    logger.log(logging.INFO,"Testing2")


    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    logger.log(logging.INFO,"Testing3")


    # Create a stream handler to print logs to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # You can set the desired log level for console output
    console_handler.setFormatter(formatter)
    console_handler.setFormatter(color_formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger