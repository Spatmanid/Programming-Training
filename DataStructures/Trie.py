# Date 11/02/2020
# @author Spyros Patmanidis
#
#
# Implement a trie with insert, search, and startsWith methods.

class TrieNode():
	def __init__(self):
		self.children = collections.defaultdict(TrieNode)
		self.isWord = False

class Trie:
	def __init__(self):
		self.root = TrieNode()

	def insert(self, word: str) -> None:
		node = self.root
		for w in word:
			if w not in node.children:
				node.children[w] = Trienode()
			node = node.children[w]
		node.isWord = True

	def search(self, word: str) -> bool:
		node = self.root
		for w in word:
			node = node.children.get(w)
			if not node:
				return False
		return node.isWord
        
	def startsWith(self, prefix: str) -> bool:
		node = self.root
		for w in prefix:
			node = node.children.get(w)
			if not node:
				return False
		return True
