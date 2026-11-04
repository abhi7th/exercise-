from fxn import *
ls =[]
fh = open("StudentExercise.csv")
next(fh)
for line in fh:
    words = line.strip().split(',')
    hr = words[0]
    if hr != '':                  
        ls.append(float(hr))
print("----------------")
print("The project file")

print("The average is {:.2f}".format(average(ls)))
print("Proportion above average: {:.0%}".format(prop_above(ls)))
print("The median is", median(ls))
