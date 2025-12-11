from pages.frame_page import FramePage as F
from locators.frame_locator import *
from playwright.sync_api import expect

def test_frame(frame_page):
    # assert min 2 frames
    assert len(frame_page.page.frames)>=2, "Should be atleast two frames"
    
    frame1 = F.locate('#frame1')
    # assert frame 1 visible
    expect(frame1).to_be_visible()
    text1 = frame1.locator(HEADING).text_content()
    # assert frame1 text
    expect(text1).to_have_text('This is a sample page')
    