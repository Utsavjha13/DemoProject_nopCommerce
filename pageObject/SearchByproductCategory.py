import os
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class prodCategory:
    click_sidebar_catalog_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a"
    click_sidebar_cat_product_Xpath = '/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a/p'
    dropD_category_ID = "SearchCategoryId"
    button_search_ID = "search-products"
    check_table_all_Xpath = '//*[@id="products-grid_wrapper"]/div[1]/div/div/div[1]/div/table/thead/tr/th[1]/input'
    DD_export_Xpath = "//div[@class='btn-group']//button[2]"
    click_export_excel_Xpath = "//*[@name='exportexcel-all']"

    def __init__(self, driver):
        self.driver = driver

    def click_catalog(self):
        self.driver.find_element(By.XPATH, self.click_sidebar_catalog_Xpath).click()
        self.driver.find_element(By.XPATH, self.click_sidebar_cat_product_Xpath).click()

    def select_category(self, catg):
        prod_cat = Select(self.driver.find_element(By.ID, self.dropD_category_ID))
        prod_cat.select_by_value(catg)

    def click_search(self):
        self.driver.find_element(By.ID, self.button_search_ID).click()

    def select_table(self):
        self.driver.find_element(By.XPATH, self.check_table_all_Xpath).click()

    def click_export_excel(self):
        self.driver.find_element(By.XPATH, self.DD_export_Xpath).click()
        self.driver.find_element(By.XPATH, self.click_export_excel_Xpath).click()

    def verify_download(self):
        location = '/Users/utsav.jha/PycharmProjects/nopCommerce/Download_files'
        wait = True
        while (wait == True):
            for fname in os.listdir(location):
                if ('Unconfirmed') in fname:
                    print('downloading files ...')
                    time.sleep(10)
                else:
                    wait = False
        return wait