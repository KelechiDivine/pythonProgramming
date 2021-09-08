def critical(msg):
    with open("/var/log/filename.log", "a") as log_file:
        log_file.write("[CRITICAL] {0}\n".format(msg))


def error(msg):
    with open("/var/log/filename.log", "a") as log_file:
        log_file.write("[ERROR] {0}\n".format(msg))


def warn(msg):
    with open("/var/log/filename.log", "a") as log_file:
        log_file.write("[WARN] {0}\n".format(msg))


def info(msg):
    with open("/var/log/filename.log", "a") as log_file:
        log_file.write("[INFO] {0}\n".format(msg))


def debug(msg):
    with open("/var/log/filename.log", "a") as log_file:
        log_file.write("[DEBUG] {0}\n".format(msg))