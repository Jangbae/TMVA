#!/usr/bin/env python
import os as os
import varsList
def reWriteRankFile(inputFile):

    lines = open(inputFile, "r").readlines()
    ofile = "%s_fix.txt" %inputFile[0: inputFile.rfind(".txt")]
    output = open(ofile, "w")
    output.writelines(" massPoint: %s            nVars %s\n" %(massPoint, nVars))
    output.writelines(" --------------------------------------------------\n")
    for i in range(0, len(lines)):
        current_line = lines[i]
        cutPosition = current_line.find(":")
        BDT = current_line.find("--- BDT                      :")
        if BDT == -1:
            output.close()
            print "file saved at: %s" %ofile

            return 1
        current_line = current_line[cutPosition+1:len(current_line)]
        output.writelines(current_line)
    

varList = varsList.varList

nVars = str(len(varList))
nVars += ""

#massPoints = ["450"]
#massPoints = ["180", "200", 
massPoints = ["200"]#, "250", "300", "350", "400", "450"]#, "500"]
nTreesList = ['150']

for nTrees in nTreesList:
    for massPoint in massPoints:
        appendName = '_n%s' %nTrees
        command1 = "python TMVAClassification_both.py -i %s -n %s " %(massPoint, nTrees)

#         command1 = "python TMVAClassification_both.py -i %s -n %s | grep \"Variable Importance\" -A 20 > /user_data/zmao/TMVA/varsRank%s_%s%s.txt" %(massPoint, nTrees, massPoint, nVars, appendName)
#         command2 = "mv TMVA.root /nfs_scratch/zmao/TMVA/TMVA%s_%s%s.root" %(massPoint, nVars, appendName)

        os.system(command1)
#         os.system(command2)
#         reWriteRankFile("/nfs_scratch/zmao/TMVA/varsRank%s_%s%s.txt" %(massPoint, nVars, appendName))
        print "finished mass point", massPoint
