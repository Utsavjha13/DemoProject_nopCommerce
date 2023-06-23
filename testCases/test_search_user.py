import pytest

from pageObject.login_page import login
from pageObject.Add_user import addNewUser
from pageObject.search_user import searchByEmail
from Utilities.readProperties import ReadConfig_searchuser
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen


class Test_search_user:
    App_url = ReadConfig.getAppURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    Create_Logs = LogGen.log_gen()
    searched_email = ReadConfig_searchuser.search()

    @pytest.mark.Sanity
    @pytest.mark.Regression

    def test_search_user_by_email(self, wd):
        self.Create_Logs.info('************* SearchCustomerByEmail **********')
        self.driver = wd
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.App_url)
        self.lp = login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.newUser = addNewUser(wd)
        self.newUser.click_outer_customer()
        self.newUser.click_inner_customer()
        self.srchEmail = searchByEmail(self.driver)
        self.srchEmail.put_email(self.searched_email)
        self.srchEmail.click_search()
        self.srchEmail.search_results(self.searched_email)
        self.flag = self.srchEmail.search_results(self.searched_email)
        if self.flag == True:
            self.Create_Logs.info('************* SearchCustomerByEmail>>>>PASSED **********')
            self.driver.quit()
            assert True
        else:
            self.Create_Logs.info('************* SearchCustomerByEmail>>>>>FAILED **********')
            self.driver.save_screenshot("/Users/utsav.jha/PycharmProjects/nopCommerce/Screenshots/test_seach_user.png")
            self.driver.quit()
            assert False
