#!/usr/bin/env python3

def partition1(coin_types, amount):
    """Given `coin_types`, a set of unique integer values to choose from (with
    replacement), and `amount` a positive integer, return the number
    of ways to use the values in `coin_types` to sum to `amount`.

    Examples, also the tests!

    Simple edge behavior
    >>> partition1([], 10)
    0
    >>> partition1([3], -10)
    0
    >>> partition1((), 0)
    0

    Basic pattern
    >>> partition1((1,10), 19)
    2
    >>> partition1((1,10), 20)
    3
    >>> partition1((1,10), 29)
    3
    >>> partition1((1,10), 30)
    4

    >>> coin_types = 1, 5, 10, 25, 50, 100, 500

    >>> partition1(coin_types, 5)
    2
    >>> partition1(coin_types, 27)
    13
    >>> partition1(coin_types, 63)
    77

    >>> partition1(coin_types, 963)
    1815250

    Hints of scaling properties
    >>> for i in range(99, 106):
    ...   i, partition1(coin_types, i)
    (99, 252)
    (100, 293)
    (101, 293)
    (102, 293)
    (103, 293)
    (104, 293)
    (105, 337)

    """

    # ensure unique entries
    items = tuple(coin_types)
    assert len(set(items)) == len(items), str(coin_types)
    # Create cache
    partition_cache = {}
    def partition1r(items, amount):
        
        # Set-up cache
        cache_value = tuple(items), amount
        
        # Implement the edge behavior (and recursion stops)
        if not items or amount < 0:
            return 0
        
        # Test to see if value is in cache
        elif cache_value in partition_cache:
            return partition_cache[cache_value]
        
        # Base case when next coin will make exact change
        elif amount - items[0] == 0:
            return 1
        
        else:
        	result = partition1r(items[1:], amount) + partition1r(items, amount - items[0])
        
        # cache result to dictionary
        partition_cache[cache_value] = result
        return result

    return partition1r(coin_types, amount)

def main(args):
    amount, *items = map(int, args)
    count = partition1(items, amount)
    print(count)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv[1:]))