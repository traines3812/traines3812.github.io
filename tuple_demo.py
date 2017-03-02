#The tuple class provides a immutable sequence of elements
empty_tuple = tuple()
print('empty_tuple ->', empty_tuple)
tuple_str = tuple('hello')
print('tuple_str ->', tuple_str)
tuple_list = tuple([1, 2, [3, 5, 7]])
print('tuple_list ->', tuple_list)
empty_tuple = ()
print('empty_tuple ->', empty_tuple)
singleton_tuple =(1,)
print('singleton_tuple ->', singleton_tuple)
tuple_syn = (3, 4, 'a', 'b')
print('tuple_syn ->', tuple_syn)
print("'a' in tuple_syn ->", 'a' in tuple_syn)
print("1 not in tuple_syn ->", 1 not in tuple_syn)
print('tuple_str ->', tuple_str)
print('min(tuple_str) ->', min(tuple_str))
print('max(tuple_str) ->', max(tuple_str))
print('sorted(tuple_str) ->', sorted(tuple_str))
print('tuple_str.count("o") ->', tuple_str.count("o"))
print('tuple_str.index("o") ->', tuple_str.index("o"))
print('len(tuple_str) ->', len(tuple_str))