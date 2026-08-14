# Day 16: Sets in Python

* A set is an unordered collection of unique items in Python.
* Sets are mutable, which means you can add or remove items, but they do not allow duplicates.
* They are useful when you need to store unique values and perform mathematical set operations.

## 1. Creating Sets
* Sets are created using curly braces {}.
* Sets do not maintain order, so items may appear in a different order when printed.

## 2. Adding Items
* add() adds a single item.
* update() can add multiple items from a list, tuple, or another set.

## 3. Removing Items
* remove() throws an error if the item doesn’t exist.
* discard() is safer because it does not throw an error.
* pop() removes a random item because sets are unordered.

## 4. Checking Membership
* Use the in keyword to check if an item exists in the set.

## 5. Set Operations
  
1. Union
* Combines items from both sets (duplicates removed).

2. Intersection
* Returns common items in both sets.

3. Difference
* Returns items in a not in b.

4. Symmetric Difference
* Returns items in either a or b, but not both.

## 6. Useful Functions
* len() gives the number of items.
* clear() empties the set.
