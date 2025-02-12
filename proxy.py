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
        
        self.folder = 'proxies'
        self.max_threads = 40

    def insert_proxy(self, user_id, ip, port):
        if self.proxy_api_check(user_id, ip, port):
            add_proxy(user_id, ip, port, 'http')
            return True
            
        else:
            return False
        
    def fetch_proxies(self):
        return get_proxies()
    
    def ip_test(self, ip, port):
        ip_test_url = 'https://httpbin.org/ip'
        
        proxy = {
                'http': f"http://{ip}:{port}",
                'https': f"http://{ip}:{port}"
            }
        
        print(proxy)
        
        response = requests.get(ip_test_url, proxies=proxy, timeout=30)
        
        print(response.text)
        
        if 'origin' in response.text:
            if ip == re.findall(r'\d+\.\d+\.\d+\.\d+', response.text)[0]:
                return True
        
        return False
    
    def proxy_api_check(self, user_id, ip, port):
            # url = f"http://proxycheck.io/v2/{ip}"
            
            try:
                url = f'http://ip-api.com/json/{ip}?fields=25882623'
                   
                if self.ip_test(ip, port):
                    return True
                    response = requests.get(url).json()
                    
                    print(response)
                    
                    if response['status'] == 'success':
                        if response['proxy'] == 'False':
                            self.insert(user_id, ip, port)
                            return True
                            
                    else:
                        return False
                    count += 1
                    
                else:
                    
                    return False
                
            except Exception as err:
                print(err)
                print(f'something is wrong with ip: {ip}')

    def load_proxies(self):
        file_names = ['http', 'socks4', 'socks5']
        
        for file_name in file_names:
            file_path = f'{self.folder}/{file_name}.txt'
            if os.path.exists(file_path):
                with open(file_path, 'r') as file:
                    print(f'starting to test {file_name}')
                    for line in file:
                        if '@' not in line and ':' in line and '.' in line:
                            self.proxy_api_check()
        print('done, saving successfull proxies')
    
    def get_random_proxy(self):
        try:
            proxy = random.choice(self.proxies)
            
            return proxy['ip'], proxy['port']
        except:
            pass
    
    def export_proxies(self, amount, proxy_type):
        filtered_proxies = [item for item in self.proxies if item['proxy_type'] == proxy_type]
        
        with open('proxies/export.txt', 'w') as file:
            for idx in range(len(filtered_proxies)):
                proxy = self.get_random_proxy(filtered_proxies)
                
                file.write(f'({proxy_type}){proxy}\n')