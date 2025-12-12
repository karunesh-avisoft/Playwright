from pages.frame_page import FramePage
from locators.frame_locator import *
from playwright.sync_api import expect

def test_frame1(frame_page):
    # assert min 2 frames
    assert len(frame_page.page.frames)>=2, "Should be atleast two frames"
    
    # ---------Frame 1 ------------
    frame1 = frame_page.locate(FRAME1)      #frame element
    # assert frame 1 visible
    expect(frame1).to_be_visible()
    
    frame1 = frame_page.page.frame(name="frame1")   #actual fram object
    text1 = frame1.locator(HEADING).first.inner_html()
    print('TEXT1: ',text1)
    # assert frame1 text
    frame_page.assert_content(text1)

def test_frame2(frame_page):
    # ---------Frame 2 ------------
    frame2 = frame_page.locate(FRAME2)      #frame element
    # assert frame 2 visible
    expect(frame2).to_be_visible()
    
    frame2 = frame_page.page.frame(name="frame2")   #actual fram object
    text2 = frame2.locator(HEADING).first.inner_html()
    print('TEXT2: ',text2)
    # assert frame2 text
    frame_page.assert_content(text2)
    