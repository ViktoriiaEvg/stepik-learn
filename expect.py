from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд на выполнение условия
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button = browser.find_element(By.ID, "book")
    # browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    # ожидание загрузки элементов
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    # считывание данных и расчет
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # ввод ответа
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    solve = browser.find_element(By.ID, "solve")
    solve.click()
    # message = browser.find_element_by_id("verify_message")

    # assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()
