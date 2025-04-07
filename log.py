import os
import logging

class Log:
    @staticmethod
    def get_logger(log_path):
        try:
            log_path_str=str(log_path)
            split_path=log_path_str.split('/')

            if len(split_path) > 1:
                logger=logging.getLogger(split_path[1])
            else:
                logger=logging.getLogger(split_path[0])

            if not logger.hasHandlers():

                formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

                file_handler=logging.FileHandler(os.path.join(log_path),mode='w')
                file_handler.setFormatter(formatter)

                stream_handler=logging.StreamHandler()
                stream_handler.setFormatter(formatter)

                logger.setLevel(logging.INFO)
                logger.addHandler(file_handler)
                logger.addHandler(stream_handler)

            return  logger
        except Exception as e:
            print(e)
            raise