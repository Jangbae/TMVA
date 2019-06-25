# TMVA

0. Check varsList.py
    - check input file location
    - check input variables for training

1. Training
    - Training script : TMVAClassification.py  
        -- arguments : -m $method -l $vListKey -n $nTrees -d $mDepth  
        -- method : BDT  
        -- vListKey : key for variable list in varsList.py  
        -- nTrees : number of trees to generation for boostrap  
        -- mDepth : depth of each tree  
    - Condor Submission script : doCondorClassification.py  
        -- nTrees : number of trees to generation for boostrap  
        -- BDTlist : training method  
        -- execution script : doCondorClassification.sh  
            --- arguments : %(RUNDIR)s %(FILENAME)s %(METHOD)s %(vListKey)s %(nTrees)s %(mDepth)s  
            --- RUNDIR : current directory  
            --- FILENAME : naming for job script  
            --- METHOD : training method  
            --- vListKey : key for variable list in varsList.py  
            --- nTrees : number of trees to generation for boostrap  
            --- mDepth : depth of each tree  

2. Application
    - Condor Submission script : doCondorApplication.py  
        -- arguments : nominal, JECup, JECdown, JERup, JERdown
        -- check "varListKey", "weightFile", "inputDir", "outputDir" in the script
                        
3. Variable Importance Evaluation
    - Condor Submission script : doCondorVariableImportance.py
        -- sepecify : nTrees, varListKeys, method, mDepth,
        -- seed : square of number of input variables
        -- subseed : remove a variable from seed
    - Evaluating variable importance : VarImportanceCalc.py
        -- excute python VarImportanceCalc.py > out.log
        -- check output log path of doCondorVariableImportance.py
    - Plotting variable importance : plottingVarImportance.py
        
        