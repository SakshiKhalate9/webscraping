import requests
from bs4 import BeautifulSoup
import csv
import os
from tqdm import tqdm

# URL to scrape
url = "https://cyberscoop.com/"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Raise an error for bad status

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the div containing the latest posts
latest_posts_div = soup.find('div', class_='latest-posts__items')

# Prepare a list to store the scraped data
posts = []

if latest_posts_div:
    articles = latest_posts_div.find_all('article', class_='post-item')
    for article in articles:
        # Extract title
        title_tag = article.find('h3', class_='post-item__title')
        title = title_tag.get_text(strip=True) if title_tag else None
        # Extract link
        link_tag = title_tag.find('a') if title_tag else None
        link = link_tag['href'] if link_tag and link_tag.has_attr('href') else None
        # Extract image URL
        img_tag = article.find('img')
        img_url = img_tag['src'] if img_tag and img_tag.has_attr('src') else None
        # Store the data
        posts.append({
            'title': title,
            'link': link,
            'image_url': img_url
        })

# Directory to save images
image_dir = 'assets/image'
os.makedirs(image_dir, exist_ok=True)

# Download images
for post in tqdm(posts, desc='Downloading images'):
    img_url = post['image_url']
    if img_url:
        # Get image filename from URL
        img_filename = os.path.basename(img_url.split('?')[0])
        img_path = os.path.join(image_dir, img_filename)
        try:
            img_response = requests.get(img_url, timeout=10)
            img_response.raise_for_status()
            with open(img_path, 'wb') as f:
                f.write(img_response.content)
            post['image_file'] = img_path
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")
            post['image_file'] = ''
    else:
        post['image_file'] = ''

# Save to CSV (with local image path)
csv_path = 'assets/csv/cyberscoop_latest_posts.csv'
with open(csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=['title', 'link', 'image_url', 'image_file'])
    writer.writeheader()
    for post in posts:
        writer.writerow(post)
        print(f"Title: {post['title']}")
        print(f"Link: {post['link']}")
        print(f"Image URL: {post['image_url']}")
        print(f"Image File: {post['image_file']}")
        print('-' * 80)
