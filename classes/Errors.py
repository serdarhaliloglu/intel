#!/usr/bin/env python

"""Returns Error Messages."""


class FilePath(object):

    """Return Messages Related to File Errors."""

    def __init__(self):
        """Instantiate the Class."""
        pass

    @staticmethod
    def file_access(file_path):
        """Don't have required permissions."""

        error_message = (
            """
            \n
            Could Not Access %s!
            This error can occur if permission is not granted
            to execute os.stat() on the requested file, even
            if the path physically exists.
            \n
            """
        ) % file_path

        return error_message

    @staticmethod
    def file_create(file_path):
        """Couldn't create the file."""

        error_message = (
            """
            \n
            Could Not Create %s!
            This error can occur if your input is invalid, or permission is
            not granted to execute os.stat() on the requested file, even
            if the path physically exists.
            \n
            """
        ) % file_path

        return error_message


class URL(object):

    """Return Messages Related to URL Errors."""

    def __init__(self):
        """Instantiate the Class."""
        pass

    @staticmethod
    def invalid_path(url_path):
        """ValueError, invalid path provided."""

        error_message = (
            """
            \n
            This is not a valid path: %s
            If you intended to provide a URL, please ensure that
            it is fully qualified.
            e.g. http://%s
            """
        ) % (url_path, url_path)

        return error_message

    @staticmethod
    def connection_error(url_path):
        """Could not connect to server."""

        error_message = (
            """
            \n
            Connection Error!
            Could not connect to: %s
            """
        ) % url_path

        return error_message


class UserInput(object):

    """Return Messages Related to User Input."""

    def __init__(self):
        """Instantiate the Class."""
        pass

    @staticmethod
    def invalid_input(user_selection):
        """User provided invalid input."""

        error_message = (
            """
            \n
            You provided an invalid input: %s!
            This is why input validation is important...
            \n
            """
        ) % user_selection

        return error_message
