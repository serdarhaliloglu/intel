#!/usr/bin/env python

"""Extract and Classify IP Addresses."""

import re  # Use Regular Expressions.


__program__ = "IPAddresses.py"
__author__ = "Johnny C. Wachter"
__copyright__ = "Copyright (C) 2014 Johnny C. Wachter"
__license__ = "MIT"
__version__ = "0.0.1"
__maintainer__ = "Johnny C. Wachter"
__contact__ = "wachter.johnny@gmail.com"
__status__ = "Development"


class ExtractIPs(object):

    """Extract and Classify IP Addresses From Input Data."""

    def __init__(self, input_data):
        """Instantiate the Class."""

        self.input_data = input_data
        
        self.ipv4_results = {
            'valid_ips': [],  # Store all valid IP Addresses.
            'invalid_ips': [],  # Store all invalid IP Addresses.
            'private_ips': [],  # Store all Private IP Addresses.
            'public_ips': []  # Store all Public IP Addresses.
        }

    def extract_ipv4_like(self):
        """Extract IP-like strings from input data.
        :rtype : list
        """
        
        ipv4_like_list = []

        ip_like_pattern = re.compile(r'([0-9]{1,3}\.){3}([0-9]{1,3})')

        for entry in self.input_data:
            
            if re.match(ip_like_pattern, entry):

                if len(entry.split('.')) == 4:
                    
                    ipv4_like_list.append(entry)
        
        return ipv4_like_list

    def validate_ipv4_like(self):
        """Validate that IP-like entries fall within the appropriate range."""
        
        if self.extract_ipv4_like():

            # We're gonna want to ignore the below two addresses.
            ignore_list = ['0.0.0.0', '255.255.255.255']

            # Separate the Valid from Invalid IP Addresses.
            for ipv4_like in self.extract_ipv4_like():
    
                # Split the 'IP' into parts so each part can be validated.
                parts = ipv4_like.split('.')
    
                # All part values should be between 0 and 255.
                if all(0 <= int(part) < 256 for part in parts):

                    if not ipv4_like in ignore_list:

                        self.ipv4_results['valid_ips'].append(ipv4_like)
    
                else:

                    self.ipv4_results['invalid_ips'].append(ipv4_like)
        
        else:
            pass
        
    def classify_ipv4_addresses(self):
        """Classify Valid IP Addresses."""
        
        if self.ipv4_results['valid_ips']:

            # Now we will classify the Valid IP Addresses.
            for valid_ip in self.ipv4_results['valid_ips']:

                private_ip_pattern = re.findall(
    
                    r"""^10\.(\d{1,3}\.){2}\d{1,3}
            
                    (^127\.0\.0\.1)|  # Loopback
            
                    (^10\.(\d{1,3}\.){2}\d{1,3})|  # 10/8 Range
            
                    # Matching the 172.16/12 Range takes several matches
                    (^172\.1[6-9]\.\d{1,3}\.\d{1,3})|
                    (^172\.2[0-9]\.\d{1,3}\.\d{1,3})|
                    (^172\.3[0-1]\.\d{1,3}\.\d{1,3})|
            
                    (^192\.168\.\d{1,3}\.\d{1,3})|  # 192.168/16 Range
            
                    # Match APIPA Range.
                    (^169\.254\.\d{1,3}\.\d{1,3})
            
                    # VERBOSE for a clean look of this RegEx.
                    """, valid_ip, re.VERBOSE
                )

                if private_ip_pattern:
    
                    self.ipv4_results['private_ips'].append(valid_ip)
    
                else:
                    self.ipv4_results['public_ips'].append(valid_ip)
                    
        else:
            pass
        
    def get_ipv4_results(self):
        """Extract and classify all valid and invalid IP-like strings.
        :returns : dict
        """
        
        self.extract_ipv4_like()
        self.validate_ipv4_like()
        self.classify_ipv4_addresses()
        
        return self.ipv4_results
