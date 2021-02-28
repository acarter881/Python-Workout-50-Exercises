#! python3
PEOPLE = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_records(people):
    l_to_f = []
    for person in people:
        l_to_f.append((person[1], person[0], person[2]))
    for person in l_to_f:
        print(f'{person[0].ljust(10)} {person[1].ljust(10)} {str(round(person[2],2)).ljust(5)}')

print(format_sort_records(PEOPLE))
