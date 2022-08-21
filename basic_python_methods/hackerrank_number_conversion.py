def print_formatted(number):
    dec_l=len(str(number))
    octal_l=len(str(oct(number).lstrip('0o')))
    hexa_l=len(str(hex(number).capitalize().lstrip('0x')))
    binary_l=len(str(bin(number).lstrip('0b')))

    for i in range(1,number+1):
        # print(i,oct(i).lstrip('0o'),hex(i).capitalize().lstrip('0x'),bin(i).lstrip('0b'))
        dec=str(i)
        octal=str(oct(i).lstrip('0o'))
        hexa=str(hex(i).lstrip('0x').capitalize())
        binary=str(bin(i).lstrip('0b'))
        print(f'%{dec_l}s'%dec,f'%{octal_l}s'%octal,f'%{hexa_l}s'%hexa,f'%{binary_l}s'%binary)
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
