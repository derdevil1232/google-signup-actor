from apify import Actor

async def main():
    async with Actor:
        Actor.log.info("Starting the Google signup bot...")

        # Your real logic would go here
        # For now, just test it with a pause
        import time
        time.sleep(5)

        Actor.log.info("Finished the bot run.")
import time, random, string, pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from io import BytesIO

async def main():
    async with Actor:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-blink-features=AutomationControlled")

        driver = webdriver.Chrome(options=options)
        driver.get("https://accounts.google.com/signup")

        # (Paste your automation logic here. Everything you wrote before.)
        # Make sure not to use `exit()` or `break` outside of a loop

        driver.quit()
