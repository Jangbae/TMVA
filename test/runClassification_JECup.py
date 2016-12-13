#!/user/bin/env python

import os as os

fs = 'em'

fileListShift = ['ChargedHiggs_HplusTB_HplusToTB_M-180_13TeV_amcatnlo_pythia8_hadd.root',
                   'ChargedHiggs_HplusTB_HplusToTB_M-200_13TeV_amcatnlo_pythia8_hadd.root',
                   'ChargedHiggs_HplusTB_HplusToTB_M-220_13TeV_amcatnlo_pythia8_hadd.root',
                   'ChargedHiggs_HplusTB_HplusToTB_M-250_13TeV_amcatnlo_pythia8_hadd.root',
                   'ChargedHiggs_HplusTB_HplusToTB_M-300_13TeV_amcatnlo_pythia8_hadd.root',
                   'ChargedHiggs_HplusTB_HplusToTB_M-350_13TeV_amcatnlo_pythia8_hadd.root',
                   'ChargedHiggs_HplusTB_HplusToTB_M-400_13TeV_amcatnlo_pythia8_hadd.root',
                   'ChargedHiggs_HplusTB_HplusToTB_M-450_13TeV_amcatnlo_pythia8_hadd.root',
                   'ChargedHiggs_HplusTB_HplusToTB_M-500_13TeV_amcatnlo_pythia8_hadd.root',
                   'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_hadd.root',
                   'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
                   'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
                   'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
		   'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
		   'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
                   'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
                   'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
                   'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
                   'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_hadd.root',
                   'ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
                   'ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
                   'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
                   'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
#                   'SingleElectron_PRH_hadd.root',

#                   'SingleElectron_PRB_hadd.root',
#                   'SingleElectron_PRC_hadd.root',
#                   'SingleElectron_PRD_hadd.root',

#     	           'SingleElectron_RRBCDEFG_hadd.root',
#                   'SingleMuon_PRH_hadd.root',

#                   'SingleMuon_PRB_hadd.root',
#                   'SingleMuon_PRC_hadd.root',
#                   'SingleMuon_PRD_hadd.root',

#		   'SingleMuon_RRBCDEFG_hadd.root',

                   'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
                   'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
                   'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_hadd.root',
                   'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_hadd.root',
                   'TT_Mtt-1000toInf_TuneCUETP8M1_13TeV-powheg-pythia8_hadd.root',
		   'TT_Mtt-700to1000_TuneCUETP8M1_13TeV-powheg-pythia8_hadd.root',
#                   'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt0to1000_hadd.root',
       		   'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt0to700_hadd.root',
	           'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt700to1000_hadd.root',
                   'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt1000toInf_hadd.root',
                   'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
                   'WW_TuneCUETP8M1_13TeV-pythia8_hadd.root',
                   'WZ_TuneCUETP8M1_13TeV-pythia8_hadd.root',
                   'ZZ_TuneCUETP8M1_13TeV-pythia8_hadd.root',
                ]

#signal mass points
#massPoints = ["180", "200", "220", "250", "300", "350", "400", "450"]
massPoints = ["500"]

# Shifts = ['tauUp', 'tauDown', 'jetUp', 'jetDown', 'bSys', 'bMis']
#Shifts = ['normal']
Shifts = ['jecup']
#inputDir = '/user_data/ssagir/LJMet_1lep_080816_HTB_step2_test/nominal/'
inputDir = '/user_data/jlee/chargedHiggs/LJMet_1lep_111816_step2preSel_aveBBdr_fixed/Test2/JECup/'
outputDir = '/user_data/jlee/chargedHiggs/atLeast3B/newSample/'

for shift in Shifts:
    outputDir = "%s%s/" %(outputDir, shift)
    for massPoint in massPoints:
        oLocation = '%s' %(outputDir)
        oLocation += "%s/" %massPoint
        if not os.path.isdir(oLocation):
            os.makedirs(oLocation)
        if shift == 'normal':
            fileList = fileListNormal
        else:
            fileList = fileListShift
        for iFile in fileList:
            rootCommand = "root -l -q  TMVAClassificationApplication_new.C\(\\\"BDT\\\",\\\"%s\\\",\\\"both\\\",\\\"%s\\\",\\\"%s\\\",\\\"%s\\\"\)" %(iFile, inputDir, massPoint, oLocation)
            os.system(rootCommand)
