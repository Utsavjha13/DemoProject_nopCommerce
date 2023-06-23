import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture()
def wd(browser):
    location = "/Users/utsav.jha/PycharmProjects/nopCommerce/Download_files"
    #   plugins.always_open_pdf_externally should true if pdf is downloading
    preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally": True}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)

    if browser == 'chrome':
        driver = webdriver.Chrome(options=ops)
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver = webdriver.Chrome(options=ops)
        print("Launching chrome browser.........")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to wd method
    return request.config.getoption("--browser")


########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata = {'Project Name':'nop Commerce',
                     'Module Name':'Customers',
                     'Tester': 'Utsav'}

# The correct way to update the 'config._metadata' dictionary in pytest is by assigning a new one to it. The reason for this is that the config._metadata attribute in pytest is not a regular dictionary but a special metadata object. When you assign a new dictionary to it, you are replacing the existing metadata object with a new one that contains your custom metadata.
# On the other hand, using config._metadata['Project Name'] = 'Hybrid Framework Practice' would only work if the config._metadata object is already initialized as a dictionary. If it is not initialized or is of a different type, assigning a new key-value pair using square brackets would raise an error.
# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
