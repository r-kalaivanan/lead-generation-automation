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

    wait = WebDriverWait(driver, 10)

    cards = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href^='/companies/']"))
    )

    companies = []

    for card in cards[:30]:
        try:
            text = card.text.strip()
            lines = text.split("\n")

            first_line = lines[0]

            if "," in first_line:
                import re
                match = re.match(r"([A-Za-z0-9\s&.-]+)([A-Z].*)", first_line)
                
                if match:
                    name = match.group(1).strip()
                    location = match.group(2).strip()
                else:
                    name = first_line
                    location = "N/A"
            else:
                name = first_line
                location = "N/A"

            description = lines[1] if len(lines) > 1 else "N/A"

            link = card.get_attribute("href")

            companies.append({
                "Name": name,
                "Website": link,
                "Location": location,
                "Description": description
            })

        except Exception as e:
            print("Error:", e)
            continue
    
    driver.quit()
    return companies