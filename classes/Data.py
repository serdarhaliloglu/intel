#!/usr/bin/env python

"""Do Stuff With the Input Data."""

import re  # For Regular Expressions.


class CleanData(object):

    """Clean Up the Input Data."""

    def __init__(self, data_path):
        """Instantiate the Class."""

        self.data_path = data_path

    def to_list(self):
        """Return a List of Unique Elements."""

        with open(self.data_path, 'rb') as infile:

            read_data = infile.read()

            # Define delimiters for the final list.
            data = re.compile(
                r"""


                [\`\~\!\#\$\%\^\&\*\(\)\_\=\+]|

                [\t\r\n\;\:\'\"\,\<\>\/\?]|

                [ \\]

                """, re.VERBOSE)

            data_list = data.split(read_data)  # Create the list.

        clean_list = []  # List to store the cleaned up input.

        for entry in data_list:

            clean_entry = entry.strip(' .,<>?/[]\\{}"\'|`~!@#$%^&*()_+-=')

            clean_list.append(clean_entry)  # Add the entry to the clean list.

        clean_unique_list = list(set(clean_list))  # Remove duplicates in list.

        return clean_unique_list
