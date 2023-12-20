from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions

def login():
    # Set up ChromeOptions
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'

    # Set up Sauce Labs options
    sauce_options = {}
    sauce_options['username'] = 'oauth-dhiradj.tangali-721a4'
    sauce_options['accessKey'] = 'e3eb87eb-6f1e-4c19-9170-f23a64bb2952'
    sauce_options['build'] = 'selenium-build-GY28E'
    sauce_options['name'] = 'LoginTest'  # Provide a meaningful name for your test

    # Set capability for Sauce Labs options
    options.set_capability('sauce:options', sauce_options)

    # Set up Sauce Labs URL
    url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"

    # Initialize WebDriver with remote execution
    driver = webdriver.Remote(command_executor=url, options=options)

    try:
        driver.get("https://testnsg.order4sure.nl")

        # Wait for the username field to be present
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

        driver.find_element(By.ID, "username").send_keys("Hubbase_stage")
        driver.find_element(By.ID, "password").send_keys("logistics")
        driver.find_element(By.ID, "submit_button").click()

        # Wait for the "Akkoord" button to be present and clickable
        akkoord_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/div/div/div/div/div/div/div/div[4]/button"))
        )
        akkoord_button.click()

        print('Login successful')
        return driver

    except Exception as e:
        print(f'An error occurred: {str(e)}')
        return None

    finally:
        # Close the browser window after the test
        driver.quit()

# Execute the login function only when the script is run directly
if __name__ == "__main__":
    login()
