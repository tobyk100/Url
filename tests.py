"""
Canonicalizer implementation and tests provided by
Nikolay A. Panov, author@niksite.ru, under the GPL
http://code.google.com/p/url-normalize/
"""
import unittest
import UrlStats
from url_normalize import url_normalize
from UrlComparators import URL

def main():
  suite = unittest.TestSuite()
  suite.addTests(TestNormalize())
  suite.addTests(TestValidator())
  suite.addTests(TestComparators())
  unittest.TextTestRunner().run(suite)

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

def TestValidator():
  tests = [
    (True, "ftp://ftp.is.co.za/rfc/rfc1808.txt"),
    (True, "http://www.ietf.org/rfc/rfc2396.txt"),
    (True, "ldap://[2001:db8::7]/c=GB?objectClass?one"),
    (True, "mailto:John.Doe@example.com"),
    (True, "news:comp.infosystems.www.servers.unix"),
    (True, "tel:+1-816-555-1212"),
    (True, "telnet://192.0.2.16:80/"),
    (True, "urn:oasis:names:specification:docbook:dtd:xml:4.1.2")]
  suite = unittest.TestSuite()

  def testcase(expected, value):
    class test(unittest.TestCase):
      def runTest(self):
        self.assertTrue(UrlStats.validate_url(value) == expected)
    return test()

  for (expected, value) in tests:
    suite.addTest(testcase(expected, value))

  return suite

def TestNormalize():
  tests1 = [
      (False, "http://:@example.com/"),
      (False, "http://@example.com/"),
      (False, "http://example.com"),
      (False, "HTTP://example.com/"),
      (False, "http://EXAMPLE.COM/"),
      (False, "http://example.com/%7Ejane"),
      (False, "http://example.com/?q=%C7"),
      (False, "http://example.com/?q=%5c"),
      (False, "http://example.com/?q=C%CC%A7"),
      (False, "http://example.com/a/../a/b"),
      (False, "http://example.com/a/./b"),
      (False, "http://example.com:80/"),
      (True, "http://example.com/"),
      (True, "http://example.com/?q=%C3%87"),
      (True, "http://example.com/?q=%E2%85%A0"),
      (True, "http://example.com/?q=%5C"),
      (True, "http://example.com/~jane"),
      (True, "http://example.com/a/b"),
      (True, "http://example.com:8080/"),
      (True, "http://user:password@example.com/"),
      (True, "ftp://ftp.is.co.za/rfc/rfc1808.txt"),
      (True, "http://www.ietf.org/rfc/rfc2396.txt"),
      (True, "ldap://[2001:db8::7]/c=GB?objectClass?one"),
      (True, "mailto:John.Doe@example.com"),
      (True, "news:comp.infosystems.www.servers.unix"),
      (True, "tel:+1-816-555-1212"),
      (True, "telnet://192.0.2.16:80/"),
      (True, "urn:oasis:names:specification:docbook:dtd:xml:4.1.2"),
      (True, "http://127.0.0.1/"),
      (False, "http://127.0.0.1:80/"),
      (True, "http://www.w3.org/2000/01/rdf-schema#"),
      (False, "http://example.com:081/")]

  suite = unittest.TestSuite()

  def testcase(expected, value):
    class test(unittest.TestCase):
      def runTest(self):
        self.assertTrue((UrlStats.canonicalize_url(value) == value) == expected)
    return test()

  for (expected, value) in tests1:
    suite.addTest(testcase(expected, value))

  return suite

if __name__ == '__main__':
  main()
