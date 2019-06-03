#!/usr/bin/python3
"""Logging utility functions for the cognida agent"""

import logging
import os

from pythonjsonlogger import jsonlogger


def log_init():
    """ logger configuration"""
    log_dir = os.getenv("LOG_DIR", "./log")
    log_file = os.getenv("LOG_FILE", "evaluation.log")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    # if log dir does not exist create it
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    json_formatter = jsonlogger.JsonFormatter()

    file_handler = logging.FileHandler(filename=f"{log_dir}/{log_file}")
    file_handler.setLevel(level=log_level)
    file_handler.setFormatter(json_formatter)

    client_handler = logging.StreamHandler()
    client_handler.setLevel(level=log_level)
    # client_handler.setFormatter(json_formatter)

    logging.basicConfig(
        level=log_level,
        handlers=[file_handler, client_handler])
