## pega uma string e retorna com as letras separadas por sep, sem as vogais
def print_user_word(user_word, sep='\t'):
    out = []
    for letter in user_word:
        if letter in 'aeiouAEIOU':
            continue
        else:
            out.append(letter)
    return sep.join(out)

def main():
    user_word = 'QUALQUERPALAVRA'
    print(print_user_word(user_word))

if __name__ == '__main__':
    main()
            