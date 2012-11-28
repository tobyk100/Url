Description
===

A Url class that contains validation, canonicalization, and comparison.

Table of contents
---
1. [Design Decisions](https://github.com/tobyk100/Url#design-decisions)
2. [URI Normalization](https://github.com/tobyk100/Url#uri-normalization)
3. [URI Canonicalization](https://github.com/tobyk100/Url#uri-canonicalization)

Design Decisions
===

URI Normalization
===
Credit for this portion of the class goes to Nikolay Panov (<pythoneer@niksite.ru>) under the GPL.
 * Take care of IDN domains.
 * Always provide the URI scheme in lowercase characters.
 * Always provide the host, if any, in lowercase characters.
 * Only perform percent-encoding where it is essential.
 * Always use uppercase A-through-F characters when percent-encoding.
 * Prevent dot-segments appearing in non-relative URI paths.
 * For schemes that define a default authority, use an empty authority if the
   default is desired.
 * For schemes that define an empty path to be equivalent to a path of "/",
   use "/".
 * For schemes that define a port, use an empty port if the default is desired
 * All portions of the URI must be utf-8 encoded NFC from Unicode strings
 
URI Canonicalization
===
I owe the following regex to django.core.validators

(?:http|ftp)s?://  
  (?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|  
  localhost|  
  \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|  
  \[?[A-F0-9]*:[A-F0-9:]+\]?)  
  (?::\d+)?    
  (?:/?|[/?]\S+)$  
