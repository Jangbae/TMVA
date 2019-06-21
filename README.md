# TMVA

0. Check varsList.py
    - check input file location
    - check input variables for training

1. Training
    - Training script : TMVAClassification.py
        arguments : -m $method -l $vListKey -n $nTrees -d $mDepth
        method : BDT
        vListKey : key for variable list in varsList.py
        nTrees : number of trees to generation for boostrap
        mDepth : depth of each tree 
    - Condor Submission script : doCondorClassification.py    
        nTrees : number of trees to generation for boostrap
        BDTlist : training method
        execution script : doCondorClassification.sh
            arguments : %(RUNDIR)s %(FILENAME)s %(METHOD)s %(vListKey)s %(nTrees)s %(mDepth)s
            RUNDIR : current directory
            FILENAME : naming for job script
            METHOD : training method
            vListKey : key for variable list in varsList.py
            nTrees : number of trees to generation for boostrap
            mDepth : depth of each tree 

2. Application
            
        