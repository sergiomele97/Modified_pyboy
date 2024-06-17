#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

from pyboy.logging.logging cimport Logger
from pyboy.plugins.base_plugin cimport PyBoyWindowPlugin
from libc.stdint cimport int64_t, uint8_t, uint16_t, uint32_t

cdef class WindowNull(PyBoyWindowPlugin):
    cdef int64_t _ftime
    pass
