
class Anagram:
    def __init__(self, word):
        self._word = word
    
    def match(self, list):
        output_list = []
        
        for comparison in list:
            # word_list = [letter for letter in self._word]
            # comparison_list = [letter for letter in comparison]

            if sorted([letter for letter in self._word]) == \
                sorted([letter for letter in comparison]):
                output_list.append(comparison)

        return output_list

