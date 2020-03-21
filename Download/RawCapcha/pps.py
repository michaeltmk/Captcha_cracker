#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:28:34 2019

@author: michael
"""

import time
from datetime import datetime as dt
from selenium import webdriver as webdriver
from selenium.webdriver.support.select import Select as Select
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib.request
import traceback
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
#import captcha2text

print(dt.today().isoformat(),': pps start')

delay_time=1



class pps: 
    def __init__(self):
        chrome=webdriver.Chrome("/usr/local/bin/chromedriver")
        chrome.implicitly_wait(10)
        chrome.get('https://www.ppshk.com/pps/pps2/revamp2/template/pc/login_c.jsp')
        self.chrome=chrome

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.chrome.quit()

    def check_captcha(self):
        for i in range(256,384):
            src=self.chrome.find_element_by_id('exampleCaptchaTag_CaptchaImage').get_attribute('src')
            urllib.request.urlretrieve(src, "/home/pi/Desktop/gdrive/pps/img/captcha%i.bmp"%i)
            time.sleep(1)
            self.chrome.refresh()

with pps() as n:
    n.check_captcha()
#n.chrome.quit()
print(dt.today().isoformat(),': pps end')