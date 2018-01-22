from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Credentials:
         url = "https://uat.app.flexerasoftware.com/login/"
         user_name = "aheballi"
         password = "Flexera1!"


class SeleniumWebdriver:
    fp = webdriver.FirefoxProfile()
    fp.set_preference("browser.download.folderList", 2)
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/octet-stream')
    #fp.set_preference("browser.helperApps.alwaysAsk.force", False)
    #fp.set_preference("browser.download.manager.showWhenStarting", False)
    fp.set_preference("browser.download.dir", '/home/anusha/Downloads/')

    #fc = webdriver.DesiredCapabilities.FIREFOX
    # fc['firefox_profile'] = fp.encoded
    # fc['marionette'] = True
    # fc['binary'] = 'tools/firefox/firefox-bin'

    #driver = webdriver.Firefox(executable_path=r'/home/anusha/SVM/geckodriver/geckodriver', firefox_profile=fp)
    driver = webdriver.Firefox(executable_path=r'/home/anusha/SVM/geckodriver/geckodriver',firefox_profile=fp)
    #driver_withoutdownloadskip = webdriver.Firefox(executable_path=r'/home/anusha/SVM/geckodriver/geckodriver')


class ElementValueLogin:
    ctrl_login = "inputEmail"
    ctrl_password = "inputPassword"
    btn_submit = "submit-btn"


class ElementValueFeatures:
    ctrl_dashboard = "link_dashboard"
    ctrl_notification = "link_notifications"
    ctrl_vulnerability = "Vulnerability Manager"

class Dashboard:
    ctrl_classname = "glyphicon-remove"
    ctrl_save_button = "//div[1]/button/span[text()='Save']"
    ctrl_dashboard = "link_dashboard"

class AddDashboard:
    ctrl_add_class = "glyphicons-plus"
    ctrl_advisories = "//div/div/ul/li[1]/a[text()='Advisories released last year']"
    ctrl_devices = "Devices Overview"
    ctrl_device_status = "Devices status - System score"
    ctrl_devices_status_time = "Devices status - Time since last scan"
    ctrl_latest_advisories_affecting_your_security = "Latest advisories affecting your security"
    ctrl_latest_advisories = "Latest advisories"
    ctrl_latest_advisories_per_watchList = "Latest advisories per watch list"
    ctrl_latest_available_patches = "Latest available patches"
    ctrl_most_critical_advisories = "Most critical advisories affecting your security"
    ctrl_most_prevalent_EOL_software_Installations = "Most prevalent EOL software installations"
    ctrl_most_prevalent_insecure_software_installtions = "Most prevalent insecure software installations"
    ctrl_opened_tickets_pattern = "Opened tickets pattern"
    ctrl_open_tickets_split = "Open tickets split by advisory criticality"
    ctrl_tickets_split_by_status = "Tickets split by status"
    ctrl_your_latest_assigned_tickets = "Your latest assigned tickets"



