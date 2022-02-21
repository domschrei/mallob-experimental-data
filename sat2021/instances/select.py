
import os
import math
import random

clauses_per_filename = dict()
result_per_filename = dict()
for line in open("clauses_and_result_per_filename", "r").readlines():
    words = line.rstrip().split(" ")
    clauses_per_filename[words[0]] = int(words[1])
    result_per_filename[words[0]] = words[2]

selection = []
for line in open("by_family", "r").readlines():
    
    words = line.rstrip().replace(",", " ").split(" ")
    family = words[0]
    num_instances = len(words)-1
    inst_with_size = []
    for inst in words[1:]:
        size = clauses_per_filename[inst]
        inst_with_size += [[inst, size]]
    inst_with_size.sort(key = lambda x: x[1])
    
    split = math.ceil(0.5*len(inst_with_size))
    lower = inst_with_size[:split]
    upper = inst_with_size[split:]
    num_to_pick = min(1, math.ceil(len(inst_with_size)*0.25))
    flip = False
    i = 0
    while i < num_to_pick:
        if flip and lower:
            j = int(len(lower) * random.random())
            selection += [lower[j][0]]
            del lower[j]
            i += 1
        elif upper:
            j = int(len(upper) * random.random())
            selection += [upper[j][0]]
            del [upper[j]]
            i += 1
        flip = not flip
    print("%s : %i/%i" % (family, num_to_pick, len(inst_with_size)))

results = dict()
results["sat"] = 0
results["unsat"] = 0
results["unknown"] = 0
for inst in selection:
    res = result_per_filename[inst]
    results[res] += 1
    print(inst, res)

print(len(selection), "sat:%i unsat:%i unknown:%i" % (results["sat"], results["unsat"], results["unknown"]))
