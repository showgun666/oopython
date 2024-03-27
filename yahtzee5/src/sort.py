"""
Denna modul innehåller funktioner som sorterar UnorderedList
"""

def insertion_sort(items):
    """ Insertion sort """
    for i in range(1, items.size()):
        j = i
        while j > 0 and items.get(j) < items.get(j-1):
            val1 = items.get(j-1)
            val2 = items.get(j)
            items.set(j, val1)
            items.set(j-1, val2)
            j -= 1
    return items

def recursive_insertion(items, i, rvrs=False):
    """ Recursive insertion sort """
    # Base case
    if i >= items.size():
        return items

    # Sort and insert according to insertion sort
    while i > 0 and ((not rvrs and items[i] < items[i-1]) or (rvrs and items[i] > items[i-1])):
        val1 = items.get(i - 1)
        val2 = items.get(i)
        items.set(i, val1)
        items.set(i - 1, val2)
        i -= 1

    # Recursion
    return recursive_insertion(items, i + 1, rvrs)
