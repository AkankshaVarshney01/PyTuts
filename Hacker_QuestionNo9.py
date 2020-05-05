# Given an integer,n, and n space-separated integers as input, create a tuple,t , of those n integers. Then compute and print the result of hash(t).

tuple_len = int(raw_input())
a = tuple(map(int, raw_input().split(' ')))
print hash(a)