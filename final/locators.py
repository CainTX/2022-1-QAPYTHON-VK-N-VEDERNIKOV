from selenium.webdriver.common.by import By


class AuthLocators:

    auth_username = (By.XPATH, "//input[@id='username']")
    auth_password = (By.XPATH, "//input[@id='password']")
    auth_submit = (By.XPATH, "//input[@id='submit']")
    auth_reg = (By.XPATH, "//a[@href='/reg']")
    auth_invalid = (By.XPATH, "//div[text() = 'Invalid username or password']")
    auth_skip = (By.XPATH, "//div[text() = 'This page is available only to authorized users']")


class RegLocators:

    reg_name = (By.XPATH, "//input[@id='user_name']")
    reg_surname = (By.XPATH, "//input[@id='user_surname']")
    reg_middle_name = (By.XPATH, "//input[@id='user_middle_name']")
    reg_username = (By.XPATH, "//input[@id='username']")
    reg_email = (By.XPATH, "//input[@id='email']")
    reg_password = (By.XPATH, "//input[@id='password']")
    reg_confirm = (By.XPATH, "//input[@id='confirm']")
    reg_term = (By.XPATH, "//input[@id='term']")
    reg_submit = (By.XPATH, "//input[@id='submit']")
    reg_login = (By.XPATH, "//a[@href='/login']")
    reg_err_exist = (By.XPATH, "//div[text() = 'User already exist']")
    reg_err_server = (By.XPATH, "//div[text() = 'Internal Server Error']")
    reg_err_password = (By.XPATH, "//div[text() = 'Passwords must match']")
    reg_err_email = (By.XPATH, "//div[text() = 'Invalid email address']")


class MainLocators:

    main_logout = (By.XPATH, "//a[@href='/logout']")
    main_logged = (By.XPATH, "//li[contains(text(), 'Logged as')]")
    main_user = (By.XPATH, "//li[contains(text(), 'User: ')]")
    main_home = (By.XPATH, "//a[text() = 'HOME']")
    main_vk_id = (By.XPATH, "//li[contains(text(), 'VK ID:')]")
    main_python = (By.XPATH, "//a[@href = 'https://www.python.org/']")
    main_flask = (By.XPATH, "//a[text() = 'About Flask']")
    main_linux = (By.XPATH, "//a[text() = 'Linux']")
    main_cent_os = (By.XPATH, "//a[text() = 'Download Centos7']")
    main_network = (By.XPATH, "//a[text() = 'Network']")
    main_news = (By.XPATH, "//a[text() = 'News']")
    main_what_api = (By.XPATH, "//a[@href='https://en.wikipedia.org/wiki/Application_programming_interface']")
    main_future = (By.XPATH, "//a[@href='https://www.popularmechanics.com/technology/infrastructure/a29666802/future-of-the-internet/']")
    main_smtp = (By.XPATH, "//a[@href='https://ru.wikipedia.org/wiki/SMTP']")
    main_footer = (By.XPATH, "//p[1][contains(text(), '')]")
    main_powered = (By.XPATH, "//p[contains(text(), '2020 - 2022')]")
    main_404 = (By.XPATH, "//span[contains(text(), 'Page Not Found')]")


