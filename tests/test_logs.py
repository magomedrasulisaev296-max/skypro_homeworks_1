import logging

from src.logs import logger


def test_logger():
    assert isinstance(logger, logging.Logger)
    assert logger.name == "src.logs"
    assert logger.level == logging.INFO

    assert len(logger.handlers) > 0

    for handler in logger.handlers:
        assert isinstance(handler, logging.Handler)
