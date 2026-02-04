# Task 6: Scraping Structured Data
# Extract a web page section and store the information.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Step 1: Open main OWASP Top Ten page
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://owasp.org/www-project-top-ten/")

# Step 2: Wait for main content
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "main")))

# Step 3: Find link to latest release, in the main page: "The most current released version is the OWASP Top Ten 2025."
release_link_elem = driver.find_element(
    By.XPATH, "//main//a[contains(text(),'OWASP Top Ten 2025')]"
)
top10_url = release_link_elem.get_attribute("href")

# Step 4: Navigate to the Top Ten page.
driver.get(top10_url)

# Step 5: Wait for the main content
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "main")))

# Step 6: Grab all <a> tags in main content: https://owasp.org/Top10/2025/
main_content = driver.find_element(By.TAG_NAME, "main")
all_links = main_content.find_elements(By.TAG_NAME, "a")

# Step 7: Filter for A0 entries (Top 10): A01_2025-Broken_Access_Control
top_10_list = []
for link in all_links:
    text = link.text.strip()
    if text.startswith("A0") and len(top_10_list) < 10:
        top_10_list.append({"Vulnerability": text, "Link": link.get_attribute("href")})

print(top_10_list)

# Write CSV
df = pd.DataFrame(top_10_list)
df.to_csv("owasp_top_10.csv", index=False)

# closing the browser
driver.quit()



# Wait until links are visible (<a href="https://owasp.org/Top10/2025/">OWASP Top Ten 2025</a>)
# top_10_link = driver.find_element(By. XPATH, "//a[contains(text(),'Top Ten 2025')]").get_attribute("href")
#vulns = WebDriverWait(driver, 10).until( EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class, 'top-ten')]//li")) )
#top10_link = top10_link_el.get_attribute("href")
#print(f"Found Top 10 link:", top10_link)

# Navigate to the 2025 top 10 page
# <li><a href="https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/">A01:2025 - Broken Access Control</a></li>
# driver.get(top_10_link)

# print(driver.current_url)

# Wait for the vulnerabilities list inside the container "top-ten"
# vulns = driver.find_elements(By.XPATH, "//ul/li/a[contains(@href,'A0')]")
#vulns = WebDriverWait(driver, 10).until( EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class, 'top-ten')]//ul/li/a") ))
    # Extract the top-10 list (title + link)
# top_10_list = []
    
#for v in vulns[:10]:
    #try:
        # a_tag = v.find_element(By.TAG_NAME, "a")
        #title = v.text.strip()
       # link = v.find_element(By.TAG_NAME, "a").get_attribute("href")
        #top_10_list.append({"Vulnerability": title, "Link": link})
    #except:
        #continue
#print(top_10_list)
# Write to csv
#df = pd.DataFrame(top_10_list)
#df.to_csv("owasp_top_10.csv", index=False)
#try:
    #if top_10_list:
       # df = pd.DataFrame(top_10_list)
        #df.to_csv("owasp_top_10.csv", index=False)
    #else:
        #print("No vulnerabilities found!")
#except Exception as e:
    #print(f"Error: {e}")





