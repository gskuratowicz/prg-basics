import re
def f(vname):
    return bool(re.match(r'^[A-Za-z_]{1}[A-Za-z0-9_]{0,4}$', vname))

print(f("aBC"))
print(f("_ab_c"))
print(f("abcdef"))
print(f("8abc"))
print(f("_aB8_"))