def check_parity(bits):
    if len(bits) != 8 or not all(bit in '01' for bit in bits):
        return "Invalid input: Must be 8 bits (0s and 1s)"

    parity = sum(int(bit) for bit in bits) % 2
    if parity == 0:
        return "Parity: Even (0)"
    else:
        return "Parity: Odd (1)"


def main():
    while True:
        bits = input("Nhập chuỗi 8 bit (Nhập dòng trống để kết thúc): ").strip()

        if not bits:
            break

        result = check_parity(bits)
        print(result)


if __name__ == "__main__":
    main()
