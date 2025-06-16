#!/usr/bin/python3
"""
Using the request library to fetch data from an API
"""
import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    data = r.json()
    for post in data:
        print(post["title"])


def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    data = r.json()
    with open("posts.csv", 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'],
                                extrasaction='ignore')
        writer.writeheader()
        writer.writerows(data)
