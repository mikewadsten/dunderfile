"""
A small library to get the caller's location (file and line number).

This library is designed to emulate using __FILE__, __LINE__ and __func__
in C code and macros.
"""

import inspect

__all__ = (
        'dunderfile', 'dunderline', 'helper',
        '__FILE__', '__LINE__', '__func__')
__version__ = '0.0.1'

# Frame records are tuples of six items:
#  - the frame object
#  - the filename
#  - the line number of the current line
#  - the function name
#  - a list of lines of context from the source code
#  - the index of the current line within that list
# inspect.stack() returns a list of these records.

def dunderfile(depth=0):
    """Return the filename of the calling location.

    :param depth: Number of additional stack frames to traverse
    """
    # stack[0] is this function itself, so [1] is the caller.
    return inspect.stack()[1 + depth][1]


def dunderline(depth=0):
    """Return the line number of the calling location.

    :param depth: Number of additional stack frames to traverse
    """
    # stack[0] is this function itself, so [1] is the caller.
    return inspect.stack()[1 + depth][2]


def dunderfunc(depth=0):
    """Return the function name of the calling location.

    :param depth: Number of additional stack frames to traverse
    """
    # stack[0] is this function itself, so [1] is the caller.
    return inspect.stack()[1 + depth][3]


class _dunder_helper(object):
    """Helper class to expose __FILE__ and __LINE__ as properties

    By using this class, or more accurately, an instance of this class,
    you can avoid the syntactic overhead of calling these functions.

    Example::

        from dunderfile import __FILE__, helper as h
        line_number = __FILE__()
        # Versus...
        line_number = h.__FILE__

    """

    @property
    def __FILE__(self):
        """Get the filename of the location where this property is used."""
        return dunderfile(depth=1)

    @property
    def __LINE__(self):
        """Get the line number of the location where this property is used."""
        return dunderline(depth=1)

    @property
    def __func__(self):
        """Get the function name of the location where this property is used.
        """
        return dunderfunc(depth=1)


helper = _dunder_helper()
# C preprocessor aliases
__FILE__ = dunderfile
__LINE__ = dunderline
__func__ = dunderfunc
