Intel
=====

Extract and Vet Indicators of Compromise from both formatted and unformatted input data.

This project is still under development, so currently only the functionality for *Extracting* has been completed. The following indicators can be extracted at this time:

* MD5 Hashes
* SHA-256 Hashes
* IP Addresses
* Domain Names

-----

### Requirements

Python 2.7  —  tested on version *2.7.5*

lxml (library for processing XML and HTML)  —  http://lxml.de/

-----

### Usage

The program accepts one or more input file paths, and will display the results to the console; optionally, you can provide an output file path.

```
usage: intel.py [-h] -i INPUT PATH [INPUT PATH ...] [-o OUTPUT FILE] [-e] [-v]

Used for Extracting and Vetting Intel.

optional arguments:
  -h, --help                                                           show this help message and exit
  -i INPUT PATH [INPUT PATH ...], --input INPUT PATH [INPUT PATH ...]  one or more paths to input file or URL.
  -o OUTPUT FILE, --output OUTPUT FILE                                 optional path to output file.
  -e, --extract                                                        extract intel from input data.
  -v, --vet                                                            vet intel from input data.
```

----

### Recently Added
* Ability to provide a URL as an input path


----

### Coming Soon

* Ability to provide PDF file as an input path
* Identification and extraction of file names
* Identification and extraction of Registry Paths/Keys
* Auto-generation of OpenIOC file containing the identified Indicators of Compromise
* Auto-genearation of CybOX file containing the identified Indicators of Compromise
* Vetting the extracted Indicators using several methods, including:
 * VirusTotal
 * NIST NSRL
 * IPVoid
 * ThreatExpert
 * VX Vault
 * urlQuery
 * URLVoid
 * etc.

----

### Examples

* [This article](http://normanshark.com/blog/plugx-used-mongolian-targets/) has good info about PlugX (Chinese backdoor trojan), and how it was used against Mongolia. The blog post can be copied and pasted to a text file, and presented to the program as input like this:

 ```
python intel.py -e -i "http://normanshark.com/blog/plugx-used-mongolian-targets/"
 ```
 
 OR

 ```
python intel.py -e -i "/Users/Johnny/Test/plugx_intel.txt"
 ```

 **Results**

 ```
606a3279d855f122ea3b34b0eb40c33f
d0d2079e1ab0e93c68da9c293918a376
6ab333c2bf6809b7bdc37c1484c771c5
73b6df33cf24889a03ecd75cf5a699b3
576aa3655294516fac3c55a364dd21d8
198fd054105ad89a93e401d8f59320d1
021babf0f0b8e5df2e5dbd7b379bd3b1
cc7b091b94c4f0641b180417b017fec2
cc1a806d25982acdb35dd196ab8171bc
yahoomesseges.com
yahoo.com
centralasia.regionfocus.com
Yahoomesseges.com
mseupdate.strangled.net
bodologetee.com
ppt.bodologetee.com
ssupdate.regionfocus.com
peaceful.swordwind.net
peaceful003.linkpc.net
peaceful.linkpc.net
mongolia.regionfocus.com
usa.regionfocus.com
 ```
 * We can see that there are a few legitimate domains that need to be excluded (e.g. yahoo.com), but removing those is much simpler than having to copy/paste each of the indicators from the blog.
