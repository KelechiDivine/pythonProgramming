def log_message(msg):
    with open("filename.log", "a") as log_file:
        log_file.write("{o}\n".format(msg))
