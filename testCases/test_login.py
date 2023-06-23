import pytest

from pageObject.login_page import login
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen


class Test_001:
    App_url = ReadConfig.getAppURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    Create_Logs = LogGen.log_gen()
    @pytest.mark.Regression

    def test_login_page_title(self, wd):
        self.Create_Logs.info("**************verify Test_001>test_login_page_title*********")
        self.driver = wd
        self.driver.implicitly_wait(10)
        self.driver.get(self.App_url)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.quit()
            self.Create_Logs.info("**************Test_001>test_login_page_title--->PASSED*********")
            assert True
        else:
            self.driver.save_screenshot("/Users/utsav.jha/PycharmProjects/nopCommerce/Screenshots/Test_001_test_login_page_title.png")
            self.driver.quit()
            self.Create_Logs.error("**************Test_001>test_login_page_title--->FAILED*********")
            assert False

    @pytest.mark.Sanity

    def test_login_test(self, wd):
        self.Create_Logs.info("**************Verify Test_001>test_login_test*********")
        self.driver = wd
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.App_url)
        self.lp = login(wd)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        page_title = self.driver.title
        if page_title == "Dashboard    nopCommerce administration":
            self.lp.clicklogout()
            self.driver.quit()
            self.Create_Logs.info("**************Test_001>test_login_test---->PASSED*********")
            assert True
        else:
            self.driver.save_screenshot("/Users/utsav.jha/PycharmProjects/nopCommerce/Screenshots/Test_001_test_login_test.png")
            self.lp.clicklogout()
            self.driver.quit()
            self.Create_Logs.error("**************Test_001>test_login_test---->FAILED*********")
            assert False
