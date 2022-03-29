from selenium.webdriver.common.by import By


class BasicLocators:
    spinner_large_custom_zindex = (By.XPATH, "//div[contains(@class, 'spinner_large_custom_zindex')]")
    center_module_buttonsWrap = (By.XPATH, '//ul[contains(@class, "center-module-buttonsWrap")]')
    right_module_userNameWrap = (By.XPATH, '//div[contains(@class, "right-module-userNameWrap")]')
    notification_locator = (By.XPATH, '//div[contains(@class, "_notification_success-bg")]')
    spinner_locator = (By.XPATH, '//div[contains(@class, "spinner")]')
    button_text = (By.XPATH, '//div[contains(@class,"button__text")]')
    fio_locator = (By.XPATH, '//div[@data-name="fio"]//input[@type="text"]')
    phone_locator = (By.XPATH, '//div[@data-name="phone"]//input[@type="text"]')
    href_profile = (By.XPATH, '//a[@href="/profile"]')
    href_logout = (By.XPATH, '//a[@href="/logout"]')
    right_module_rightButton = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
    authForm_module_button = (By.XPATH, '//div[contains(@class,"authForm-module-button")]')
    responseHead_module_button = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    email_locator = (By.NAME, 'email')
    password_locator = (By.NAME, 'password')