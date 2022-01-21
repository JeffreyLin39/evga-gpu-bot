from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://www.evga.com/products/productlist.aspx?type=8"
chrome_prefs = {}
DRIVER_PATH = "C:/Python310/SeleniumDrivers/chromedriver.exe"
PROFILE = "user-data-dir=C:/Users/Jeffrey Lin/AppData/Local/Google/Chrome/User Data"
VPN_PATH = r'C:\\Program Files (x86)\\Windscribe\\Windscribe.exe'
PRODUCT_ID = os.getenv('Product_ID')
CARD_NAME = os.getenv('Card_Name')
CARD_NUMBER = os.getenv('Card_Number')
EXPIRY_MONTH = os.getenv('Expiry_Month')
EXPIRY_YEAR = os.getenv('Expiry_Year')
CVV = os.getenv('CVV')
