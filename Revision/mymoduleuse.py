import mymodule as mod


for x in mod.data.keys() :
    print(f"{x} :\t{mod.data[x]}")

y = dir(mod)
print(y)