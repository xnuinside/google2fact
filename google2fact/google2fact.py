
from os import getenv
import time

from .read_codes import get_code
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user_mail = getenv('GMAIL')
password = getenv('GMAIL_PASSWORD')


def get_auth(browser):

    username = browser.find_element_by_id('Email')
    username.send_keys(user_mail)
    next_button = browser.find_element_by_id('next')
    next_button.click()
    password = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'Passwd')))
    password.send_keys(password)
    signInButton = browser.find_element_by_id('signIn')
    signInButton.click()

    try_another_way = browser.find_element_by_xpath(
        '//*[@id="skipChallenge"]')
    try_another_way.click()
    time.sleep(1)
    code_button = browser.find_element_by_xpath(
        '//*[@id="view_container"]/form/div[2]/div/div/div/ul/li[2]/div')
    code_button.click()
    time.sleep(2)

    code = get_code()

    try:
        code_input = browser.find_element_by_xpath(
            '//*[@id="backupCodePin"]')
        code_input.send_keys(code)
        next_button = browser.find_element_by_xpath(
            '//*[@id="backupCodeNext"]')
        next_button.click()
    except:
        pass
