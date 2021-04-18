#! python3

class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
        return dict.__getitem__(self, key)
        
fd = FlexibleDict()

fd['1'] = 100
print(fd[1])
