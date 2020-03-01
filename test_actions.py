
# -*- coding: utf-8" -*

import os
import unittest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ApiDemos-debug.apk')
        desired_caps['appPackage'] = 'io.appium.android.apis'
        desired_caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_notification(self):
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Views"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="Expandable Lists"]').click()
        self.driver.find_element_by_xpath('//android.widget.TextView[@text="1. Custom Adapter"]').click()
        ppl_names = self.driver.find_element_by_xpath('//android.widget.TextView[@text="People Names"]')
        ppl_names.click()
        arnold = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Arnold"]')
        self.assertTrue(arnold.is_displayed())
        action = TouchAction(self.driver)
        action.long_press(arnold).release().perform()
        message = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Sample action"]')
        self.assertIn("Sample action", message.text)
        message.click()
        for i in range(3):
            self.driver.back()
        api_title = self.driver.find_element_by_xpath('//android.widget.TextView[@text="API Demos"]')
        self.assertTrue("API" in api_title.text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
