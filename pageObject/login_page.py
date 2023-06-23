from selenium.webdriver.common.by import By


class login:
    login_icon_Xpath = "//*[@id='en-page']/body/div[7]/header/nav/ul/li[3]/span/span/svg"
    login_option_Xpath = '//*[@id="en-page"]/body/div[7]/header/nav/ul/li[3]/ul/li[1]/a/span'
    inputbox_username_Id = 'Email'
    inputbox_Password_Id = 'Password'
    button_login_Xpath = '//*[@class="buttons"]//button'
    button_logout_Xpath= "//*[@class='nav-link' and contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver = driver

    def setUsername(self, username):
        self.driver.find_element(By.ID, self.inputbox_username_Id).clear()
        self.driver.find_element(By.ID, self.inputbox_username_Id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.inputbox_Password_Id).clear()
        self.driver.find_element(By.ID, self.inputbox_Password_Id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_Xpath).click()


    def clicklogout(self):
        self.driver.find_element(By.XPATH,self.button_logout_Xpath).click()
