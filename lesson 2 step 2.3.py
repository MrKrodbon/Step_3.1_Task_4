from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = " http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_class_name("btn-primary").click()
    Warn = browser.switch_to_alert()
    Warn.accept()
    Answer = browser.find_element_by_id("answer")
    x = browser.find_element_by_id("input_value")

    y = calc(int(x.text))
    Answer.send_keys(str(y))
    SubmButton = browser.find_element_by_class_name("btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()