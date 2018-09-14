
def binary_search(alist, value, is_sorted=True):
    '''
    Binary search algorithm.
    
    Parameters:
    `alist` -- sorted list of numeric values.
    `value` -- value to search for in the `alist`.
    `is_sorted` -- if True (default) assume that the `alist` is already sorted.
        Otherwise perform sorting before actual searching.

    Returns:
    The `value` if it exists in the `alist`, None otherwise.

    Throws:
    TypeError if `alist` contains values other than numeric or if `value` is not numeric.
    '''

    if len(alist) == 0:
        return None

    if not is_sorted:
        alist.sort()
    
    ibegin, iend = 0, len(alist) - 1
    i = int(iend / 2)

    if value < alist[i]:
        iend = i
        i = int((iend - ibegin) / 2)
    elif value > alist[i+1]:
        ibegin = i + 1
