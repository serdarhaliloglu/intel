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

-----

### Usage

The program accepts one or more input file paths, and will display the results to the console; optionally, you can provide an output file path.

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

----

### Coming Soon

* Ability to provide a URL as an input path
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
