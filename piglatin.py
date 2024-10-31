class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.punctuations = ['.', ',', ':', ';', '?', '!', '(', ')', "'"]
        self.append_to_y = 'nay'
        self.append_to_vowel = 'yay'
        self.append_to_consonant = 'ay'

    def get_phrase(self) -> str:
        return self.phrase

    def get_transformed_phrase_with_consonant(self, word) -> str:
        first_letter = word[0]
        rest_of_the_phrase = word[1:]
        return rest_of_the_phrase + first_letter + self.append_to_consonant

    def transform_word(self, word) -> str :
        indexes_of_punctuations = []
        for i in range(0, len(word)):
            if word[i] in self.punctuations:
                indexes_of_punctuations.append((word[i], i))

        temp_str = ""
        i = 0
        for i in range(0, len(word)):
            if word[i] in self.vowels:
                break
            temp_str += word[i]
        rest_of_the_phrase = word[i:]
        s = rest_of_the_phrase + temp_str + self.append_to_consonant
        for values in indexes_of_punctuations:
            s = s[:values[1]] + values[0] + s[values[1]:]
        return s

    def get_transformed_phrase_with_consonants(self, word) -> str:
        if '-' in word:
            splitted_phrase = word.split('-')
            l = []
            for i in range(0, len(splitted_phrase)):
                l.append(self.transform_word(splitted_phrase[i]))

            return '-'.join(l)
        if word[0][0] not in self.vowels:
            return self.transform_word(word)
        else:
            temp_str = ""
            if word[-1].lower() == 'y':
                temp_str = word + self.append_to_y
            elif self.phrase[-1].lower() in self.vowels:
                temp_str = word +  self.append_to_vowel
            else:
                temp_str = word +  self.append_to_consonant
            return temp_str



    def translate(self) -> str:
        if not self.phrase:
            return "nil"
        self.phrase = self.phrase.lower()
        splitted_phrase = self.phrase.split()
        temp_splitted_phrase = splitted_phrase
        for i in range(len(splitted_phrase)):
            temp_splitted_phrase[i] = self.get_transformed_phrase_with_consonants(splitted_phrase[i])
        self.phrase = ' '.join(temp_splitted_phrase)
        if len(self.phrase.split()) == 1:
            return  self.phrase.strip()

        return self.phrase

if __name__ != '__main__':
    print("HELLO")
    obj = PigLatin("hello")
    print(obj.translate())
