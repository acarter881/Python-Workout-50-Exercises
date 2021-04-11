#! python3

def get_sv(textFile):
    payload = []
    with open(textFile, 'r') as f:
        for row in f:
            row = row.strip('\n')
            check = {char for char in row if char in {'a','e','i','o','u'}}
            if len(check) == 5:
                payload.append(row)
                
    return set(payload)

print(get_sv('C:\\Users\\Alex\\Desktop\\hello\\Python\\words.txt'))
