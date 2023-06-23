import time

import pytest
from selenium.webdriver.common.by import By

from pageObject.login_page import login
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen
from pageObject.Add_user import addNewUser
from Utilities.readProperties import NewUserReadconfig
import string
import random


class Test_002:
    App_url = ReadConfig.getAppURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    Create_Logs = LogGen.log_gen()
    email = NewUserReadconfig.setemail()
    fname = NewUserReadconfig.setfname()
    lname = NewUserReadconfig.setlname()
    Newpassword = NewUserReadconfig.setpassword()
    dob = NewUserReadconfig.setdob()
    news = NewUserReadconfig.setNews()
    comp = NewUserReadconfig.setComp()
    gender = NewUserReadconfig.setgender()
    role = NewUserReadconfig.setrole()
    vendor = NewUserReadconfig.setVendor()


    @pytest.mark.Regression

    def test_Add_newUser_test(self, wd):
        self.Create_Logs.info("**************Verify Test_001>test_Add_newUser_test*********")
        self.driver = wd
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.App_url)
        self.lp = login(wd)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.newUser = addNewUser(wd)
        self.newUser.click_outer_customer()
        self.newUser.click_inner_customer()
        self.newUser.add_new_button()
        self.newUser.set_personal_details(self.email, self.Newpassword, self.fname, self.lname)
        self.newUser.set_gender(self.gender)
        self.newUser.set_dob(self.dob)
        self.newUser.set_company_name(self.comp)
        self.newUser.set_customer_role(self.role)
        self.newUser.set_newsLetter(self.news)
        # self.newUser.set_vendor(self.vendor)
        self.newUser.save_button()
        self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'new customer has been added successfully' in self.msg:
            self.driver.save_screenshot("/Users/utsav.jha/PycharmProjects/nopCommerce/Screenshots/test_Add_newUser_test.png")
            self.Create_Logs.info("********* Add customer Test Passed *********")
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot("/Users/utsav.jha/PycharmProjects/nopCommerce/Screenshots/test_Add_newUser_test_failed.png")
            self.Create_Logs.error("********* Add customer Test Failed ************")
            self.driver.quit()
            assert False
