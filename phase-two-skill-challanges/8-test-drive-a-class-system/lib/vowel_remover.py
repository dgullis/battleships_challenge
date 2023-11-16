class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        newText = ""
        for letter in self.text:
            if letter not in self.vowels:
                    newText += letter
        return newText
        # i = 0
        # while i < len(self.text):
        #     if self.text[i].lower() in self.vowels:
        #         self.text = self.text[:i] + self.text[i+1:]
        #     i += 1
        # return self.text
    
remover = VowelRemover("aeiou")
print(remover.remove_vowels())