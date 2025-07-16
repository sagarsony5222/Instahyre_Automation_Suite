import logging
import os
from datetime import datetime

# Create log directory to 'log' in the root directory
LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "log")
os.makedirs(LOG_DIR, exist_ok=True)

# Timestamped log file
log_filename = datetime.now().strftime("log_%Y-%m-%d_%H-%M-%S.log")
log_filepath = os.path.join(LOG_DIR, log_filename)

# Configure logger
logger = logging.getLogger("AutomationLogger")
logger.setLevel(logging.DEBUG)

# Formatter
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s", "%Y-%m-%d %H:%M:%S"
)

# File Handler
file_handler = logging.FileHandler(log_filepath)
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Console Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# Attach handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
