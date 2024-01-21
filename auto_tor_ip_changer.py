# -*- coding: utf-8 -*-

import time
import os
import requests

class SetupManager:
    @staticmethod
    def install_requests():
        try:
            import requests
        except ImportError:
            print('[+] Requests library is not installed. Installing...')
            os.system('pip install requests')
            os.system('pip install requests[socks]')
            print('[!] Requests library installed.')

    @staticmethod
    def check_tor_installation():
        try:
            check_tor = os.system('where tor > nul 2>&1')
        except Exception as e:
            raise RuntimeError(f"Error checking Tor installation: {e}")

class IPChanger:
    def __init__(self, tor_proxy='socks5://127.0.0.1:9050'):
        self.tor_proxy = tor_proxy

    def get_external_ip(self):
        url = 'https://www.myexternalip.com/raw'
        response = requests.get(url, proxies=dict(http=self.tor_proxy, https=self.tor_proxy))
        return response.text

    def display_ip_change(self):
        print('[+] Your IP has been changed to:', self.get_external_ip())

class AutoTOR:
    def __init__(self, tor_proxy='socks5://127.0.0.1:9050'):
        self.setup_manager = SetupManager()
        self.setup_manager.install_requests()
        self.setup_manager.check_tor_installation()
        self.ip_changer = IPChanger(tor_proxy)

    def start(self):
        os.system("cls")
        self.print_banner()
        self.execute_ip_change()

    def print_banner(self):
        print('''
                    _          _______
         /\\        | |        |__   __|
        /  \\  _   _| |_ ___      | | ___  _ __
       / /\\ \\| | | | __/ _ \\     | |/ _ \\| '__|
      / ____ \\ |_| | || (_) |    | | (_) | |
     /_/    \\_\\__,_|\\__\\___/     |_|\\___/|_|
              
    ''')

    def execute_ip_change(self):
        x = self.get_user_input("[+] Time to change IP in seconds [type=60] >> ", int)
        lin = self.get_user_input("[+] How many times do you want to change your IP [type=1000] for infinite IP change type [0] >> ", int)

        if lin == 0:
            while True:
                try:
                    time.sleep(x)
                    self.ip_changer.display_ip_change()
                except KeyboardInterrupt:
                    print('\nAuto Tor is closed.')
                    input("Press Enter to exit...")
                    quit()
        else:
            for _ in range(lin):
                time.sleep(x)
                self.ip_changer.display_ip_change()

    def get_user_input(self, prompt, data_type):
        while True:
            try:
                user_input = data_type(input(prompt))
                return user_input
            except ValueError:
                print("Invalid input. Please enter a valid value.")

def main():
    tor_proxy = input("[+] Enter the Tor proxy (default: socks5://127.0.0.1:9050): ") or 'socks5://127.0.0.1:9050'
    auto_tor = AutoTOR(tor_proxy)
    auto_tor.start()

if __name__ == "__main__":
    main()
