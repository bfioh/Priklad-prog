import sys


def get_middle_size(data):
    lines = data.strip().split('\n')[1:]
    size = 0
    files = 0

    for line in lines:
        a = line.split()
        if len(a) >= 5:
            file_size = int(a[4])
            size += file_size
            files += 1

    if files == 0:
        return 0
    else:
        return size / files


if __name__ == "__main__":
    data = sys.stdin.read()
    mean_size = get_middle_size(data)
    print(mean_size)
