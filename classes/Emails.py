#!/usr/bin/env python


"""Identify and Extract Email Addresses."""

from email.utils import parseaddr  # Validate email addresses.

from classes.Domains import ExtractDomains  # Extract domains from input data.


__program__ = "Emails.py"
__author__ = "Johnny C. Wachter"
__copyright__ = "Copyright (C) 2015 Johnny C. Wachter"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Johnny C. Wachter"
__contact__ = "wachter.johnny@gmail.com"
__status__ = "Development"


class EmailAddresses(object):
    """Extract Email Addresses From Input Data."""

    def __init__(self, input_data):
        """Instantiate the class."""

        # Because we access attributes of an object by reference.
        self.input_data = input_data

    @staticmethod
    def valid_email_format(entry):
        """Validate Email Address."""

        valid_email_address = False

        parsed_entry = parseaddr(entry)  # Run data through parser. Invalid entry returns a two-tuple of empty strings.
        rfc_compliant_email = parsed_entry[1]  # Second part of tuple is the email address.

        # Check if string in second part of tuple contains '@' symbol.
        if '@' in rfc_compliant_email:

            split_email = rfc_compliant_email.split('@')  # Split at '@' so domain can be verified.

            # Get only the domain portion of the email for further validation.
            # Domains class expects type 'list' so we'll store the domain portion of the email as such.
            email_domain = [split_email[1]]

            domains = ExtractDomains(email_domain).get_valid_domains()  # Use Domains class to verify that it is valid.

            # If domain is valid, then append to list which will be returned at the end.
            if domains['domain_list']:

                valid_email_address = True

        return valid_email_address

    def extract_email_addresses(self):
        """Returns a list containing email addresses."""

        data = self.input_data  # Type 'list' is suggested for your input.

        email_addresses = []  # List to house final results.

        for entry in data:

            if self.valid_email_format(entry):

                email_addresses.append(entry)

        return email_addresses
