from apify import Actor
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import random
import string

async def main():
    async with Actor:
        Actor.log.info("Starting Google signup automation...")

        # Configure Chrome for Apify environment
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        try:
            driver = webdriver.Chrome(options=options)
            driver.get("https://accounts.google.com/signup")

            # Wait for the page to load
            time.sleep(3)

            # Generate random first + last name
            first_name = "Cee"
            last_name = "Three"
            username_suffix = ''.join(random.choices(string.digits, k=8))
            full_username = f"cee3eeontop{username_suffix}"

            Actor.log.info(f"Generated username: {full_username}")

            # Example interaction (you'll need to expand this logic)
            first_name_field = driver.find_element(By.ID, "firstName")
            last_name_field = driver.find_element(By.ID, "lastName")

            first_name_field.send_keys(first_name)
            last_name_field.send_keys(last_name)
            last_name_field.send_keys(Keys.ENTER)

            time.sleep(5)  # wait for the next page

            # Save the email to emails.txt
            with open("emails.txt", "a") as f:
                f.write(full_username + "\n")

            Actor.log.info("Signup flow completed. Username written to emails.txt.")

        except Exception as e:
            Actor.log.error(f"An error occurred: {str(e)}")
        finally:
            driver.quit()
            Actor.log.info("Browser closed.")
