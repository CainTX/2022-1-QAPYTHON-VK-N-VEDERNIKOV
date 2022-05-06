from base_page import BasePage, locators
import credentials


class CampaignPage(BasePage):
    campaign_locators = locators.LocatorsCampaign()

    def create_campaign(self):
        self.logger.info("Создание кампании")
        self.wd_wait_visibility(self.campaign_locators.campaign_center_buttonsWrap)
        self.wd_wait_invisibility(self.campaign_locators.company_spinner_zindex)
        self.search_click(self.campaign_locators.campaign_dashboard)
        self.search_click(self.campaign_locators.campaign_create)

        self.logger.info("Заполнение шаблона и реквизитов")
        self.search_click(self.campaign_locators.campaign_traffic)
        self.clear_send(self.campaign_locators.campaign_ad_url, credentials.campaign_url)
        self.search_click(self.campaign_locators.campaign_age)

        self.clear_send(self.campaign_locators.campaign_budget_daily, "30000")
        self.clear_send(self.campaign_locators.campaign_budget_total, "3000000")
        self.search_click(self.campaign_locators.campaign_banner)
        self.logger.info("Поиск и подргрузка изображения")
        self.wd_wait_clickable(self.campaign_locators.campaign_dropArea)
        self.clear_send(self.campaign_locators.campaign_image_240, self.campaign_locators.os_image_path, clear=False)
        self.clear_send(self.campaign_locators.campaign_name_t, self.campaign_locators.campaign_name())
        self.wd_wait_visibility(self.campaign_locators.campaign_hidden_wrap)
        self.search_click(self.campaign_locators.campaign_create)

        self.logger.info("Проверка на отображение созданной кампании")
        self.wd_wait_visibility(self.campaign_locators.campaign_search)
        self.clear_send(self.campaign_locators.campaign_search, self.campaign_locators.campaign_name())
        self.wd_wait_visibility(self.campaign_locators.campaign_option_module)
        self.find(self.campaign_locators.campaign_li_name)
