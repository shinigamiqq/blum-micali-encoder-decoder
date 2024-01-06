def generator(g, p, length):
    x = 150
    sequence = []
    for i in range(length):
        new_x = pow(g, x, p)
        if new_x < ((p-1)/2):
            sequence.append(1)
        else:
            sequence.append(0)
        x = new_x
    return sequence

def check_pastulates(sequence, length):
    counter_zeroes = 0
    counter_ones = 0
    for i in range(length):
        if sequence[i] == 0:
            counter_zeroes+=1
        else:
            counter_ones+=1
    print('1: ', counter_ones, '0: ', counter_zeroes)
    if abs((counter_zeroes - counter_ones)) > 100:
        print("Bad sequence.")

    for n_gram in range(2, 11):
        n_gram_counts = {}
        for i in range(length - n_gram + 1):
            subsequence = tuple(sequence[i:i+n_gram])
            n_gram_counts[subsequence] = n_gram_counts.get(subsequence, 0) + 1

        print(f"{n_gram}-gram:")
        for subsequence, count in n_gram_counts.items():
            print(f"{subsequence}: {count}")

        print()


def encoder(word, sequence):
    dictionary = {
    ' ': '00000',
    'А': '00001',
    'Б': '00010',
    'В': '00011',
    'Г': '00100',
    'Д': '00101',
    'Е': '00110',
    'Ж': '00111',
    'З': '01000',
    'И': '01001',
    'К': '01010',
    'Л': '01011',
    'М': '01100',
    'Н': '01101',
    'О': '01110',
    'П': '01111',
    'Р': '10000',
    'С': '10001',
    'Т': '10010',
    'У': '10011',
    'Ф': '10100',
    'Х': '10101',
    'Ц': '10110',
    'Ч': '10111',
    'Ш': '11000',
    'Щ': '11001',
    'Ъ': '11010',
    'Ы': '11011',
    'Ь': '11100',
    'Э': '11101',
    'Ю': '11110',
    'Я': '11111',
    }
    encoded_text = []
    text = []
    coded = []
    final = []
    result = []
    count = 0
    for char in word:
        encoded_text.append(char)
    #print(encoded_text)
    text = ''.join(dictionary.get(char, char) for char in encoded_text)
    for char in text:
        coded.append(char)
        count+=1
    #print(count)
    result = [int(item) for item in coded]
    #print("Закодированное слово:")
    #print(result)
    final = [0] * 1500
    for i in range(1500):
        final[i] = (sequence[i] + result[i]) % 2
    return final


def decoder(encoded_word, sequence):
    dictionary = {
    '00000' : ' ',
    '00001': 'А',
    '00010': 'Б',
    '00011': 'В',
    '00100': 'Г',
    '00101': 'Д',
    '00110': 'Е',
    '00111': 'Ж',
    '01000': 'З',
    '01001': 'И',
    '01010': 'К',
    '01011': 'Л',
    '01100': 'М',
    '01101': 'Н',
    '01110': 'О',
    '01111': 'П',
    '10000': 'Р',
    '10001': 'С',
    '10010': 'Т',
    '10011': 'У',
    '10100': 'Ф',
    '10101': 'Х',
    '10110': 'Ц',
    '10111': 'Ч',
    '11000': 'Ш',
    '11001': 'Щ',
    '11010': 'Ъ',
    '11011': 'Ы',
    '11100': 'Ь',
    '11101': 'Э',
    '11110': 'Ю',
    '11111': 'Я',
    }
    word = []
    word = [0] * 1500

    for i in range(1500):
        word[i] = (encoded_word[i] - sequence[i]) % 2
    grouped_word = [word[i:i+5] for i in range(0, 1500, 5)]

    decoded_word = ""

    for group in grouped_word:
        for code in dictionary:
            if group == [int(i) for i in code]:
                decoded_word += dictionary[code]
                break
    text_file = open("output", "w")
    text_file.write(decoded_word)
    text_file.close()
    return decoded_word


g = 743
p = 869
sequence = []
sequence = generator(g, p, 1500)

#print("Sequence:")
#print(sequence)


file_path = 'text'
with open(file_path, 'r', encoding='utf-8') as file:
    file_content = file.read()

encoded_word= encoder(file_content, sequence)

print("encoded_word:")
print(encoded_word)

new_g = int(input("Input g: "))
new_p = int(input("Input p: "))

if (new_g == g and new_p == p):
    decoded_word = decoder(encoded_word, sequence)
    print("decoded_word:")
    print(decoded_word)
else:
    print("Invalid values. Access denied.")

#print("Проверка пастулатов")
#check_pastulates(sequence, 1500)
