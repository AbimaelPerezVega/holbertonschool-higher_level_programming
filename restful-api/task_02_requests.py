import requests
import csv

def fetch_and_print_posts():
    # Send a GET request to the JSONPlaceholder posts endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    # Print the status code of the response
    print(f"Status Code: {response.status_code}")
    
    # If the request was successful, parse the JSON data and print post titles
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    # Send a GET request to the JSONPlaceholder posts endpoint
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    
    # If the request was successful, parse the JSON data
    if response.status_code == 200:
        posts = response.json()
        
        # Structure the data into a list of dictionaries
        posts_data = [{"id": post["id"], "title": post["title"], "body": post["body"]} for post in posts]
        
        # Specify the CSV file name
        csv_file = "posts.csv"
        
        # Write the data into the CSV file
        with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(posts_data)

# The main script to run the functions
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
