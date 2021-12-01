"""
CANNOT include majority of driver data...

element identifiers...
"""
import time
import os
from urllib.request import urlopen
from openpyxl import load_workbook as LW
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchAttributeException
#from threading import Thread, Event

from messages import * # not best practice... feels good though huh?


def launch(e) -> dict:
    """
    Parameter e: engineering page
    Precondition: e must be a valid string
    """
    try:
        options = Options()
        ###################################
        # comment out options for debugging:
        options.add_argument('--headless')
        # ...or if you enjoy watching.
        ####################################
        chrome_driver = os.getcwd() + '\\chromedriver.exe'
        driver = webdriver.Chrome(options=options, executable_path=chrome_driver)
        driver.get()