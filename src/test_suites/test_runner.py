import HTMLTestRunner
import os
import unittest

from isphere_test import ISphereTests

dir = os.path.normpath(os.getcwd() + os.sep + os.pardir) + "\\report"
search_test = unittest.TestLoader().loadTestsFromTestCase(ISphereTests)
isphere_test = unittest.TestSuite([search_test])
outputfile = open(dir + "\TestReport.html", "w")


runner = HTMLTestRunner.HTMLTestRunner(stream=outputfile,
                                       title='Test Report',
                                       description='ISphere Test'
                                       )

runner.run(isphere_test)
