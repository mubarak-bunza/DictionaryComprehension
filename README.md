## EXERCISE 3 (Dict Comprehension)

Write a function named `dict_comp` that takes in two integer values `stop` and `step` as arguments and returns a dictionary generated using python comprehensions, which will have string keys in the format `"items-#"` and values of type `list`, where each list is of length `step` and contains only integers. 

The integers within the list values will be sequentially generated, such that integers in a second list is a continuation of those in the first list and so on for others until we get to `stop` 

```python
# Example output dictionary given that : stop = 10 and step = 4 

{
   "items-1": [ 1, 2, 3, 4 ],
   "items-2": [ 5, 6, 7, 8 ], 
}

```

Notice in the example above, the first list starts from 1 and not 0 and that the remaining integers `9 & 10` were discarded since they are not up to 4 integers to make up another entry in the dictionary.