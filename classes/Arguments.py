#!/usr/bin/env python

"""Get and Validate Arguments Provided by the User."""

from classes import Errors  # Present error messages to the user.

import argparse  # Awesome argument parser.
import os  # A portable way of using operating system dependent functionality.
import sys  # Interact with the interpreter.


class GetArguments(object):

    """Get and validate arguments provided by the user."""

    def __init__(self):
        """Instantiate the Class."""
        pass

    def valid_input_path(self, user_input):
        """Validate input argument provided by the user."""

        self.user_input = user_input

        if os.path.isfile(user_input):

            # We'll use exception handling to prevent race conditions.
            try:
                with open(user_input) as infile:
                    pass

            except IOError:

                # File exists but I can't access it.
                file_access = Errors.FilePath().file_access(user_input)

                raise argparse.ArgumentTypeError(file_access)  # Tell the user.

        else:

            invalid_input = Errors.UserInput().invalid_input(user_input)

            raise argparse.ArgumentTypeError(invalid_input)

        return user_input

    def valid_output_path(self, user_input):
        """Ensure that output file can be used by the program."""

        self.user_input = user_input

        # Verification before attempting to override an existing file.
        if os.path.isfile(user_input):

            confirmation = raw_input(
                """
                This is an existing file! Are you sure that you want to
                override it? (y/n):
                """
            ).lower()

            if confirmation == "y":

                with open(user_input, 'a') as outfile:
                    pass

            elif confirmation == "n":

                sys.exit()

            else:

                # User selected a non-existent option.
                invalid_input = UserSelection().invalid_input(user_input)

                raise argparse.ArgumentTypeError(invalid_input)

        else:

            try:
                with open(user_input, 'a') as outfile:
                    pass

            except IOError:

                # File couldn't be created.
                file_create = Errors.FilePath().file_create(user_input)

                raise argparse.ArgumentTypeError(file_create)

        return user_input

    def valid_arguments(self):
        """Obtain valid arguments from the user."""

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
            metavar='INPUT FILE', nargs='+',
            help=("one or more input file paths.")
        )

        parser.add_argument(
            "-o", "--output", type=self.valid_output_path, required=False,
            metavar='OUTPUT FILE', help=("optional path to output file.")
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
