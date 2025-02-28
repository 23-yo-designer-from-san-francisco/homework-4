import selenium
from Base.BaseComponent import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT, has_element


class PlaylistImage(Component):
    IMAGE = '//div[@class="playlist__description-avatar"]'
    PLAYLIST_DESCR = "playlist__description-avatar"

    def open_edit_window(self):
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.PLAYLIST_DESCR))
        )
        self.driver.find_element(by=By.XPATH, value=self.IMAGE).click()


class PlaylistTextBlock(Component):
    TITLE = '//div[@class="playlist__description-title"]'
    EDIT_WINDOW_BTN = '//div[@class="playlist__description-text playlist__description-edit-btn"]'

    def open_edit_window(self):
        btn = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.EDIT_WINDOW_BTN)
        )
        btn.click()

    def title(self):
        title = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.TITLE).text
        )
        return title


class PlaylistEditWindow(Component):
    EDIT_WINDOW = '//div[@class="editwindow"]'
    CLOSE_BTN = '//img[@class="editwindow__close"]'
    TITLE_INPUT = '//input[@class="editwindow__form-input"]'
    SAVE_BUTTON = '//input[@class="editwindow__form-submit"]'
    DELETE_BUTTON = '//img[@class="editwindow__delete"]'
    DELETE_CONFIRM_BUTTON = '//img[@class="editwindow__delete confirm"]'
    WARNING_CLS = "editwindow__form-msg"
    LINK = '//div[@class="editwindow__link"]'
    PUBLICITY_SWITCH = '//span[@class="slider"]'
    IS_OPEN = "display: block;"
    EDIT_SUBMIT = "editwindow__form-submit"

    def close_by_close_btn(self):
        button = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.CLOSE_BTN)
        )
        button.click()

    def close_by_ext_area(self):
        area = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.EDIT_WINDOW)
        )
        area.click()

    def clear_title(self):
        input = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.TITLE_INPUT)
        )
        input.clear()

    def set_title(self, title):
        input = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.TITLE_INPUT)
        )
        input.clear()
        input.send_keys(title)

    def save(self):
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.element_to_be_clickable((By.CLASS_NAME, self.EDIT_SUBMIT))
        )
        self.driver.find_element(by=By.XPATH, value=self.SAVE_BUTTON).click()

    def click_on_delete(self):
        button = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.DELETE_BUTTON)
        )
        button.click()

    def click_on_delete_confirm(self):
        button = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.DELETE_CONFIRM_BUTTON)
        )
        button.click()

    def toggle_publicity(self):
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.element_to_be_clickable((By.XPATH, self.PUBLICITY_SWITCH))
        )
        self.driver.find_element(by=By.XPATH, value=self.PUBLICITY_SWITCH).click()


class PlaylistPageControls(Component):
    EDIT_BUTTON = '//div[contains(text(), "Edit playlist")]'
