# This script automatically reserves Wilson weightlifting slots.
# usage: python GymScheduler.py --day=monday --startTime=9:20AM
# use cron (unix) or TaskScheduler (windows) to get this to run automatically 48 hours before
# you need selenium webdriver for chrome and selenium python bindings installed.

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import sys
from datetime import datetime


netId = "replaceWithNetId";
password = "replaceWithPassword";
otpCode = "replaceWithOtpCode" # MUST BE CHANGED EVERYTIME!
enrollTime = datetime(2021, 10, 28, 7,0,0,0);
loginTime = datetime(2021, 10, 28, 6,55,0,0) # time to login and go to the enroll page. Don't wanna be too early or else the login will timeout
pollFreq = sys.float_info.min;





#time = datetime.datetime.strptime(timeStr, "%I:%M%p");
while datetime.now() < loginTime:
    print("Waiting for loginTime")
browser = webdriver.Chrome();
browser.get("https://dukehub.duke.edu");
xpath = "//*[contains(text(),'Student,')]"
WebDriverWait(browser, 100, pollFreq).until(EC.element_to_be_clickable((By.XPATH, xpath))).click();
WebDriverWait(browser, 100, pollFreq).until(EC.element_to_be_clickable((By.ID, "expand-netid"))).click();
WebDriverWait(browser, 100).until(EC.visibility_of(browser.find_element_by_id("j_username"))).send_keys(netId);
browser.find_element_by_id("j_password").send_keys(password);

WebDriverWait(browser, 100, pollFreq).until(EC.element_to_be_clickable((By.ID, "duoPasscodeInput"))).send_keys(otpCode);
browser.find_element_by_id("Submit").click();
WebDriverWait(browser, 100, pollFreq).until(EC.presence_of_element_located((By.ID, "app")));
browser.get("https://dukehub.duke.edu/psp/CSPRD01/EMPLOYEE/SA/s/WEBLIB_HCX_EN.H_SHOPPING_CART.FieldFormula.IScript_Main");
WebDriverWait(browser, 100, pollFreq).until(EC.presence_of_element_located((By.ID, "app")));
browser.set_window_size(1002, 931);
browser.switch_to.frame(0)
enrollXpath = "//*[contains(text(),'Enroll')]"

while datetime.now() < enrollTime:
    print("Waiting for enrollTime")

browser.find_element(By.CSS_SELECTOR, ".flex-fill > .cx-MuiButton-contained > .cx-MuiButton-label").click()

input("press to close program");