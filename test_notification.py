
# -*- coding: utf-8" -*

import os
import unittest
from appium import webdriver


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
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_notification(self):
        self.driver.open_notifications()
        notifications = self.driver.find_elements_by_class_name('android.widget.TextView')
        title = False
        body = False
        for element in notifications:
            print(element.text)
            if element.text == "USB debugging connected":
                title = True
            elif element.text == "Tap to disable USB debugging.":
                body = True
        self.assertTrue(title)
        self.assertTrue(body)
        self.driver.back()
        

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
