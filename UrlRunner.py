import sys
from Url import Url

"""
Parameters:
  url_stats - a list of url stats to display, see GetStats for more.
Returns:
  Nothing
Side Effects:
  Prints stats to stdout
"""
def DisplayStats(url_stats):
  for stat in url_stats:
    print "Source: {}".format(stat['source'])
    print "Valid: {}".format(stat['valid'])
    print "Canonical: {}".format(stat['canonicalized'])
    print "Source unique: {}".format(stat['source_unique'])
    print "Canonicalized URL unique: {}\n".format(stat['canonicalized_unique'])


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print "Usage: " + argv[0] + " filename\n"
    sys.exit(1)

  try:
    file = open(sys.argv[1], "rb")
  except IOError:
    print "Could not open " + filename + " for reading\n"
    sys.exit(1)

  urls = [Url(line.strip()) for line in file]
  stats = Url.GetStats(urls)
  DisplayStats(stats)
  exit(0)
