import logging
from logging.config import fileConfig
import configparser
import asyncio
import sys
import os


configs_path = os.path.realpath(os.path.dirname(sys.argv[0])) + "/"

# Get config path from args
if len(sys.argv) > 1:
    configs_path = sys.argv[1]

# Check exists config
for config in ["config.ini", "logging.ini"]:
    if not os.path.isfile(os.path.join(configs_path, config)):
        raise FileExistsError(f"File {config} not found in path {configs_path}")

# Read config
config = configparser.ConfigParser()
config.read(os.path.join(configs_path, "config.ini"))
logging.config.fileConfig(os.path.join(configs_path, "logging.ini"), disable_existing_loggers=False)
log = logging.getLogger(__name__)


NAME = "blanket"
VERSION = "0.0.1"
HASH_ = None
TOKEN = config.get("icq_bot", "token")
POLL_TIMEOUT_S = int(config.get("icq_bot", "poll_time_s"))
REQUEST_TIMEOUT_S = int(config.get("icq_bot", "request_timeout_s"))
TASK_TIMEOUT_S = int(config.get("icq_bot", "task_timeout_s"))
TASK_MAX_LEN = int(config.get("icq_bot", "task_max_len"))

loop = asyncio.get_event_loop()
