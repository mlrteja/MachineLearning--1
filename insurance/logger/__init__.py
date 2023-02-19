import logging
from datetime import datetime
import os 
# Creating logs directory to store log in files

LOG_DIR="Insurance_log"
# Creating file name for log file based on current timestamp

current_time_stamp=f"{datetime.now().strftime('%y-%m-%d-%H-%M-%S')}"

# Here, We are going to define the path to store log with folder_name

log_file_name = f"log_{current_time_stamp}.log"

#Creating LOG_DIR if it does not exists.

os.makedirs(LOG_DIR,exist_ok=True)

#Creating file path for projects.
log_file_path=os.path.join(LOG_DIR,log_file_name)

# If you want to read log select baseconfig and press f12 from your system.
logging.basicConfig(filename=log_file_path,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
#level=logging.INFO,
level=logging.DEBUG)






