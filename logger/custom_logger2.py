import os
import logging
from datetime import datetime


class CustomLogger:
    def __init__(self,log_dir="logs"):
        #Ensure logs directory exists
        self.logs_dir=os.path.join(os.getcwd(),log_dir)
        os.makedirs(self.logs_dir,exist_ok=True)

        # Timestamped log file (for persistance)
        log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        log_file_path=os.path.join(self.logs_dir,log_file)
        
        # configure logging
        logging.basicConfig(
            filename=log_file_path,
            
            format="[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s",
            level=logging.INFO,

        )


    def get_logger(self ,name=__file__):
        

        return logging.getLogger(os.path.basename(name))





if __name__ == "__main__":
    
    logger = CustomLogger().get_logger(__file__)
    logger.info("User uploaded a file")
    # logger.error("Failed to process PDF", error="File not found", user_id=123)
