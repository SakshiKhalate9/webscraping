# 📰 CyberScoop News Scraper

A Python-based web scraping project that extracts the **latest cybersecurity news articles** from the CyberScoop homepage.
The script collects article titles, links, and images, downloads the images locally, and stores the data in a CSV file for further analysis or use in data projects.

This project demonstrates **web scraping, data extraction, image downloading, and structured data storage using Python**.

---

## 🌐 Source Website

Data is scraped from the cybersecurity news platform **CyberScoop**.

---

# 📌 Features

* Scrapes **latest cybersecurity news articles**
* Extracts:

  * Article Title
  * Article Link
  * Article Image URL
* Downloads images locally
* Saves structured data into a **CSV file**
* Displays progress while downloading images using **tqdm**
* Clean project structure for easy expansion

---

# 🛠 Technologies Used

* **Python**
* **Requests** – for sending HTTP requests
* **BeautifulSoup4** – for parsing HTML
* **CSV Module** – for saving structured data
* **tqdm** – for progress bars
* **OS Module** – for file and directory handling

---

# 📂 Project Structure

```
cyberscoop-news-scraper
│
├── script.py
│
├── assets
│   ├── csv
│   │   └── cyberscoop_latest_posts.csv
│   │
│   └── image
│       ├── image1.jpg
│       ├── image2.jpg
│       └── image3.jpg
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/cyberscoop-news-scraper.git
cd cyberscoop-news-scraper
```

Install required libraries:

```bash
pip install requests beautifulsoup4 tqdm
```

---

# ▶️ How to Run

Run the Python script:

```bash
python script.py
```

After running the script:

* Images will be downloaded to:

```
assets/image/
```

* Extracted article data will be saved to:

```
assets/csv/cyberscoop_latest_posts.csv
```

---

# 📊 Example Output

CSV File Example:

| Title                       | Link        | Image URL   | Image File              |
| --------------------------- | ----------- | ----------- | ----------------------- |
| Cybersecurity Policy Update | https://... | https://... | assets/image/image1.jpg |
| AI Security Risks           | https://... | https://... | assets/image/image2.jpg |

---

# 📈 Possible Improvements

Future enhancements for this project:

* Add **multiple cybersecurity news sources**
* Store data in a **database (SQLite / MongoDB)**
* Create an **automated daily scraper**
* Add **error logging**
* Build a **dashboard to visualize scraped news**

---

# 🎯 Learning Outcomes

Through this project you will understand:

* How web scraping works
* HTML parsing using BeautifulSoup
* Handling real-world website structures
* Downloading and managing external assets
* Saving structured datasets for analysis

---

# 👩‍💻 Author

**Sakshi Khalate**

This project is part of a **Python Web Scraping and Data Collection practice project**.

---

# ⭐ If you like this project

Consider giving the repository a **star ⭐ on GitHub**.
It helps others discover the project and supports open learning.
