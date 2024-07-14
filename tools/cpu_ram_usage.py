import psutil


def cpu_usage() -> int:
    cpu_usage = int(psutil.cpu_percent())

    return cpu_usage


def ram_usage() -> int:
    ram_usage = int(psutil.virtual_memory().percent)

    return ram_usage