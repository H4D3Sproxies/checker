import threading
import requests
from database import add_proxy, get_proxies
import os
import random
import re

lock = threading.Lock()

class Proxy():
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.requests = []
        self.results = []
        self.bad_results = []
        self.used_proxies = []
        self.proxies = []
        self.host_ip = ""
        
        self.folder = 'proxies'
        self.max_threads = 40
        
        self.refresh_host_ip()
        self.fetch_proxies()

    def insert_proxy(self, user_id, ip, port):
        add_proxy(user_id, ip, port, 'http')
        
    def fetch_proxies(self, user_id):
        self.proxies = get_proxies(user_id)
    
    def refresh_host_ip(self):
        test_url = 'https://httpbin.org/ip'
        
        response = requests.get(test_url, timeout=10)
        self.host_ip = re.findall(r'\d+\.\d+\.\d+\.\d+', response.text)[0]
    
    def proxy_api_check(self):        
        count = 1
        print(len(self.requests))
        for proxy in self.requests:
            ip, port = proxy[0].split(':')
            # url = f"http://proxycheck.io/v2/{ip}"
            
            try:
                # url = f'http://ip-api.com/json/{ip}?fields=25882623'
                url = f'http://check.getipintel.net/check.php?ip={ip}'
                response = requests.get(url).json()
                
                print(response)
                
                if count % 50 == 0:
                    print(count)
                
                if response['status'] == 'success':
                    if response['proxy'] == 'False':
                        add_proxy(ip, port, proxy[1])
                        print(response)
                        
                else:
                    print('*******************************************')
                    print(response)
                    print('*******************************************')
                count += 1
                
            except Exception as err:
                print(ip)
                print(response)

    def load_proxies(self):
        file_names = ['http', 'socks4', 'socks5']
        
        for file_name in file_names:
            file_path = f'{self.folder}/{file_name}.txt'
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    print(f'starting to test {file_name}')
                    for line in file:
                        if '@' not in line and ':' in line and '.' in line:
                            self.requests.append([line, file_name])
        print('done, saving successfull proxies')
        self.proxy_api_check()
    
    def get_random_proxy(self, proxy_list):
        try:
            proxy = random.choice(proxy_list)
            
            proxy_list.remove(proxy)
            
            return proxy['ip'], proxy['port']
        except:
            pass
    
    def export_proxies(self, amount, proxy_type):
        filtered_proxies = [item for item in self.proxies if item['proxy_type'] == proxy_type]
        
        with open('proxies/export.txt', 'w') as file:
            for idx in range(len(filtered_proxies)):
                proxy = self.get_random_proxy(filtered_proxies)
                
                file.write(f'({proxy_type}){proxy}\n')


    def fetch_proxies(self):
        self.proxies = get_proxies()
        
    