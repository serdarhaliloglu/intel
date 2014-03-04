#!/usr/bin/env python

"""Extract and Validate NBIs and HBIs From Multiple Intel Sources."""

from classes.Arguments import GetArguments  # Get and validate arguments.
from classes.Data import CleanData  # # Format input data to a python list.
from classes.FileHashes import ExtractHashes  # Extract hashes from input data.
from classes.IPAddresses import ExtractIPs  # Extract IPs from input data.
from classes.Domains import ExtractDomains  # Extract domains from input data.

__program__ = "intel.py"
__author__ = "Johnny C. Wachter"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Johnny C. Wachter"
__contact__ = "wachter.johnny@gmail.com"
__status__ = "Development"


def extract_indicators(input_data):
    """Extract Indicators From the Input Data."""

    # Dictionary to house all of the results.
    results = {

        'md5_hashes': [],
        'sha256_hashes': [],
        'ip_addresses': [],
        'domains': []
    }

    hashes = ExtractHashes(input_data).get_valid_hashes()
    ips = ExtractIPs(input_data).get_valid_ips()
    domains = ExtractDomains(input_data).get_valid_domains()

    if hashes['md5_hashes']:

        results['md5_hashes'] = hashes['md5_hashes']

    if hashes['sha256_hashes']:

        results['sha256_hashes'] = hashes['sha256_hashes']

    if ips['public_ips']:

        results['ip_addresses'] = ips['public_ips']

    if domains['domain_list']:

        results['domains'] = domains['domain_list']

    return results


def main():
    """Where the Automagic Happens."""

    args = GetArguments().valid_arguments()

    input_data = []  # List to store all input data to be analyzed.

    for input_path in args.input:

        # Append input data to the list.
        input_data.extend(CleanData(input_path).to_list())

    input_data = list(set(input_data))  # Cleaned up and deduped.

    if args.output:

        # Open the output file in append mode.
        outfile = open(args.output, 'a+b')

    # Do, iff the 'extract' argument was passed.
    if args.extract:

        # Extracts indicators we care about and returns a dictionary.
        results = extract_indicators(input_data)

        # Iterate over the dictionary and get the lists that are not empty.
        results = [value for key, value in results.iteritems() if key]

        # There's gotta be a more pythonic way for iterating a list of lists...
        for result_list in results:
            if result_list:
                for entry in result_list:
                    print entry

                    if args.output:

                        entry = entry + "\n"

                        outfile.write(entry)


if __name__ == "__main__":
    main()
