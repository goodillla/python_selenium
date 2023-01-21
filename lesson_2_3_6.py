from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn[type='submit']")
    submit.click()

    new_window = browser.window_handles[1]
    print((new_window))
    browser.switch_to.window(new_window)

    x = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x.text
    print(x)
    y = calc(x)
    print(y)

    answer = browser.find_element(By.CSS_SELECTOR, "input#answer")
    answer.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn[type='submit']")
    submit.click()

    alert = browser.switch_to.alert
    print(alert.text)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()