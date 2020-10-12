#Method : 1) for single Sided Stair-case
# %%
rows = int(input("how many stairs do you want?"))
def staircase(num_stairs):
    n = num_stairs - 1
    for stairs in range(num_stairs):
        print (' ' * n, '#' * stairs)
        n = n-1
    print('#' * num_stairs)
staircase(rows)


#Method : 1) for Double sided stair-case   
# %%














