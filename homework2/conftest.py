from locators_test import *
from selectors_test import *
from fixtures import *
from utility import *


class BaseAuth(BasicSelectors, BasicLocators):

    def login(self, driver, w_cookie=True):
        if w_cookie is True and os.path.exists(os.getcwd() + f"\\{credentials.email}_cookies"):
            self.logger.info("Авторизация через куки")
            self.wdWaitVisibility(self.auth_responseHead_button)
            for cookie in pickle.load(open(f"{credentials.email}_cookies", "rb")):
                driver.add_cookie(cookie)
            driver.refresh()
            self.logger.info("Успешная авторизация через куки")

        else:
            self.logger.info("Авторизация вручную")
            self.wdWaitVisibility(self.auth_responseHead_button)
            self.search_click(self.auth_responseHead_button)
            self.clear_send(self.auth_email_locator, credentials.email)
            self.clear_send(self.auth_password_locator, credentials.email_password)
            self.search_click(self.auth_Form_module_button)
            pickle.dump(driver.get_cookies(), open(f"{credentials.email}_cookies", "wb"))
            self.logger.info("Успешная авторизация вручную")

    def negative_auth1(self):
        self.logger.info("Авторизация без ввода пароля")
        self.wdWaitVisibility(self.auth_responseHead_button)
        self.search_click(self.auth_responseHead_button)
        self.clear_send(self.auth_email_locator, credentials.email)
        self.clear_input(self.auth_password_locator)
        self.mouse_to_element(self.auth_Form_module_button)

        self.logger.info("Проверка на доступность кнопки авторизации")
        self.find(self.module_disabled_m)

    def negative_auth2(self, driver):
        self.logger.info("Авторизация c неверным паролем")
        self.wdWaitVisibility(self.auth_responseHead_button)
        self.search_click(self.auth_responseHead_button)
        self.clear_send(self.auth_email_locator, credentials.email)
        self.clear_send(self.auth_password_locator, "123")
        self.search_click(self.auth_Form_module_button)

        self.logger.info("Проверка на отображение страницы с ошибкой")
        self.wdWaitVisibility(self.invalid_pass_check)
        if "login/?error_code" in driver.current_url:
            assert True


class BaseCampaign(BasicSelectors, LocatorsCampaign):

    def create_company(self):
        self.logger.info("Создание кампании")
        self.wdWaitVisibility(self.campaign_center_buttonsWrap)
        self.wdWaitInvisibility(self.company_spinner_zindex)
        self.search_click(self.campaign_dashboard)
        self.wd_search_click(self.campaign_create)

        self.logger.info("Заполнение шаблона и реквизитов")
        self.wd_search_click(self.campaign_traffic)
        self.search_send(self.campaign_ad_url, credentials.company_url)
        self.wd_search_click(self.campaign_age)

        self.search_send(self.campaign_budget_daily, "30000")
        self.search_send(self.campaign_budget_total, "3000000")
        self.search_click(self.campaign_banner)
        self.logger.info("Поиск и подргрузка изображения")
        self.wdWaitClickable(self.campaign_dropArea)
        self.search_send(self.campaign_image_240, self.os_image_path)
        self.clear_send(self.campaign_name_t, self.campaign_name())
        self.wdWaitVisibility(self.campaign_hidden_wrap)
        self.wd_search_click(self.campaign_create)

        self.logger.info("Проверка на отображение созданной кампании")
        self.wdWaitVisibility(self.campaign_search)
        self.search_send(self.campaign_search, self.campaign_name())
        self.wdWaitVisibility(self.campaign_option_module)
        self.find(self.campaign_li_name)


class BaseSegment(BasicSelectors, LocatorsSegment):

    def create_segment(self, with_delete=True):
        self.logger.info("Создание сегмента")
        self.wdWaitInvisibility(self.segment_spinner_zindex)
        self.wdWaitVisibility(self.segment_profile)
        self.wd_search_click(self.segment_href)
        self.wdWaitClickable(self.segment_create)
        self.search_click(self.segment_adv_camp_list)
        self.wd_search_click(self.segment_add_list)

        self.logger.info("Указываем название сегмента и шаблон из кампаний")
        if with_delete is False:
            self.logger.info("Сегмент создается без проверки удаления")
            self.clear_send(self.segment_placeholder_all_c, self.segment_name('segment_name_random'))
            self.search_send(self.segment_placeholder_campaign, credentials.c_name_static)
            self.wd_search_click(self.segment_span_name_static)
            self.search_click(self.segment_add)
            self.wd_search_click(self.segment_s_list)
            self.wd_search_click(self.segment_create)
            self.wd_search_click(self.segment_ad_camp)
            self.wd_search_click(self.segment_checkbox_s)
            self.wd_search_click(self.segment_add_s)
            self.clear_send(self.segment_create_form, self.segment_name('segment_name_audit'))
            self.wd_search_click(self.segment_create)

            self.logger.info("Проверка на отображение сегмента")
            self.wdWaitVisibility(self.segment_search_id)
            self.search_send(self.segment_search_id, self.segment_name('segment_name_audit'))
            self.wd_search_click(self.segment_li_title_s)
        else:
            self.logger.info("Сегмент создается для удаления")
            self.clear_send(self.segment_placeholder_all_c, self.segment_name('segment_delete_name'))
            self.search_send(self.segment_placeholder_campaign, credentials.c_name_static)
            self.wd_search_click(self.segment_span_name_static)
            self.search_click(self.segment_add)
            self.wd_search_click(self.segment_s_list)
            self.wd_search_click(self.segment_create)
            self.wd_search_click(self.segment_ad_camp)
            self.wd_search_click(self.segment_checkbox)
            self.wd_search_click(self.segment_add_s)
            self.clear_send(self.segment_create_form, self.segment_name('segment_delete_audit'))
            self.wd_search_click(self.segment_create)

            self.logger.info("Проверка на отображение сегмента")
            self.wdWaitVisibility(self.segment_search_id)
            self.search_send(self.segment_search_id, self.segment_name('segment_delete_audit'))
            self.wd_search_click(self.segment_li_title)

    def delete_segment(self):
        self.logger.info("Удаление сегмента")
        self.wdWaitVisibility(self.segment_search_id)
        self.search_send(self.segment_search_id, self.segment_name('segment_delete_audit'))
        self.wd_search_click(self.segment_li_title)
        self.wd_search_click(self.segment_span_remove)
        self.wd_search_click(self.segment_delete_a)

        self.logger.info("Проверка удаленного сегмента")
        self.wdWaitVisibility(self.segment_search_id)
        self.search_send(self.segment_search_id, self.segment_name('segment_delete_audit'))
        self.wdWaitVisibility(self.segment_nothing)
        self.find(self.segment_nothing)
