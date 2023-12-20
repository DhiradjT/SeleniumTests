# from selenium.webdriver.common.by import By
# from logintest import login  
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# def menu_test(driver):
#     if driver is not None:
#         try:
#             # Wait for the element to be present in the DOM
#             element = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p"))
#             )

#             # Scroll into view to ensure the element is visible and clickable
#             driver.execute_script("arguments[0].scrollIntoView(true);", element)

#             # Wait for the element to be clickable
#             element = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p"))
#             )
            
#             element.click()

#             print('Doorverwezen Naar Order4Sure')

#             # Continue with other menu testing actions

#         except Exception as e:
#             print(f'An error occurred during menu testing: {str(e)}')

# if __name__ == "__main__":
#     driver = login()
#     menu_test(driver)


from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_webdriver():
    # Set up ChromeOptions
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'

    # Set up Sauce Labs options
    sauce_options = {}
    sauce_options['username'] = 'oauth-dhiradj.tangali-721a4'
    sauce_options['accessKey'] = 'e3eb87eb-6f1e-4c19-9170-f23a64bb2952'
    sauce_options['build'] = 'selenium-build-GY28E'
    sauce_options['name'] = 'MenuTest'  # Provide a meaningful name for your test

    # Set capability for Sauce Labs options
    options.set_capability('sauce:options', sauce_options)

    # Set up Sauce Labs URL
    url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"

    # Initialize WebDriver with remote execution
    driver = webdriver.Remote(command_executor=url, options=options)
    return driver

def menu_test(driver):
    if driver is not None:
        try:
            # Wait for the element to be present in the DOM
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p"))
            )

            # Scroll into view to ensure the element is visible and clickable
            driver.execute_script("arguments[0].scrollIntoView(true);", element)

            # Wait for the element to be clickable
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p"))
            )
            
            element.click()

            print('Doorverwezen Naar Order4Sure')

            # Continue with other menu testing actions

        except Exception as e:
            print(f'An error occurred during menu testing: {str(e)}')

if __name__ == "__main__":
    driver = initialize_webdriver()
    menu_test(driver)







