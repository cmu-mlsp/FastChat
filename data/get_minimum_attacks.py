import json
import argparse
from tqdm import tqdm




def write_min_attacks(res, minimumu=1): 
    
    controls = {}
    for i, c in enumerate(res['controls']) :

        try:
            controls[c].append((i, res['losses'][i]))

        except:
            controls[c] = []
            controls[c].append((i, res['losses'][i]))
            
            
    controls_min = {}
    for c, l in controls.items():
        l = sorted(l, key=lambda x: x[1])

        try:
            controls_min[c] = l[0]
        except:
            controls_min[c] = []
            controls_min[c] = l[0]
            
            
    controls_min_sorted = sorted(controls_min.items(), key=lambda x: x[1][1])


    attacks_info = []
    for con, (i, loss) in controls_min_sorted[:minimumu]:
        prompt_dict = {}
        
        tests = list(res['tests'][0].keys())[:-4]
        for k in tests:
        

            ls = min(res['tests'][654][k], key= lambda x: x[3])
            prompt_dict[k] = ls 




        temp = sorted(prompt_dict.items(), key= lambda x: x[1][3])

        prompt, info = temp[0]        
        attacks_info.append((con, i, loss, prompt, info ))


        
    total= ""
    for attack, _, _, _, _ in attacks_info:
        for test in res['params']['test_goals']:
            total += f"{test}{attack}\n"      
    
    with open("attack_strings.txt", 'w') as f:

        f.write(total)
        
        
    print("Attacks saved successfully!!")

parser = argparse.ArgumentParser()



#Path
parser.add_argument('--json_path', type=str, required=True)

#Data
parser.add_argument('--min_attcks', type=int, default=1)


args = parser.parse_args()





if __name__=='__main__':
    
    json_file = args.json_path
    
    with open(json_file, 'r') as f:
        attacks = f.read()
    attacks = json.loads(attacks)
    write_min_attacks(attacks, minimumu = args.min_attcks)
    
    
    
    

    