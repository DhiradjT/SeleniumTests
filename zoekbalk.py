from selenium import webdriver
from logintest import login
from selenium.webdriver.common.by import By

driver = login()
driver = webdriver.Firefox()
if driver is not None:
    try:
        driver.get("https://testnsg.order4sure.nl")


        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[3]/p").click()
        print('Doorverwezen Naar Order4Sure -> Orderoverzicht')

        # zoeken met OrdernummerO4S
        driver.find_element(By.ID, "ordernummerO4S").send_keys("")
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[2]/div[8]/button[1]").click()

        # zoeken met Ordernummer Pilkington
        driver.find_element(By.ID, "ordernummerAlcib").send_keys("")
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[2]/div[8]/button[1]").click()

        # zoeken met Klantnaam / Debiteurenummer
        driver.find_element(By.ID, "klantnaam").send_keys("Falkena Glas en Schilderwerken")
        driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[1]/div[2]/div[8]/button[1]").click()

    except Exception as e:
        print(f'Er is een fout opgetreden: {str(e)}')

    finally:
        driver.quit()