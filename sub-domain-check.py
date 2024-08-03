import requests
from time import sleep
from tabulate import tabulate
import json
import os

class SubdomainChecker:
    def __init__(self, json_file):
        self.json_file = json_file
        self.subdomains = self.load_subdomains()
        self.last_modified = os.path.getmtime(json_file)

    def load_subdomains(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
            return data['subdomains']

    def check_for_updates(self):
        current_modified = os.path.getmtime(self.json_file)
        if current_modified != self.last_modified:
            self.last_modified = current_modified
            self.subdomains = self.load_subdomains()
            print("Subdomains list updated.")

    def check_status(self):
        status_list = []
        for subdomain in self.subdomains:
            try:
                response = requests.head(subdomain, timeout=5)
                status_code = response.status_code
                if status_code == 200:
                    status_list.append([subdomain, "Up"])
                else:
                    status_list.append([subdomain, "Down"])
            except requests.ConnectionError:
                status_list.append([subdomain, "Down"])
        return status_list

    def display_status(self, status_list):
        table = tabulate(status_list, headers=["Subdomain", "Status"], tablefmt="pretty")
        print(table)

    def run(self, interval=60):
        while True:
            self.check_for_updates()
            status_list = self.check_status()
            self.display_status(status_list)
            sleep(interval)

if __name__ == "__main__":
    json_file = 'subdomains.json'
    checker = SubdomainChecker(json_file)
    checker.run()
