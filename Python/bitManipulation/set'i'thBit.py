n = 12
i = 1

# bitwise or
# 8 4 2 1

# 1 1 0 0 --> 12
# 0 0 1 0 --> i after left shift
# -------
# 1 1 1 0

n = n | (1<<i)
print(n)