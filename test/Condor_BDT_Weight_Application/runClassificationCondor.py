#!/user/bin/env python

import os as os
import sys

mass = sys.argv[1]
filename = sys.argv[2]
shi = sys.argv[3]

fileListAll = [
	str(filename)
#	'ChargedHiggs_HplusTB_HplusToTB_M-180_13TeV_amcatnlo_pythia8',
# 	'ChargedHiggs_HplusTB_HplusToTB_M-200_13TeV_amcatnlo_pythia8',
# 	'ChargedHiggs_HplusTB_HplusToTB_M-220_13TeV_amcatnlo_pythia8',
# 	'ChargedHiggs_HplusTB_HplusToTB_M-250_13TeV_amcatnlo_pythia8',
# 	'ChargedHiggs_HplusTB_HplusToTB_M-300_13TeV_amcatnlo_pythia8',
# 	'ChargedHiggs_HplusTB_HplusToTB_M-350_13TeV_amcatnlo_pythia8',
# 	'ChargedHiggs_HplusTB_HplusToTB_M-400_13TeV_amcatnlo_pythia8',
# 	'ChargedHiggs_HplusTB_HplusToTB_M-450_13TeV_amcatnlo_pythia8',
# 	'ChargedHiggs_HplusTB_HplusToTB_M-500_13TeV_amcatnlo_pythia8',
# 	
#     'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#     'TT_Mtt-1000toInf_TuneCUETP8M1_13TeV-powheg-pythia8',
#     'TT_Mtt-700to1000_TuneCUETP8M1_13TeV-powheg-pythia8',
#     'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt0to700',
#     'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt1000toInf',
#     'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt700to1000',
#     'WW_TuneCUETP8M1_13TeV-pythia8',						      
#     'WZ_TuneCUETP8M1_13TeV-pythia8',						      
#     'ZZ_TuneCUETP8M1_13TeV-pythia8',						      
#     'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
#     'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
#     'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1',		      
#     'ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1',		      
#     'ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1',		      
#     'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1',		      
#     'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1',		      
#     'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',		      
#     'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',			      
#     'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',					      
#     'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8',			      
#   
#     'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
#     'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
#     'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
#     'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
#     'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
#     'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
#     'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
#     'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',              	      
#   
#     'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#     'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',    
#     'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#     'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#     'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#     'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
#     'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 
    ]

fileListNomOnly = [
    # These don't need to be run for shifted directories
    #'ST_tW_top_5f_scaleup_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', #DON'T EXIST CURRENTLY
    #'ST_tW_top_5f_scaledown_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', #DON'T EXIST CURRENTLY	      
    #'ST_tW_antitop_5f_scaleup_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', #DON'T EXIST CURRENTLY      
    #'ST_tW_antitop_5f_scaledown_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1', #DON'T EXIST CURRENTLY    
    #'TT_TuneCUETP8M1_13TeV-powheg-scaledown-pythia8', #shape samples, not needed if you aren't running the other shapes
    #'TT_TuneCUETP8M1_13TeV-powheg-scaleup-pythia8', #shape samples, not needed if you aren't running the other shapes

#    'SingleElectron_PRH',
#     'SingleMuon_PRH',
#     'SingleElectron_RRBCDEFG',
#     'SingleMuon_RRBCDEFG',
    ]
    
#signal mass points
#massPoints = ["180", "200", "220", "250", "300", "350", "400", "450"]
massPoints = [str(mass)]

# Shifts = ['JECup', 'JECdown', 'JERup', 'JERdown']
#Shifts = ['nominal']
Shifts = [str(shi)]
#inputDir = '/user_data/ssagir/LJMet_1lep_080816_HTB_step2_test/nominal/'

inputDir = '/user_data/jlee/chargedHiggs/LJMet_1lep_111816_step2preSel_aveBBdr_fixed/Test2/nominal/'
outputDir = '/user_data/jlee/chargedHiggs/atLeast3B/LJMet_1lep_111816_step2preSel_aveBBdr_fixed_BDT/Condor'

#outputDir += '180/' 
for massPoint in massPoints:
    outputDir = "%s%s/" %(outputDir, massPoint)
    for shift in Shifts:
        oLocation = '%s' %(outputDir)
        oLocation += "%s/" %shift
        if not os.path.isdir(oLocation):
            os.makedirs(oLocation)
        if shift == 'nominal':
            fileList = fileListAll+fileListNomOnly
        else:
            fileList = fileListAll
        for iFile in fileList:
#            rootCommand = "root -l -q -b /home/jlee/CMS/ChargedHiggs/CMSSW_7_2_4/src/TMVA/test/TMVAClassificationApplication_new.C\(\\\"BDT\\\",\\\"%s\\\",\\\"both\\\",\\\"%s\\\",\\\"%s\\\",\\\"%s\\\"\)" %(iFile+'_hadd.root', inputDir, massPoint, oLocation)
            rootCommand = "root -l -q -b /home/jlee/CMS/ChargedHiggs/CMSSW_7_2_4/src/TMVA/test/TMVAClassificationApplication_new.C\(\\\"BDT\\\",\\\"%s\\\",\\\"both\\\",\\\"%s\\\",\\\"%s\\\",\\\"%s\\\"\)" %(iFile, inputDir, massPoint, oLocation)
            os.system(rootCommand)
