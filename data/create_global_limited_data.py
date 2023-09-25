import json
import numpy as np

np.random.seed(2438539480)

dataset_pairs = [
        ('gpt4_responses_valid.json', 'gpt4_responses_valid_25.json'),
        ('claude_responses_valid_201.json','claude_responses_valid_25.json'),
        ('gpt3.5_fitb_response_valid_2500.json', 'gpt3.5-fitb-valid-2500.json')
        ]

for gdsfn, ldsfn in dataset_pairs:

    with open(gdsfn) as f:
        gds = json.load(f)
    with open(ldsfn) as f:
        lds = json.load(f)

    if 'gpt3.5' in gdsfn:
        gds.extend(lds)

    print(f'processing {gdsfn}({len(gds)}), {ldsfn}({len(lds)})')

    lds_str_set = [str(x) for x in lds]

    gds_filtered = [x for x in gds if str(x) not in lds_str_set]
    print(f'len(gds_filtered)={len(gds_filtered)}')

    gds_limited = [gds[i] for i in np.random.choice(len(gds), size=len(lds), replace=False)]
    overlap = len([x for x in gds_limited if str(x) in lds_str_set])
    print(f'len(gds_limited)={len(gds_limited)}')
    print(f'overlap={overlap}({overlap/len(gds_limited):.4f})')

    gds_filtered_limited = [gds_filtered[i] for i in np.random.choice(len(gds_filtered), size=len(lds), replace=False)]
    print(f'len(gds_filtered_limited)={len(gds_filtered_limited)}')

    basefn = gdsfn[:-5]
    with open(f'{basefn}-limited.json', 'w') as f:
        json.dump(gds_limited, f)
    with open(f'{basefn}-filtered_limited.json', 'w') as f:
        json.dump(gds_filtered_limited, f)
    
