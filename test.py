import psutil
import time

with open('cpu_log.txt', 'a') as file:
    while True:
        disk_usage = psutil.disk_usage('/')
        print(f"Total: {disk_usage.total / (1024 ** 3):.2f} Go")
        print(f"Utilisé: {disk_usage.used / (1024 ** 3):.2f} Go")
        print(f"Libre: {disk_usage.free / (1024 ** 3):.2f} Go")

        net_io_counters = psutil.net_io_counters()
        print(f"Octets reçus : {net_io_counters.bytes_recv}")
        print(f"Octets envoyés : {net_io_counters.bytes_sent}")

        cpu_percent = psutil.cpu_percent()
        timestamp = int(time.time())
        log_string = f'{timestamp}, {cpu_percent}\n,{disk_usage}    \n,{net_io_counters}\n'
        file.write(log_string)

        time.sleep(10)