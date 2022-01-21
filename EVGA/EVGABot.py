from selenium import webdriver
from EVGA.constants import *
from selenium.webdriver.common.keys import Keys
import subprocess
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EVGABot(webdriver.Chrome):
    def __init__(self, images=False, VPN_Connection=True, driver_path=DRIVER_PATH):
        option = webdriver.ChromeOptions()
        option.add_argument(PROFILE)
        option.add_experimental_option(
            "excludeSwitches", ["enable-automation"])
        option.add_experimental_option('useAutomationExtension', False)
        option.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {
            "images": 2}
        if images:
            chrome_prefs["profile.default_content_settings"] = {"images": 3}
            chrome_prefs["profile.managed_default_content_settings"] = {
                "images": 3}

        if VPN_Connection:
            self.vpn = subprocess.Popen([VPN_PATH])
            time.sleep(3)

        super(EVGABot, self).__init__(driver_path, options=option)
        self.implicitly_wait(1000)

    def __exit__(self, *args):
        try:
            self.vpn.terminate()
        except:
            pass
        self.quit()

    def findItem(self):
        self.get(BASE_URL)
        try:
            WebDriverWait(self, 3).until(
                EC.presence_of_element_located((
                    By.CSS_SELECTOR, f"[title='Add {PRODUCT_ID} to cart']"
                ))
            )
            return True
        except:
            self.refresh()
            try:
                WebDriverWait(self, 3).until(
                    EC.presence_of_element_located((
                        By.CLASS_NAME, 'text'
                    ))
                )
                return False
            except:
                return None

    def waitThenClick(self, element):

        item = self.find_element_by_id(element)

        WebDriverWait(self, 30).until(
            EC.invisibility_of_element_located((
                By.CLASS_NAME, 'ajax-bg'
            ))
        )

        return item

    def script(self):
        try:

            self.find_element_by_css_selector(
                f"[title='Add {PRODUCT_ID} to cart']").click()
            self.find_element_by_id('LFrame_CheckoutButton').click()
            self.find_element_by_class_name('btnCheckoutContinue').click()
            self.find_element_by_id('cbAgree').click()
            self.find_element_by_id('rdoShipFee65').click()
            self.find_element_by_id('ctl00_LFrame_btncontinue').click()
            self.waitThenClick('rdoCreditCard').click()
            self.find_element_by_id('ctl00_LFrame_btncontinue').click()
            self.find_element_by_id(
                'ctl00_LFrame_txtNameOnCard').send_keys(CARD_NAME)
            self.find_element_by_id(
                'ctl00_LFrame_txtCardNumber').send_keys(CARD_NUMBER)

            element = self.find_element_by_id('ctl00_LFrame_ddlMonth')
            element.click()
            element = element.find_element_by_css_selector(
                f"[value='{EXPIRY_MONTH}']").click()

            element = self.find_element_by_id('ctl00_LFrame_ddlYear')
            element.click()
            element = element.find_element_by_css_selector(
                f"[value='{EXPIRY_YEAR}']").click()

            self.find_element_by_id('ctl00_LFrame_txtCvv').send_keys(CVV)
            self.find_element_by_id('ctl00_LFrame_ImageButton2').click()
            self.find_element_by_id('ctl00_LFrame_cbAgree').click()
            self.find_element_by_id('ctl00_LFrame_btncontinue').click()
            return True

        except Exception as e:
            print(e)
            return False
