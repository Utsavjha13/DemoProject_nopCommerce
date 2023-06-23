from selenium.webdriver.common.by import By


class searchByEmail:
    inputbox_Srch_Email_ID = 'SearchEmail'
    button_srch_ID = 'search-customers'
    row = "//table[@id='customers-grid']/tbody/tr"

    def __init__(self, driver):
        self.driver = driver

    def put_email(self, email):
        self.driver.find_element(By.ID, self.inputbox_Srch_Email_ID).clear()
        self.driver.find_element(By.ID, self.inputbox_Srch_Email_ID).send_keys(email)

    def click_search(self):
        self.driver.find_element(By.ID, self.button_srch_ID).click()

    def len_row(self):
        row_num = len(self.driver.find_elements(By.XPATH, self.row))
        return row_num

    def search_results(self, email):
        flag = False
        for i in range(1, self.len_row() + 1):
            user_email = self.driver.find_element(By.XPATH,
                                                  "//table[@id='customers-grid']//tbody//tr[" + str(i) + "]//td[2]")
            if user_email.text == email:
                flag = True
                break
        return flag
