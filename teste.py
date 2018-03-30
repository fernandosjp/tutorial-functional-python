from functools import partial
from re import sub
# from string import punctuation
from collections import Counter
from multiprocessing.dummy import Pool

map_parallel = Pool(4)

# Implement pipe
def pipe(*funcs):
    def inner(arg):
        result = arg
        for func in funcs:
            result = func(result)
        return result
    return inner

remove_blank_lines = partial(filter, lambda x: x != '\n')
remove_break_lines = partial(map_parallel.map, lambda x: str.strip(x, '\n'))
lower = partial(map, str.lower)
remove_punctuation = partial(map, lambda x: sub(r'[\.,;?!-\()]', '', x))
join = partial(str.join, ' ')
split = partial(str.split, sep=' ')

parse = pipe(open, remove_blank_lines,
             remove_break_lines, lower, remove_punctuation,
             join, split)

count_parse = pipe(parse, Counter)
result = count_parse('clean_architecture.txt')
print (result)
