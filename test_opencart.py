from classes import LoginPage, MainPage, Catalogue, ProductDescription, RegisterPage


def test_check_elements_loginpage(browser):
    browser.get(browser.url + "/index.php?route=account/login")
    browser.find_element(*LoginPage.CONTINUE_BTN)
    browser.find_element(*LoginPage.LOGIN_BTN)
    browser.find_element(*LoginPage.EMAIL_FIELD)
    browser.find_element(*LoginPage.NEWSLETTER_LINK)
    browser.find_element(*LoginPage.DOWNLOADS_LINK)


def test_check_elements_mainpage(browser):
    browser.get(browser.url)
    browser.find_element(*MainPage.OPENCART_LOGO)
    browser.find_element(*MainPage.BIG_PICTURE)
    browser.find_element(*MainPage.SEARCH_FIELD)
    browser.find_element(*MainPage.SEARCH_BUTTON)
    browser.find_element(*MainPage.PHOTOCAMERA)


def test_check_elements_product_description(browser):
    browser.get(browser.url + "/macbook")
    browser.find_element(*ProductDescription.DESCR_TAB)
    browser.find_element(*ProductDescription.TWEET_LINK)
    browser.find_element(*ProductDescription.QTY_FIELD)
    browser.find_element(*ProductDescription.PRICE)
    browser.find_element(*ProductDescription.PRODUCT_PICTURE)


def test_check_elements_product_catalogue(browser):
    browser.get(browser.url + "/desktops/mac")
    browser.find_element(*Catalogue.DESKTOP_IMAC)
    browser.get(browser.url + "/desktops")
    browser.find_element(*Catalogue.DROPDOWN_LIST_VALUE)
    browser.get(browser.url + "/component/mouse")
    browser.find_element(*Catalogue.MICE_TRACKBALLS)
    browser.get(browser.url + "/tablet")
    browser.find_element(*Catalogue.TABLETS_LBTN)
    browser.get(browser.url + "/smartphone")
    browser.find_element(*Catalogue.PDA_HTC)


def test_check_elements_register_page(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    browser.find_element(*RegisterPage.PRIVACY_CHECKBOX)
    browser.find_element(*RegisterPage.SUBSCRIBE_RADIOBUTTON)
    browser.find_element(*RegisterPage.PD_HEADER)
    browser.find_element(*RegisterPage.LOGIN_LINK)
    browser.find_element(*RegisterPage.FIRSTNAME)


