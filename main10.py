def symbolCounter(s:str):
    syms_counter = {}
    for i in s:
        if syms_counter.get(i) is None:
            syms_counter[i] = 1
        syms_counter[i] += 1
    return syms_counter
print(symbolCounter(input()))