"""
This is the main module that utilizes functions from system_info to print out system information.
"""
from system_info import (
    get_os_info,
    get_cpu_info,
    get_memory_info,
    get_disk_info,
    get_network_info,
)


def main():
    """
    Prints out system information using functions from system_info module.
    """
    print("Operating System Information: ", get_os_info())
    print("CPU Information: ", get_cpu_info())
    print("Memory Information: ", get_memory_info())
    print("Disk Information: ", get_disk_info())
    print("Network Information: ", get_network_info())


if __name__ == "__main__":
    main()
