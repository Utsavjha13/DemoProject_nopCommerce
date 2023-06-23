import configparser
import random
import string

config = configparser.RawConfigParser()
config.read("/Users/utsav.jha/PycharmProjects/nopCommerce/Configurations/configuration.ini")


class ReadConfig:
    @staticmethod
    def getAppURL():
        url = config.get('Login Info', 'AppUrl')
        return url

    @staticmethod
    def getusername():
        username = config.get('Login Info', 'username')
        return username

    @staticmethod
    def getpassword():
        password = config.get('Login Info', 'password')
        return password


class NewUserReadconfig:
    @staticmethod
    def setemail():
        email_name = "".join(random.choices(string.ascii_lowercase, k=5))
        email = email_name + "@gmail.com"
        return email

    @staticmethod
    def setpassword():
        password = config.get('New user', 'password')
        return password

    @staticmethod
    def setfname():
        fname = "".join(random.choices(string.ascii_lowercase, k=7))
        return fname

    @staticmethod
    def setlname():
        lname = "".join(random.choices(string.ascii_lowercase, k=5))
        return lname

    @staticmethod
    def setdob():
        day = random.choice(range(1, 31))
        month = random.choice(range(1, 13))
        years = random.choice(range(1920, 2022))
        dob = str(month) + "/" + str(day) + "/" + str(years)
        return dob

    @staticmethod
    def setNews():
        newslist = ["Test store 2", "Your store name"]
        news = random.choice(newslist)
        return news

    @staticmethod
    def setComp():
        comp = random.choice(range(25436, 35675))
        return comp

    @staticmethod
    def setgender():
        genlist = ["Male", "Female"]
        gender = random.choice(genlist)
        return gender

    @staticmethod
    def setrole():
        rolelist = ["Registered", "Administrators", "Forum Moderators", "Guests"]
        role = random.choice(rolelist)
        return role

    @staticmethod
    def setVendor():
        genlist = ["Vendor 1", "Vendor 2"]
        Vendor = random.choice(genlist)
        return Vendor


class ReadConfig_searchuser:
    @staticmethod
    def search():
        email = config.get('search user', 'email')
        return email


class ReadConfig_product_cat_search:

    @staticmethod
    def catg_search():
        catg = random.choice(range(1, 17))
        return str(catg)

