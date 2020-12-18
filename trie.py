class Node:
    def __init__(self, x):
        self.letter = x
        self.next_letters = {}
        self.is_complete = False

class Trie:

    def __init__(self):
        """
        Initialize
        """
        self.startNode = Node(None)
    
    def get_all_words(self):
        def get_all_helper(node, curr_str, res):

            if node.is_complete:
                res.append(curr_str)
                #return
                # see note below on the return statement!

                # NOTE: oftentimes with algorithm/recursive structures like this, you put a return statement here.
                # however, since we may want to add our word to the list 'early' in the case of having both "app" and "apple" in our trie,
                # we can't fully stop yet since we still need to traverse through "apple" after finding the complete word "app".

                # I suppse if you *only* wanted to find the smallest subwords, you could keep the return in. (Need to prove, though)
            
            for letter, next_node in node.next_letters.items():
                curr_str += letter
                get_all_helper(next_node, curr_str, res)
                curr_str = curr_str[:-1]


        res = []
        start = self.startNode
        get_all_helper(start, "", res)

        return res

    def get_smallest_subwords(self):
        def get_smallest_helper(node, curr_str, res):

            if node.is_complete:
                res.append(curr_str)
                return
                # see note on return statement in the get_all_words() function.
            
            for letter, next_node in node.next_letters.items():
                curr_str += letter
                get_smallest_helper(next_node, curr_str, res)
                curr_str = curr_str[:-1]


        res = []
        start = self.startNode
        get_smallest_helper(start, "", res)

        return res
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # traverse as far as we can to add to existing letters if possible
        itr = self.startNode
        letter_idx = 0
        while word[letter_idx] in itr.next_letters:
            itr = itr.next_letters[word[letter_idx]]
            letter_idx += 1
            
            # breaking here + the for loop iteration afterwards
            # should account for if we add a word that is a substring of another word
            # ex: adding "apple" and then adding "app"
            if letter_idx == len(word):
                break
            
        for i in range(letter_idx, len(word)):
            letter = word[i]
            newNode = Node(letter)
            itr.next_letters[letter] = newNode
            itr = newNode  
            
        # finished adding word, so this word is complete. 
        itr.is_complete = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        itr = self.startNode
        
        for letter in word:
            
            if letter in itr.next_letters:
                itr = itr.next_letters[letter]
            else:
                return False
        
        return itr.is_complete
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
                
        itr = self.startNode
        
        for letter in prefix:
            
            if letter in itr.next_letters:
                itr = itr.next_letters[letter]
            else:
                return False
        
        return True


obj = Trie()
obj.insert("apple")
obj.insert("app")
obj.insert("bear")
obj.insert("bearicus")
obj.insert("be")
print(obj.get_all_words())
print(obj.get_smallest_subwords())
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)