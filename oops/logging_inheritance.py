from csv import writer
from time import sleep

class ConsoleLogger:
    def log(self, message):
        print(message)

class TextFileLogger:
    def __init__(self, file_object):
        self.file_object = file_object
    
    def log(self, message):
        self.file_object.write(message)     # f.write()
        self.file_object.write("\n")
        self.file_object.flush()

class CSVFileLogger:
    def __init__(self, file_object):
        self.file_object = file_object
    
    def log(self, message):
        words = message.split()
        csv_writer = writer(self.file_object)
        csv_writer.writerow(words)
        self.file_object.flush()
# -------------------------------------------------------------------------
# Using Inheritance
class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredTextFileLogger(TextFileLogger):
    def __init__(self, file_object, pattern):
        self.pattern = pattern
        super().__init__(file_object)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredCSVFileLogger(CSVFileLogger):
    def __init__(self, file_object, pattern):
        self.pattern = pattern
        super().__init__(file_object)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

# -------------------------------------------------------------------------
# COMPOSITION
# this is a classic example of "composition"
# "FilteredLogger" has "ConsoleLogger"
# "FilteredLogger" has "TextFileLogger"
# "FilteredLogger" has "CSVFileLogger"
class FilteredLogger:
    def __init__(self, pattern, logger_type):
        self.pattern = pattern
        self.logger_type = logger_type
    
    # Polymorphic behavior or duck typing
    def log(self, message):
        if self.pattern in message:
            self.logger_type.log(message)       # ?? which class's "log" method is called?
# -------------------------------------------------------------------------
# Independent Parent
class FilteredLogger:
    def __init__(self, pattern):
        self.pattern = pattern
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)
# -------------------------------------------------------------------------
# Using multiple Inheritance
class ConsoleFilteredLogger(FilteredLogger, ConsoleLogger):
    def __init__(self, pattern):
        FilteredLogger.__init__(self, pattern)

class FilteredTextFileLogger(FilteredLogger, TextFileLogger):
    def __init__(self, pattern, file_object):
        FilteredLogger.__init__(self, pattern)
        TextFileLogger.__init__(self, file_object)
# -------------------------------------------------------------------------
with open("/Users/sandeep/Desktop/Training/_python/data_files/sample.log", "r") as f:
    with open("info_messages.txt", "w") as fw:
        logger = FilteredTextFileLogger("INFO", fw)
        for line in f:
            logger.log(line.strip())
            # sleep(0.1)