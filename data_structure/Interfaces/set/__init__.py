"""
    Set maintains a collection of items based on an
    `intrinsic` property involved what the items are, 
    based on a unique `key`, 
    x.key, 
    associated with each item `x`


 Examples = sets are generalizations of `dictionaries` and other `query databases`
 
 
Methods defined on set interfaces are as 




|                                          Set Interface                                                       |
|--------------------------------------------------------------------------------------------------------------|
|`CONTAINER`   |   build( X:iterable)    |   given an iterable X, build set from items in X.                   |
|              |      len()              |   return the number of stored items.                                |                 
|--------------------------------------------------------------------------------------------------------------|
|`STATIC`      |     find(k)             |   return the stored item with key 'k'.                              |
|--------------------------------------------------------------------------------------------------------------|
|`DYNAMIC`     |     insert(x)           |   add 'x' to set (replace item with 'x.key' if one already exists). |
|              |     delete(k)           |   remove and return the stored item with key 'k'.                   |
|--------------------------------------------------------------------------------------------------------------|
|`ORDER`       |     iter_ord()          |   return the stored item one-by-one in key order.                   |
|              |     find_min()          |   return the stored item with smallest key.                         |
|              |     find_max()          |   return the stored item with largest key.                          |
|              |     find_prev(k)        |   return the stored item with largest key smaller than 'k'.         | 
|              |     find_next(k)        |   return the stored item with smallest key larger than 'k'.         |
|--------------------------------------------------------------------------------------------------------------|
|                 NOTE : `find_` operations returns "None" if no qualifying item exists                        |


--> Storing items in an array in arbitrary order can implement a set (not so efficient).
--> Stored items sorted increasing by key allows:
   --  faster find min/max (at first and last index of array)
   --  faster finds via binary search : `O(logn)`


"""