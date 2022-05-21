#!/usr/bin/env python3
filepath = 'TEST_PREDICTS.txt'

with open(filepath, 'r') as f:
    lines = f.readlines()
    for l in lines:
        vals = l.split('\t')
        profile = vals[0]
        irony_str = 'I' if int(vals[1]) == 1 else 'NI'
        output_str = f'<author id="{profile}"\nlang="en"\ntype="{irony_str}"\n/>\n'
        with open(f'{profile}.xml', 'w') as of:
            of.write(output_str)


