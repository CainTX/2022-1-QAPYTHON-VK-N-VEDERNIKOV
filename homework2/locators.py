from utility import *
from selenium.webdriver.common.by import By
import os


class BasicLocators:

    auth_rightButton = (By.XPATH, '//div[contains(@class, "right-module-rightButton")]')
    auth_Form_module_button = (By.XPATH, '//div[contains(@class,"authForm-module-button")]')
    auth_responseHead_button = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    auth_email_locator = (By.NAME, 'email')
    auth_password_locator = (By.NAME, 'password')

    module_disabled_m = (By.XPATH, '//div[contains(@class,"authForm-module-disabled")]')
    invalid_pass_check = (By.XPATH, "//div[text() = 'Invalid login or password']")


class LocatorsSegment(RandomNameSegment):

    segment_nothing = (By.XPATH, "//li[@title = 'Ничего не найдено...']")
    segment_delete_a = (By.XPATH, "//div[text() = 'Удалить']")
    segment_span_name_static = (By.XPATH, f"//span[text() = 'Test_baza']")
    segment_span_remove = (By.XPATH, f"//a[text() = '{RandomNameSegment.segment_name('segment_delete_audit')}']"
                                     f"//following::div[contains(@data-test, 'remove')]//span")
    segment_li_title_s = (By.XPATH, f"//li[@title = '{RandomNameSegment.segment_name('segment_name_audit')}']")
    segment_li_title = (By.XPATH, f"//li[@title = '{RandomNameSegment.segment_name('segment_delete_audit')}']")
    segment_search_id = (By.XPATH, "//input[@placeholder = 'Поиск по названию или id...']")
    segment_create_form = (By.XPATH, "//div[contains(@class, 'input_create-segment-form')]//input[@type = 'text']")
    segment_add_s = (By.XPATH, "//div[text() = 'Добавить сегмент']")
    segment_checkbox_s = (By.XPATH, f"//span[text() = '{RandomNameSegment.segment_name('segment_name_random')}']"
                                    f"//preceding::input[@type = 'checkbox']")
    segment_checkbox = (By.XPATH, f"//span[text() = '{RandomNameSegment.segment_name('segment_delete_name')}']"
                                  f"//preceding::input[@type = 'checkbox']")
    segment_ad_camp = (By.XPATH, "//div[text() = 'Рекламные кампании']")
    segment_s_list = (By.XPATH, "//span[text() = 'Список сегментов']")
    segment_add = (By.XPATH, "//div[text() = 'Добавить']")
    segment_placeholder_campaign = (By.XPATH, "//input[@placeholder = 'Поиск кампаний...']")
    segment_placeholder_all_c = (By.XPATH, "//input[@placeholder = 'Введите название списка кампаний...']")
    segment_add_list = (By.XPATH, "//div[text() = 'Добавить список']")
    segment_adv_camp_list = (By.XPATH, "//a[@href = '/segments/advertising_campaigns_list']")
    segment_create = (By.XPATH, "//div[text() = 'Создать сегмент']")
    segment_spinner_zindex = (By.XPATH, "//div[contains(@class, 'company_spinner_zindex')]")
    segment_href = (By.XPATH, "//a[@href = '/segments']")
    segment_profile = (By.XPATH, '//a[@href="/profile"]')


class LocatorsCampaign(RandomNameCampaign):

    campaign_li_name = (By.XPATH, f"//li[@title = '{RandomNameCampaign.campaign_name()}']")
    campaign_hidden_wrap = (By.XPATH, "//div[contains(@class, 'js-buttons-hidden-wrap')]")
    campaign_option_module = (By.XPATH, "//div[contains(@class, 'optionListTitle-module-title')]")
    campaign_search = (By.XPATH, "//input[@placeholder= 'Поиск...']")
    campaign_name_t = (By.XPATH, "//div[@class='js-bottom-campaign-name-wrap']//input")
    campaign_image_240 = (By.XPATH, "//div//input[@data-test = 'image_240x400']")
    campaign_dropArea = (By.XPATH, "//div[contains(@class, 'upload-module-dropArea')]")
    campaign_banner = (By.XPATH, "//span[text() = 'Баннер']")
    campaign_budget_total = (By.XPATH, "//div[contains(@class, 'js-budget-setting-total')]//input")
    campaign_budget_daily = (By.XPATH, "//div[contains(@class, 'js-budget-setting-daily')]//input")
    campaign_slider = (By.XPATH, "//span[@class = 'slider-ts__handle__disc']")
    campaign_age = (By.XPATH, "//div[@data-targeting='age']")
    campaign_ad_url = (By.XPATH, "//input[@data-gtm-id = 'ad_url_text']")
    campaign_traffic = (By.XPATH, "//div[text() = 'Трафик']")
    campaign_create = (By.XPATH, "//div[text() = 'Создать кампанию']")
    campaign_dashboard = (By.XPATH, '//a[@href="/dashboard"]')
    campaign_center_buttonsWrap = (By.XPATH, '//ul[contains(@class, "center-module-buttonsWrap")]')
    company_spinner_zindex = (By.XPATH, "//div[contains(@class, 'company_spinner_zindex')]")
    os_image_path = (os.getcwd() + "\\x_test.png")
