import pytest
from playwright.sync_api import Page
from pages.practice_form_page import PracticeFormPage
from pages.alerts_page import AlertPage
from pages.frame_page import FramePage

@pytest.fixture
def form_page(page: Page):
    page.set_default_navigation_timeout(60000)
    form = PracticeFormPage(page)
    form.open()
    return form

@pytest.fixture
def alert_page(page: Page):
    page.set_default_navigation_timeout(60000)
    alert = AlertPage(page)
    alert.open()
    return alert

@pytest.fixture
def frame_page(page: Page):
    frame = FramePage(page)
    frame.open()
    return frame