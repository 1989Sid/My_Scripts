import subprocess
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to the Vivaldi browser executable
vivaldi_path = "/usr/bin/vivaldi"

# Step 1: Open a new tab in Vivaldi with the ChatGPT URL
subprocess.run([vivaldi_path, "https://chatgpt.com"])

# Wait for the browser to open
time.sleep(5)

# Step 2: Ask the user what they want to search
search_query = input("What do you want to search? ")

# Set up Selenium to use Vivaldi (assuming Vivaldi uses the Chrome driver)
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = vivaldi_path

# Expand the path to the ChromeDriver as needed
chromedriver_path = os.path.expanduser("~/Downloads/chromedriver")
service = Service(chromedriver_path)

# Initialize the WebDriver with the Vivaldi browser
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://chatgpt.com")

# Step 3: Enter the search query into ChatGPT and fetch the output
try:
    # Wait until the input box is present
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )

    # Enter the search query
    input_box.send_keys(search_query)
    input_box.send_keys(Keys.RETURN)

    # Wait for the response (Adjust the selector based on actual page structure)
    response_box = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".response-class"))  # Adjust this selector
    )

    # Fetch the response text
    response_text = response_box.text
    print("ChatGPT response:", response_text)

finally:
    # Close the browser
    driver.quit()
