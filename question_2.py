def is_palindrome(binary_string):
    return binary_string == binary_string[::-1]

def decimal_to_binary_palindrome(decimal):
    binary = bin(decimal)[2:]
    return is_palindrome(binary)

def main():
    number = int(input("Nhập một số nguyên dương: "))
    result = decimal_to_binary_palindrome(number)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()