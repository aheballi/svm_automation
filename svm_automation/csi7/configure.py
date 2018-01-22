from selenium import webdriver


class Credentials:
    url = "https://csi7.secunia.com"
    username = "Anusha_user"
    password = "Flexera1!"

class ElementValueLogin:
    ctrl_login = "ext-comp-1034"
    ctrl_password = "ext-comp-1035"
    btn_submit = "ext-gen32"

class ElementFeatureValue:
   #id1 = "ext-gen270"
   ctrl_scanning_xpath = "//li[2]//a/span[text()='Scanning']"
   ctrl_download_tag = "Download Local Agent"
   ctrl_download_link = "Microsoft Windows"