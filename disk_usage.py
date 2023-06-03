import shutil


# Function to get disk usage statistics
def get_disk_usage(path):
    total, used, free = shutil.disk_usage(path)
    return total, used, free
