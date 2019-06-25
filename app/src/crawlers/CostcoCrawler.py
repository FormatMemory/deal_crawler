from src.crawlers.BrowserRobot import BrowserRobot
from config.secret import COSTCO_URL, COSTCO_DEAL_URL, COSTCO_USERNAME, COSTCO_PASSWORD


class CostcoCrawler(BrowserRobot):
    def __init__(self):
        self.driver = None
        BrowserRobot.__init__(self)

    def run(self):
        try:
            self.login()
            self.go_sample_deal()
            self.save_source()
        except Exception as e:
            print(str(e))
        else:
            self.logout()

    def login(self):
        try:
            print(COSTCO_URL)
            self.driver.get(COSTCO_URL)
            self.driver.find_element_by_id("header_sign_in").click()
            self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sign In'])[2]/following::div[2]").click()
            self.driver.find_element_by_id("logonId").clear()
            self.driver.find_element_by_id("logonId").send_keys(COSTCO_USERNAME)
            self.driver.find_element_by_id("logonPassword").clear()
            self.driver.find_element_by_id("logonPassword").send_keys(COSTCO_PASSWORD)
            self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Remember Me'])[1]/following::input[1]").click()
        except Exception as e:
            print(str(e))
        else:
            print("Login Success")

    def logout(self):
        try:
            self.driver.get(COSTCO_URL)
            self.driver.find_element_by_id("myaccount-d").click()
            self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Preferences'])[1]/following::input[1]").click()
            print("end Logout")
        except Exception as e:
            print(str(e))

    def go_sample_deal(self):
        try:
            self.driver.get(COSTCO_DEAL_URL)
            self.driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Also available with AppleCare+'])[1]/following::img[1]").click()
            self.driver.find_element_by_link_text("New Apple iMac 21.5\" - Intel Core i5 3.0 GHz - 8GB Memory - 1TB Fusion Drive - 2GB Radeon Pro 560X Graphics").click()
        except Exception as e:
            print(str(e))
        else:
            return self.driver.page_source