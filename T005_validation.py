"""Exact supporting checks for T005; the continuum proofs are in T005_theory.md.

Python 3.12+, standard library only. No simulation, finite deviation grid or
external packages. Price checks enumerate every affine piece for each selected
quality pair, but the selection of quality pairs does not prove the theorem.
Accepted T004 rational evidence is read and reused, not independently rerun.
"""
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path
from itertools import product
import hashlib
import json
import platform
import sys

ROOT = Path(__file__).resolve().parent
OUT = Path(__file__).resolve().parent
SNAP = ROOT
WITNESS = SNAP / 'independent_witness.json'
accepted = json.loads(WITNESS.read_text(encoding='utf-8'))


def frac(value):
    return F(value['exact'])


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def serial(value):
    if isinstance(value, F):
        return {'exact': str(value), 'float': float(value)}
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, dict):
        return {str(k): serial(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serial(v) for v in value]
    return value


M = h = l = o = v = t = c = F(1)
w, d, k, E, V = F(1, 10), F(1, 50), F(1, 200), F(3, 5), F(4)
B = 9*t*c
A, C, K = (B-1)/(3*(B-2)), c*(B-1)/(2*(B-2)**2), t/2-F(1)/(18*c)
ds = frac(accepted['segmented']['symmetric_q_change'])
dp = frac(accepted['pooled']['profiles']['10']['b'][0])-frac(accepted['pooled']['profiles']['10']['b'][1])
dm = max(abs(ds), abs(dp))
margins = {
    'B_minus_2': B-2,
    't_minus_Dmax_minus_E': t-dm-E,
    'positive_effort_domain': (B-2)/(3*c)-dm,
    'upper_effort_slack': E-F(1)/(3*c)-dm/(B-2),
    'reservation_slack': V-3*t,
    'profit_lower_bound': K-A*dm-k,
    'negative_delta_S': -ds,
    'positive_delta_P': dp,
    'strict_pooled_dominance': A*dp-C*dp*dp-k,
}
assert all(x > 0 for x in margins.values())


def demand(pi, pj, qi, qj):
    """Own-coordinate exact Hotelling demand including nonpurchase."""
    return max(F(0), min(F(1), (t+qi-qj-pi+pj)/(2*t), (V+qi-pi)/t))


def price_candidates(pj, qi, qj):
    """Exhaustive stationary/breakpoint set of a piecewise quadratic revenue.

    Demand is max(0,min(three affine functions)). Include all line crossings,
    each line's zero, zero price and the reservation choke price. On each
    open interval the selected affine line is fixed; include its revenue peak.
    Prices above the choke price all yield zero and need no enumeration.
    """
    lines = [(F(1), F(0)), ((t+qi-qj+pj)/(2*t), F(1)/(2*t)),
             ((V+qi)/t, F(1)/t)]  # intercept, minus slope
    cap = V+qi
    points = {F(0), cap}
    for alpha, beta in lines:
        if beta:
            x = alpha/beta
            if 0 <= x <= cap:
                points.add(x)
    for (a, b), (aa, bb) in product(lines, repeat=2):
        if b != bb:
            x = (a-aa)/(b-bb)
            if 0 <= x <= cap:
                points.add(x)
    breaks = sorted(points)
    for left, right in zip(breaks, breaks[1:]):
        middle = (left+right)/2
        alpha, beta = min(lines, key=lambda line: line[0]-line[1]*middle)
        if alpha-beta*middle > 0 and beta:
            peak = alpha/(2*beta)
            if left <= peak <= right:
                points.add(peak)
    return sorted(points)


effort_grid = [F(0), E/4, E/2, 3*E/4, E]
price_count = candidate_count = 0
max_price_gain = F(0)
largest_offpath_quality_gap = F(0)
price_case_digest = hashlib.sha256()
effort_count = 0
max_effort_gain = F(0)
for mobility in [F(0), F(1, 2), F(1)]:
    for access in ['00', '10', '01', '11']:
        local = accepted['segmented']['profiles'][access]
        pooled = accepted['pooled']['profiles'][access]
        base = [(1-mobility)*frac(local['b'][i])+mobility*frac(pooled['b'][i]) for i in range(2)]
        D = base[0]-base[1]
        equilibrium_effort = [F(1)/(3*c)+D/(B-2), F(1)/(3*c)-D/(B-2)]
        for effort_pair in product(effort_grid, repeat=2):
            quality = [base[i]+effort_pair[i] for i in range(2)]
            largest_offpath_quality_gap = max(largest_offpath_quality_gap, abs(quality[0]-quality[1]))
            prices = [t+(quality[i]-quality[1-i])/3 for i in range(2)]
            for i in range(2):
                j = 1-i
                cand = price_candidates(prices[j], quality[i], quality[j])
                cand.append(prices[i])
                baseline = prices[i]*demand(prices[i], prices[j], quality[i], quality[j])
                optimum = max(x*demand(x, prices[j], quality[i], quality[j]) for x in cand)
                gain = optimum-baseline
                assert gain == 0
                max_price_gain = max(max_price_gain, gain)
                price_count += 1
                candidate_count += len(cand)
                price_case_digest.update(f'{mobility}|{access}|{effort_pair}|{i}|{optimum}\n'.encode())
        for i in range(2):
            j = 1-i
            own_D = base[i]-base[j]
            # Complete global effort objective: evaluate endpoints and vertex.
            vertex = (3*t+own_D-equilibrium_effort[j])/(B-1)
            effort_candidates = [F(0), E, min(E, max(F(0), vertex))]
            def effort_profit(e):
                price = t+(own_D+e-equilibrium_effort[j])/3
                return price*price/(2*t)-c*e*e/2-k*int(access[i])
            gain = max(map(effort_profit, effort_candidates))-effort_profit(equilibrium_effort[i])
            assert gain == 0
            max_effort_gain = max(max_effort_gain, gain)
            effort_count += 1

# Exact polynomial-in-D coefficient comparison at selected rational (t,c).
# This is finite algebraic corroboration; the general identity is proved by
# substitution in L1, not inferred from these parameter settings.
polynomial_checks = []
for tt, cc in [(F(1),F(1)),(F(2),F(1)),(F(3,2),F(4,3)),(F(1),F(1,2))]:
    BB = 9*tt*cc
    ep = [F(1)/(3*cc), F(1)/(BB-2)]
    pp = [tt, BB/(3*(BB-2))]
    direct = [pp[0]**2/(2*tt)-cc*ep[0]**2/2,
              pp[0]*pp[1]/tt-cc*ep[0]*ep[1],
              pp[1]**2/(2*tt)-cc*ep[1]**2/2]
    reduced = [tt/2-F(1)/(18*cc), (BB-1)/(3*(BB-2)), cc*(BB-1)/(2*(BB-2)**2)]
    assert direct == reduced
    polynomial_checks.append({'t':tt,'c':cc,'coefficients_K_A_C':direct,'residuals':[x-y for x,y in zip(direct,reduced)]})

# Theorem P3 uses accepted alternative-outside gains; only its new comparison
# across the two institutions is calculated here.
fixed = accepted['fixed_local_leisure_pooled']
delta_fixed = frac(fixed['profiles']['10']['b'][0])-frac(fixed['profiles']['10']['b'][1])
fixed_cross_change = frac(fixed['profiles']['11']['q'][0])-frac(accepted['segmented']['profiles']['00']['q'][0])
assert delta_fixed == F(17,350) and fixed_cross_change == -F(31,450)
assert max(abs(ds),abs(delta_fixed)) == dm
assert frac(fixed['gain_against_S']) > 0 and frac(fixed['gain_against_F']) > 0

with localcontext() as ctx:
    ctx.prec = 50
    dec = lambda x: Decimal(x.numerator)/Decimal(x.denominator)
    aa, cc, kk, ddp, dds = map(dec,[A,C,k,dp,ds])
    delta0 = ((aa*aa+4*cc*kk).sqrt()-aa)/(2*cc)
    delta1 = (aa-(aa*aa-4*cc*kk).sqrt())/(2*cc)
    thresholds = {'precision_decimal_digits':50,'zero_cost_mu':-dds/(ddp-dds),
        'positive_cost_delta_0':delta0,'positive_cost_delta_1':delta1,
        'positive_cost_mu_0':(delta0-dds)/(ddp-dds),
        'positive_cost_mu_1':(delta1-dds)/(ddp-dds)}
    assert 0 < thresholds['positive_cost_mu_0'] < thresholds['positive_cost_mu_1'] < 1

reuse_summary = {}
for name in ['segmented','pooled','fixed_local_leisure_pooled']:
    row = accepted[name]
    reuse_summary[name] = {field:row[field] for field in ['gain_against_S','gain_against_F','symmetric_q_change']}

result = serial({
    'task_id':'T005_derivation',
    'status':'producer_derivation_complete_pending_independent_proof_review',
    'scope':'New global continuum proofs in theory; finite exact supporting calculations here; unchanged independent witness reused',
    'environment':{'python':sys.version,'executable':Path(sys.executable).name,'platform':platform.platform(),
                   'third_party_libraries':[], 'arithmetic':'fractions.Fraction exact; Decimal precision 50 only for threshold radicals',
                   'random_seed':None,'numerical_tolerance':None},
    'parameters':dict(M=M,h=h,l=l,o=o,v=v,w=w,d=d,k=k,t=t,c=c,E=E,V=V),
    'deltas':{'segmented':ds,'pooled':dp,'D_max':dm},
    'domain_margins':margins,
    'new_price_checks':{'selected_mobility':[F(0),F(1,2),F(1)],'selected_efforts':effort_grid,
        'unilateral_deviation_problems':price_count,'candidate_evaluations':candidate_count,
        'all_affine_pieces_exhausted_per_problem':True,'max_improvement':max_price_gain,
        'largest_offpath_quality_gap':largest_offpath_quality_gap,
        'case_digest_sha256':price_case_digest.hexdigest(),
        'limitation':'Finite selection of quality pairs; not a substitute for L1 or a proof by grid'},
    'new_effort_checks':{'unilateral_deviation_problems':effort_count,
        'global_endpoints_and_vertex_per_problem':True,'max_improvement':max_effort_gain},
    'polynomial_in_D_checks_at_rational_parameters':polynomial_checks,
    'accepted_exact_evidence_reused':reuse_summary,
    'fixed_outside_theorem':{'delta_fixed':delta_fixed,'continuation_Dmax':dm,
        'cross_institution_quality_change':fixed_cross_change,
        'within_pooled_quality_change_reused':fixed['symmetric_q_change'],
        'exact_symmetric_matching':False},
    'mobility_thresholds':thresholds,
    'known_failure_cases':[
        {'case':'w=d=0','pooled_opening_gains':'-k against either rival','status':'analytic identity'},
        {'case':'w>=2vh/Z','customer_harm':False,'status':'analytic inequality for d>=0'},
        {'case':'k>=A*delta_P-C*delta_P^2','strict_full_dominance':False,'status':'analytic inequality'},
        {'case':'prior linear demand beta=lambda=0.5','status':'preserved provisional result only; no global continuation certification; effort bound active'},
    ],
    'hashes':{'script_sha256':sha(Path(__file__)), 'theory_sha256':sha(OUT/'T005_theory.md'),
        'accepted_witness_sha256':sha(WITNESS),
        'immutable_model_sha256':sha(SNAP/'assumptions.md'),
        'immutable_review_sha256':sha(SNAP/'proof_review.md')},
})
(OUT/'T005_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':result['status'],'domain_margins':result['domain_margins'],
    'new_price_checks':result['new_price_checks'],'new_effort_checks':result['new_effort_checks'],
    'mobility_thresholds':result['mobility_thresholds']},indent=2))
