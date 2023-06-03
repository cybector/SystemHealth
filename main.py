from system_info import *
from disk_usage import get_disk_usage


# Main function to print system information
def main():
    path = "C:\\"
    total, used, free = get_disk_usage(path)
    print(f"Disk Usage Statistics for drive {path}")
    print(f"Total: {total // (2**30)} GiB")
    print(f"Used: {used // (2**30)} GiB")
    print(f"Free: {free // (2**30)} GiB")
    print(f"\nCPU usage: {get_cpu_usage()}%")
    print(f"\nMemory usage: {get_memory_usage()}%")
    print("\nRunning processes:")
    for proc in get_running_processes():
        print(proc)
    hostname, ip_address = get_network_info()
    print(f"\nNetwork info: Hostname: {hostname}, IP Address: {ip_address}")
    print(f"\nOperating System info: {get_os_info()}")
    print(f"\nLast system boot time: {get_boot_time()}")


if __name__ == "__main__":
    main()
