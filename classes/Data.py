#!/usr/bin/env python

"""Get and Format the Input Data."""

import os  # A portable way of using operating system dependent functionality.
import sys  # Interact with the interpreter.
from HTMLParser import HTMLParser  # Parse text files formatted in HTML and XHTML.

try:
    import lxml
    from lxml.html.clean import Cleaner
    from lxml import etree

except ImportError(lxml):
    sys.exit(
        """
        You're missing the lxml module.  Please acquire it here:
        http://lxml.de/installation.html
        """)

try:
    import requests

except ImportError(requests):
    sys.exit(
        """
        You're missing the requests module.  Please acquire it here:
        http://docs.python-requests.org/en/latest/user/install/
    """)

__program__ = "Data.py"
__author__ = "Johnny C. Wachter"
__copyright__ = "Copyright (C) 2012 Johnny C. Wachter"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Johnny C. Wachter"
__contact__ = "wachter.johnny@gmail.com"
__status__ = "Development"


class TagStripper(HTMLParser):
    """Used to strip tags from HTML."""

    def __init__(self):
        """Instantiate the Class."""

        self.reset()  # Reset the instance.  Loses all unprocessed data.
        self.html_data_list = []  # List to house the HTML text data read from tags.

    def handle_data(self, data_entry):
        """Override this method in HTMLParser."""
        self.html_data_list.append(data_entry)  # Add html data entry to the aforementioned list.

    def get_html_data(self):
        return ''.join(self.html_data_list)


class GetData(object):
    """Get and Classify the Input Data."""

    def __init__(self, data_path):
        """Instantiate the Class."""

        self.data_path = data_path

    def get_url(self):
        """Get the relevant part of a web page."""

        get_url = requests.get(self.data_path)
        page_data = get_url.content

        cleaner = Cleaner()
        cleaner.javascript = True  # Remove JavaScript code from HTML.
        cleaner.scripts = True  # Remove other code from HTML.
        cleaner.style = True  # Remove CSS and styles from HTML.
        cleaner.links = True  # Remove Links from HTML.
        cleaner.kill_tags = ['a', 'img']  # Remove these tags.

        # Store the cleaned up HTML.
        page_html = cleaner.clean_html(page_data)

        # Strip tags from final results.
        strip_tags = TagStripper()  # Instantiate the HTML Tag Stripper.
        strip_tags.feed(page_html)  # Strip all HTML tags.

        return strip_tags.get_html_data()


class CleanData(object):

    """Clean Up the Input Data."""

    def __init__(self, input_data):
        """Instantiate the Class."""

        self.input_data = input_data

    def to_list(self):
        """Return a List of Unique Elements."""

        if os.path.isfile(self.input_data):

            with open(self.input_data, 'rb') as infile:

                read_data = infile.read()

        elif isinstance(self.input_data, str):

            read_data = self.input_data

        data_list = read_data.split()
        clean_list = []  # List to store the cleaned up input.
        for entry in data_list:

            clean_entry = entry.strip(' .,<>?/[]\\{}"\'|`~!@#$%^&*()_+-=')

            clean_list.append(clean_entry)  # Add the entry to the clean list.

        clean_unique_list = list(set(clean_list))  # Remove duplicates in list.

        return clean_unique_list
