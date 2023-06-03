"""
This module provides a function for retrieving disk usage information.
"""
import shutil


def get_disk_usage(path):
    """
    Returns the total, used, and free disk space for the given path.
    """
    total, used, free = shutil.disk_usage(path)
    return total, used, free
