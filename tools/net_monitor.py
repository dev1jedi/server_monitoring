import psutil
import os
import time

def monitor_network_usage() -> int:
    net_io_counters = psutil.net_io_counters(pernic=True)

    interface = os.environ.get("NETINTERFACE")

    start_bytes_sent = net_io_counters[interface].bytes_sent / (1024 * 1024)
    start_bytes_recv = net_io_counters[interface].bytes_recv / (1024 * 1024)

    time.sleep(1)

    end_bytes_sent = net_io_counters[interface].bytes_sent / (1024 * 1024)
    end_bytes_recv = net_io_counters[interface].bytes_recv / (1024 * 1024)

    sent_diff = end_bytes_sent - start_bytes_sent
    recv_diff = end_bytes_recv - start_bytes_recv
    net_usage = int(sent_diff) + int(recv_diff)

    return net_usage
