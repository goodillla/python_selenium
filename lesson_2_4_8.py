from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = WebDriverWait(browser, 15).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100")
    )

    button = browser.find_element(By.CSS_SELECTOR, "button#book")
    button.click()

    x = browser.find_element(By.CSS_SELECTOR, "span#input_value")
    x = x.text
    print(x)
    y = calc(x)
    print(y)

    input = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input.send_keys(y)

    submit = browser.find_element(By.CSS_SELECTOR, "button#solve")
    submit.click()

    message = browser.find_element(By.CSS_SELECTOR, "verify_message")

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()