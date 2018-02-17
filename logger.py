# uncompyle6 version 2.11.2
# Python bytecode 3.5 (3351)
# Decompiled from: Python 2.7.13 (default, Apr  4 2017, 08:47:57) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.38)]
# Embedded file name: ./logger.py
# Compiled at: 2017-07-13 19:41:28
# Size of source mod 2**32: 1870 bytes
from logging import StreamHandler, DEBUG, getLogger as realGetLogger, Formatter
from colorama import Fore, Back, init, Style
init()

class ColourStreamHandler(StreamHandler):
    """ A colorized output SteamHandler """
    colours = {'DEBUG': Back.BLUE + Fore.YELLOW,
     'INFO': Fore.YELLOW,
     'WARN': Fore.YELLOW,
     'WARNING': Fore.YELLOW,
     'ERROR': Fore.RED,
     'CRIT': Back.RED + Fore.WHITE,
     'CRITICAL': Back.BLUE + Fore.YELLOW}

    def emit(self, record):
        try:
            message = self.format(record)
            self.stream.write(self.colours[record.levelname] + message + Style.RESET_ALL)
            self.stream.write(getattr(self, 'terminator', '\n'))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)


def getLogger(name=None, fmt='%(message)s'):
    """ Get and initialize a colourised logging instance if the system supports
    it as defined by the log.has_colour
    :param name: Name of the logger
    :type name: str
    :param fmt: Message format to use
    :type fmt: str
    :return: Logger instance
    :rtype: Logger
    """
    log = realGetLogger(name)
    handler = ColourStreamHandler()
    handler.setLevel(DEBUG)
    handler.setFormatter(Formatter(fmt))
    log.addHandler(handler)
    log.setLevel(DEBUG)
    log.propagate = 0
    return log


def main():
    log = getLogger('test')
    log.info('asdf')
    log.debug('qwerqwe')
    print(Fore.RED + ' asdasdf')