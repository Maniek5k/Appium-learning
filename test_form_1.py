
# -*- coding: utf-8" -*

import os
import unittest
from appium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def PATH(p): return os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class TestowanieAplikacji(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platfomVersion'] = '7.0'
        desired_caps['deviceName'] = 'Gigaset GS170'
        desired_caps['app'] = PATH('ContactManager.apk')
        desired_caps['appPackage'] = 'com.example.android.contactmanager'
        desired_caps['appActivity'] = 'com.example.android.contactmanager.ContactManager'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_contact_form(self):
        add_contact = self.driver.find_element_by_id('com.example.android.contactmanager:id/addContactButton')
        add_contact.click()
        sleep(1)
        name = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactNameEditText')
        name.send_keys('test name')
        phone = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactPhoneEditText')
        phone.send_keys('123555777')
        mail = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactEmailEditText')
        mail.send_keys('test@mail.com')
        self.assertEqual(name.text, 'test name')
        self.assertEqual(phone.text, '123555777')
        self.assertEqual(mail.text, 'test@mail.com')
        save = self.driver.find_element_by_id('com.example.android.contactmanager:id/contactSaveButton')
        save.click()
        alert = 'android:id/alertTitle'
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.ID, alert)))
        alert_message = self.driver.find_element_by_id(alert).text
        self.assertTrue("Contact Manager" in alert_message)
        close_error = self.driver.find_element_by_id('android:id/aerr_restart')
        close_error.click()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestowanieAplikacji)
    unittest.TextTestRunner(verbosity=2).run(suite)
