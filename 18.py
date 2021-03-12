#! python3

def get_final_line(fileName):
    finalRow = ''
    with open(fileName) as f:
        for row in f.readlines():
            if '\n' not in row:
                finalRow = row
    return finalRow

print(get_final_line('./Python/list.txt'))
                
