from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os, time

def buscar_videos_por_hashtag(hashtag):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"

    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/google-chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)

    videos = []
    try:
        posts = driver.find_elements(By.CSS_SELECTOR, 'article a')
        for post in posts:
            href = post.get_attribute("href")
            if "/reel/" in href:
                img = post.find_element(By.TAG_NAME, 'img')
                videos.append({
                    "link": href,
                    "thumb": img.get_attribute("src") if img else ""
                })
            if len(videos) >= 9:
                break
    except Exception as e:
        print("Erro:", e)

    driver.quit()
    return videos
