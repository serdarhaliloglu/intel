#!/usr/bin/env python

"""Get and Validate Arguments Provided by the User."""

from classes import Errors  # Present error messages to the user.

import argparse  # Awesome argument parser.
import os  # A portable way of using operating system dependent functionality.
import sys  # Interact with the interpreter.
import urllib2  # Make HTTP Requests.


class GetArguments(object):

    """Get and validate arguments provided by the user."""

    def __init__(self):
        """Instantiate the Class."""
        pass

    @staticmethod
    def valid_input_path(user_input):
        """Return Valid URL and File Paths.
        :param user_input: existing fully qualified file path
        :returns: valid path and type (file path / url path)
        :rtype: tuple
        """

        # If it's an existing file, append it to appropriate list.
        if os.path.isfile(user_input):

            path_type = 'file_path'

        else:

            try:
                # Try to open URL and append its path to appropriate list.
                urllib2.urlopen(user_input)
                path_type = 'url_path'

            except urllib2.URLError:

                # Couldn't connect to server.
                error_message = Errors.URL().connection_error(user_input)

                raise argparse.ArgumentTypeError(error_message)

            except ValueError:

                # Couldn't connect to server.
                error_message = Errors.URL().invalid_path(user_input)

                raise argparse.ArgumentTypeError(error_message)

        return user_input, path_type

    @staticmethod
    def valid_output_path(user_input):
        """Ensure that output file can be used by the program.
        :param user_input: fully qualified path of an output file
        :returns: valid file path after confirmation that save location is okay
        :rtype: str
        """

        # Verification before attempting to override an existing file.
        if os.path.isfile(user_input):

            confirmation = raw_input(
                """
                This is an existing file! Are you sure that you want to
                override it? (y/n):
                """
            ).lower()

            if confirmation == "y":

                try:
                    outfile = open(user_input, 'a')
                    outfile.close()
                
                except IOError:
                    
                    # File could not be accessed
                    error_message = Errors.FilePath().file_access(user_input)
                    
                    raise argparse.ArgumentTypeError(error_message)

            elif confirmation == "n":

                sys.exit()

            else:

                # User selected a non-existent option.
                invalid_input = Errors.UserInput().invalid_input(user_input)

                raise argparse.ArgumentTypeError(invalid_input)

        else:

            try:
                outfile = open(user_input, 'a')
                outfile.close()

            except IOError:

                # File couldn't be created.
                error_message = Errors.FilePath().file_create(user_input)

                raise argparse.ArgumentTypeError(error_message)

        return user_input

    @property
    def valid_arguments(self):
        """Obtain valid arguments from the user.
        :returns : Validated arguments provided by the user
        :rtype : class 'argparse.Namespace'
        """

        # For Argparse, see: http://docs.python.org/dev/library/argparse.html
        parser = argparse.ArgumentParser(
            prog="intel.py",
            description="Used for Extracting and Vetting Intel.",
            epilog="Thanks for using this program!\n---\n3LINE",
            formatter_class=lambda prog: argparse.RawTextHelpFormatter(
                prog, max_help_position=100)
        )

        parser.add_argument(
            "-i", "--input", type=self.valid_input_path, required=True,
            metavar='INPUT PATH', nargs='+',
            help="one or more paths to input file or URL."
        )

        parser.add_argument(
            "-o", "--output", type=self.valid_output_path, required=False,
            metavar='OUTPUT FILE', help="optional path to output file."
        )

        parser.add_argument(
            "-e", "--extract", action='store_true',
            help="extract intel from input data."
        )

        parser.add_argument(
            "-v", "--vet", action='store_true',
            help="vet intel from input data."
        )

        args = parser.parse_args()

        return args
