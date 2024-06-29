from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver options
options = Options()
options.headless = False  # Set to True for headless mode

# Path to geckodriver, make sure it's added to your system PATH or provide the full path here
geckodriver_path = 'F:\BELAJAR_SELEINUM\belajar_selenium\geckodriver\geckodriver.exe'

# Initialize the WebDriver (for Firefox)
driver = webdriver.Firefox(options=options, executable_path=geckodriver_path)

def get_rendered_html(driver, url):
    driver.get(url)
    
    # Wait for the body tag to be present, indicating the page has fully loaded
    
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )

    # Get the rendered HTML source code
    rendered_html = driver.page_source
    return rendered_html

# URL of the login page
login_url = 'https://belajar-nextjs-alfi.vercel.app/login'

# Get the rendered HTML source code
rendered_html = get_rendered_html(driver, login_url)
print(rendered_html)

# Close the WebDriver
driver.quit()

