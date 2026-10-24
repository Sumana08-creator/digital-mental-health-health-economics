from pathlib import Path
import sys
import pandas as pd
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/"src"))
from health_economics import cost_effectiveness,budget_impact,equity_summary,deterministic_sensitivity

data=pd.read_csv(ROOT/"data"/"synthetic_cohort.csv")
out=ROOT/"outputs"; out.mkdir(exist_ok=True)
means,result=cost_effectiveness(data,threshold_eur_per_qaly=30000) # illustrative input only
means.to_csv(out/"cost_effectiveness_by_group.csv",index=False)
pd.DataFrame([result]).to_csv(out/"cost_effectiveness_summary.csv",index=False)
scenarios=[]
for pop in (5000,10000,25000):
    for uptake in (0.10,0.25,0.50):
        scenarios.append(budget_impact(pop,uptake,145,25000,20))
pd.DataFrame(scenarios).to_csv(out/"budget_impact_scenarios.csv",index=False)
equity_summary(data).to_csv(out/"equity_summary.csv",index=False)
deterministic_sensitivity(data).to_csv(out/"deterministic_sensitivity.csv",index=False)
print("Analysis complete. Synthetic outputs saved to",out)
print(pd.DataFrame([result]).to_string(index=False))
print("Reminder: all data and inputs are synthetic and illustrative.")
