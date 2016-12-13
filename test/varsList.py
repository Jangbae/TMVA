#!/usr/bin/env python


#input variables
varList = ['mass_minBBdr', 
	   #'mass_minLLdr', 
	   'lepDR_minBBdr', 
       'mass_maxBBpt', 'mass_maxBBmass', 'mass_maxJJJpt', 
       'aveBBdr', 
	    #'theJetLeadPt',# 'AK4HT', 'BJetLeadPt',
	   'AK4HTpMETpLepPt',
	    #'topPt',
	   'minDR_lepJet','ptRel_lepJet',
	    #'MT_lepMet', 
	   #'mass_lepJets0','mass_lepJets1','mass_lepJets2',
	   #'deltaPhi_lepJets0','deltaPhi_lepJets1','deltaPhi_lepJets2',
#NEW VARIABLES	   
       'deltaR_lepJets0','deltaR_lepJets1','deltaR_lepJets2',
		#'deltaR_lepBJets0',
		#'minDR_lepBJet',#'minBBdr',
		#'mass_lepBJet0',
        #'mass_lepBB_minBBdr',
       'mass_lepJJ_minJJdr','NJets_JetSubCalc','minMleppBjet']
#preFix = '/user_data/jlee/chargedHiggs/LJMet_1lep_111816_step2preSel_aveBBdr_fixed/Training/nominal/'

#preFix = '/user_data/jlee/chargedHiggs/LJMet_1lep_111816_step2preSel/Training/nominal/'
#preFix = '/user_data/ssagir/LJMet_1lep_080816_HTB_step2_train/nominal/'


preFix = '/user_data/ssagir/LJMet_1lep_120916_step2preSel_train/nominal/'
bkg = [


'DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_hadd.root',
'QCD_HT100to200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'QCD_HT200to300_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'QCD_HT300to500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'QCD_HT2000toInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'ST_s-channel_4f_leptonDecays_13TeV-amcatnlo-pythia8_TuneCUETP8M1_hadd.root',
'ST_t-channel_antitop_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
'ST_t-channel_top_4f_leptonDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
'ST_tW_antitop_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
'ST_tW_top_5f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_hadd.root',
'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_hadd.root',
'TT_Mtt-1000toInf_TuneCUETP8M1_13TeV-powheg-pythia8_hadd.root',
'TT_Mtt-700to1000_TuneCUETP8M1_13TeV-powheg-pythia8_hadd.root',
'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt0to700_hadd.root',
'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt1000toInf_hadd.root',
'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt700to1000_hadd.root',
'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
#'WJetsToLNu_HT-100To200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
#'WJetsToLNu_HT-200To400_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
#'WJetsToLNu_HT-400To600_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
#'WJetsToLNu_HT-600To800_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
#'WJetsToLNu_HT-800To1200_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
#'WJetsToLNu_HT-1200To2500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
#'WJetsToLNu_HT-2500ToInf_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
'WW_TuneCUETP8M1_13TeV-pythia8_hadd.root',
'WZ_TuneCUETP8M1_13TeV-pythia8_hadd.root',
'ZZ_TuneCUETP8M1_13TeV-pythia8_hadd.root'
]
'''
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
#        'ST_tW_top_4f_inclusiveDecays_13TeV-powheg-pythia8_TuneCUETP8M1_hadd.root',
        'TT_Mtt-1000toInf_TuneCUETP8M1_13TeV-powheg-pythia8_hadd.root',
	'TT_Mtt-700to1000_TuneCUETP8M1_13TeV-powheg-pythia8_hadd.root',
        'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt0to700_hadd.root',
        'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt700to1000_hadd.root',
#        'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt0to1000_hadd.root',
        'TT_TuneCUETP8M1_13TeV-powheg-pythia8_Mtt1000toInf_hadd.root',
        'TTWJetsToLNu_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
        'TTWJetsToQQ_TuneCUETP8M1_13TeV-amcatnloFXFX-madspin-pythia8_hadd.root',
        'TTZToLLNuNu_M-10_TuneCUETP8M1_13TeV-amcatnlo-pythia8_hadd.root',
        'TTZToQQ_TuneCUETP8M1_13TeV-amcatnlo-pythia8_hadd.root',
        'WJetsToLNu_TuneCUETP8M1_13TeV-madgraphMLM-pythia8_hadd.root',
        'WW_TuneCUETP8M1_13TeV-pythia8_hadd.root',
        'WZ_TuneCUETP8M1_13TeV-pythia8_hadd.root',
        'ZZ_TuneCUETP8M1_13TeV-pythia8_hadd.root',
      ]
'''
