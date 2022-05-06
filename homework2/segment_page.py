import locators
from base_page import BasePage
import credentials


class SegmentPage(BasePage):
    segment_locators = locators.LocatorsSegment()

    def create_segment(self, with_delete=True):
        self.logger.info("Создание сегмента")
        self.wd_wait_invisibility(self.segment_locators.segment_spinner_zindex)
        self.wd_wait_visibility(self.segment_locators.segment_profile)
        self.search_click(self.segment_locators.segment_href)
        self.wd_wait_clickable(self.segment_locators.segment_create)
        self.search_click(self.segment_locators.segment_adv_camp_list)
        self.search_click(self.segment_locators.segment_add_list)

        self.logger.info("Указываем название сегмента и шаблон из кампаний")
        if with_delete is False:
            self.logger.info("Сегмент создается без проверки удаления")
            self.clear_send(self.segment_locators.segment_placeholder_all_c, self.segment_locators.segment_name('segment_name_random'))
            self.clear_send(self.segment_locators.segment_placeholder_campaign, credentials.c_name_static)
            self.search_click(self.segment_locators.segment_span_name_static)
            self.search_click(self.segment_locators.segment_add)
            self.search_click(self.segment_locators.segment_s_list)
            self.search_click(self.segment_locators.segment_create)
            self.search_click(self.segment_locators.segment_ad_camp)
            self.search_click(self.segment_locators.segment_checkbox_s)
            self.search_click(self.segment_locators.segment_add_s)
            self.clear_send(self.segment_locators.segment_create_form, self.segment_locators.segment_name('segment_name_audit'))
            self.search_click(self.segment_locators.segment_create)

            self.logger.info("Проверка на отображение сегмента")
            self.wd_wait_visibility(self.segment_locators.segment_search_id)
            self.clear_send(self.segment_locators.segment_search_id, self.segment_locators.segment_name('segment_name_audit'))
            self.search_click(self.segment_locators.segment_li_title_s)
        else:
            self.logger.info("Сегмент создается для удаления")
            self.clear_send(self.segment_locators.segment_placeholder_all_c, self.segment_locators.segment_name('segment_delete_name'))
            self.clear_send(self.segment_locators.segment_placeholder_campaign, credentials.c_name_static)
            self.search_click(self.segment_locators.segment_span_name_static)
            self.search_click(self.segment_locators.segment_add)
            self.search_click(self.segment_locators.segment_s_list)
            self.search_click(self.segment_locators.segment_create)
            self.search_click(self.segment_locators.segment_ad_camp)
            self.search_click(self.segment_locators.segment_checkbox)
            self.search_click(self.segment_locators.segment_add_s)
            self.clear_send(self.segment_locators.segment_create_form, self.segment_locators.segment_name('segment_delete_audit'))
            self.search_click(self.segment_locators.segment_create)

            self.logger.info("Проверка на отображение сегмента")
            self.wd_wait_visibility(self.segment_locators.segment_search_id)
            self.clear_send(self.segment_locators.segment_search_id, self.segment_locators.segment_name('segment_delete_audit'))
            self.search_click(self.segment_locators.segment_li_title)

    def delete_segment(self):
        self.logger.info("Удаление сегмента")
        self.wd_wait_visibility(self.segment_locators.segment_search_id)
        self.clear_send(self.segment_locators.segment_search_id, self.segment_locators.segment_name('segment_delete_audit'))
        self.search_click(self.segment_locators.segment_li_title)
        self.search_click(self.segment_locators.segment_span_remove)
        self.search_click(self.segment_locators.segment_delete_a)

        self.logger.info("Проверка удаленного сегмента")
        self.wd_wait_visibility(self.segment_locators.segment_search_id)
        self.clear_send(self.segment_locators.segment_search_id, self.segment_locators.segment_name('segment_delete_audit'))
        self.wd_wait_visibility(self.segment_locators.segment_nothing)
        self.find(self.segment_locators.segment_nothing)
