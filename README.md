Intel
=====

Currently, you can provide one or more input files containing properly, or
poorly formatted raw text from which you wish to extract Indicators of Compromise.

The output will be printed to the console, or an output file if you choose.


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
