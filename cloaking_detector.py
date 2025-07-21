from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

def check_cloaking(url):
    try:
        # Simulate browser visit (user)
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        user_view = driver.page_source
        driver.quit()

        # Simulate bot visit
        headers = {'User-Agent': 'Googlebot'}
        bot_response = requests.get(url, headers=headers, timeout=5)
        bot_view = bot_response.text

        # Compare
        diff = abs(len(user_view) - len(bot_view))
        cloaking = diff > 500  # Adjust threshold if needed

        return {"cloaking": cloaking, "difference": diff}

    except Exception as e:
        return {"cloaking": False, "difference": 0}
