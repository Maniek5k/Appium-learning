
# -*- coding: utf-8" -*

import os
import unittest
from appium import webdriver
from time import sleep

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

    def test_wifi(self):
        preference = self.driver.find_element_by_xpath('//android.widget.TextView[@text="Preference"]')
        preference.click()
        dependencies_xpath = '//android.widget.TextView[@text="3. Preference dependencies"]'
        pref_dependencies = self.driver.find_element_by_xpath(dependencies_xpath)
        pref_dependencies.click()
        checkboxes = self.driver.find_elements_by_android_uiautomator('new UiSelector().checkable(true)')
        print(len(checkboxes))
        checkbox = self.driver.find_element_by_id('android:id/checkbox')
        checkbox_checked = checkbox.get_attribute("checked")
        if len(checkboxes) >= 1:
            if checkbox_checked == "false":
                checkbox.click()
                self.assertTrue(checkbox_checked)
                wifi_settings = self.driver.find_element_by_xpath('//android.widget.TextView[@text="WiFi settings"]')
                wifi_settings.click()
                wifi_input = self.driver.find_element_by_id('android:id/edit')
                wifi_input.send_keys("password")
                submit = self.driver.find_element_by_id('android:id/button1')
                submit.click()
            else:
                raise ValueError("false isn't true")
        self.driver.back()
        self.driver.back()
        api_title = self.driver.find_element_by_xpath('//android.widget.TextView[@text="API Demos"]')
        self.assertTrue("API" in api_title.text)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
