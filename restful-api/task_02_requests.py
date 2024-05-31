#!/usr/bin/env python3
import csv
import requests


def fetch_and_print_posts():
    """
    Fetches posts from a RESTful API and prints their titles.

    This function sends a GET request to the specified API
    endpoint and retrieves a list of posts.
    It then prints the title of each post.

    Args:
            None

    Returns:
            None
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetches posts from the given API endpoint and saves them to a CSV file.

    This function sends a GET request to the API endpoint
    "https://jsonplaceholder.typicode.com/posts"
    to retrieve a list of posts. It then extracts the necessary
    information from each post and saves
    it to a CSV file named "posts.csv" with the columns 'id',
    'title', and 'body'.

    Returns:
            None
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()
        post_list = [{'id': post['id'], 'title': post['title'],
                      'body': post['body']} for post in posts]
        csv_file = 'posts.csv'
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(post_list)
