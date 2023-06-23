import logging


class LogGen:
    @staticmethod
    def log_gen():
        logging.basicConfig(filename="/Users/utsav.jha/PycharmProjects/nopCommerce/Logs/automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            force=True)
        logs = logging.getLogger()
        logs.setLevel(logging.INFO)
        return logs
