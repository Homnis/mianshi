class Chain():
    def __init__(self, little):
        self.little = little


times = int(input("输入比较次数:"))
all = {}
for i in range(times):
    x = int(input("输入较大值："))
    y = int(input("输入较小值："))
    if all.get(x):
        all[x].little.append(y)
    else:
        all[x] = Chain([y])

first=int(input("fitst:"))
second=int(input("second:"))
if all.get(first):
    if second in all[first].little:
        print(1)
    else:
        for i in all[first].little:
            if second in all.get(i).little:
                print(1)