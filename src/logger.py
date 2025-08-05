import logging
import os
from datetime import datetime

log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
'''
datetime.now() → gets the current system date and time
.strftime('&m_%d_%Y_%H_%M_%S') → formats the date and time into a string
log ki jo file bnegi(after running),it'll be in this format
'''
log_path=os.path.join(os.getcwd(),"logs",log_file)
'''
current working directory mei logs naam ka folder bnao
aur usme log_file daaldo upar wali
aur is file ka path log_path variable mei store krvado
'''
os.makedirs(log_path,exist_ok=True)
'''
makes a log folder with the path you built above
exist_ok=True means don't raise an error if the folder already exists
'''

log_file_path=os.path.join(log_path,log_file)

logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    # defines how each log message looks
    level=logging.INFO # only logs INFO and higher
)

if __name__=="__main__":
    logging.info("Logging has started")