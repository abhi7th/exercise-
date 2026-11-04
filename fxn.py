ls = [2,3,4]
def average(ls):
    return sum(ls) / len(ls)

def prop_above(ls):
    avg = average(ls)
    count = 0
   
    for num in ls:
        if num > avg:
            count += 1

    return count / len(ls)

def median(ls):
    sorted_ls = sorted(ls)

    n = len(sorted_ls)
    middle = n // 2

    if n % 2 == 0:
        return (sorted_ls[middle - 1] + sorted_ls[middle]) / 2
    else :
        return sorted_ls[middle]

print("the average is",average(ls))

print("the prop_above",prop_above(ls))

print("the median is" ,median(ls))
