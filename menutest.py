from logintest import login  
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#menu test@
# Alle items in het menu getest + vermeld welke menu item wat is, 
# zodat testen die moeten navigeren in de toekomst makkelijker worden@


driver = login()  

if driver is not None:
    try:
        driver.get("https://testnsg.order4sure.nl")

        # ORDER4SURE #

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p").click()
        print('Doorverwezen Naar Order4Sure')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[1]/p").click()
        print('Doorverwezen Naar Order4Sure -> Bestellen')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[2]/p").click()
        print('Doorverwezen Naar Order4Sure -> Screenline bestellen')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[3]/p").click()
        print('Doorverwezen Naar Order4Sure -> Orderoverzicht')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[4]/p").click()
        print('Doorverwezen Naar Order4Sure -> Tijdelijk opgeslagen bestellingen')

        # ORDER4SURE #

          # SALES4SURE #

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div/div[3]/p").click()
        print('Doorverwezen Naar Sales4Sure')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[1]/p").click()
        print('Doorverwezen Naar Sales4Sure -> Offerte')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[2]/p").click()
        print('Doorverwezen Naar Sales4Sure -> Screenline offerte')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[3]/p").click()
        print('Doorverwezen Naar Sales4Sure -> Offerteoverzicht')

        # SALES4SURE #  

          # BEHEER #

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div/div[4]/p").click()
        print('Doorverwezen Naar Beheer')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[1]/p").click()
        print('Doorverwezen Naar Beheer -> Gebruikers')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[2]/p").click()
        print('Doorverwezen Naar Beheer -> Nieuwe Gebruiker')


        # BEHEER #

          # SERVICE4SURE #

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div/div[5]/p").click()
        print('Doorverwezen Naar Service4Sure')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[1]/p").click()
        print('Doorverwezen Naar Service4Sure -> Ticket Indienen')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[2]/p").click()
        print('Doorverwezen Naar Service4Sure -> Ticket Overzicht')


        # SERVICE4SURE #

          # MARKETING4SURE #

        
        # time.sleep(15)  # Introducing a static wait of 5 seconds
        # element = driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div/div[6]")
        # element.click()
        # wait = WebDriverWait(driver, 10)  # Waiting up to 10 seconds
        # element = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div/div[6]/p")))
        # element.click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-child(6)")))
        element.click()
        print('Doorverwezen Naar Marketing4Sure')

        # driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[1]/div/div/div[6]").click()
        # print('Doorverwezen Naar Marketing4Sure')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[1]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Producten')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[2]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Normering')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[3]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Bestekteksten')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[4]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Energietoeslag')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[5]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Apps')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[6]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Spectrum')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[7]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Referentieprojecten')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[8]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Cradle-to-cradle')

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[9]/p").click()
        print('Doorverwezen Naar Marketing4Sure -> Routecodes')

        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div:nth-child(6)")))
        element.click()
        print('Doorverwezen Naar Marketing4Sure -> Contact')
        # MARKETING4SURE #

            # STATUS4SURE Laten we voorlopig eruit #

        # driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p").click()
        # driver.get("https://test.login4sure.com/simplesaml/module.php/core/loginuserpass.php?AuthState=_65bb09bf35e57955c1a30ce44aec8a947c4e6403de%3Ahttps%3A%2F%2Ftest.login4sure.com%2Fsimplesaml%2Fsaml2%2Fidp%2FSSOService.php%3Fspentityid%3Dhttps%253A%252F%252Fwww.surestatus.com%252Flib%252Fsimplesaml%252Fmodule.php%252Fsaml%252Fsp%252Fmetadata.php%252Fdefault-sp%26RelayState%3Dhttps%253A%252F%252Fwww.surestatus.com%252F%26cookieTime%3D1701163539")
        # print('Doorverwezen Naar Status4Sure')


        # STATUS4SURE #

           # LEARN4SURE Laten we voorlopig eruit #

        # driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p").click()
        # driver.get("https://www.learn4sure.nl/NSG/")
        # driver.get("https://testnsg.order4sure.nl")
        # print('Doorverwezen Naar Learn4Sure')

        # LEAR4SURE #


 # RACKLIST4SURE #

        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p").click()
        print('Doorverwezen Naar Racklist4Sure')
        print('Test is geslaagd!')


        # RACKLIST4SURE #


    except Exception as e: 
        print(f'Er is een fout opgetreden: {str(e)}')
    
    finally:
        driver.quit()