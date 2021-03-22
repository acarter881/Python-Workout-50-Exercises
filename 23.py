#! python3
import os
import json
from statistics import mean

def print_scores(directory):
    scores = {}

    for filename in os.listdir(directory):
        scores[filename] = {}

        with open(os.path.join(directory, filename), 'r') as infile:
            for result in json.load(infile):
                for subject, score in result.items():
                    scores[filename].setdefault(subject, [])
                    scores[filename][subject].append(score)
        print(filename)
        for subject, score in scores[filename].items():
            print(f'\t{subject}: min {min(score)}, max {max(score)}, average {int(mean(score))}')

print_scores('C:\\Users\\Alex\\Desktop\\hello\\scores')
