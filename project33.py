# Design a File Logger SystemProblem: Create a class Logger that logs operations to a file. Use parameterized constructors to define the log file path.Implement a destructor to automatically close the file when the object is destroyed. Use method overloading to support different types of logs (info, warning, error).
class Logger:
    def __init__(self, file):
        self.f = open(file, "w")
        print("Logger started")

    def log_info(self, msg):
        self.f.write("INFO: " + msg + "\n")

    def log_warning(self, msg):
        self.f.write("WARNING: " + msg + "\n")

    def log_error(self, msg):
        self.f.write("ERROR: " + msg + "\n")

    def __del__(self):
        self.f.close()
        print("File closed")


# usage
log = Logger("log.txt")

log.log_info("Program started")
log.log_warning("Low memory")
log.log_error("Something went wrong")

del log