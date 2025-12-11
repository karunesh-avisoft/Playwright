def test_alerts(alert_page):
    # normal alert
    alert_page.click_alert()
    
    # timer alert
    alert_page.click_timer_alert()

    # confirm alert
    alert_page.click_dialog()
    
    # prompt
    alert_page.click_prompt()