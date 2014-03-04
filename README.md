Intel
=====

Identify, Extract, and Vet Indicators of Compromise from both formatted and unformatted input data.  The idea is to simplify the life of a security analyst/researcher when attempting to gather and share intelligence.  The project will be delivered as a collection of libs which can be used independently (e.g. IPAddresses *class* provides functionality for identifying, extracting, and classifying IP Addresses), and my own small program which leverages them in way that I find useful for day-to-day work.

The project is still under development, so currently only the functionality for *Extracting* Indicators (IP Addresses, MD5 and SHA-256 Hashes, and Domain Names) has been completed.

The output will be printed to the console, and if you choose, an output file.


Requirements
============

* Python 2.7 - this program only been tested on 2.7 for now.

```
usage: intel.py [-h] -i INPUT FILE [INPUT FILE ...] [-o OUTPUT FILE] [-e] [-v]

Used for Extracting and Vetting Intel.

optional arguments:
  -h, --help                                                           show this help message and exit
  -i INPUT FILE [INPUT FILE ...], --input INPUT FILE [INPUT FILE ...]  one or more input file paths.
  -o OUTPUT FILE, --output OUTPUT FILE                                 optional path to output file.
  -e, --extract                                                        extract intel from input data.
  -v, --vet                                                            vet intel from input data.
```
