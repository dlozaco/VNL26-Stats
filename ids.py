"""Scrap unique player profile IDs across VNL skill leaderboards."""

import re
import time

import undetected_chromedriver as uc
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

categories = [
    "best-scorers",
    "best-attackers",
    "best-blockers",
    "best-servers",
    "best-setters",
    "best-diggers",
    "best-receivers",
]

BASE = (
    "https://es.volleyballworld.com/volleyball/competitions/"
    "volleyball-nations-league/statistics/men/"
)

options = uc.ChromeOptions()
options.add_argument("--headless")
driver = uc.Chrome(options=options)

all_ids = []

for cat in categories:
    data_url = BASE + cat + "/"
    driver.get(data_url)

    try:
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='/players/']"))
        )
    except TimeoutException:
        print(f"Timeout en {cat}")
        continue

    links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/players/']")
    for link in links:
        href = link.get_attribute("href")
        match = re.search(r"/players/(\d+)", href)
        if match:
            all_ids.append(int(match.group(1)))

    print(f"{cat}: {len(links)} jugadores encontrados")
    time.sleep(2)

driver.quit()

all_ids = list(set(all_ids))
print(f"\nTotal IDs únicos: {len(all_ids)}")
print(f"ID mínimo: {min(all_ids)}")
print(f"ID máximo: {max(all_ids)}")
print(f"Rango completo: {sorted(all_ids)}")
