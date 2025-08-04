class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a','e', 'i', 'o','u', 'A', 'E', 'I', 'O', 'U']
        list_str_sentence = sentence.split(" ")
        result = []
        for word in list_str_sentence:
            if word[0] in vowels:
                new_word = word
            else:
                tmp = word[0]
                new_word = word[1:]+tmp
            new_word+='ma'
            result.append(new_word)
        # print(result)
        for i in range(0, len(result)):
            result[i]+=((i+1)*'a')
        return ' '.join(result)