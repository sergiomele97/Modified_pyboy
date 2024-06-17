#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

import time
import pyboy
from pyboy import utils
from pyboy.plugins.base_plugin import PyBoyWindowPlugin
from pyboy.utils import WindowEvent

logger = pyboy.logging.get_logger(__name__)


class WindowNull(PyBoyWindowPlugin):


    
    def __init__(self, pyboy, mb, pyboy_argv):
        super().__init__(pyboy, mb, pyboy_argv)

        if not self.enabled():
            return

        self._ftime = time.perf_counter_ns()
        
        if pyboy_argv.get("window") in ["headless", "dummy"]:
            logger.error(
                'Prueba 2 Deprecated use of "headless" or "dummy" window. Change to "null" window instead. https://github.com/Baekalfen/PyBoy/wiki/Migrating-from-v1.x.x-to-v2.0.0'
            )


    def frame_limiter(self, speed):
        self._ftime += int((1.0 / (60.0*speed)) * 1_000_000_000)
        now = time.perf_counter_ns()
        if (self._ftime > now):
            delay = (self._ftime - now) // 1_000_000
            time.sleep(delay / 1000)
        else:
            self._ftime = now
        return True

    def enabled(self):
        return self.pyboy_argv.get("window") in ["null", "headless", "dummy"]

    def set_title(self, title):
        logger.debug(title)
