# pylint: disable=redefined-builtin
"""Implement basic list operations without using Python's built-in list methods."""
def append(list1, list2):
    """Return a new list containing the elements of list1 followed by list2."""
    len1 = length(list1)
    len2 = length(list2)
    total = len1 + len2
    result = [None] * total
    for i in range(len1):
        result[i] = list1[i]
    for i in range(len1,total):
        result[i] = list2[i-len1]
    return result


def concat(lists):
    """Concatenate a list of lists into a single list."""
    result = []
    for item in lists:
        result = append(result,item)
    return result


def filter(function, list):
    """Return a new list containing elements that satisfy the given predicate."""
    total_len = length(list)
    result = []
    for i in range(total_len):
        if function(list[i]):
            result = append(result,[list[i]])
    return result


def length(list):
    """Return the number of elements in a list."""
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    """Return a new list with the function applied to each element."""
    total_len = length(list)
    result = [None] * total_len
    for i in range(total_len):
        result[i] = function(list[i])
    return result


def foldl(function, list, initial):
    """Reduce a list from left ot right using an accumulator fuction."""
    acc = initial
    for i in range(length(list)):
        acc = function(acc,list[i])
    return acc


def foldr(function, list, initial):
    """Reduce a list from right to left using an accumulator function."""
    acc = initial
    new_list = reverse(list)
    for i in range(length(new_list)):
        acc = function(acc,new_list[i])
    return acc


def reverse(list):
    """Return a new list with elements in reverse order."""
    total_len = length(list)
    reversed_list = [None] * total_len
    for i in range(total_len):
        reversed_list[i] = list[- i - 1]
    return reversed_list
