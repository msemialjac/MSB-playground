import csv


def read_rolls():
    with open('battle-table.csv') as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            read_roll(row)


outcomes_csv ={}


def read_roll(row: dict):
    name = row['Attacker']
    del row['Attacker']  # delete comparison dict value
    del row[name]  # delete draw outcome

    outcomes_csv[name] = {"defeats": [], "defeated_by": []}
    for k in row.keys():
        can_defeat = row[k].strip().lower() == 'win'
        if can_defeat:
            outcomes_csv[name]["defeats"].append(k)
        else:
            outcomes_csv[name]["defeated_by"].append(k)


read_rolls()  # building outcomes dict
rolls_csv = list(outcomes_csv.keys())  # building rolls list
