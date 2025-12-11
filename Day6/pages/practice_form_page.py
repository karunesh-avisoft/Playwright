from playwright.sync_api import Page, expect
from locators.practice_form_locators import PracticeFormLocators as L
import re


class PracticeFormPage:

    def __init__(self, page: Page):
        self.page = page

    # ---------------- Locators ----------------
    @property
    def first_name(self):
        return self.page.locator(L.FIRST_NAME)

    @property
    def last_name(self):
        return self.page.locator(L.LAST_NAME)

    @property
    def email(self):
        return self.page.locator(L.EMAIL)

    @property
    def mobile(self):
        return self.page.locator(L.MOBILE)

    @property
    def subject(self):
        return self.page.locator(L.SUBJECT)

    # Dynamic Locator
    def gender(self, gen):
        return self.page.get_by_text(re.compile(rf"^{gen}$", re.IGNORECASE))

    def hobby(self, hob):
        return self.page.locator("label", has_text=hob)

    @property
    def picture(self):
        return self.page.locator(L.PICTURE)

    @property
    def current_address(self):
        return self.page.locator(L.CURRENT_ADDR)

    @property
    def state_dropdown(self):
        return self.page.locator(L.STATE_DROPDOWN)

    @property
    def city_dropdown(self):
        return self.page.locator(L.CITY_DROPDOWN)

    @property
    def submit(self):
        return self.page.locator(L.SUBMIT_BTN)

    @property
    def modal(self):
        return self.page.locator(L.MODAL)

    @property
    def rows(self):
        return self.modal.locator(L.TABLE_ROWS)

    # -------------- Actions --------------------

    def open(self):
        self.page.goto("https://demoqa.com/automation-practice-form")
        expect(self.page.locator("h1", has_text="Practice Form")).to_be_visible()
        self.page.locator("#userForm").scroll_into_view_if_needed()

    def fill_personal_info(self, data):
        self.first_name.type(data["first_name"])
        self.last_name.type(data["last_name"])
        self.email.type(data["email"])
        self.mobile.type(data["mobile"])

    def select_gender(self, gen):
        self.gender(gen).click()  # dynamic locator

    def select_subjects(self, subjects):
        for sub in subjects:
            self.subject.type(sub)
            self.subject.press("Enter")

    def select_hobbies(self, hobbies):
        for hob in hobbies:
            self.hobby(hob).click()  # dynamic loactor

    def upload_picture(self, file_path):
        self.picture.set_input_files(file_path)

    def enter_address(self, address):
        self.current_address.press_sequentially(address)

    def select_state_city(self, state, city):
        self.state_dropdown.click()
        self.page.get_by_text(state, exact=True).click()

        self.city_dropdown.click()
        self.page.get_by_text(city, exact=True).click()

    def submit_form(self):
        self.submit.click()
        expect(self.modal).to_be_visible()

    def get_first_name_from_modal(self):
        return self.rows.nth(0).locator("td").nth(1)
