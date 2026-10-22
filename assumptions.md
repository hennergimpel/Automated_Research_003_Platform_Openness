# Model specification: modular access and contributor mobility

Version 0.1, 22 October 2026. Proposed model for independent review and full derivation. All formulas below are producer derivations, not reviewed propositions. The exact task outputs and calculations are described in the companion feasibility report.

## Economic setting and primitives

Two incumbent software/service firms, indexed i in {1,2}, serve differentiated customer needs. Each already exposes a maintenance-critical module H. Its additional module L is initially closed but functional. The firm chooses selective access S (H open, L closed) or full access F (both open). Let a_i=0 denote S and a_i=1 denote F. This is the marginal access decision of an existing open-core business, not a model of all four proprietary/core/edge/full strategies or new market entry. Firms cannot pay, ration or redirect volunteers in the base model. Licensing and cross-codebase reuse are held fixed; no spillover or coordination penalty is required for the mechanism.

Primitive parameters are:

| Symbol | Domain and meaning |
|---|---|
| M | M>0, total mass of potential volunteers, each with one unit of available time |
| h,l,o | Strictly positive attractiveness weights for each H task opportunity, each L opportunity, and the two outside opportunities together |
| v,w | v>0, w>=0; customer-facing maintenance produced by one volunteer unit in H or L. Do not assume w<v globally. |
| mu | [0,1], fraction of volunteers able to move between the two opportunity catchments |
| d | d>=0, direct customer utility gain from access to L, holding maintenance fixed |
| k | k>=0, fixed cost of exposing L; the access-ranking reversal does not require k>0 |
| t | t>0, horizontal product differentiation |
| c | c>0, quadratic internal-effort cost coefficient |
| E | E>0, feasible upper bound on internal maintenance effort |
| V | Common customer reservation value, with sufficient covered-market domain specified below |

No randomness affects aggregate output. A continuum of contributor preference types has the stated product distribution; firms know this distribution. A contributor knows their own type. Firms observe access and aggregate contributions, then effort and prices. Contributor task returns do not respond to subsequent prices or internal effort. This isolates short-run task preference and rules out dynamic contributor entry, endogenous wages, signaling and quality-driven reciprocal participation.

### Contributor institution and outside alternatives

There are two genuine opportunity catchments. Catchment i contains H_i, optional L_i if a_i=1, and a distinct outside activity O_i. The outside activities produce no quality for either product. They can be interpreted as work on unrelated projects, not two labels for the same leisure choice. Mobile volunteers, mass mu*M, can choose from the union of both catchments. Immobile volunteers, mass (1-mu)*M/2 assigned to each catchment, choose within it. Thus total potential time remains M for every mu. Access rights and eligibility for both product and outside tasks define this mobility institution.

For each feasible alternative r, contributor type epsilon receives utility log(b_r)+epsilon_r, where b_H=h, b_L=l and b_O=o/2. The epsilon_r are independent with CDF exp(-exp(-x)), unit scale. Each contributor chooses one utility-maximizing feasible alternative. Ties have measure zero; any tie convention gives the same aggregates. Relative to their best available outside activity, contributors work on an H/L module only if doing so weakly improves their utility. No participation is forced, no closed module receives effort, and a positive mass takes an outside option for o>0. Total active contribution is endogenous despite fixed potential mass M.

The choice probability is b_r divided by the sum of available b weights. This can be derived directly: integrate the density of log(b_r)+epsilon_r at u against the probability that every alternative has utility below u. The integrand is b_r*exp(-u)*exp[-exp(-u)*sum b], whose integral is b_r/sum b. This specifies optimizing behavior rather than an arbitrary assignment rule. It remains a restrictive random-utility model, especially its independent module tastes and proportional substitution.

**Matching interpretation:** At mu=0 each local menu has outside weight o/2. At mu=1 there are two unchanged outside activities, total weight o. No outside utility parameter is changed between regimes. Pooling therefore expands outside as well as product opportunities. A comparison allowing cross-product movement while retaining exactly one common outside opportunity is a different institution and loses exact symmetric matching; it is a proposed robustness check, not quietly treated as equivalent.

## Timing, actions and payoffs

1. The two incumbents simultaneously choose a_i in {0,1}, committing access and paying k*a_i.
2. Volunteers choose a feasible task or outside activity; contributions become available and are publicly observed.
3. Firms simultaneously choose internal effort e_i in [0,E], at cost c*e_i^2/2.
4. Firms simultaneously choose prices p_i>=0 for their differentiated software/service offerings.
5. Customers choose firm 1, firm 2 or nonpurchase (utility zero).

Customers are a unit mass uniformly distributed on x in [0,1], with firms located at 0 and 1. Define maintenance increment z_i=v*n_Hi+w*n_Li and effective customer quality Q_i=e_i+z_i+d*a_i. Customer utilities are V+Q_1-t*x-p_1 and V+Q_2-t*(1-x)-p_2. The direct benefit d can represent inspectability/customization access; it is distinct from maintenance quality z_i. Marginal service cost is normalized to zero. Profit is p_i*D_i-c*e_i^2/2-k*a_i, where D_i is demand determined by these choices and the nonpurchase option.

The incumbents' entry commitments and product locations are sunk; entry/exit and monopoly continuations are outside this model. Zero is the operating participation benchmark. The proposed domain ensures positive continuation profits in every access profile, so an equilibrium is not supported by negative-profit forced participation. This participation check does not claim to solve an endogenous entry game.

The equilibrium concept is backward-induction equilibrium of the finite access game and simultaneous effort/price subgames, together with utility-maximizing choices for almost every contributor and customer type. Private contributor tastes have no strategic interdependence or aggregate uncertainty, so the firms face a deterministic continuation game. A strict dominant access strategy entails no selection assumption. At thresholds or outside the strict region, retain all pure/mixed access equilibria rather than imposing symmetry.

## Allocation and the exactly matched benchmark

Let Z=o+2h. Summing mobile and immobile choices gives

    n_Hi = mu*M*h/[Z+l(a_i+a_j)] + (1-mu)*M*h/[Z+2l*a_i],
    n_Li = mu*M*l*a_i/[Z+l(a_i+a_j)] + (1-mu)*M*l*a_i/[Z+2l*a_i].       (1)

Outside mass is M-sum_i(n_Hi+n_Li), strictly positive. At either symmetric profile a_1=a_2=a, (1) reduces to n_Hi=M*h/(Z+2la), n_Li=M*l*a/(Z+2la), independently of mu. Thus the benchmark matches **both** S/S and F/F maintenance, participation, effort, prices and profits, not merely one baseline point. The product payoff primitives and individual opportunity weights are the same. Only the opportunity eligibility institution changes.

Let b_i=z_i+d*a_i, and define the pre-internal-effort quality difference D=b_i-b_j. At F/S, define

    delta_P = d + M*w*l/(Z+l),
    delta_S = d + M*l*(w*Z-2*v*h)/[Z*(Z+2l)],
    delta(mu) = mu*delta_P + (1-mu)*delta_S.                            (2)

Subscripts P and S here mean pooled and segmented, not proprietary and selective. To avoid ambiguity in the eventual manuscript, spell out the institution labels. At S/S and F/F, D=0; at F/S, D=delta(mu); at S/F, D=-delta(mu).

The pool gives the two already-open H modules identical contribution levels even after an asymmetric opening. Their quality effects cancel in the product-quality difference. Only the new L output remains, M*w*l/(Z+l). This cancellation is the source of the competitive wedge, not an imposed cost of openness. With segmentation the firm bears all of its own task substitution and cannot divert rival maintenance.

## Interior candidate continuation and sufficient domain

Set B=9tc, R=B/(B-2), A=(B-1)/[3(B-2)], C=c(B-1)/[2(B-2)^2], and K=t/2-1/(18c). Set Dmax=max(|delta_P|,|delta_S|), which bounds all mu in [0,1]. Use the following conservative domain for the main theorem:

    B>2;
    Dmax+E<t;
    Dmax<(B-2)/(3c);
    E>1/(3c)+Dmax/(B-2);
    V>3t;
    K-A*Dmax-k>0.                                                     (3)

The second inequality bounds quality differences even after any effort deviation in [0,E], not only at the candidate equilibrium. The next two keep equilibrium efforts strictly inside their bounds. The last is a sufficient participation condition for every access profile. These restrictions are nonempty at the witness in the feasibility report; they are not maximal or necessary conditions.

For a given effort pair, the covered-market interior candidate prices are

    p_i=t+(Q_i-Q_j)/3,   D_i=1/2+(Q_i-Q_j)/(6t).

Substituting these prices into profit yields p_i^2/(2t)-c*e_i^2/2-k*a_i. The effort FOCs yield the candidate

    e_i=1/(3c)+D/(B-2),  e_j=1/(3c)-D/(B-2),
    Q_i-Q_j=R*D,
    p_i=t+R*D/3,
    pi_i=K+A*D+C*D^2-k*a_i.                                          (4)

The effort objective has second derivative 1/(9t)-c<0; the reaction system has positive eigenvalues under B>2. These facts support global effort optimization once the price continuation is proved throughout the effort box. At the proposed price equilibrium the rival alone gives each customer a nonnegative option under (3), so any unilateral price deviation has fully covered, possibly clipped demand. The next derivation task must finish the global price argument and rule out other price equilibria including boundary/nonpurchase cases; finite deviations are only supporting evidence. Do not treat FOCs as the final proof of subgame perfection.

## Provisional proposition ledger

**P1: Matching and mobility wedge.** Under the primitives, (1) holds, and all symmetric-profile allocations are invariant to mu. The access-induced quality difference is (2). The own-project dilution is present even at mu=0. Proof route: individual choice integral, aggregation, then substitution in all four profiles. No numerical evidence is needed for the algebra; independent review remains pending.

**P2: Strict access reversal and lower customer quality.** Under (3), suppose

    delta_S<0<delta_P,   0<=k<A*delta_P-C*delta_P^2.                    (5)

Then the candidate continuation predicts unique S/S with segmentation and unique F/F with complete pooling, each in strict dominant access strategies. A positive d is permitted. The candidate F/F outcome has lower effective customer quality than S/S, the same internal effort 1/(3c), the same price t, and lower profit by k (strict when k>0). Consumer surplus falls by -delta_S>0. No total-welfare statement is implied.

Proof route: full-opening gains against S and F are, respectively,

    g_S=A*delta+C*delta^2-k,     g_F=A*delta-C*delta^2-k.               (6)

The reduced payoff is strictly increasing in D on (3). At delta_S<0 both gains are negative for k>=0. At delta_P>0, (5) makes both positive. Symmetric net quality difference F/F minus S/S equals delta_S by (1), even though that is not the asymmetric pooled difference. Hence the same inequality that makes additional opening unattractive under segmentation also gives lower symmetric customer quality under pooling. Equation (6) establishes all four access deviations once (4) is proved globally. This is not a numerical equilibrium-selection result.

**P3, optional short corollary: mobility threshold and boundary.** In the P2 region delta(mu) strictly increases with mobility. With k=0, its sign switches at mu0=-delta_S/(delta_P-delta_S); below it S is dominant and above it F is dominant. At equality all access profiles are weak equilibria. For k>0, thresholds solve g_S=0 and g_F=0. A narrow intervening region may have both asymmetric pure equilibria and a mixed equilibrium; do not jump directly from S/S to F/F or assert uniqueness there. Define the mixed equilibrium from the full two-by-two payoff matrix if reported. At w>=2vh/Z, symmetric maintenance cannot fall even before adding d; large outside attractiveness o weakens the dilution. General formulas apply even when (5) fails, but the theorem does not.

## Scope, falsifiers and next proof obligations

1. Derive and check the entire price subgame on the effort box, including nonpurchase, clipping, large price deviations, ties and uniqueness. If (3) is insufficient, tighten a nonempty domain rather than extrapolate an interior solution.
2. Verify effort best responses globally and the bounded domains algebraically; do not silently extend to unbounded effort, singular B=2 or effort corners.
3. Prove P1 and P2 from primitives and exhibit an open parameter region, not just the single witness. Reconcile every inequality with the actual access costs and timing.
4. Explain the matching restriction involving outside catchments. Compare the fixed-single-outside institution separately; do not rename it exact matching.
5. Test one source of substantive fragility: strict own/rival demand slopes, more correlated module tastes, or a priority-steering technology. The numerical strict-slope exercise is promising but has not checked all global deviations. It should not expand into an unbounded general model.
6. Bound the contribution against the eight read sources and the standard business-stealing interpretation. Relative-performance incentives are inherited; the proposed addition is the exact symmetric-match reversal generated by modular access and priority mismatch.
7. Boundary inventory: M or l tending to zero removes the contribution wedge; w=0 and d=0 gives delta_P=0 and no strict full-opening gain; k beyond (5) defeats full dominance; d large enough removes customer harm; large o can remove dilution; w high can improve quality. mu endpoints are allowed. h,l,o must remain positive for the log specification; zero values are limits, not logarithms evaluated at zero. No claims on c/E boundaries until solved.

Welfare accounting would have to include customers, firms, contributors and outside activity returns. New opportunities weakly benefit individual choice utility, so customer harm and firm profit loss do not establish social inefficiency. At most describe the result as lower customer-facing maintenance and a competitive access incentive. A claim that a single profit-maximizing owner would choose differently requires a separate monopoly/merger model. The existing model supports only the simpler comparison with an administrator maximizing maintenance quality.
