import matplotlib.pyplot as plt

outFile = open('out.log')
importanceList = []
variableList = []

for line in outFile.readlines():
    if 'importance' in line:
        importanceList.append(float(line.split("importance :  ")[1].split("      variable :  ")[0]))
        variableList.append(line.split("importance :  ")[1].split("      variable :  ")[1][:-1])

sortedList = sorted(zip(importanceList,variableList), key=lambda x: x[0], reverse=True)
sortedImportance = []
sortedVariable = []
for indx, (value, var) in enumerate(sortedList):
    sortedImportance.append(value)
    sortedVariable.append(var)    
    
x_pos = []
for i in range(0,len(variableList)):
    x_pos.append(i*10-50)

f, ax = plt.subplots(figsize=(20,10))
plt.ylim(-1, 30)
plt.xlim(-60, 480)
plt.bar(x_pos, sortedImportance, width = 10, align='center')
plt.xticks(x_pos, sortedVariable, rotation=90,fontsize=10)
plt.subplots_adjust(left=0.05,right=0.95,bottom=0.3)
plt.ylabel('Importance(%)', fontsize=25)
plt.xlabel('Variable', fontsize=25)
plt.title('Variable Importance', fontsize = 30)
plt.grid(True)
plt.savefig("plot.png")