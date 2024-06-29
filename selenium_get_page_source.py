from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    chrome_options = Options()
    
    # activated below if on mac os
    chrome_options.add_argument("--headless")  # Ensure GUI is off

    # chrome_options.headless = True
    
    driver = webdriver.Firefox(options=chrome_options)

    # driver.get( "https://itam.acehprov.go.id/login" )
    
    driver.get( "https://belajar-nextjs-alfi.vercel.app/login" )
   
    

    # WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "username"))
    # )

    # give time to render the content
    time.sleep(5)

    print("find element: ", driver.find_element(By.ID, "username") )
    print("URL before login: ", driver.current_url)
    # time.sleep(5)
   
    # Now you can interact with the page
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    submit_button = driver.find_element(By.TAG_NAME, "button")

    username_input.send_keys("Admin")
    password_input.send_keys("admin")
    submit_button.click()

    print("URL after login: ", driver.current_url)
    # time.sleep(5)

    html_source = driver.page_source
    #
    print(html_source)
    driver.quit()

if __name__ == "__main__":
    main()

