from logintest import login
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = login()

if driver is not None:
    try:
        driver.get("https://testnsg.order4sure.nl")

        # Click on the first paragraph
        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div/div/div/div[2]/p").click()
        print('Redirected to the page')

        # Click on the second paragraph
        driver.find_element(By.XPATH, "/html/body/div[1]/section[2]/div[2]/div/div/div[1]/p").click()
        print('Redirected to the page')

        # Fill in the company name
        driver.find_element("id", "bedrijfnaamnum").send_keys("3065860, Falkena Glas en Schilderwerken")

        # Select delivery method
        dropdown_levering = Select(driver.find_element("id", "leverggvns"))
        dropdown_levering.select_by_value("standaard")

        # Select group, sub-group, etc. (similar to the example below)
        dropdown_groep = Select(driver.find_element("id", "groep[1]"))
        dropdown_groep.select_by_value("isolat")

        dropdown_subgroep = Select(driver.find_element("id", "subgroep[1]"))
        dropdown_subgroep.select_by_value("S3")

        dropdown_opbouw = Select(driver.find_element("id", "opbouw[1]"))
        dropdown_opbouw.select_by_value("4-spouw-*4 S3")

        dropdown_spouw = Select(driver.find_element("id", "spouw[1]"))
        dropdown_spouw.select_by_value("6")

        dropdown_spouwtype = Select(driver.find_element("id", "spouwtype[1]"))
        dropdown_spouwtype.select_by_value("nothing")

        # Fill in other form fields
        driver.find_element("id", "aantal[1]").send_keys("4")
        driver.find_element("id", "breedte[1]").send_keys("1500")
        driver.find_element("id", "hoogte[1]").send_keys("1500")

        # Submit the form
        driver.find_element("id", "submitorderform").click()
        print('Order placed successfully')

    except Exception as e:
        print(f'An error occurred: {str(e)}')

    finally:
        driver.quit()