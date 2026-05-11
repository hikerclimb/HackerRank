def print_formatted(number):
    
    for i in range(1,number+ 1):
        num = str(i).rjust(len(bin(number).replace('0b', '')))
        octa = oct(i).replace('0o', '').rjust(len(bin(number).replace('0b', '')))
        hexa = hex(i).replace('0x', '').rjust(len(bin(number).replace('0b', ''))).upper()
        bina = bin(i).replace("0b", '').rjust(len(bin(number).replace('0b', '')))
        print(f'{num} {octa} {hexa} {bina}')
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
