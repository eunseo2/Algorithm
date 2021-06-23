def solution(n, lost, reserve):
    newLost = list(set(lost)- set(reserve))
    newReserve = list(set(reserve)- set(lost))
    Lost = newLost.copy()
    for i in newLost: 
        if i-1 in newReserve:
            newReserve.remove(i-1)
            Lost.remove(i)
        elif i+1 in newReserve :
            newReserve.remove(i+1)
            Lost.remove(i)
            
    return n-len(Lost)