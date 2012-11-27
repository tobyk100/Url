"""
Canonicalizer implementation and tests provided by
Nikolay A. Panov, author@niksite.ru, under the GPL
http://code.google.com/p/url-normalize/
"""
import unittest
import UrlStats
from Url import Url

def main():
  suite = unittest.TestSuite()
  suite.addTests(TestNormalize())
  suite.addTests(TestValidator())
  #suite.addTests(TestComparators())
  unittest.TextTestRunner().run(suite)
"""
def TestComparators():
  suite = unittest.TestSuite()

  def testcase(expected, value):
    class test(unittest.TestCase):
      def runTest(self):
        self.assertTrue(UrlStats.validate_url(value) == expected)
    return test()

  for (expected, value) in tests:
    suite.addTest(testcase(expected, value))

  return suite
"""
def TestValidator():
  tests = [
    (True, Url("ftp://ftp.is.co.za/rfc/rfc1808.txt")),
    (True, Url("http://www.ietf.org/rfc/rfc2396.txt")),
    (True, Url("ldap://[2001:db8::7]/c=GB?objectClass?one")),
    (True, Url("mailto:John.Doe@example.com")),
    (True, Url("news:comp.infosystems.www.servers.unix")),
    (True, Url("tel:+1-816-555-1212")),
    (True, Url("telnet://192.0.2.16:80/")),
    (True, Url("urn:oasis:names:specification:docbook:dtd:xml:4.1.2"))]
  suite = unittest.TestSuite()

  def testcase(expected, value):
    class test(unittest.TestCase):
      def runTest(self):
        self.assertTrue(value.isValid() == expected)
    return test()

  for (expected, value) in tests:
    suite.addTest(testcase(expected, value))

  return suite

def TestNormalize():
  tests1 = [
      (False, Url("http://:@example.com/")),
      (False, Url("http://@example.com/")),
      (False, Url("http://example.com")),
      (False, Url("HTTP://example.com/")),
      (False, Url("http://EXAMPLE.COM/")),
      (False, Url("http://example.com/%7Ejane")),
      (False, Url("http://example.com/?q=%C7")),
      (False, Url("http://example.com/?q=%5c")),
      (False, Url("http://example.com/?q=C%CC%A7")),
      (False, Url("http://example.com/a/../a/b")),
      (False, Url("http://example.com/a/./b")),
      (False, Url("http://example.com:80/")),
      (True, Url("http://example.com/")),
      (True, Url("http://example.com/?q=%C3%87")),
      (True, Url("http://example.com/?q=%E2%85%A0")),
      (True, Url("http://example.com/?q=%5C")),
      (True, Url("http://example.com/~jane")),
      (True, Url("http://example.com/a/b")),
      (True, Url("http://example.com:8080/")),
      (True, Url("http://user:password@example.com/")),
      (True, Url("ftp://ftp.is.co.za/rfc/rfc1808.txt")),
      (True, Url("http://www.ietf.org/rfc/rfc2396.txt")),
      (True, Url("ldap://[2001:db8::7]/c=GB?objectClass?one")),
      (True, Url("mailto:John.Doe@example.com")),
      (True, Url("news:comp.infosystems.www.servers.unix")),
      (True, Url("tel:+1-816-555-1212")),
      (True, Url("telnet://192.0.2.16:80/")),
      (True, Url("urn:oasis:names:specification:docbook:dtd:xml:4.1.2")),
      (True, Url("http://127.0.0.1/")),
      (False, Url("http://127.0.0.1:80/")),
      (True, Url("http://www.w3.org/2000/01/rdf-schema#")),
      (False, Url("http://example.com:081/"))]

  suite = unittest.TestSuite()

  def testcase(expected, value):
    class test(unittest.TestCase):
      def runTest(self):
        self.assertTrue((value.getNormalized() == value.url) == expected)
    return test()

  for (expected, value) in tests1:
    suite.addTest(testcase(expected, value))

  return suite

if __name__ == '__main__':
  main()
