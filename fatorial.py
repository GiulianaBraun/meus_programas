## retorna o fatorial de um inteiro n
def fatorial(n):
    if n == 1:
        return 1
    return n*fatorial(n-1)

def main():
    n = 5
    print(fatorial(5))

if __name__ == '__main__':
    main()