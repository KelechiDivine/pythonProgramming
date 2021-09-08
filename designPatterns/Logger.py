def log_message(msg):
    with open("/var/log/filename.log", "a") as  log_file:
        log_file.write("{0}\n".format(msg))