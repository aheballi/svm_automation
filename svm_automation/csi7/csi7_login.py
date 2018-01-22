from csi7.configure import Credentials
from csi7.configure import ElementValueLogin
from selenium_elements.selenum_fetchelement import Element
from util.conf import selenium_webdriver

class Login:
    launch_browser = selenium_webdriver.driver
    launch_browser.get(Credentials.url)
    Element.fetch_element_by_id(launch_browser, ElementValueLogin.ctrl_login).send_keys(Credentials.username)
    Element.fetch_element_by_id(launch_browser, ElementValueLogin.ctrl_password).send_keys(Credentials.password)
    Element.fetch_element_by_id(launch_browser, ElementValueLogin.btn_submit).click()