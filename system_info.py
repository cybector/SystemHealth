import socket
import psutil
import platform
from datetime import datetime


# Function to get disk usage statistics
def get_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    return total, used, free


# Function to get CPU usage
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


# Function to get memory usage
def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent


# Function to get list of running processes
def get_running_processes():
    processes = [proc.info for proc in psutil.process_iter(["pid", "name"])]
    return processes


# Function to get network info like hostname and IP address
def get_network_info():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return hostname, ip_address


# Function to get OS information
def get_os_info():
    os_info = platform.uname()
    return os_info


# Function to get system boot time
def get_boot_time():
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.fromtimestamp(boot_time_timestamp)
    return boot_time
