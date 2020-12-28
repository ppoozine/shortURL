from loguru import logger
import os

os.chmod("application/log", 0o777)

logger.add(
    "application/log/error.log",
    format="[INFO]|[{time:YYYY-MM-DD HH:mm:ss}]| [{level}]| {file} {function} {line}| {message}",
    rotation="500 MB",
    encoding="utf-8",
    level="INFO",
    diagnose=False,
    backtrace=False
)