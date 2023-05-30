alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def counter(message: str, step: int) -> str:
    cypher = ""
    for letter in message:
        # other symbols
        if letter not in alphabet:
            cypher = cypher + letter

        else:
            cypher_index = alphabet.index(letter) + step

            # if the stepped letter is out of the alphabet range
            if letter in alphabet and cypher_index >= len(alphabet):
                while cypher_index >= len(alphabet):
                    cypher_index = cypher_index - len(alphabet)
                cypher = cypher + alphabet[cypher_index]

            # if the stepped letter is in the alphabet range
            elif letter in alphabet and cypher_index < len(alphabet):
                cypher = cypher + alphabet[cypher_index]

    return cypher


if __name__ == '__main__':
    print(counter("100", 100))
