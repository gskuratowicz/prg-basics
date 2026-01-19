import re
pattern = r'^[A-Za-z_][A-Za-z0-9_]{0,5}$'
def f(vname):
    return bool(re.match(pattern,vname))
print(f("aBC"))
print(f("_ab_c"))
print(f("abcdef"))
print(f("8abc"))
print(f("no_book"))