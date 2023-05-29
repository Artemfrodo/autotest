# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "submit_button")
#     button.click()
#
# finally:
#     # закрываем браузер после всех манипуляций
#     browser.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/simple_form_find_task.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# link = "http://suninjuly.github.io/find_link_text"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#     e = str(math.ceil(math.pow(math.pi, math.e) * 10000))
#     a = browser.find_element(By.LINK_TEXT, e)
#     a.click()
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
# finally:
#     time.sleep(30)
#     browser.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/huge_form.html")
#     elements = browser.find_elements(By.TAG_NAME, "input")
#     for element in elements:
#         element.send_keys("Игорь лох")
#
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# link = "http://suninjuly.github.io/find_xpath_form"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     input1 = browser.find_element(By.TAG_NAME, "input")
#     input1.send_keys("Ivan")
#     input2 = browser.find_element(By.NAME, "last_name")
#     input2.send_keys("Petrov")
#     input3 = browser.find_element(By.CLASS_NAME, "city")
#     input3.send_keys("Smolensk")
#     input4 = browser.find_element(By.ID, "country")
#     input4.send_keys("Russia")
#     button = browser.find_element(By.XPATH, "//button[@type='submit']")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(15)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
#
# # не забываем оставить пустую строку в конце файла

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     elements1 = browser.find_element(By.CSS_SELECTOR, "input.first[required]")
#     elements2 = browser.find_element(By.CSS_SELECTOR, "input.second[required]")
#     elements3 = browser.find_element(By.CSS_SELECTOR, "input.third[required]")
#     a = [elements1, elements2, elements3]
#     for element in a:
#         element.send_keys("Игорь лох")
#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
# # try:
# #     link = "http://suninjuly.github.io/registration1.html"
# #     browser = webdriver.Chrome()
# #     browser.get(link)
# #     elements = browser.find_elements(By.CSS_SELECTOR, "input:not([required])")
# #     for element in elements:
# #             element.send_keys("Игорь лох")
# #     # Отправляем заполненную форму
# #     button = browser.find_element(By.CSS_SELECTOR, ".btn-default")
# #     button.click()
# #
# #     # Проверяем, что смогли зарегистрироваться
# #     # ждем загрузки страницы
# #     time.sleep(1)
# #
# #     # находим элемент, содержащий текст
# #     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
# #     # записываем в переменную welcome_text текст из элемента welcome_text_elt
# #     welcome_text = welcome_text_elt.text
# #
# #     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
# #     assert "Congratulations! You have successfully passed second test!" == welcome_text
# #
# # finally:
# #     # ожидание чтобы визуально оценить результаты прохождения скрипта
# #     time.sleep(10)
# #     # закрываем браузер после всех манипуляций
# #     browser.quit()
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# try:
#     link = "https://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     y = calc(x)
#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer.send_keys(y)
#     check = browser.find_element(By.CSS_SELECTOR, "[for=robotCheckbox]")
#     check.click()
#     radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     radio.click()
#     submit = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
#     submit.click()
# finally:
#     time.sleep(10)
#     browser.quit()
# import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# try:
#     link = "http://suninjuly.github.io/get_attribute.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     treasure = browser.find_element(By.CSS_SELECTOR, "img")
#     x = treasure.get_attribute("valuex")
#     x_element = x
#     y = calc(x)
#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer.send_keys(y)
#     check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     check.click()
#     radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     radio.click()
#     submit = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
#     submit.click()
# finally:
#     time.sleep(10)
#     browser.quit()
import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import Select
# try:
#     link = " https://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     num1 = browser.find_element(By.CSS_SELECTOR, "#num1")
#     num2 = browser.find_element(By.CSS_SELECTOR, "#num2")
#     num1 = num1.text
#     num2 = num2.text
#     x = int(num1)
#     y = int(num2)
#     sum = x + y
#     sum = str(sum)
#     select = Select(browser.find_element(By.TAG_NAME, "select"))
#     select.select_by_value(sum)
#     button = browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
# finally:
#     time.sleep(10)
#     browser.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(By.TAG_NAME, "button")
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import Select
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# try:
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     inputx = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = inputx.text
#     y = calc(x)
#     input_answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     input_answer.send_keys(y)
#     check = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
#     check.click()
#     radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
#     radio.click()
#     button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()
import math
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import Select
# import os
# try:
#     link = "http://suninjuly.github.io/file_input.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     first = browser.find_element(By.CSS_SELECTOR, "[name=firstname]")
#     first.send_keys("Dima lox")
#     last = browser.find_element(By.CSS_SELECTOR, "[name=lastname]")
#     last.send_keys("Igor lox")
#     email = browser.find_element(By.CSS_SELECTOR, "[name=email]")
#     email.send_keys("Artem cool")
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file_path = os.path.join(current_dir, 'shit.txt')
#     file_insert = browser.find_element(By.CSS_SELECTOR, "#file")
#     file_insert.send_keys(file_path)
#     button = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import Select
# import os
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# try:
#     link = "http://suninjuly.github.io/alert_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button_submit = browser.find_element(By.CSS_SELECTOR, "[type=submit]")
#     button_submit.click()
#     confirm = browser.switch_to.alert
#     confirm.accept()
#     input_value = browser.find_element(By.CSS_SELECTOR,"#input_value")
#     x = input_value.text
#     y = calc(x)
#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer_input = answer.send_keys(y)
#     button_submit2 = browser.find_element(By.CSS_SELECTOR,".btn-primary")
#     button_submit2.click()
# finally:
#     time.sleep(10)
#     browser.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import Select
# import os
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
# try:
#     link = "http://suninjuly.github.io/redirect_accept.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button_troll = browser.find_element(By.CSS_SELECTOR, ".trollface.btn")
#     button_troll.click()
#     new_window = browser.window_handles[1]
#     browser.switch_to.window(browser.window_handles[1])
#     input_value = browser.find_element(By.CSS_SELECTOR,"#input_value")
#     x = input_value.text
#     y = calc(x)
#     answer = browser.find_element(By.CSS_SELECTOR, "#answer")
#     answer_input = answer.send_keys(y)
#     button_submit2 = browser.find_element(By.CSS_SELECTOR,".btn-primary")
#     button_submit2.click()
# finally:
#     time.sleep(10)
#     browser.quit()
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# from selenium.webdriver.support.ui import Select
# import os
# try:
#     link = "http://suninjuly.github.io/cats.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     button = browser.find_element(By.ID, "button")
# finally:
#     time.sleep(10)
#     browser.quit()
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    button_location = browser.find_element(By.CSS_SELECTOR, "#book")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"), "$100"))
    button_location.click()
    input_value = browser.find_element(By.CSS_SELECTOR, "#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_value)
    x = input_value.text
    y = calc(x)
    answer = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input = answer.send_keys(y)
    button_submit = browser.find_element(By.CSS_SELECTOR,"#solve")
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()
