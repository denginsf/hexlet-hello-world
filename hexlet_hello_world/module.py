from more_itertools import sliced, substrings

subs = ["".join(s) for s in substrings("more")]
print(subs)

slices = list(sliced((13, 4, 5, 6, 7, 8), 3))
print(slices)
fwesfwefwfe