"""Functions for an illustrative synthetic health-economic evaluation."""
import numpy as np
import pandas as pd

INTERVENTION = "Digital_support"
COMPARATOR = "Usual_support"

def _summarise(df):
    needed = {"group","baseline_utility","followup_utility","health_service_cost_eur","programme_cost_eur","improved"}
    missing = needed - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    d = df.copy()
    d["qaly_12m_approx"] = (d.baseline_utility + d.followup_utility) / 2
    d["total_cost_eur"] = d.health_service_cost_eur + d.programme_cost_eur
    return d.groupby("group").agg(
        n=("group","size"), mean_total_cost_eur=("total_cost_eur","mean"),
        mean_qaly_12m_approx=("qaly_12m_approx","mean"),
        improvement_rate=("improved","mean"),
        mean_health_service_cost_eur=("health_service_cost_eur","mean"),
        mean_programme_cost_eur=("programme_cost_eur","mean")).reset_index()

def _dominance(cost, effect):
    if cost < 0 and effect > 0: return "Dominant in this illustrative sample"
    if cost > 0 and effect < 0: return "Dominated in this illustrative sample"
    if cost < 0 and effect < 0: return "Less effective and less costly; trade-off required"
    if cost > 0 and effect > 0: return "More effective and more costly; compare with justified threshold"
    return "No clear dominance; inspect estimates and uncertainty"

def cost_effectiveness(df, threshold_eur_per_qaly=None):
    means = _summarise(df).set_index("group")
    if INTERVENTION not in means.index or COMPARATOR not in means.index:
        raise ValueError("Both intervention and comparator groups are required.")
    a, b = means.loc[INTERVENTION], means.loc[COMPARATOR]
    dc = float(a.mean_total_cost_eur - b.mean_total_cost_eur)
    dq = float(a.mean_qaly_12m_approx - b.mean_qaly_12m_approx)
    result = {"incremental_cost_eur_per_participant":dc,
              "incremental_qaly_12m_approx_per_participant":dq,
              "incremental_improvement_rate":float(a.improvement_rate-b.improvement_rate),
              "icer_eur_per_qaly":float("nan") if np.isclose(dq,0) else dc/dq,
              "interpretation":_dominance(dc,dq)}
    if threshold_eur_per_qaly is not None:
        result["threshold_eur_per_qaly_scenario"] = float(threshold_eur_per_qaly)
        result["incremental_net_monetary_benefit_eur"] = float(threshold_eur_per_qaly*dq-dc)
    return means.reset_index(), result

def budget_impact(eligible_population, uptake, annual_cost_per_user, implementation_cost=0, offset_per_user=0):
    if eligible_population < 0: raise ValueError("eligible_population must be non-negative")
    if not 0 <= uptake <= 1: raise ValueError("uptake must be between 0 and 1")
    if min(annual_cost_per_user, implementation_cost, offset_per_user) < 0:
        raise ValueError("Costs and offsets must be non-negative")
    users = eligible_population * uptake
    gross = users * annual_cost_per_user + implementation_cost
    return {"eligible_population":int(eligible_population),"uptake":float(uptake),
            "expected_users":float(users),"annual_cost_per_user_eur":float(annual_cost_per_user),
            "implementation_cost_eur":float(implementation_cost),"offset_per_user_eur":float(offset_per_user),
            "gross_budget_impact_eur":float(gross),"net_budget_impact_eur":float(gross-users*offset_per_user)}

def equity_summary(df):
    d = df.copy()
    d["qaly_12m_approx"] = (d.baseline_utility+d.followup_utility)/2
    d["total_cost_eur"] = d.health_service_cost_eur+d.programme_cost_eur
    return d.groupby(["access_group","group"]).agg(n=("group","size"),
        mean_total_cost_eur=("total_cost_eur","mean"),
        mean_qaly_12m_approx=("qaly_12m_approx","mean"),
        improvement_rate=("improved","mean")).reset_index()

def deterministic_sensitivity(df, cost_multipliers=(0.75,1.0,1.25), qaly_multipliers=(0.5,1.0,1.5)):
    means, base = cost_effectiveness(df)
    m = means.set_index("group")
    base_health_cost = m.loc[INTERVENTION,"mean_health_service_cost_eur"]-m.loc[COMPARATOR,"mean_health_service_cost_eur"]
    base_qaly = base["incremental_qaly_12m_approx_per_participant"]
    out=[]
    for cm in cost_multipliers:
        for qm in qaly_multipliers:
            dc = float(base_health_cost + m.loc[INTERVENTION,"mean_programme_cost_eur"]*cm)
            dq = float(base_qaly*qm)
            out.append({"programme_cost_multiplier":cm,"incremental_qaly_multiplier":qm,
                        "incremental_cost_eur":dc,"incremental_qaly":dq,
                        "icer_eur_per_qaly":float("nan") if np.isclose(dq,0) else dc/dq,
                        "interpretation":_dominance(dc,dq)})
    return pd.DataFrame(out)
