# Task 3: Write a Program to Extract this Data

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time
import pandas as pd
import json

# Load the web page.
url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)

# Wait up to 10 seconds for (at least one) search result to appear
# without this delay time the output I get was "Number of li elements found 0, empty DataFrame" 
li_elements = WebDriverWait(driver, 10).until( EC.presence_of_all_elements_located((By.CLASS_NAME, "cp-search-result-item")) )

# Find all search result (li element)
li_elements = driver.find_elements(By.CLASS_NAME, "cp-search-result-item")
print(f"Number of li elements found", len(li_elements))

# Collecting result
results = []
for li in li_elements:
    try:
        title_el = li.find_element(By.CSS_SELECTOR, "span.title-content").text
    except:
        title_el = "N/A"

    try:
        author_els = li.find_elements(By.CSS_SELECTOR, "a.author-link")
        author_el = ", ".join([a.text.strip()for a in author_els]) if author_els else "N/A"
    except:
        author_el = "N/A"

    try:
        format_el = li.find_element(By.CSS_SELECTOR, "span.display-info-primary").text
    except:
        format_el = "No format/year"

# result   
    book_dict = {
            "Title": title_el,
            "Author": author_el,
            "Format-Year": format_el
        }
    results.append(book_dict)

# Delay between items
# time.sleep(3), change it into webdriverwait 

# Create DataFrame
df = pd.DataFrame(results)
# The authors get shortened/hidden/using three dots(...)
# Prevent truncation when printing
pd.set_option("display.max_colwidth", None) 
pd.set_option("display.width", None) 
pd.set_option("display.max_rows", None)
print(df)
# print(df["Author"].head()) # testing the author section 

# Task 4: Write out the Data
# save to csv
df.to_csv("get_books.csv", index=False)

# Save to JSON
with open("get_books.json", "w", encoding="utf8") as f:
    json.dump(results, f, indent=4)

driver.quit()




