#!/bin/bash

#infilename=${1}
#outfilename=${2}
#inputDir=${3}
#outputDir=${4}

#scratch=${PWD}
#macroDir=${PWD}


infilename=$1
outfilename=$2
inputDir=$3
outputDir=$4
mass=$5
shifts=$6

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc481

scramv1 project CMSSW CMSSW_7_2_4
cd CMSSW_7_2_4
eval `scramv1 runtime -sh`
cd -
bash
source /home/jlee/CMS/ChargedHiggs/CMSSW_7_2_4/src/TMVA/test/Condor_BDT_Weight_Application/WeightApplication_setup.sh /home/jlee/CMS/ChargedHiggs/CMSSW_7_2_4/src/TMVA
#export PATH=$PATH:$macroDir
#echo python /home/jlee/CMS/ChargedHiggs/CMSSW_7_2_4/src/TMVA/test/Condor_BDT_Weight_Application/runClassificationCondor.py $mass $infilename
python /home/jlee/CMS/ChargedHiggs/CMSSW_7_2_4/src/TMVA/test/Condor_BDT_Weight_Application/runClassificationCondor.py $mass $infilename $shifts

#root -l -b -q makeStep2.C\(\"$macroDir\",\"$inputDir/$infilename\",\"$outputDir/$outfilename\"\)

