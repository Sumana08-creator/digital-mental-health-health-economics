import sys, unittest
from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from health_economics import cost_effectiveness,budget_impact,equity_summary,deterministic_sensitivity

class TestHealthEconomics(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=pd.read_csv(ROOT/"data"/"synthetic_cohort.csv")
    def test_cea(self):
        means,result=cost_effectiveness(self.data,30000)
        self.assertEqual(len(means),2)
        self.assertIn("icer_eur_per_qaly",result)
        self.assertIn("incremental_net_monetary_benefit_eur",result)
    def test_bia(self):
        r=budget_impact(1000,.25,100,1000,10)
        self.assertEqual(r["expected_users"],250)
        self.assertEqual(r["gross_budget_impact_eur"],26000)
        self.assertEqual(r["net_budget_impact_eur"],23500)
    def test_invalid_uptake(self):
        with self.assertRaises(ValueError): budget_impact(1000,1.2,100)
    def test_equity(self):
        self.assertEqual(set(equity_summary(self.data).access_group),{"Higher_access","Lower_access"})
    def test_sensitivity(self):
        self.assertEqual(len(deterministic_sensitivity(self.data)),9)

if __name__=="__main__": unittest.main()
