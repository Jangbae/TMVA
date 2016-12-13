#include "variables.C"
#include "correlations.C"
#include "efficiencies.C"
#include "mvas.C"
#include "rulevis.C"
#include "mvaeffs.C"
#include <stdio.h>

void plotall( TString st = "defualt")
{
  
//  cout << st << endl;
  TString fin = st;
  cout << fin << endl;//"TMVA_500.root"
  cout << "=== execute: variables()" << endl;
  variables( fin );

  cout << "=== execute: correlations()" << endl;
  correlations( fin );

  cout << "=== execute: mvas()" << endl;
  mvas( fin );
  mvas( fin, CompareType );
  cout << "=== execute: efficiencies()" << endl;
  efficiencies( fin );

  cout << "=== execute: mvaeffs()" << endl;
  mvaeffs( fin );
  
}
