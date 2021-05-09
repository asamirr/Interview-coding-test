import os
 
bidsMap = {}
tmp = 0
 
def parseInput(file):
    with open(os.getcwd() + "/"+ file) as f:
        tmp = int(f.readline().split(' ')[1])
        for line in f:
            firName, secName, bid = line.split(" ")
            bidsMap[firName + ' ' + secName] = int(bid)
    # print (type(tmp))
    return bidsMap, tmp
 
def shiftSort(bidsMap, tmp):
    sortBidsMap = {k: v for k, v in sorted(bidsMap.items(), key=lambda item: item[1], reverse=True)}
    # print(type(sortBidsMap))
 
    biddersList = []
    amountList = []
 
    for key in sortBidsMap:
        biddersList.append(key)
 
    values = list(sortBidsMap.values())
    winners = values[1 : tmp+1]
    # print(winners)
    for i in winners:
        amountList.append(i)
 
    n = len(biddersList) - tmp
    for i in range(n):
        amountList.append("Lost")
 
    shiftList = dict(zip(biddersList, amountList))
    return shiftList
 
def solve():
    bidsMap, tmp = parseInput("in.txt")
    # print(tmp)
    newBidsMap = shiftSort(bidsMap, tmp)
    with open("out.txt", "w") as f:
        if len(newBidsMap) < 1:
            f.write("No winners")
        else:
            for key, value in newBidsMap.items():
                f.write('%s %s \n' %(key, value))
 
solve()