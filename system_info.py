"""
This module provides functions for retrieving system information.
"""
import platform
import socket
import psutil
from disk_usage import get_disk_usage


def get_os_info():
    """
    Returns information about the operating system.
    """
    uname = platform.uname()
    return (
        uname.system,
        uname.node,
        uname.release,
        uname.version,
        uname.machine,
        uname.processor,
    )


def get_cpu_info():
    """
    Returns information about the CPU.
    """
    return (
        psutil.cpu_count(logical=False),
        psutil.cpu_count(logical=True),
        psutil.cpu_percent(),
        str(psutil.cpu_freq().max) + "Mhz",
    )


def get_memory_info():
    """
    Returns information about the memory.
    """
    svmem = psutil.virtual_memory()
    return (
        str(svmem.total / (1024.0**3)) + " GB",
        str(svmem.available / (1024.0**3)) + " GB",
        svmem.percent,
    )


def get_disk_info():
    """
    Returns information about the disk.
    """
    return get_disk_usage("/")


def get_network_info():
    """
    Returns information about the network.
    """
    return socket.gethostname(), socket.gethostbyname(socket.gethostname())
