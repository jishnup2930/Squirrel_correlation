import json
from math import sqrt

def load_journal(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

def compute_phi(file_name, event):
    journal = load_journal(file_name)
    n11, n00, n10, n01, n1p, n0p, np1, np0 = 0, 0, 0, 0, 0, 0, 0, 0
    for entry in journal:
        if event in entry['events'] and entry['squirrel']:
            n11 += 1
    for entry in journal :
        if event not in entry['events'] and not entry['squirrel']:
            n00+=1
    for entry in journal:
        if event in entry['events'] and not entry['squirrel']:
            n10+=1
    for entry in journal:
        if event not in entry['events'] and entry['squirrel']:
            n01+=1
    
    for entry in journal:
        if event in entry['events']:
            n1p+=1
    for entry in journal:
        if event not in entry['events']:
            n0p+=1
    for entry in journal:
        if entry['squirrel']:
            np1+=1
    for entry in journal:
        if not entry['squirrel']:
            np0+=1
 
    phi = (n11 * n00 - n10 * n01) / sqrt( n1p * n0p * np1 * np0)
    return phi

def compute_correlations(file_name):
    journal = load_journal(file_name)
    events = set(event for entry in journal for event in entry['events'])
    correlations = {}
    for event in events:
        correlations[event] = compute_phi(file_name, event)
    return correlations

def diagnose(file_name):
    correlations = compute_correlations(file_name)
    max_corr = max(correlations, key=correlations.get)
    min_corr = min(correlations, key=correlations.get)
    return max_corr, min_corr

def main():
    journal_file = "journal.json"
    max_corr, min_corr = diagnose(journal_file)
    print(f"To prevent transforming into a squirrel, Scott should consider avoiding {max_corr} and focusing on {min_corr}.")

if __name__=='__main__':
    main()