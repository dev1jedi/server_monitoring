import psutil
import os

def monitor_network_usage() -> int:
    net_io_counters = psutil.net_io_counters(pernic=True)

    interface = os.environ.get("NETINTERFACE")

    bytes_sent = net_io_counters[interface].bytes_sent / (1024 * 1024)
    bytes_recv = net_io_counters[interface].bytes_recv / (1024 * 1024)

    net_usage = int(bytes_sent) + int(bytes_recv)

    return net_usage
