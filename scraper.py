from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_companies():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # runs without opening browser

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.get("https://www.ycombinator.com/companies")

    companies = []

    wait = WebDriverWait(driver, 10)

    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href^='/companies/']"))
    )

    for card in cards[:30]:
        try:
            name = card.text.split("\n")[0]
            link = "https://www.ycombinator.com" + card.get_attribute("href")  

            companies.append({
                "Name": name,
                "Website" : link,
                "Location": "N/A",
            })
        except:
            continue
    
    driver.quit()
    return companies