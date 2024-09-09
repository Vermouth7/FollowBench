import json
import os

import pandas as pd

directory = "res9"
types = ['content', 'situation', 'style', 'format', 'example', 'mixed']


hsr_all_levels = {i: [] for i in range(1, 6)}
ssr_all_levels = {i: [] for i in range(1, 6)}
csl_all_values = []
type_completion_values = {}

for file_type in types:
    hsr_type_values = []
    ssr_type_values = []
    csl_type_values = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv") and filename.startswith(file_type):
            file_path = os.path.join(directory, filename)
            
            if filename.startswith(f"{file_type}_hsr"):
                df = pd.read_csv(file_path)
                df = df.iloc[:, 1:].replace('%', '', regex=True).astype(float)
                hsr_type_values.append(df.mean(axis=1).mean())
                for i in range(1, 6):
                    hsr_all_levels[i].extend(df[f'level {i}'].values)
            
            elif filename.startswith(f"{file_type}_ssr"):
                df = pd.read_csv(file_path)
                df = df.iloc[:, 1:].replace('%', '', regex=True).astype(float)
                ssr_type_values.append(df.mean(axis=1).mean())
                for i in range(1, 6):
                    ssr_all_levels[i].extend(df[f'level {i}'].values)
            
            elif filename.startswith(f"{file_type}_csl"):
                df = pd.read_csv(file_path)
                csl_type_values.extend(df["CSL"].values)
                csl_all_values.extend(df["CSL"].values)
    
    type_completion_values[file_type] = {
        'HSR': sum(hsr_type_values) / len(hsr_type_values) if hsr_type_values else 0.0,
        'SSR': sum(ssr_type_values) / len(ssr_type_values) if ssr_type_values else 0.0,
        'CSL': sum(csl_type_values) / len(csl_type_values) if csl_type_values else 0.0,
        'AverageCompletion': (
            (sum(hsr_type_values) / len(hsr_type_values) if hsr_type_values else 0.0) + 
            (sum(ssr_type_values) / len(ssr_type_values) if ssr_type_values else 0.0) 
        ) / 2
    }

hsr_avg_by_level = [sum(hsr_all_levels[i]) / len(hsr_all_levels[i]) if len(hsr_all_levels[i]) > 0 else 0.0 for i in range(1, 6)]
ssr_avg_by_level = [sum(ssr_all_levels[i]) / len(ssr_all_levels[i]) if len(ssr_all_levels[i]) > 0 else 0.0 for i in range(1, 6)]

hsr_overall_avg = sum(hsr_avg_by_level) / len(hsr_avg_by_level) if len(hsr_avg_by_level) > 0 else 0.0
ssr_overall_avg = sum(ssr_avg_by_level) / len(ssr_avg_by_level) if len(ssr_avg_by_level) > 0 else 0.0

csl_avg = sum(csl_all_values) / len(csl_all_values) if len(csl_all_values) > 0 else 0.0

results = {
    'HSR Levels': {
        'Level 1': hsr_avg_by_level[0],
        'Level 2': hsr_avg_by_level[1],
        'Level 3': hsr_avg_by_level[2],
        'Level 4': hsr_avg_by_level[3],
        'Level 5': hsr_avg_by_level[4],
        'Overall': hsr_overall_avg
    },
    'SSR Levels': {
        'Level 1': ssr_avg_by_level[0],
        'Level 2': ssr_avg_by_level[1],
        'Level 3': ssr_avg_by_level[2],
        'Level 4': ssr_avg_by_level[3],
        'Level 5': ssr_avg_by_level[4],
        'Overall': ssr_overall_avg
    },
    'CSL Average': csl_avg,
    'Type Completion Values': type_completion_values
}


output_file = os.path.join(directory, "overall_avg_results.json")
with open(output_file, 'w') as f:
    json.dump(results, f, indent=4)