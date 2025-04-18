def get_summary_rss(out):
    memory_all = 0
    with open(out, 'r') as file:
        lines = file.readlines()[1:]
        for line in lines:
            columns = line.split()
            rss_memory = int(columns[5])
            memory_all += rss_memory
    format_vivoda = ['B', 'KiB', 'MiB', 'GiB', 'TiB']
    inbdex_vivoda = 0
    while memory_all >= 1024 and inbdex_vivoda < len(format_vivoda) - 1:
        memory_all /= 1024
        inbdex_vivoda += 1

    return f"Использование памяти в общей сумме: {memory_all:.2f} {format_vivoda[inbdex_vivoda]}"


if __name__ == '__main__':
    out = 'output_file.txt'
    print(get_summary_rss(out))