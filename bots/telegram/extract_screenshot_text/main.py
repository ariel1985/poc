from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Initialize options for headless Chrome
options = Options()
options.headless = True  # Activates headless mode
options.add_argument("--window-size=1920,1080")  # Sets the window size

# Specify the path to ChromeDriver or add it to your PATH
chromedriver_path = '/path/to/chromedriver'

# Initialize the driver with the appropriate options
driver = webdriver.Chrome(options=options, executable_path=chromedriver_path)

# Go to a web page
driver.get('https://www.example.com')

# Take a screenshot and save it to a file
driver.save_screenshot('example_com_screenshot.png')

# Close the browser
driver.quit()
