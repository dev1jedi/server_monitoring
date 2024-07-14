from fastapi import FastAPI
from tools import cpu_ram_usage, net_monitor

app = FastAPI()

@app.get("/cpu_usage")
async def cpu_usage():
    cpu = cpu_ram_usage.cpu_usage()

    return {"cpu": cpu}

@app.get("/ram_usage")
async def ram_usage():
    ram = cpu_ram_usage.ram_usage()

    return {"ram": ram}

@app.get("/net_usage")
async def net_usage():
    net = net_monitor.monitor_network_usage()

    return {"net": net}

@app.get("/all_stats")
async def stats():
    cpu = cpu_ram_usage.cpu_usage()
    ram = cpu_ram_usage.ram_usage()
    net = net_monitor.monitor_network_usage()

    return {"cpu": cpu, "ram": ram, "net": net}