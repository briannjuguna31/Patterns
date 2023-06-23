class Logger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log(self, message):
        # Log the message to the specified log file or console
        with open(self.log_file, 'a') as file:
            file.write(message + '\n')


# Usage example
logger1 = Logger("log_file_1.txt")
logger1.log("This is a log message from logger1.")

logger2 = Logger("log_file_2.txt")
logger2.log("This is a log message from logger2.")