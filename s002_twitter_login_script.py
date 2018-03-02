from selenium import webdriver
from getpass import getpass

username = input('Enter your twitter id : ')
password = getpass('Enter your password : ')

driver = webdriver.Chrome()
driver.get('https://twitter.com/login')

username_box = driver.find_element_by_class_name('js-username-field')
username_box.send_keys(username)

password_box = driver.find_element_by_class_name('js-password-field')
password_box.send_keys(password)

login_btn = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
login_btn.submit()