index = 0

def test(index):
    index+=1
    print(index)
    return index

for i in range(5):
    index = test(index)