import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import string
import random


class addNewUser:
    customer_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/i"
    Inner_customer_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    button_Add_new_Xpath = '//*[@class="btn btn-primary"]//i'
    inputbox_Email_Id = 'Email'
    inputbox_password_Id = 'Password'
    inputbox_firstName_Id = 'FirstName'
    inputbox_lastName_Id = 'LastName'
    checkBox_G_Male_Id = 'Gender_Male'
    checkBox_G_Female_Id = 'Gender_Female'
    inputbox_DateOfBirth_Id = 'DateOfBirth'
    inputbox_Company_Id = 'Company'
    checkbox_IsTaxExempt_Xpath = '//*[@id="IsTaxExempt"]'
    inputbox_NewsLetter_Xpath = '//*[@id="customer-info"]/div[2]/div[9]/div[2]/div/div[1]/div/div'
    selectbox_CR_Xpath = '//*[@id="customer-info"]/div[2]/div[10]/div[2]/div/div[1]/div/div'
    selectbox_CR_delte_Xpath='//*[@id="SelectedCustomerRoleIds_taglist"]/li/span[2]'
    selectBox_CR_register_Xpath = "//li[contains(text(),'Registered')]"
    selectBox_CR_guest_Xpath = "//li[contains(text(),'Guests')]"
    selectBox_CR_Administrators_Xpath = "//li[contains(text(),'Administrators')]"
    selectBox_CR_FM_Xpath = "//li[contains(text(),'Forum Moderators')]"
    selectbox_managerofvender_Id = 'VendorId'
    inputbox_adminComments_Id = 'AdminComment'
    button_Save_Xpath = '//*[@name="save"]'
    success_Xpath = "/html/body/div[3]/div[1]/div[1]"
    input_youstorename_Xpath='//li[contains(text(),"Your store name")]'
    input_teststore2_Xpath= '//li[contains(text(),"Test store 2")]'

    def __init__(self, driver):
        self.driver = driver

    def click_outer_customer(self):
        self.driver.find_element(By.XPATH, self.customer_Xpath).click()

    def click_inner_customer(self):
        self.driver.find_element(By.XPATH, self.Inner_customer_Xpath).click()

    def add_new_button(self):
        self.driver.find_element(By.XPATH, self.button_Add_new_Xpath).click()

    def set_personal_details(self, email, fname, lname, password):
        self.driver.find_element(By.ID, self.inputbox_Email_Id).send_keys(email)
        self.driver.find_element(By.ID, self.inputbox_password_Id).send_keys(password)
        self.driver.find_element(By.ID, self.inputbox_firstName_Id).send_keys(fname)
        self.driver.find_element(By.ID, self.inputbox_lastName_Id).send_keys(lname)

    def set_gender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.checkBox_G_Male_Id).click()

        elif gender == "Female":
            self.driver.find_element(By.ID, self.checkBox_G_Female_Id).click()

    def set_dob(self, dob):
        self.driver.find_element(By.ID, self.inputbox_DateOfBirth_Id).send_keys(dob)

    def set_company_name(self, comp):
        self.driver.find_element(By.ID, self.inputbox_Company_Id).send_keys(comp)

    def set_IsTaxExempt(self):
        self.driver.find_element(By.XPATH, self.checkbox_IsTaxExempt_Xpath).click()

    def set_customer_role(self, role):
        self.driver.find_element(By.XPATH, self.selectbox_CR_Xpath).click()

        if role == "Registered":
            self.roles = self.driver.find_element(By.XPATH, self.selectBox_CR_register_Xpath)
        elif role == "Guests":
            self.driver.find_element(By.XPATH, self.selectbox_CR_delte_Xpath).click()
            self.roles = self.driver.find_element(By.XPATH, self.selectBox_CR_guest_Xpath)
        elif role == "Administrators":
            self.roles = self.driver.find_element(By.XPATH, self.selectBox_CR_Administrators_Xpath)
        elif role == "Forum Moderators":
            self.roles = self.driver.find_element(By.XPATH, self.selectBox_CR_FM_Xpath)
        else:
            self.roles = self.driver.find_element(By.XPATH, self.selectBox_CR_guest_Xpath)
        # self.roles.click()
        self.driver.execute_script("arguments[0].click();", self.roles)

    def set_newsLetter(self, newss):
        self.driver.find_element(By.XPATH, self.inputbox_NewsLetter_Xpath).click()
        if newss== "Your store name":
            self.news = self.driver.find_element(By.XPATH,self.input_youstorename_Xpath)
        elif newss== "Test store 2":
            self.news = self.driver.find_element(By.XPATH,self.input_teststore2_Xpath)
        else:
            self.newss = self.driver.find_element(By.XPATH, self.input_youstorename_Xpath)
        # self.news.click()
        self.driver.execute_script("arguments[0].click();", self.news)

    def set_vendor(self, vendor):
        vd = Select(self.driver.find_element(By.ID, self.selectbox_managerofvender_Id))
        vd.select_by_visible_text(vendor)

    def save_button(self):
        self.driver.find_element(By.XPATH, self.button_Save_Xpath).click()

    def successmsg(self):
        self.msg = self.driver.find_element(By.TAG_NAME, 'body').text


