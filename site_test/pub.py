from paho.mqtt import publish
from datetime import datetime

def send_data(d1, d2, d3, d4, d5, d6):
    data = [str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), str(d1), str(d2), str(d3), str(d4), str(d5), str(d6)]
    publish.single("user_33e0a052/1", " ".join(data), hostname="srv1.clusterfly.ru", port=9124, auth={'username':'user_33e0a052','password':'pass_88cf2f67'})
    
send_data(1, 2, 3, 1, 5, 6)