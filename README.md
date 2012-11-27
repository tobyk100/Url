Description
===

A Url class that contains validation, canonicalization, and comparison.

Table of contents
---
1. [Usage](https://github.com/tobyk100/Url#usage)
2. [Design Decisions](https://github.com/tobyk100/Url#design-decisions)
2. [URI Normalization](https://github.com/tobyk100/Url#uri-normalization)
3. [URI Canonicalization](https://github.com/tobyk100/Url#uri-canonicalization)

Usage
===
    python UrlRunner.py filename
   
    filename should be a line separated list of urls. 
   
    Example input:
        http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations  
        http://en.wikipedia.org/wiki/Unit_testing#Language-level_unit_testing_support
      
    Example ouput:
        Source: http://en.wikipedia.org/wiki/Unit_testing#Unit_testing_limitations  
        Valid: true  
        Canonical: http://en.wikipedia.org/wiki/Unit_testing  
        Source unique: True  
        Canonicalized URL unique: False  
        Source: http://en.wikipedia.org/wiki/Unit_testing#Language-level_unit_testing_support  
        Valid: true  
        Canonical: http://en.wikipedia.org/wiki/Unit_testing  
        Source unique: True  
        Canonicalized URL unique: False  
   

Design Decisions
===
This section will cover the original design decision in 3 parts, 
we will examine why two of those parts were inadeqaute and what is different
in the design of this version.

1. URI normalization was outsourced to the fine module that Nikolay Panov wrote. 
   The details of what is normalized are listed below. One interesting design decision
   made by Nikolay was to ommit the default port, this creates output where some URIs have ports
   (non-default) and some do not. This is a bit strange, but not worth the time to tweak his code.
2. URI Validation was initially defined as the comparison between a pre-normalized and post-normalized
   URI. So, a URI was defined to be valid iff it was in normal form. This clearly had the benefit of 
   reducing the work load as now we had one function to implement instead of two. However, 
   this was too simplified, for instance www.Google.com would be considered invalid since the normal
   form would change the case of G. So for this version I decided to implement a URI validator based 
   on regex from django.core.validator. 
3. URI comparison was written by group member Chee Wei. In our group's original design and Chee Wei's implementation
   we decided that valid url's are < invalid url's. I thought that this took too much away from the caller
   since the list returned would be really two lists (valid, invalid) smashed together with no clear dividing line.
   So I define comparison as simple string comparison. This way the user can choose whether to validate or 
   normalize urls before comparing/sorting. 

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
 
URI Validation
===
I owe the following regex to django.core.validators. Please note that the implementation in Python
uses an ignore case flag which is not represented in the regex.

(?:http|ftp)s?://  
  (?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|  
  localhost|  
  \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|  
  \[?[A-F0-9]*:[A-F0-9:]+\]?)  
  (?::\d+)?    
  (?:/?|[/?]\S+)$  
