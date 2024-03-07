import os
from pathlib import Path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.chrome.options import Options


# برای قسمت ۲ آموزش ۱۰ دقیقه آخر رو اجرا نکرد
# chrome_options = Options()
# chrome_options.add_argument("--incognito")
# chrome_options.add_argument("--headless")

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://yahoo.com")

sleep(3)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
sleep(5)

currnet_path = Path(__file__).parent
file_name = os.path.join(str(currnet_path), 'session3.png')

driver.save_screenshot(file_name)