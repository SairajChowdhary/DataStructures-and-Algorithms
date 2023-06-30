from typing import List, Optional


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add(self, word: str) -> None:
       
        pos = self.root
        for char in word:
            if char not in pos.children:
                pos.children[char] = TrieNode()
            pos = pos.children[char]
        pos.is_end = True

    def add_words(self, word_list: List[str]) -> None:
       
        for word in word_list:
            self.add(word)

    def get_suggestions(self, prefix: str) -> Optional[List[str]]:
       
        pos = self.root
        for char in prefix:
            if char not in pos.children:
               
                return None
            pos = pos.children[char]
        result = set()
        self._traverse(pos, prefix, result)
        return result

    def _traverse(self, pos: TrieNode, curr: str, result: set) -> None:
       
        if pos.is_end:
            result.add(curr)
        for child in pos.children:
            self._traverse(pos.children[child], curr + child, result)
