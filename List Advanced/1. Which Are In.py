substrings = input().split(", ")
words = input().split(", ")

occ_substrings = [substr for substr in substrings for word in words if substr in word]

print(sorted(set(occ_substrings), key=occ_substrings.index))
