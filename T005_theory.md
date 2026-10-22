# Modular access, contributor mobility and customer quality

Derivation package, version 1.0, 22 October 2026. Producer proofs for independent scientific review. The main model and its sufficient domain are unchanged from the frozen specification. Sections 1–5 provide a self-contained compact mathematical core for the paper; Sections 6–9 supply optional boundary detail and computational provenance. None of this document asserts that its own proofs have passed independent review.

## 1. Primitives and question

Two incumbent firms already expose a maintenance module H. Each chooses S (retain that access, a_i=0) or F (also expose a functional module L, a_i=1), paying k a_i. This is an extension-of-access decision, not a choice among every proprietary or modular architecture. There are no code spillovers, wages, quotas or contributor steering. Opening can change the composition of voluntary maintenance even when the new tasks attract more total participation. The question is whether eligibility to contribute across rival codebases changes firms' access incentives while holding their symmetric outcomes fixed.

Potential contributors have mass M>0 and one unit of time each. Catchment i contains H_i, optional L_i and a distinct outside activity O_i. A mass (1−μ)M/2 can choose within each catchment; a mass μM can choose from their union, with μ∈[0,1]. Both product and outside opportunities are pooled. The two outside activities are genuine distinct opportunities, not duplicate labels for leisure. Utility from alternative r is log(b_r)+ε_r, with independent unit-scale Gumbel tastes across alternatives: Pr(ε_r≤x)=exp(−exp(−x)). Weights are h>0 for H, l>0 for L and o/2>0 for each outside activity. Every contributor selects a maximum-utility feasible alternative; ties have zero mass. Private task returns do not depend on later investment, prices or other contributors. Aggregates equal the type-distribution shares, with no aggregate uncertainty.

An H unit produces customer-valued maintenance v>0; an L unit produces w≥0. Thus z_i=v n_Hi+w n_Li. Opening L also provides a direct customer benefit d≥0. Firms observe access and contributions, simultaneously choose e_i∈[0,E], E>0, at cost ce_i²/2, c>0, and then simultaneously choose prices p_i≥0. Customers of unit mass are uniform on x∈[0,1], with utilities V+Q_1−tx−p_1 and V+Q_2−t(1−x)−p_2, or zero from nonpurchase. Here t>0 and Q_i=e_i+z_i+da_i. Profit is p_i q_i−ce_i²/2−ka_i, with k≥0. Locations and entry are sunk. No exit/monopoly continuation is part of the game. Prices, efforts and access may in principle be randomized independently; the results below specify when all Nash equilibria are degenerate or when access mixing remains possible.

## 2. Contributor allocation and the domain

Write Z=o+2h. For any feasible menu, the probability of selecting alternative r is b_r/Σb: integrating its density against the other alternatives' distribution functions gives ∫ b_r exp(−u)exp[−exp(−u)Σb]du=b_r/Σb. Therefore

    n_Hi = μMh/[Z+l(a_i+a_j)] + (1−μ)Mh/[Z+2la_i],
    n_Li = μMla_i/[Z+l(a_i+a_j)] + (1−μ)Mla_i/[Z+2la_i].             (1)

Outside participation is strictly positive. All product work is voluntary relative to the contributor's best eligible outside activity. More access weakly improves every contributor's maximized choice utility under a coupling that preserves existing tastes, but need not improve customer-valued maintenance.

Set b_i=z_i+da_i and D=b_i−b_j. At (F,S),

    δ_P = d+Mwl/(Z+l),
    δ_S = d+Ml(wZ−2vh)/[Z(Z+2l)],
    δ(μ) = μδ_P+(1−μ)δ_S.                                      (2)

At (S,F), D=−δ(μ); at symmetric profiles D=0. Define

    B=9tc, R=B/(B−2), A=(B−1)/[3(B−2)],
    C=c(B−1)/[2(B−2)²], K=t/2−1/(18c),
    D_max=max(|δ_P|,|δ_S|).

The sufficient continuation domain, denoted H, is

    B>2,  D_max+E<t,  D_max<(B−2)/(3c),
    E>1/(3c)+D_max/(B−2),  V>3t,  K−A D_max−k>0.                 (H)

These restrictions apply to every access profile and every μ, including off-equilibrium effort pairs. They are sufficient, not necessary. In particular |Q_i−Q_j|≤D_max+E<t throughout the effort box, and Q_i≥0. We do not extend the formulas to singular denominators or effort corners outside H.

## 3. Global continuation lemma

**L1 (prices and effort).** On H, every access profile and mobility value has a unique effort/price continuation, even allowing independent mixed strategies. For D=b_i−b_j it is

    e_i=1/(3c)+D/(B−2),       e_j=1/(3c)−D/(B−2),
    Q_i−Q_j=RD,              p_i=t+RD/3,
    q_i=1/2+RD/(6t),         π_i=K+AD+CD²−ka_i.                 (3)

All efforts and demands are interior; prices and profits are positive. Every customer purchases. In particular the price formula is sequentially rational after *every* effort pair, not merely at equilibrium efforts.

**Proof.** First fix any efforts and put Δ=Q_i−Q_j, |Δ|<t. Exact demand, including nonpurchase and all clipping, is

    q_i(p_i,p_j)=max{0,min{1,(t+Δ−p_i+p_j)/(2t),(V+Q_i−p_i)/t}}. (4)

A sufficiently small positive price guarantees positive demand against every nonnegative rival price, since t+Δ>0 and V+Q_i>0. Thus every equilibrium action earns strictly positive operating revenue; zero prices and prices ≥V+Q_i cannot be in equilibrium supports. Supports can consequently be taken compact, with every support point a best response (revenue is continuous).

Let U_i be firm i's maximum support price. If p_i>max{2t,U_j−t+Δ}, demand is strictly below one against all rival support prices. In every state with positive demand, a sufficiently small price cut ε increases demand by at least ε/(2t); states with zero demand cannot lose revenue. For positive-demand states the revenue gain is at least ε[p_i/(2t)−q_i]−ε²/(2t)>0. The strict upper bound on demand permits a uniform sufficiently small cut. Since expected revenue is positive, positive-demand states have positive probability. Such p_i cannot be a best response. Hence

    U_i≤max{2t,U_j−t+Δ}.

The analogous inequality for j has −Δ. If either U exceeds 2t, these two inequalities imply both U_i≤U_j−t+Δ and U_j≤U_i−t−Δ, a contradiction. Thus both supports lie in [0,2t]. Since V>3t and Q_i≥0, each firm's offer at every supported price yields strictly positive utility even at the other endpoint. Nonpurchase therefore cannot occur at any support-price pair.

For a fixed rival price r∈[0,2t], the exact covered-demand revenue p·clip((t+Δ+r−p)/(2t),0,1) has a unique peak at m_i(r)=(t+Δ+r)/2∈(0,2t). On the possible full-demand segment revenue is increasing; its endpoint r+Δ−t lies strictly below m_i(r), because r+Δ<3t. On the interior-demand segment revenue is a strictly concave quadratic, and beyond zero demand it is zero. Revenue increases up to the peak and decreases thereafter until zero. Consequently every best response to a rival distribution lies between m_i(L_j) and m_i(U_j), where L_j is its minimum support price. (A price outside these bounds is improved by moving toward them, strictly on a positive-revenue set.) Thus U_i−L_i≤(U_j−L_j)/2, and conversely for j. Both widths are zero. The resulting pure equilibrium cannot have demand zero or one, since both firms guarantee positive revenue. Its two interior FOCs yield p_i=t+Δ/3 and q_i=1/2+Δ/(6t).

Existence and global optimality also follow directly: each candidate rival price is less than 4t/3 and alone covers all customers, even after any unilateral price deviation. Its best response is the unique quadratic peak just derived. Equation (4) covers all prices, including deviations that eliminate demand. Customer indifference occurs only at a single x and does not change aggregate demand.

Substitute this unique price continuation into effort profits. Apart from the fixed access cost, firm i maximizes [t+(D+e_i−e_j)/3]²/(2t)−ce_i²/2 on [0,E]. Its own second derivative is 1/(9t)−c<0, and its global best response is

    BR_i(e_j)=clip((3t+D−e_j)/(B−1),0,E).

The joint response map is a contraction in the sup norm, with constant 1/(B−1)<1, so there is exactly one pure equilibrium. Against a distribution of rival effort the expected objective remains strictly concave, giving a unique best response, so nondegenerate mixed equilibria cannot exist. Solving the interior response equations gives (3); H places those efforts strictly inside [0,E], so they are the unique fixed point. Algebraic substitution gives the stated profit. Finally π_i≥K−A D_max−k>0. This verifies operating participation on the stated sunk-entry benchmark without claiming an entry/exit equilibrium. ∎

## 4. Matched allocations and strict reversal

**P1 (exact symmetric matching).** At a symmetric access profile (a,a), for every μ,

    n_Hi=Mh/(Z+2la),  n_Li=Mla/(Z+2la).

Hence contributions, outside participation, efforts, quality, prices and profits at each of (S,S) and (F,F) are identical across mobility institutions. The asymmetric pre-effort quality advantage is (2).

**Proof.** When a_i=a_j, the two denominators in (1) coincide, so μ cancels. For (F,S), pooled H contributions are equal across firms, leaving d+Mwl/(Z+l) as their quality difference. Segmented contributions yield d+M(vh+wl)/(Z+2l)−Mvh/Z=δ_S. The mixture is affine in μ. Apply L1. ∎

**P2 (strict incentive reversal with lower customer quality).** Suppose H holds and

    δ_S<0<δ_P,       0≤k<Aδ_P−Cδ_P².                            (R)

Then the segmented institution μ=0 has unique access equilibrium (S,S), and the pooled institution μ=1 has unique access equilibrium (F,F), each in strict dominant strategies. These are unique subgame-perfect firm outcomes even allowing mixed strategies. Pooled equilibrium customer quality and customer surplus are lower by −δ_S>0; internal effort and prices are unchanged. Profit per firm falls by k, strictly if k>0. Total active contribution rises.

**Proof.** Given the rival's S or F respectively, gains from opening are

    g_S(δ)=Aδ+Cδ²−k,       g_F(δ)=Aδ−Cδ²−k.                    (5)

These expressions compare all four access deviations using (3). On H, |δ|≤D_max<A/(2C)=(B−2)/(3c). If δ=δ_S<0, A+Cδ>A/2>0, so g_S<0, and g_F<0 too. If δ=δ_P>0, (R) gives g_F>0 and g_S≥g_F>0. Strict dominance excludes every alternative pure or mixed access equilibrium.

At either symmetric profile, (3) gives e_i=1/(3c), p_i=t, q_i=1/2 and π_i=K−ka_i. By P1 the quality change from (S,S) to (F,F), across or within institutions, is d+M(vh+wl)/(Z+2l)−Mvh/Z=δ_S. Customers keep the same choices and prices, so each customer's net utility, and therefore aggregate consumer surplus, changes by δ_S. Total active contribution is M(2h+2la)/(Z+2la); its increase is 2Mlo/[Z(Z+2l)]>0. Thus more participation coexists with less customer-valued maintenance. ∎

The strategic force is inherited relative-performance business stealing: opening can damage the rival more than the opener. The specific consequence here comes from voluntary sorting into additional modules across competing codebases. Symmetric matching isolates this cross-codebase channel from within-project dilution, which already exists under segmentation. It relies on proportional menu shares and pooling both genuine outside opportunities; it is not a generic property of mobility.

## 5. Nonempty region and a fixed-outside boundary

The strict domain is explicit: positive M,h,l,o,v,t,c,E,V; nonnegative w,d,k; and H plus R. Its strictly positive-w,d,k part is open in the ordinary Euclidean parameter space, because all denominators are positive and every displayed inequality is strict. It is nonempty: take M=h=l=o=v=t=c=1, w=1/10, d=1/50, k=1/200, E=3/5, V=4. The already independently computed exact witness has δ_S=−7/75 and δ_P=9/200. The continuation margins are B−2=7, t−D_max−E=23/75, (B−2)/(3c)−D_max=56/25, E−1/(3c)−D_max/(B−2)=19/75, V−3t=1, and K−AD_max−k=727/1800. The strict pooled-opening margin is 5869/490000. Thus the result is not tied to a single isolated parameter point.

At this witness, the already computed opening gains (against S, against F) are (−1793/45000,−619/15000) when segmented and (6031/490000,5869/490000) when pooled. Per-firm community maintenance moves from 1/3 to 11/50, while total active contribution moves from 2/3 to 4/5. Effective customer quality falls by 7/75 after the positive direct access benefit. These exact values are reused from the frozen independent calculation; they are not newly represented as an independent replication by this producer.

**P3 (fixed outside opportunity; matching lost, reversal survives).** A separate institution keeps one outside alternative of weight o/2 eligible for each contributor, even after access to both product catchments is allowed. Let Z*=2h+o/2 and δ*=d+Mwl/(Z*+l). Replace D_max in H by D*=max(|δ_S|,|δ*|). If δ_S<0<δ*, k<Aδ*−Cδ*², and

    d+M(vh+wl)/(Z*+2l)−Mvh/Z<0,                               (F)

then segmented (S,S) and pooled (F,F) are again the unique access equilibria, and the latter has lower customer quality. Symmetric allocations across institutions are generally different.

**Proof.** In this institution, local shares are unchanged. Pooled shares have denominator Z*+l(a_i+a_j), so asymmetric H outputs still cancel, giving δ*. The same continuation lemma and access-gain argument apply with D*. The actual cross-institution symmetric quality change is precisely the left side of (F); efforts and prices remain the same at symmetric profiles. This proves the result on the stated inequality domain, rather than merely evaluating a witness. At the witness, δ*=17/350<D*=7/75, so the original continuation margins apply; the reused exact pooled gains are 493261/36015000 and 479389/36015000. The cross-institution quality change in (F) is −31/450. The within-pooled-institution change is instead −61/450: these comparisons must not be conflated. All strict inequalities persist in an open neighborhood. ∎

This boundary removes the expansion of outside menus while retaining reversal; it deliberately abandons exact symmetric matching. It does not establish robustness to arbitrary taste correlation, endogenous contributor entry or alternative product-demand slopes.

## 6. Optional mobility corollary, including every access equilibrium

This section is dispensable for the main two-proposition paper. It is fully derived for the original institution under H and R. Write s=δ_P−δ_S>0. The signs of (5) completely determine access behavior, with δ=δ_S+μs. Both gains are strictly increasing in δ on [δ_S,δ_P], since their derivatives are A±2Cδ>0.

For k=0 define μ_0=−δ_S/s∈(0,1). For μ<μ_0, S is strictly dominant; for μ>μ_0, F is strictly dominant. At μ=μ_0 all four pure profiles and every independent mixed-strategy pair are equilibria, since both opening gains vanish. This last statement is stronger and more precise than saying only that every pure profile is a weak equilibrium.

For k>0 define

    δ_0=[sqrt(A²+4Ck)−A]/(2C),
    δ_1=[A−sqrt(A²−4Ck)]/(2C),
    μ_r=(δ_r−δ_S)/s, r=0,1.

The radical in δ_1 is real: k<Aδ_P−Cδ_P²<A²/(4C). Monotonicity and R imply 0<δ_0<δ_1<δ_P and 0<μ_0<μ_1<1 (here μ_0 denotes the cost-adjusted threshold associated with δ_0). With x_i the probability that firm i opens:

| Mobility | All access equilibria (x_1,x_2) |
|---|---|
| μ<μ_0 | (0,0) only |
| μ=μ_0 | {(0,x):x∈[0,1]} ∪ {(x,0):x∈[0,1]} |
| μ_0<μ<μ_1 | (1,0), (0,1), and (x*,x*) only |
| μ=μ_1 | {(1,x):x∈[0,1]} ∪ {(x,1):x∈[0,1]} |
| μ>μ_1 | (1,1) only |

Here x*=g_S(δ)/[2Cδ²]∈(0,1). To verify exhaustiveness, a firm's opening gain against rival opening probability x is g_S−2Cδ²x. In the intermediate interval, mixing requires x=x*, giving either the two strict asymmetric profiles or the single fully mixed profile. At either threshold the same linear expression yields exactly the listed edges. Below/above the thresholds dominance excludes other profiles. Correlated equilibria are not asserted or enumerated.

## 7. Limits and known failures

- Productivity alignment: if w≥2vh/Z, the symmetric maintenance change Ml(wZ−2vh)/[Z(Z+2l)] is nonnegative. Adding d≥0 cannot restore customer harm. More generally harm requires d<Ml(2vh−wZ)/[Z(Z+2l)]. This is a customer-productivity condition, not a judgment that volunteers value the wrong activities.
- At w=d=0, δ_P=0 and both pooled opening gains are exactly −k; strict full dominance fails (at k=0 contributors can be diverted without creating a private relative advantage). This is distinct from a singular task weight: w=0 is allowed, whereas h,l,o must remain strictly positive.
- As M→0 or l→0, the contributor-generated wedge δ_P−δ_S tends to zero; if d stays positive, direct access benefits remain. At the actual zero limit the logit formulation with l=0 is interpreted as deleting the task, not taking log(0). As o→∞ the contribution effects vanish; a positive d can remove harm. At k≥Aδ_P−Cδ_P² strict full dominance fails. A large d removes harm. These limits do not assert continuation validity after H fails.
- Mixed and asymmetric access equilibria in Section 6 are real selection boundaries. They must not be replaced by a unique symmetric outcome at all mobility levels.
- The earlier supplementary linear-demand calculation at own/rival slope parameters β=λ=0.5 had effort-bound activity and failed strict full dominance; it reported both symmetric access equilibria. Its discarded unconstrained effort values exceeded E. That demand model still lacks a global clipped-demand/nonpurchase proof and is excluded from the theorem and robustness claim. The present proof does not upgrade those provisional numerical conclusions. The fixed-outside theorem is the one focused robustness result used here.
- H excludes B≤2, zero or insufficient effort capacity, reservation values too low for this proof, and quality gaps reaching t. No equilibrium or nonexistence statement is made for those excluded cases. The positive-profit condition is only a sufficient sunk-entry participation check.

Contributor utility, customer surplus and firm profit are different objects. Enlarging a feasible menu weakly benefits the contributor for each fixed taste realization, even if customers lose. Outside-activity utility also matters. No total-welfare, socially optimal access, governance remedy, calibrated closed-source recommendation or profit-maximizing merger conclusion follows. The business-stealing logic is inherited; the restricted modular task-composition consequence and matched institutional comparison delimit the contribution. The previously reviewed eight-work positioning is reused without new novelty or literature-completeness claims.

## 8. Reproducible calculations and evidence boundaries

Run `T005_validation.py` with Python 3.12 (standard library only). It writes `T005_results.json` alongside itself. It imports the unchanged independent rational witness as evidence, rather than rerunning that review. Its new checks (i) calculate exact H margins relevant to the proofs; (ii) exhaust all pieces of the unilateral price-deviation objective for rational quality pairs generated at selected effort pairs, including corners; (iii) maximize each selected effort-deviation quadratic exactly over [0,E]; (iv) use polynomial coefficient identities for the effort-stage reduction; and (v) calculate the optional mobility thresholds and fixed-outside cross-institution comparison. Enumeration is exhaustive over each selected one-dimensional deviation problem, but finite coverage of parameter/effort pairs remains corroboration, not the proof of L1 on its continuum domain. L1 supplies that proof. No random draws, simulated data, optimizer convergence or grid density supports a general claim.

The script records arithmetic, interpreter, script/theory/input hashes, case counts, exact maximum deviation gains, and numerical precision for radical thresholds. Immutable inputs and final artifacts are pinned in `T005_claim_ledger.json`. The ledger hashes the theory (containing the frozen primitives and domains), validation script, result file and accepted evidence; it does not attempt a circular self-hash. `T005_support/freeze.py` creates the ledger and task receipt after validation and is a packaging helper, not mathematical evidence.

## 9. Production record and paper compression

The global price argument, including mixed-support exclusion, and global bounded-effort argument are new work in this task. The contributor allocation algebra and rational feasibility witness were already prepared and independently checked at the prior gate; they are restated self-contained here because review history cannot substitute for a paper's argument. The fixed-outside claim is now an inequality-domain theorem using the same continuation proof, with previously checked rational gains reused. No primitives or domain inequalities were tightened or changed. SymPy was probed but unavailable; the final script therefore uses only standard-library exact arithmetic. No package installation, external research, paid service, empirical collection or submission occurred.

For the eight-page manuscript: retain primitives, H, L1, P1/P2 and their complete compact proofs; give the fixed-outside comparison in one paragraph with its short algebraic proof and the strict witness. The access-threshold classification is optional and can be omitted entirely instead of moving essential proof outside the page cap. Integrate the common notation and avoid reproducing the extended provenance and failure inventory verbatim. Main scientific proof material must still count toward the eight pages; no separate proof-appendix exemption is presumed. The technical artifact's length is not a claim that a rendered paper already fits. Requested execution was gpt-6-astra/high; actual provider model/effort and token counts are not independently exposed to this worker. Fresh independent proof review is the next scientific step; no user action is needed.
