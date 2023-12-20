from logintest import login 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = login()

if driver is not None:
    try:
        driver.get("https://testnsg.order4sure.nl")

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p").click()
        print('Doorverwezen Naar Order4Sure')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[3]/p").click()
        print('Doorverwezen Naar Order4Sure -> Orderoverzicht')

#zoeken met OrdernummerO4S
        driver.find_element(By,ID, "ordernummer04S").send_keys("")
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[2]/div[8]/button[1]")

#zoeken met Ordernummer Pilkington
        driver.find_element(By,ID, "ordernummerAlcib").send_keys("")
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[2]/div[8]/button[1]")





#zoeken met Klantnaam / Debiteurenummer     
        driver.find_element(By.ID, "klantnaam").send_keys("Falkena Glas en Schilderwerken")
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[2]/div[8]/button[1]")
        
    except Exception as e: 
        print(f'Er is een fout opgetreden: {str(e)}')
    
    finally:
        driver.quit()