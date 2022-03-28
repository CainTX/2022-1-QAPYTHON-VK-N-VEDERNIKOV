from fixtures import *


class BasicLocators:

    #segment
    segment_nothing = (By.XPATH, "//li[@title = 'Ничего не найдено...']")
    segment_detete_a = (By.XPATH, "//div[text() = 'Удалить']")
    segment_span_name_static = (By.XPATH, f"//span[text() = 'Test_baza']")
    segment_span_remove = (By.XPATH, f"//a[text() = '{s_name_a}']//following::div[contains(@data-test, 'remove')]//span")
    segment_li_title_s = (By.XPATH, f"//li[@title = '{ss_name_a}']")
    segment_li_title = (By.XPATH, f"//li[@title = '{s_name_a}']")
    segment_search_id = (By.XPATH, "//input[@placeholder = 'Поиск по названию или id...']")
    segment_create_form = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]//input[@type = 'text']")
    segment_add_s = (By.XPATH, "//div[text() = 'Добавить сегмент']")
    segment_checkbox_s = (By.XPATH, f"//span[text() = '{ss_name}']//preceding::input[@type = 'checkbox']")
    segment_checkbox = (By.XPATH, f"//span[text() = '{s_name}']//preceding::input[@type = 'checkbox']")
    segment_ad_camp = (By.XPATH, "//div[text() = 'Рекламные кампании']")
    segment_s_list = (By.XPATH, "//span[text() = 'Список сегментов']")
    segment_add = (By.XPATH, "//div[text() = 'Добавить']")
    # segment_span_name = (By.XPATH, f"//span[text() = '{c_name}']")
    segment_placeholder_campaign = (By.XPATH, "//input[@placeholder = 'Поиск кампаний...']")
    segment_placeholder_all_c = (By.XPATH, "//input[@placeholder = 'Введите название списка кампаний...']")
    segment_add_list = (By.XPATH, "//div[text() = 'Добавить список']")
    segment_adv_camp_list = (By.XPATH, "//a[@href = '/segments/advertising_campaigns_list']")
    segment_create = (By.XPATH, "//div[text() = 'Создать сегмент']")

    #company
    os_image_path = (os.getcwd() + "\\x_test.png")
    company_li_name = (By.XPATH, f"//li[@title = '{c_name}']")
    company_hidden_wrap = (By.XPATH, "//div[contains(@class, 'js-buttons-hidden-wrap')]")
    company_option_module = (By.XPATH, "//div[contains(@class, 'optionListTitle-module-title')]")
    company_search = (By.XPATH, "//input[@placeholder= 'Поиск...']")
    company_name = (By.XPATH, "//div[@class='js-bottom-campaign-name-wrap']//input")
    company_image_240 = (By.XPATH, "//div//input[@data-test = 'image_240x400']")
    company_dropArea = (By.XPATH, "//div[contains(@class, 'upload-module-dropArea')]")
    company_banner = (By.XPATH, "//span[text() = 'Баннер']")
    company_budget_total = (By.XPATH, "//div[@class = 'budget-setting__input-wrap js-budget-setting-total']//input")
    company_budget_daily = (By.XPATH, "//div[@class = 'budget-setting__input-wrap js-budget-setting-daily']//input")
    company_slider = (By.XPATH, "//span[@class = 'slider-ts__handle__disc']")
    company_age = (By.XPATH, "//div[@data-targeting='age']")
    company_ad_url = (By.XPATH, "//input[@data-gtm-id = 'ad_url_text']")
    company_traffic = (By.XPATH, "//div[text() = 'Трафик']")
    company_create = (By.XPATH, "//div[text() = 'Создать кампанию']")
    company_module_disabled = (By.XPATH, '//div[contains(@class,"authForm-module-disabled")]')
    company_invalid_pass_check = (By.XPATH, "//div[text() = 'Invalid login or password']")
    company_spinner_zindex = (By.XPATH, "//div[contains(@class, 'company_spinner_zindex')]")
    company_center_buttonsWrap = (By.XPATH, '//ul[contains(@class, "center-module-buttonsWrap")]')

    #hrefs
    href_segment = (By.XPATH, "//a[@href = '/segments']")
    href_dashboard = (By.XPATH, '//a[@href="/dashboard"]')
    href_profile = (By.XPATH, '//a[@href="/profile"]')

    #auth
    auth_rightButton = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
    auth_Form_module_button = (By.XPATH, '//div[contains(@class,"authForm-module-button")]')
    auth_responseHead_button = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    auth_email_locator = (By.NAME, 'email')
    auth_password_locator = (By.NAME, 'password')