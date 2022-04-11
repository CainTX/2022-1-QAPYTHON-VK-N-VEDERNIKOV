from locators_test import *
from selectors_test import *
from fixtures import *
from utility import *


class AuthCase(BaseCase):

    def login(self, driver, w_cookie=True):
        if w_cookie is True and os.path.exists(os.getcwd() + f"\\{credentials.email}_cookies"):
            self.logger.info("Авторизация через куки")
            self.wdWaitVisibility(self.locators.auth_responseHead_button)
            for cookie in pickle.load(open(f"{credentials.email}_cookies", "rb")):
                driver.add_cookie(cookie)
            driver.refresh()
            self.logger.info("Успешная авторизация через куки")

        else:
            self.logger.info("Авторизация вручную")
            self.wdWaitVisibility(self.locators.auth_responseHead_button)
            self.search_click(self.locators.auth_responseHead_button)
            self.clear_send(self.locators.auth_email_locator, credentials.email)
            self.clear_send(self.locators.auth_password_locator, credentials.email_password)
            self.search_click(self.locators.auth_Form_module_button)
            pickle.dump(driver.get_cookies(), open(f"{credentials.email}_cookies", "wb"))
            self.logger.info("Успешная авторизация вручную")

    def negative_auth1(self):
        self.logger.info("Авторизация без ввода пароля")
        self.wdWaitVisibility(self.locators.auth_responseHead_button)
        self.search_click(self.locators.auth_responseHead_button)
        self.clear_send(self.locators.auth_email_locator, credentials.email)
        self.clear_input(self.locators.auth_password_locator)
        self.mouse_to_element(self.locators.auth_Form_module_button)

        self.logger.info("Проверка на доступность кнопки авторизации")
        self.find(self.locators.module_disabled_m)

    def negative_auth2(self, driver):
        self.logger.info("Авторизация c неверным паролем")
        self.wdWaitVisibility(self.locators.auth_responseHead_button)
        self.search_click(self.locators.auth_responseHead_button)
        self.clear_send(self.locators.auth_email_locator, credentials.email)
        self.clear_send(self.locators.auth_password_locator, "123")
        self.search_click(self.locators.auth_Form_module_button)

        self.logger.info("Проверка на отображение страницы с ошибкой")
        self.wdWaitVisibility(self.locators.invalid_pass_check)
        if "login/?error_code" in driver.current_url:
            assert True


class CampaignCase(BaseCase):

    def create_campaign(self):
        self.logger.info("Создание кампании")
        self.wdWaitVisibility(self.campaign_locators.campaign_center_buttonsWrap)
        self.wdWaitInvisibility(self.campaign_locators.company_spinner_zindex)
        self.search_click(self.campaign_locators.campaign_dashboard)
        self.wd_search_click(self.campaign_locators.campaign_create)

        self.logger.info("Заполнение шаблона и реквизитов")
        self.wd_search_click(self.campaign_locators.campaign_traffic)
        self.search_send(self.campaign_locators.campaign_ad_url, credentials.campaign_url)
        self.wd_search_click(self.campaign_locators.campaign_age)

        self.search_send(self.campaign_locators.campaign_budget_daily, "30000")
        self.search_send(self.campaign_locators.campaign_budget_total, "3000000")
        self.search_click(self.campaign_locators.campaign_banner)
        self.logger.info("Поиск и подргрузка изображения")
        self.wdWaitClickable(self.campaign_locators.campaign_dropArea)
        self.search_send(self.campaign_locators.campaign_image_240, self.campaign_locators.os_image_path)
        self.clear_send(self.campaign_locators.campaign_name_t, self.campaign_locators.campaign_name())
        self.wdWaitVisibility(self.campaign_locators.campaign_hidden_wrap)
        self.wd_search_click(self.campaign_locators.campaign_create)

        self.logger.info("Проверка на отображение созданной кампании")
        self.wdWaitVisibility(self.campaign_locators.campaign_search)
        self.search_send(self.campaign_locators.campaign_search, self.campaign_locators.campaign_name())
        self.wdWaitVisibility(self.campaign_locators.campaign_option_module)
        self.find(self.campaign_locators.campaign_li_name)


class SegmentCase(BaseCase):

    def create_segment(self, with_delete=True):
        self.logger.info("Создание сегмента")
        self.wdWaitInvisibility(self.segment_locators.segment_spinner_zindex)
        self.wdWaitVisibility(self.segment_locators.segment_profile)
        self.wd_search_click(self.segment_locators.segment_href)
        self.wdWaitClickable(self.segment_locators.segment_create)
        self.search_click(self.segment_locators.segment_adv_camp_list)
        self.wd_search_click(self.segment_locators.segment_add_list)

        self.logger.info("Указываем название сегмента и шаблон из кампаний")
        if with_delete is False:
            self.logger.info("Сегмент создается без проверки удаления")
            self.clear_send(self.segment_locators.segment_placeholder_all_c, self.segment_locators.segment_name('segment_name_random'))
            self.search_send(self.segment_locators.segment_placeholder_campaign, credentials.c_name_static)
            self.wd_search_click(self.segment_locators.segment_span_name_static)
            self.search_click(self.segment_locators.segment_add)
            self.wd_search_click(self.segment_locators.segment_s_list)
            self.wd_search_click(self.segment_locators.segment_create)
            self.wd_search_click(self.segment_locators.segment_ad_camp)
            self.wd_search_click(self.segment_locators.segment_checkbox_s)
            self.wd_search_click(self.segment_locators.segment_add_s)
            self.clear_send(self.segment_locators.segment_create_form, self.segment_locators.segment_name('segment_name_audit'))
            self.wd_search_click(self.segment_locators.segment_create)

            self.logger.info("Проверка на отображение сегмента")
            self.wdWaitVisibility(self.segment_locators.segment_search_id)
            self.search_send(self.segment_locators.segment_search_id, self.segment_locators.segment_name('segment_name_audit'))
            self.wd_search_click(self.segment_locators.segment_li_title_s)
        else:
            self.logger.info("Сегмент создается для удаления")
            self.clear_send(self.segment_locators.segment_placeholder_all_c, self.segment_locators.segment_name('segment_delete_name'))
            self.search_send(self.segment_locators.segment_placeholder_campaign, credentials.c_name_static)
            self.wd_search_click(self.segment_locators.segment_span_name_static)
            self.search_click(self.segment_locators.segment_add)
            self.wd_search_click(self.segment_locators.segment_s_list)
            self.wd_search_click(self.segment_locators.segment_create)
            self.wd_search_click(self.segment_locators.segment_ad_camp)
            self.wd_search_click(self.segment_locators.segment_checkbox)
            self.wd_search_click(self.segment_locators.segment_add_s)
            self.clear_send(self.segment_locators.segment_create_form, self.segment_locators.segment_name('segment_delete_audit'))
            self.wd_search_click(self.segment_locators.segment_create)

            self.logger.info("Проверка на отображение сегмента")
            self.wdWaitVisibility(self.segment_locators.segment_search_id)
            self.search_send(self.segment_locators.segment_search_id, self.segment_locators.segment_name('segment_delete_audit'))
            self.wd_search_click(self.segment_locators.segment_li_title)

    def delete_segment(self):
        self.logger.info("Удаление сегмента")
        self.wdWaitVisibility(self.segment_locators.segment_search_id)
        self.search_send(self.segment_locators.segment_search_id, self.segment_locators.segment_name('segment_delete_audit'))
        self.wd_search_click(self.segment_locators.segment_li_title)
        self.wd_search_click(self.segment_locators.segment_span_remove)
        self.wd_search_click(self.segment_locators.segment_delete_a)

        self.logger.info("Проверка удаленного сегмента")
        self.wdWaitVisibility(self.segment_locators.segment_search_id)
        self.search_send(self.segment_locators.segment_search_id, self.segment_locators.segment_name('segment_delete_audit'))
        self.wdWaitVisibility(self.segment_locators.segment_nothing)
        self.find(self.segment_locators.segment_nothing)
