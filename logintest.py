from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login():
    driver = webdriver.Firefox()
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
        # You might want to uncomment the following line to close the browser after the test
        # driver.quit()
        pass

# Execute the login function only when the script is run directly
if __name__ == "__main__":
    login()















# from selenium import webdriver

# # Defineer de login-functie
# def login():
#     # Initialiseer de Selenium-webdriver (kies de gewenste browser)
# driver = webdriver.Firefox()

# try:
#         # Navigeer naar de inlogpagina
#         driver.get("https://testnsg.order4sure.nl")

#         # Controleer of de inlogknop aanwezig is (dit kan variëren afhankelijk van de website)
#         if driver.find_element("id", "submit_button").is_displayed():
#             # Voer de inlogstappen uit (bijvoorbeeld invullen van gebruikersnaam en wachtwoord)
#             driver.find_element("id", "username").send_keys("Hubbase_stage")
#             driver.find_element("id", "password").send_keys("logistics")
#             driver.find_element("id", "submit_button").click()
#             print('login succes')
#             return driver
# except Exception as e:
#        print(f'Er is een fout opgetreden: {str(e)}')
#     return None            
        
#             # Hier kun je verdere stappen van je test uitvoeren nadat je bent ingelogd
#     #         return driver
#     # except Exception as e:
#     #     print(f'Er is een fout opgetreden: {str(e)}')
#     #     return None
    
# finally:
#         pass
#         # Sluit de browser altijd, ongeacht of er een fout is opgetreden of niet

# # Voeg een if-statement toe om de login-functie alleen uit te voeren als firsttest.py direct wordt uitgevoerd
# if __name__ == "__main__":
#     login()