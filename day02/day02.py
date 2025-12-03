def day02(ranges_str: str) -> int:
    result = 0
    for r in ranges_str.split(','):
        start_str, end_str = r.split('-')
        start, end = int(start_str), int(end_str)
        for i in range(start, end + 1):
            i_str = str(i)
            if len(i_str) % 2 == 0 and i_str[0:len(i_str) // 2] * 2 == i_str:
                result += i

    return result


if __name__ == "__main__":
    with open('input', 'r') as f:
        print(day02(f.read()))
