import logging

_logger = logging.getLogger("hamster")
_logger.setLevel('DEBUG')
_logger.addHandler(logging.StreamHandler())

d = _logger.debug
w = _logger.warning
i = _logger.info
e = _logger.error
