import time

from pageObject.login_page import login
from pageObject.SearchByproductCategory import prodCategory
from Utilities.readProperties import ReadConfig
from Utilities.logger import LogGen
from Utilities.readProperties import ReadConfig_product_cat_search


class Test_product_Search:
    App_url = ReadConfig.getAppURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    catg = ReadConfig_product_cat_search.catg_search()
    Create_Logs = LogGen.log_gen()

    def test_productSearch(self, wd):
        self.Create_Logs.info("**************verify Test_product_Search*********")
        self.driver = wd
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.App_url)
        self.lp = login(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.Create_Logs.info("**************Login Completed*********")
        self.pc = prodCategory(self.driver)
        self.pc.click_catalog()
        self.pc.select_category(self.catg)
        self.pc.click_search()
        self.pc.select_table()
        self.pc.click_export_excel()
        self.Create_Logs.info("**************File downloaded*********")
        flag = self.pc.verify_download()
        time.sleep(10)
        if flag == False:
            self.Create_Logs.info("***********Test_product_Search>>>PASSED************")
            self.driver.quit()
            assert True
        else:
            self.Create_Logs.info("***********Test_product_Search>>>FAILED************")
            self.driver.quit()
            assert False
