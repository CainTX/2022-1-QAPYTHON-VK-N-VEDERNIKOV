from locators_test import BasicLocators
from selectors_test import BasicSelectors

from fixtures import *


class Base(BasicSelectors, BasicLocators):

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

    def negative_auth1(self, driver):
        self.logger.info("Авторизация без ввода пароля")
        self.wdWaitVisibility(self.auth_responseHead_button)
        self.search_click(self.auth_responseHead_button)
        self.clear_send(self.auth_email_locator, credentials.email)
        self.clear_input(self.auth_password_locator)
        self.mouse_to_element(self.auth_Form_module_button)

        self.logger.info("Проверка на доступность кнопки авторизации")
        self.find(self.company_module_disabled)

    def negative_auth2(self, driver):
        self.logger.info("Авторизация c неверным паролем")
        self.wdWaitVisibility(self.auth_responseHead_button)
        self.search_click(self.auth_responseHead_button)
        self.clear_send(self.auth_email_locator, credentials.email)
        self.clear_send(self.auth_password_locator, "123")
        self.search_click(self.auth_Form_module_button)

        self.logger.info("Проверка на отображение страницы с ошибкой")
        self.wdWaitVisibility(self.company_invalid_pass_check)
        if "login/?error_code" in driver.current_url:
            assert True

    def create_company(self, driver):
        self.logger.info("Создание кампании")
        self.wdWaitVisibility(self.company_center_buttonsWrap)
        self.wdWaitInvisibility(self.company_spinner_zindex)
        self.search_click(self.href_dashboard)
        self.wd_search_click(self.company_create)

        self.logger.info("Заполнение шаблона и реквизитов")
        self.wd_search_click(self.company_traffic)
        self.search_send(self.company_ad_url, credentials.company_url)
        self.wd_search_click(self.company_age)

        # Добавил для теста работы со слайдером, работает, но в нем нет необходимости
        # elem = self.find(self.company_slider)
        # webdriver.ActionChains(driver).drag_and_drop_by_offset(elem, 190, 0).perform()

        self.search_send(self.company_budget_daily, "30000")
        self.search_send(self.company_budget_total, "3000000")
        self.search_click(self.company_banner)
        self.logger.info("Поиск и подргрузка изображения")
        self.wdWaitClickable(self.company_dropArea)
        self.search_send(self.company_image_240, self.os_image_path)
        self.clear_send(self.company_name, c_name)
        self.wdWaitVisibility(self.company_hidden_wrap)
        self.wd_search_click(self.company_create)

        self.logger.info("Проверка на отображение созданной кампании")
        self.wdWaitVisibility(self.company_search)
        self.search_send(self.company_search, c_name)
        self.wdWaitVisibility(self.company_option_module)
        self.find(self.company_li_name)

    def create_segment(self, driver, with_delete=True):
        self.logger.info("Создание сегмента")
        self.wdWaitInvisibility(self.company_spinner_zindex)
        self.wdWaitVisibility(self.href_profile)
        self.wd_search_click(self.href_segment)
        self.wdWaitClickable(self.segment_create)
        self.search_click(self.segment_adv_camp_list)
        self.wd_search_click(self.segment_add_list)

        self.logger.info("Указываем название сегмента и шаблон из кампаний")
        if with_delete is False:
            self.logger.info("Сегмент создается без проверки удаления")
            self.clear_send(self.segment_placeholder_all_c, ss_name)
        else:
            self.logger.info("Сегмент создается для удаления")
            self.clear_send(self.segment_placeholder_all_c, s_name)
        self.search_send(self.segment_placeholder_campaign, credentials.c_name_static)
        self.wd_search_click(self.segment_span_name_static)
        self.search_click(self.segment_add)
        self.wd_search_click(self.segment_s_list)
        self.wd_search_click(self.segment_create)
        self.wd_search_click(self.segment_ad_camp)
        if with_delete is False:
            self.wd_search_click(self.segment_checkbox_s)
        else:
            self.wd_search_click(self.segment_checkbox)
        self.wd_search_click(self.segment_add_s)
        if with_delete is False:
            self.clear_send(self.segment_create_form, ss_name_a)
        else:
            self.clear_send(self.segment_create_form, s_name_a)
        self.wd_search_click(self.segment_create)

        self.logger.info("Проверка на отображение сегмента")
        self.wdWaitVisibility(self.segment_search_id)
        if with_delete is False:
            self.search_send(self.segment_search_id, ss_name_a)
            self.wd_search_click(self.segment_li_title_s)
        else:
            self.search_send(self.segment_search_id, s_name_a)
            self.wd_search_click(self.segment_li_title)

    def delete_segment(self, driver):
        self.logger.info("Удаление сегмента")
        self.wdWaitVisibility(self.segment_search_id)
        self.search_send(self.segment_search_id, s_name_a)
        self.wd_search_click(self.segment_li_title)
        self.wd_search_click(self.segment_span_remove)
        self.wd_search_click(self.segment_detete_a)

        self.logger.info("Проверка удаленного сегмента")
        self.wdWaitVisibility(self.segment_search_id)
        self.search_send(self.segment_search_id, s_name_a)
        self.wdWaitVisibility(self.segment_nothing)
        self.find(self.segment_nothing)