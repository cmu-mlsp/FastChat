import json
import os
import numpy as np
import sys

val_frac = float(sys.argv[1])
train_frac = 1 - val_frac

jsons = [x for x in os.listdir() if x.endswith('.json')]
for jfn in jsons:
    print('creating train and val set for', jfn)
    with open(jfn) as f:
        data = json.load(f)
    datalen = len(data)
    val_idxs = set(np.random.choice(datalen, int(datalen*val_frac)).tolist())
    train_data = []
    val_data = []
    for i, d in enumerate(data):
        if i in val_idxs:
            val_data.append(d)
        else:
            train_data.append(d)
    ofn = f'{jfn[:-5]}-{int(100*val_frac):d}pc.json'
    with open(ofn, 'w') as f:
        json.dump(val_data, f)
    ofn = f'{jfn[:-5]}-{int(100*train_frac):d}pc.json'
    with open(ofn, 'w') as f:
        json.dump(train_data, f)
