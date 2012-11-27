import sys
import Url

if __name__ == "__main__":
  if sys.argc != 2:
    print "Usage: " + argv[1] + " filename\n"
    sys.exit(1)

  try:
    file = open(filename, "rb")
  except IOError:
    print "Could not open " + filename + " for reading\n"
    sys.exit(1)

  urls = [Url(line.strip()) for line in file]
  stats = GetStats(urls)
  DisplayStats(stats)
  exit(0)
