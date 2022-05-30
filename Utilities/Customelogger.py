

import logging


class loggings:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Logs/totallogs.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d%Y %I:%M:%S%P')
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger