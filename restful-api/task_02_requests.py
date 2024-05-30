#!/usr/bin/env python3
import csv
import requests


def fetch_and_print_posts():
    get = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {requests.status_code}")
    
    if requests.status_code == 200:
        parse = requests.json()
        for post in parse:
            print(post['title'])
    