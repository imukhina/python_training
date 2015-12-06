# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_santon(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_santon(self):
        success = True
        wd = self.wd
        wd.get("http://santehnika-online.ru/")
        wd.find_element_by_link_text("Акриловые ванны").click()
        wd.find_element_by_css_selector("img[alt=\"Акриловая ванна Serena Classic (170 см)\"]").click()
        wd.find_element_by_css_selector("#cmplproduct88078 > div.block_option > label.switch > span.switch").click()
        wd.find_element_by_id("linked_9_88078").click()
        wd.find_element_by_css_selector("#cmplproduct533850 > div.block_option > label.switch > span.switch").click()
        wd.find_element_by_id("linked_11_533850").click()
        wd.find_element_by_link_text("Акриловые ванны").click()
        wd.find_element_by_css_selector("img[alt=\"Акриловая ванна Aquanet Nord (170 см)\"]").click()
        wd.find_element_by_css_selector("span.switch").click()
        if not wd.find_element_by_id("linked_1_33825").is_selected():
            wd.find_element_by_id("linked_1_33825").click()
        wd.find_element_by_xpath("//div[@class='borgray']/div[1]/div[2]/input").click()
        wd.find_element_by_id("simplemodal-overlay").click()
        wd.find_element_by_css_selector("div.owl-wrapper-outer").click()
        wd.find_element_by_css_selector("#floating_form_cart > div.ofzakinput > input.yellow").click()
        wd.find_element_by_id("NEW_LOGIN").click()
        wd.find_element_by_id("NEW_LOGIN").clear()
        wd.find_element_by_id("NEW_LOGIN").send_keys("+7 (977) 777-77-71")
        wd.find_element_by_id("NEW_EMAIL").click()
        wd.find_element_by_id("NEW_EMAIL").clear()
        wd.find_element_by_id("NEW_EMAIL").send_keys("fdff77dfd@fd.jf")
        wd.find_element_by_id("order_ajax_button").click()
        self.assertTrue(success)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
