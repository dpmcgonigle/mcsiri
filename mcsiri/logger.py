import logging
import os
from logging import handlers as handlers
from typing import Optional, List


def setup_logger(
    log_file: Optional[str] = None,
    log_level: Optional[int] = logging.INFO,
    stream_logs: bool = False,
) -> None:
    """Set up the logger.

    Args:
        log_file (Optional[str], optional): The log file. Defaults to None.
        log_level (Optional[int], optional): The log level. Defaults to logging.INFO.
        stream_logs (bool, optional): Whether to stream logs to stdout. Defaults to False.
    """
    msg_format = (
        "[%(asctime)s] p%(process)s {%(filename)s "
        "%(funcName)s:%(lineno)d} %(levelname)s - %(message)s"
    )
    date_format = "%Y-%m-%d %H:%M:%S"

    # always add console logging
    log_handlers: List[logging.Handler] = []

    if stream_logs:
        log_handlers.append(logging.StreamHandler())

    if log_file:
        if not os.path.exists(os.path.dirname(log_file)):
            os.makedirs(os.path.dirname(log_file))
        log_handlers.append(_file_handler(log_file))

    logging.basicConfig(
        format=msg_format,
        datefmt=date_format,
        level=log_level,
        handlers=log_handlers,
    )


def _file_handler(log_file: str) -> logging.Handler:
    return handlers.RotatingFileHandler(log_file, maxBytes=25600000, backupCount=10)
