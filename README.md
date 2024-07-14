#Server_monitoring

I needed to have a simple application for monitoring my servers and I did this.
This app uses psutil for checking cpu, ram and network load and also uses fastapi such as simple API server

#Installation guide:

##Clone the repository:
```
mkdir monitoring
cd /montitoring

git clone https://github.com/dev1jedi/server_monitoring
```

##Create python environment(for linux):
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

##Check your ethernet adapter and add to env variable:
```
ifconfig

export NETINTERFACE="eth0"(for example)
```

##Install nginx and configure
```
sudo apt install nginx
sudo systemctl enable nginx
```
Open **nginxapp.conf** and replace the line **server_name <your_domain_or_ip>;** with your server ip or domain

```
sudo cp nginxapp.conf /etc/nginx/conf.d/

sudo systemctl restart nginx
```

##Run app:
```
nohup uvicorn main:app --host 127.0.0.1 --port 8000 &
```

#Example of use:
```python
import requests

r = requests.get("http://<your_server>:80/all_stats").json()

print(r)

> {"cpu": "50", "ram": "39", "net": "2500"}
```




