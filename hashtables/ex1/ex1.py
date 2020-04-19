#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    Given a package with a weight limit `limit` and a list `weights` of item weights, implement a function `get_indices_of_item_weights` that finds two items whose sum of weights equals the weight limit `limit`. Your function will return an instance of an `Answer` tuple that has the following form:
    ```
(zero, one)
    """
    
    for item in range(length): #! Inserts limit and lists of weights into hash table
        hash_table_insert(ht, weights[item], item)
     
    
    
  
def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
