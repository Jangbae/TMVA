import os,sys,datetime,time
from ROOT import *

start_time = time.time()

#IO directories must be full paths
shift = sys.argv[1]

inputDir='/user_data/ssagir/LJMet_1lep_120816_step1/'+shift
outputDir='/user_data/ssagir/LJMet_1lep_120816_step1hadds/'+shift

os.system('mkdir -p '+outputDir)

dirList = [
	'X53X53_M-1000_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1000_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1100_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1100_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1200_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1200_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1300_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1300_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1400_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1400_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1500_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1500_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1600_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-1600_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-700_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-700_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-800_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-800_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-900_LH_TuneCUETP8M1_13TeV-madgraph-pythia8',
	'X53X53_M-900_RH_TuneCUETP8M1_13TeV-madgraph-pythia8',

	'ChargedHiggs_HplusTB_HplusToTB_M-180_13TeV_amcatnlo_pythia8',
	'ChargedHiggs_HplusTB_HplusToTB_M-200_13TeV_amcatnlo_pythia8',
	'ChargedHiggs_HplusTB_HplusToTB_M-220_13TeV_amcatnlo_pythia8',
	'ChargedHiggs_HplusTB_HplusToTB_M-250_13TeV_amcatnlo_pythia8',
	'ChargedHiggs_HplusTB_HplusToTB_M-300_13TeV_amcatnlo_pythia8',
	'ChargedHiggs_HplusTB_HplusToTB_M-350_13TeV_amcatnlo_pythia8',
	'ChargedHiggs_HplusTB_HplusToTB_M-400_13TeV_amcatnlo_pythia8',
	'ChargedHiggs_HplusTB_HplusToTB_M-450_13TeV_amcatnlo_pythia8',
	'ChargedHiggs_HplusTB_HplusToTB_M-500_13TeV_amcatnlo_pythia8',
	
    'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'TT_Mtt-1000toInf_TuneCUETP8M1_13TeV-powheg-pythia8',
    'TT_Mtt-700to1000_TuneCUETP8M1_13TeV-powheg-pythia8',
    'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt0to700',
    'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt1000toInf',
    'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt700to1000',
    'WW_TuneCUETP8M1_13TeV-pythia8',						      
    'WZ_TuneCUETP8M1_13TeV-pythia8',						      
    'ZZ_TuneCUETP8M1_13TeV-pythia8',						      
    'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8',
    'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
    'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1',		      
    'ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1',		      
    'ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1',		      
    'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1',		      
    'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1',		      
    'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',		      
    'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8',			      
    'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8',					      
    'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8',			      
  
    'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
    'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
    'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
    'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
    'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
    'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
    'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',			      
    'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',              	      
  
    'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',    
    'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8',
    'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8', 
    ]

if shift == 'nominal':
    # These don't need to be run for shifted directories
    #dirList.append('ST_tW_top_5f_scaleup_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1')
    #dirList.append('ST_tW_top_5f_scaledown_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1')	      
    #dirList.append('ST_tW_antitop_5f_scaleup_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1')	      
    #dirList.append('ST_tW_antitop_5f_scaledown_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1')      
    dirList.append('TT_TuneCUETP8M1_13TeV-powheg-scaledown-pythia8')
    dirList.append('TT_TuneCUETP8M1_13TeV-powheg-scaleup-pythia8')
#     dirList.append('SingleElectron_PRB')
#     dirList.append('SingleMuon_PRB')
#     dirList.append('SingleElectron_PRC')
#     dirList.append('SingleMuon_PRC')
#     dirList.append('SingleElectron_PRD')
#     dirList.append('SingleMuon_PRD')
    dirList.append('SingleElectron_PRH')
    dirList.append('SingleMuon_PRH')
    dirList.append('SingleElectron_RRBCDEFG')
    dirList.append('SingleMuon_RRBCDEFG')
          
for sample in dirList:
    rootfiles = [x for x in os.listdir(inputDir+'/'+sample) if '.root' in x]
    print '##########'*15
    print 'HADDING:', sample,len(rootfiles)
    print '##########'*15
    nFilesPerHadd = 999

    if len(rootfiles) < nFilesPerHadd:
        haddcommand = 'hadd -f '+outputDir+'/'+sample+'_hadd.root '
        for file in rootfiles:
            haddcommand+=' '+inputDir+'/'+sample+'/'+file
        os.system(haddcommand)
    else:
        for i in range(int(len(rootfiles)/nFilesPerHadd)):
            haddcommand = 'hadd -f '+outputDir+'/'+sample+'_'+str(i+1)+'_hadd.root '
            begin=i*nFilesPerHadd
            end=begin+nFilesPerHadd
            if len(rootfiles) - end < nFilesPerHadd: end=len(rootfiles)
            for j in range(begin,end):
                haddcommand+=' '+inputDir+'/'+sample+'/'+rootfiles[j]
            os.system(haddcommand)

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))



