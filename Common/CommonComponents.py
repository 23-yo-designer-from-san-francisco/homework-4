import selenium.common.exceptions
from Base.BaseComponent import Component
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from tests.utils import CHECK_FREQ, TIMEOUT, element_attribute_not_to_include


class Player(Component):
    TRACK_LIKE = '//img[@class="player-fav"]'
    CURRENT_TIME = '//div[@class="player__time"]'
    PREV_TRACK = '//img[@id="player-left"]'
    PREV_TRACK_CLASS = '//img[@class="player-skip-left"]'
    PLAY = '//img[@id="player-play"]'
    NEXT_TRACK = '//img[@id="player-right"]'
    NEXT_TRACK_CLASS = '//img[@class="player-skip-right"]'
    PLAYER = '//div[@class="player"]'
    MUTE = 'img[class^="mute"]'
    MUTE_XPATH = '//img[@class="mute"]'
    PLAYER_PAUSED = "pause"
    IN_FAVORITES = "data-in_favorites"

    def mute(self):
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.MUTE)))
        self.driver.find_element_by_css_selector(self.MUTE).click()

    def get_playing_track_id(self):
        id = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.TRACK_LIKE).get_attribute("data-id")
        )
        return id

    def get_like_btn(self):
        return self.driver.find_element(by=By.XPATH, value=self.TRACK_LIKE)

    def remove_like(self):
        self.get_like_btn().click()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            element_attribute_not_to_include((By.XPATH, self.TRACK_LIKE), self.IN_FAVORITES)
        )

    def add_like(self):
        self.get_like_btn().click()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.element_attribute_to_include((By.XPATH, self.TRACK_LIKE), self.IN_FAVORITES)
        )

    def prev_track(self):
        prev = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.PREV_TRACK)
        )
        prev.click()

    def next_track(self):
        next = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.NEXT_TRACK)
        )
        next.click()

    def toggle_play(self):
        pause = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.PLAY)
        )
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(EC.element_to_be_clickable((By.XPATH, self.PLAY)))
        pause.click()


class Albums(Component):
    FIRST_ALBUM = '//div[@class="top-album"]'
    TITLE = '//div[@class="top-album__title"]'
    ARTIST = '//div[@class="top-album__artist"]'
    PLAY_ICON = "i[class^=top-album__play]"
    ALBUM_LABEL = '//div[@class="album__description-label"]'
    PLAYER_STARTED_PLAYING = "0:01"
    ALBUM_TEXT = "album"

    def open_first_album(self):
        self.driver.find_element(by=By.XPATH, value=self.FIRST_ALBUM).click()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.ALBUM_LABEL).text == self.ALBUM_TEXT
        )

    def get_first_album_title(self):
        return self.driver.find_element(by=By.XPATH, value=self.TITLE).text

    def get_first_album_id(self):
        id = self.driver.find_element_by_css_selector(self.PLAY_ICON).get_attribute("data-id")
        return id

    def play_first_album(self):
        play = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element_by_css_selector(self.PLAY_ICON)
        )
        play.click()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=Player.CURRENT_TIME).text == self.PLAYER_STARTED_PLAYING
        )


class Topbar(Component):
    SETTINGS = '//i[@class="topbar-icon fa-solid fa-gear"]'
    AVATAR = '//img[@class="avatar__img"]'
    LOGOUT = '//i[@class="topbar-icon js-logout fa-solid fa-right-from-bracket"]'
    SIGNIN_BUTTON = "signin-button"

    def log_out(self):
        logout = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.LOGOUT)
        )
        logout.click()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.element_attribute_to_include((By.ID, self.SIGNIN_BUTTON), "href")
        )


class TopArtists(Component):
    ARTIST_LABEL = '//div[@class="artist__description"]'
    FIRST_ARTIST = '//img[@class="suggested-artist__img"]'

    def open_first_artist(self):
        self.driver.find_element(by=By.XPATH, value=self.FIRST_ARTIST).click()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.ARTIST_LABEL)
        )

    def get_artist_title(self):
        return self.driver.find_element(by=By.XPATH, value=self.ARTIST_LABEL).text

    def get_first_artist_id(self):
        return self.driver.find_element(by=By.XPATH, value=self.FIRST_ARTIST).get_attribute("data-id")


class Sidebar(Component):
    LOGO = '//a[@class="sidebar__icon__logo"]'
    HOME = '//a[@class="sidebar__icon" and @href="/"]'
    FAVORITES = '//a[@class="sidebar__icon" and @href="/favorites"]'
    FAVORITES_DESCRIPTION = "favorites__description-title"

    def go_home_by_logo(self):
        self.driver.find_element(by=By.XPATH, value=self.LOGO).click()


class Tracks(Component):
    PLAY = '//img[@class="track-play"]'
    PLAYLIST = '//img[@class="track-list-item-playlist"]'
    PLAYLISTS_MENU = '//div[@class="menu"]'
    FIRST_TRACK_ARTIST = '//div[@class="track__container__artist"]'
    FIRST_TRACK_TITLE = '//div[@class="track__container__name"]'
    FIRST_TRACK_ALBUM = '//img[@class="track__artwork__img"]'
    TRACK_LIKE_BTN = '//img[@class="track-fav" and @data-id="{}"]'
    ALBUM_CLASS = "album"
    ARTIST_CLASS = "artist"
    IN_FAVORITES = "data-in_favorites"
    LOGIN_UI = "login-ui"

    def get_track_artist(self, i=0):
        artist = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_elements(by=By.XPATH, value=self.FIRST_TRACK_ARTIST)[i].text
        )
        return artist

    def get_first_track_title(self):
        track_title = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.FIRST_TRACK_TITLE).text
        )
        return track_title

    def play_track(self, i=0, last=False):
        play = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_elements(by=By.XPATH, value=self.PLAY)
        )
        if last:
            i = len(play) - 1
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(EC.element_to_be_clickable(play[i]))
        play[i].click()

    def pause_track(self):
        self.play_track()

    def get_track_id(self, i=0):
        return WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_elements(by=By.XPATH, value=self.PLAY)[i].get_attribute("data-id")
        )

    def open_first_add_to_playlist(self):
        playlist = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.PLAYLIST)
        )
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(EC.element_to_be_clickable((By.XPATH, self.PLAYLIST)))
        playlist.click()

    def open_first_album(self):
        album = WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.FIRST_TRACK_ALBUM)
        )
        album.click()

    def get_like_btn(self, track_id):
        return WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            lambda d: d.find_element(by=By.XPATH, value=self.TRACK_LIKE_BTN.format(track_id))
        )

    def remove_like(self, track_id):
        self.get_like_btn(track_id).click()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            element_attribute_not_to_include((By.XPATH, self.TRACK_LIKE_BTN.format(track_id)), self.IN_FAVORITES)
        )

    def add_like(self, track_id):
        self.get_like_btn(track_id).click()
        WebDriverWait(self.driver, TIMEOUT, CHECK_FREQ).until(
            EC.element_attribute_to_include((By.XPATH, self.TRACK_LIKE_BTN.format(track_id)), self.IN_FAVORITES)
        )
