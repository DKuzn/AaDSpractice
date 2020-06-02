from Binary_search_tree.binary_search_tree import MyBinarySearchTree
import random as rd


tree = MyBinarySearchTree(rd.randint(5, 50))

for i in range(20):
    tree.insert(rd.randint(5, 50))

print('Pre-order traversal:', end=' ')
tree.pre_order()
print('\nIn-order traversal:', end=' ')
tree.in_order()
print('\nPost-order traversal:', end=' ')
tree.post_order()
key = rd.randint(5, 50)
print('\nSequence less', key, ':', end=' ')
tree.sequence_less_key(key)
