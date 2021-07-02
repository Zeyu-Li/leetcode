class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set([char for char in sentence])) == 26