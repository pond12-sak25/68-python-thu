set_a = {1, 2, 3, 4}
set_b = {2, 3}
set_c = {1, 2, 3, 4}
set_d = {1, 2, 3, 4, 5}

print("Is set_b a superset of set_b?", set_a >=set_a)
print("Is set_c a subset of set_a?", set_b <=set_a)

print("Is set_a a proper superset of set_b?", set_a > set_b)
print("Is set_b a proper subset of set_a?", set_b < set_a)

print("are set_a and set_c equal?", set_a == set_c)
print("is set_b a suset of set_d? and not equal?: ", set_b <= set_d and set_b != set_d)