import logging
from datetime import datetime
import os

Log_File = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}"  # File with current time.
log_path = os.path.join(os.getcwd(), 'logs', Log_File)  # log folder created in cwd(), with name - "logs_<LOG_FILE>"
os.makedirs(log_path, exist_ok=True)

log_file_path = os.path.join(log_path, Log_File)

logging.basicConfig(filename=log_file_path, format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
                    level=logging.INFO)
