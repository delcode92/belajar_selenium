from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options


def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensure GUI is off

    chrome_options.headless = True
    
    driver = webdriver.Firefox(options=chrome_options)

    driver.get( "https://belajar-nextjs-alfi-it07bfpjg-delcode92s-projects.vercel.app/login" )
    time.sleep(5)
    
    html_source = driver.page_source

    print(html_source)
    driver.quit()

if __name__ == "__main__":
    main()

