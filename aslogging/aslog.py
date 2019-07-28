import colorama


def log(string):
    print("[{0}+{1}] {2}".format(colorama.Fore.GREEN, colorama.Fore.RESET, string))


def warning_log(string):
    print("[{0}?{1}] {2}".format(
        colorama.Fore.YELLOW, colorama.Fore.RESET, string))


def error_log(string):
    print("[{0}*{1}] {2}".format(
        colorama.Fore.RED, colorama.Fore.RESET, string))
