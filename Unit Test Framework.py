# import unittest as ut
#
# class Test(ut.TestCase):
#     def test_firstTest(self):
#         print("XYZ")
#
# if __name__=='__main__':
#     ut.main()
#
# ut.main()

#*****************************
#Calling Google and bing

# import unittest as ut
# from selenium import webdriver
#
# class SearchEnginesTest(ut.TestCase):
#     def test_Google(self):
#         self.driver=webdriver.Chrome(executable_path="E:\RPA\chromedriver.exe")
#         self.driver.get('https://www.google.co.in/')
#         self.driver.maximize_window()
#         print('Title of the page is',self.driver.title)
#         self.driver.quit()
#
#     def test_Bing(self):
#         self.driver = webdriver.Chrome(executable_path="E:\RPA\chromedriver.exe")
#         self.driver.get('https://www.bing.com/')
#         self.driver.maximize_window()
#         print('Title of the page is',self.driver.title)
#         self.driver.quit()
#
# if __name__=='__main__':
#     SearchEnginesTest.test_Google(ut)
#     SearchEnginesTest.test_Bing(ut)

# Unit Test Framework Methods
#
# import unittest as ut
# import logging as lg
#
# def test_setUpModule():
#     print('SetUpModule')
#
# def test_tearDownModule():
#     print('TearDownModule')
#
# class AppTesting(ut.TestCase):
#     @classmethod
#     def test_setUp(self):
#         print('This is login test')
#
#     @classmethod
#     def test_tearDown(self):
#         print('This is logout test')
#
#     @classmethod
#     def test_setUpClass(cls):
#         print('Opening apps')
#
#     @classmethod
#     def test_tearDownClass(cls):
#         print('Closing apps')
#
#     def test_firstTest(self):
#         print('First Test')
#         lg.warning('First test successful')
#
#     def test_secondTest(self):
#         print('Second Test')
#         lg.warning('Second test successful')
#
#     def test_thirdTest(self):
#         print('Third Test')
#         lg.warning('Third test successful')
#
# if __name__=='__main__':
#     ut.main()

#Skipping Tests
# import unittest
#
# class AppTesting(unittest.TestCase):
#     @unittest.SkipTest
#     def test_search(self):
#         print('This is first test')
#     def test_advance_search(self):
#         print('This is advance test')
#     @unittest.skipIf(1==1,"One is equal to one")
#     def test_prepaid(self):
#         print('This is prepaid recharge')
#     @unittest.skip('Skipping because I want to')
#     def test_postpaid(self):
#         print('This is postpaid recharge')
#     def test_logInByGmail(self):
#         print('This is login by email test')
#     def test_logInByTwitter(self):
#         print('This is login by twitter')
#
# if __name__ == "__main__":
#     unittest.main()

#Assertion in UnitTest Framework (Assertionis the verification for the test caseto evaluate some item on execution)
#
# import unittest as ut
# from selenium import webdriver
#
# class Test(ut.TestCase):
#     def testName(self):
#         driver=webdriver.Chrome(executable_path="E:\RPA\chromedriver.exe")
#         driver.get('https://www.google.com/')
#         titleWebPage=driver.title
#         self.assertEqual("Google",titleWebPage,"Web page title is not same")
#         driver.quit()
#
# if __name__ == "__main__":
#     ut.main()

