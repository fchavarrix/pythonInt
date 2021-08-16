def run():
    palindrome = lambda x: x == x[::-1]
    print(palindrome('Hannah'))

if __name__ == '__main__':
    run()