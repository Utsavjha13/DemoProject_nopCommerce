import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class find_product_rating:
    click_sidebar_catalog_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a"
    click_catalog_prod_reviw_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[4]/a/i"
    length_of_row_Xpath = '//*[@id="productreviews-grid"]//tbody//tr'
    page_Xpath = '//*[@class="dataTables_length"]//label//select'

    def __init__(self, driver):
        self.driver = driver

    def product_review_page(self):
        self.driver.find_element(By.XPATH, self.click_sidebar_catalog_Xpath).click()
        self.driver.find_element(By.XPATH, self.click_catalog_prod_reviw_Xpath).click()

    def full_page(self):
        time.sleep(2)
        self.page100 = Select(self.driver.find_element(By.XPATH, self.page_Xpath))
        self.page100.select_by_value('100')

    def five_star_rating(self,star):
        row = len(self.driver.find_elements(By.XPATH, self.length_of_row_Xpath))
        product_list = []
        for i in range(1, row + 1):
            rating = self.driver.find_element(By.XPATH, '//*[@id="productreviews-grid"]//tbody//tr['+str(i)+']//td[8]')
            if int(rating.text) == star:
                product = self.driver.find_element(By.XPATH, '//*[@id="productreviews-grid"]//tbody//tr['+str(i)+']//td[3]')
                product_list.append(product.text)

        return product_list

