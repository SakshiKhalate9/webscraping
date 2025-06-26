import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_zdnet_ai_carousels():
    url = "https://www.zdnet.com/topic/artificial-intelligence/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    # Find all carousels (Product Research, How-to Guides, etc.)
    carousels = soup.find_all("div", class_="c-dynamicCarousel")
    results = []

    for carousel in carousels:
        section_title = carousel.find("h4", class_="c-sectionHeading")
        if not section_title:
            continue
        section_title = section_title.get_text(strip=True)
        items = []
        # Find all items in the carousel
        for item in carousel.select(".c-listingCarouselHorizontal_item a"):
            title = item.get("title") or item.get_text(strip=True)
            link = "https://www.zdnet.com" + item.get("href")
            # Try to get image
            img_tag = item.find("img")
            img_url = img_tag["src"] if img_tag and img_tag.get("src") else None
            items.append({
                "title": title,
                "url": link,
                "image": img_url
            })
        if items:
            results.append({
                "section": section_title,
                "articles": items
            })

    return results

def download_image(url, save_dir, filename):
    if not url:
        return None
    try:
        response = requests.get(url, stream=True, timeout=10)
        response.raise_for_status()
        ext = os.path.splitext(url)[1].split('?')[0]
        if not ext or len(ext) > 5:
            ext = '.jpg'
        filepath = os.path.join(save_dir, filename + ext)
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return filepath
    except Exception as e:
        return None

def save_to_csv(data, csv_path, image_dir):
    rows = []
    for section in data:
        for idx, article in enumerate(section["articles"]):
            image_url = article["image"]
            image_filename = f"{section['section'].replace(' ', '_')}_{idx+1}"
            local_image_path = download_image(image_url, image_dir, image_filename) if image_url else None
            rows.append({
                "section": section["section"],
                "title": article["title"],
                "url": article["url"],
                "image": local_image_path if local_image_path else image_url
            })
    import pandas as pd
    df = pd.DataFrame(rows)
    df.to_csv(csv_path, index=False)

if __name__ == "__main__":
    data = scrape_zdnet_ai_carousels()
    save_to_csv(data, "assets/csv_dir/zdnet_ai_carousels.csv", "assets/images/img")
    for section in data:
        print(f"Section: {section['section']}")
        for article in section["articles"]:
            print(f"  - {article['title']}")
            print(f"    URL: {article['url']}")
            print(f"    Image: {article['image']}")
        print()
