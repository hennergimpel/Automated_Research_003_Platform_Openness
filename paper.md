# Opening the Wrong Work: Contributor Mobility and Software Maintenance Competition

## Abstract

Opening more software modules gives volunteers more ways to contribute, but the work they prefer need not deliver the maintenance customers value. We model two firms that already expose a maintenance module and choose whether to expose an additional module. Contributors voluntarily select tasks or outside activities; firms then choose internal effort and prices. Comparing segmented and pooled opportunity sets, we hold the allocations at both symmetric access profiles exactly fixed. On an explicit nonempty open parameter region, selective access is strictly dominant under segmentation, whereas expanded access is strictly dominant under pooling. The pooled equilibrium has more active contribution but lower customer quality and surplus, with unchanged internal effort and prices. The mechanism is access-induced diversion of high-value maintenance across rival codebases. A separate fixed-outside-opportunity theorem retains reversal while losing exact matching. The result concerns technical eligibility in already-open codebases, with fixed licensing and no code spillovers; it does not establish a total-welfare loss or a general recommendation to restrict access.

## Introduction

Opening more of a software product gives contributors more ways to help. It does not ensure that the additional work improves the maintenance customers need. A firm may already expose a maintenance-critical module while considering access to a second module with attractive tasks but lower customer value. Contributors choose tasks for their own reasons; the firm sells the resulting product. When the same contributors can work on competing codebases, extending access can also divert maintenance from a rival. Can this competitive effect induce both firms to expand access even though both products become worse for customers?

This is an information systems question about the interaction between technical access and decentralized maintenance governance. The technical choice determines which modules people can modify. The organizational arrangement determines whose opportunity sets overlap and whether firms can direct their work. We isolate voluntary task selection without wages, quotas or priority steering. Contributors optimize private returns, whereas customers value maintenance output. The title's “wrong work” refers to this customer-productivity mismatch, not to a failure of contributors to pursue their own objectives.

Mallipeddi et al. (2024) connect openness to maintenance investment and product competition, treating community effort as an input whose effectiveness depends on access strategy. We instead make module-level work and contributor allocation explicit. Our contribution is a matched strategic comparison: changing contributor eligibility reverses firms' strict access incentives while leaving the allocation at each symmetric access profile unchanged. With separate contributor catchments, retaining selective access is strictly dominant. With pooled catchments, extending access is strictly dominant. The resulting pooled equilibrium has more participation but lower customer quality and surplus. A nonempty open parameter region supports this result, including positive maintenance productivity, direct customer benefits from access and opening costs.

The mechanism uses familiar relative-performance business stealing. A firm opens because the new tasks divert valuable maintenance from its competitor as well as from itself. Its relative position can improve despite an absolute loss. The specific result concerns modular task composition and a tightly specified opportunity institution. It does not establish that openness usually harms quality, that partial access is generally optimal, or that restricting access raises social welfare. We provide complete continuation and access arguments, an exact illustration, and a separate fixed-outside-opportunity boundary.

## Related Research and Contribution Boundary

The seed's maintenance game provides the closest IS benchmark. Mallipeddi et al. (2024) jointly analyze access, internal maintenance and prices, with community effectiveness, coordination costs and passive spillovers. Their conditional exclusion of partial openness in a favorable-demand regime is not a universal conclusion; adverse-demand cases already admit partial access. Our model is related to theirs rather than a nested extension: it studies expanding an already-open codebase, fixes licensing, excludes code spillovers and uses a covered horizontal-differentiation market. It does not solve the seed's full proprietary/core/extension/full choice set or overturn its results.

Modular access and endogenous contributions are established ideas. Casadesus-Masanell and Llanes (2011) analyze core/extension access with adoption, complementarity and user innovation; our modules contribute additive maintenance to an already-functional product. August et al. (2013) model originator and commercial-contributor investment with service competition. August et al. (2018) show how licensing and service-market structure affect investment and value creation, including attention to noncommercial contributors. August et al. (2021) analyze strategic contribution among three firms with sequential investment and licensing-dependent cross-quality effects. These studies make endogenous effort and strategic responses central. Our distinction is voluntary sorting across separate rival codebases induced by technical task eligibility while appropriation rules remain fixed.

Kumar et al. (2011) connect product competition to a developer market with wages and signaling, and distinguish functionality from usability. Thus competition for developers and a gap between developer activity and customer quality are not new. We remove the hiring and signaling market to identify an access-induced task-allocation channel. Soundy et al. (2021) formally study finite contributor budgets allocated across public projects, with strategic reward and completion effects; they also show that pure equilibrium need not exist generally. Our smooth aggregate allocation follows from specified private random utilities, not an assumed general existence result. Finally, Athey and Ellison (2014) model evolving contributor populations and quality. Their dynamic feedback motivates our boundary: a fixed potential contributor population and static private returns are short-run restrictions. Elastic entry or quality-dependent task returns could change the result. Across these eight works, the incremental claim is the matched reversal in maintenance competition, not the invention of scarce attention, modular access or strategic contribution.

## Model and Admissible Domain

Two incumbent firms, indexed by $i,j\in\{1,2\}$, already expose maintenance module $H$. Each simultaneously chooses selective access $S$ ($a_i=0$) or full access $F$ ($a_i=1$), adding access to a functional module $L$ at cost $ka_i$. “Full” means both modeled modules. Entry and locations are sunk; there is no exit or monopoly continuation. There are no wages, code spillovers or contribution quotas. Licensing and task productivity do not change with access.

A mass $M>0$ of potential contributors each has one unit of time. Catchment $i$ contains $H_i$, $L_i$ if open, and an outside activity $O_i$. A mass $(1-\mu)M/2$ can choose within each catchment; a mass $\mu M$ can choose from their union, where $\mu\in[0,1]$. Both codebases and both outside opportunities are pooled. The outside activities are genuinely distinct opportunities, not duplicate labels for the same leisure option. This proportional menu institution is chosen to match symmetric allocations exactly; it is not a generic definition of mobility.

Utility from feasible alternative $r$ is $\log b_r+\varepsilon_r$, with independent unit-scale Gumbel tastes, $\Pr(\varepsilon_r\leq x)=\exp[-\exp(-x)]$. Weights are $h>0$ for each $H$ task, $l>0$ for each open $L$ task, and $o/2>0$ for each outside activity. A contributor chooses a utility maximum, with zero-mass ties. Private returns are independent of subsequent investment, prices and others' contributions. Aggregates equal distributional shares, with no aggregate uncertainty. Integrating the density of one alternative against the other distribution functions gives $\int b_r e^{-u}\exp[-e^{-u}\sum_s b_s]du=b_r/\sum_s b_s$. Writing $Z=o+2h$, the implied contributions are

$$n_{Hi}=\frac{\mu Mh}{Z+l(a_i+a_j)}+\frac{(1-\mu)Mh}{Z+2la_i},\qquad n_{Li}=\frac{\mu Mla_i}{Z+l(a_i+a_j)}+\frac{(1-\mu)Mla_i}{Z+2la_i}.\tag{1}$$

Outside participation is strictly positive; no contributor is assigned work involuntarily. Opening adds an alternative and weakly raises maximized contributor utility when existing tastes are coupled across menus. This fact does not imply a customer-quality improvement.

An $H$ unit generates customer maintenance value $v>0$, an $L$ unit value $w\geq0$, and opening generates direct customer benefit $d\geq0$. Set $z_i=vn_{Hi}+wn_{Li}$. After access and contribution, firms observe the allocation and simultaneously choose internal effort $e_i\in[0,E]$, $E>0$, costing $ce_i^2/2$, $c>0$. They then simultaneously choose prices $p_i\geq0$. Unit-mass customers are uniform on $x\in[0,1]$ and choose among utilities $V+Q_1-tx-p_1$, $V+Q_2-t(1-x)-p_2$ and nonpurchase utility zero, with $t>0$ and $Q_i=e_i+z_i+da_i$. Profit is $p_iq_i-ce_i^2/2-ka_i$, $k\geq0$. Firms may independently mix at each stage; the endpoint results below exclude nondegenerate mixing.

Let $b_i=z_i+da_i$ and $D=b_i-b_j$. At $(F,S)$ the opening firm's pre-effort advantage is

$$\delta_P=d+\frac{Mwl}{Z+l},\quad \delta_S=d+\frac{Ml(wZ-2vh)}{Z(Z+2l)},\quad \delta(\mu)=\mu\delta_P+(1-\mu)\delta_S.\tag{2}$$

At $(S,F)$ the gap is $-\delta(\mu)$; symmetric gaps are zero. Define $B=9tc$, $R=B/(B-2)$, $A=(B-1)/[3(B-2)]$, $C=c(B-1)/[2(B-2)^2]$, $K=t/2-1/(18c)$, and $D_{\max}=\max(|\delta_P|,|\delta_S|)$. Our sufficient continuation domain $\mathcal H$ is

$$B>2,\quad D_{\max}+E<t,\quad D_{\max}<\frac{B-2}{3c},\quad E>\frac1{3c}+\frac{D_{\max}}{B-2},\quad V>3t,\quad K-AD_{\max}-k>0.\tag{H}$$

These conditions hold uniformly over access profiles, mobility and all off-path effort pairs. They ensure $|Q_i-Q_j|<t$ throughout the effort box and nonnegative quality. They are sufficient rather than necessary. We make no equilibrium claim for excluded effort corners, low reservation values or singular denominators.

## Equilibrium Continuation

**Lemma 1.** On $\mathcal H$, every access profile and mobility value has a unique effort/price continuation, including among independent mixed strategies. With $D=b_i-b_j$,

$$\begin{aligned}e_i&=\frac1{3c}+\frac D{B-2},\quad e_j=\frac1{3c}-\frac D{B-2},\quad Q_i-Q_j=RD,\\p_i&=t+\frac{RD}{3},\quad q_i=\frac12+\frac{RD}{6t},\quad \pi_i=K+AD+CD^2-ka_i.\end{aligned}\tag{3}$$

Efforts and demands are interior, prices and profits positive, and all customers purchase. The price continuation is sequentially rational after every effort pair.

**Proof.** Fix arbitrary feasible efforts and write $\Delta=Q_i-Q_j$, so $|\Delta|<t$. Demand at arbitrary nonnegative prices, including nonpurchase and clipping, is

$$q_i(p_i,p_j)=\max\left\{0,\min\left\{1,\frac{t+\Delta-p_i+p_j}{2t},\frac{V+Q_i-p_i}{t}\right\}\right\}.\tag{4}$$

A sufficiently small positive price guarantees positive demand against any rival price. Thus equilibrium revenue is positive, zero prices and prices at least $V+Q_i$ are not best responses, and supports can be bounded compactly. Continuity makes every support point a best response. Let $U_i$ be the largest supported price. If $p_i>\max\{2t,U_j-t+\Delta\}$, demand is uniformly below one. In every positive-demand state a sufficiently small price cut $\epsilon$ increases demand by at least $\epsilon/(2t)$, with revenue gain at least $\epsilon[p_i/(2t)-q_i]-\epsilon^2/(2t)>0$. Zero-demand states cannot lose revenue. The strict distance from full demand permits a common cut size, and positive expected revenue ensures a positive-probability gain. Consequently $U_i\leq\max\{2t,U_j-t+\Delta\}$. The corresponding inequality for $j$ has $-\Delta$. If either upper bound exceeded $2t$, the inequalities would imply $U_i\leq U_i-2t$, a contradiction. Both supports lie in $[0,2t]$.

Since $V>3t$ and $Q_i\geq0$, every supported offer is attractive even at the opposite endpoint, so nonpurchase is absent at every support-price pair. Against fixed rival price $r\in[0,2t]$, covered clipped revenue has its unique peak at $m_i(r)=(t+\Delta+r)/2\in(0,2t)$. Revenue increases on any full-demand segment, whose endpoint $r+\Delta-t$ is below this peak because $r+\Delta<3t$; it is a strictly concave quadratic on the interior-demand segment and zero in the tail. Thus a best response to any rival distribution lies between $m_i(L_j)$ and $m_i(U_j)$, where $L_j$ is its minimum support price: moving inward improves revenue pointwise on a positive-revenue set. Support widths therefore satisfy $U_i-L_i\leq(U_j-L_j)/2$ and conversely; both vanish. Positive revenue for both firms excludes zero/full-market equilibrium. Interior first-order conditions give $p_i=t+\Delta/3$ and $q_i=1/2+\Delta/(6t)$. For existence and global optimality, each candidate rival price is below $4t/3$ and alone covers the market even after unilateral deviations. Its unique global best response is the quadratic peak just derived. Equation (4) also covers deviations into zero demand. Customer ties occur only at one location and do not change aggregates.

Substituting prices, firm $i$ maximizes $[t+(D+e_i-e_j)/3]^2/(2t)-ce_i^2/2$ on $[0,E]$, apart from its fixed access cost. Own curvature is $1/(9t)-c<0$, and its global response is $\operatorname{clip}[(3t+D-e_j)/(B-1),0,E]$. The joint response map contracts in the sup norm by $1/(B-1)<1$, hence has one pure fixed point. Expected profit against a rival effort distribution retains strict concavity and a unique best response, excluding nondegenerate effort mixing. Solving the interior response equations yields (3), and $\mathcal H$ places those efforts strictly inside the box. Substitution gives the stated profit, bounded below by $K-AD_{\max}-k>0$. This is a sunk-entry participation check, not an entry/exit equilibrium. $\square$

## Access Reversal and Customer Quality

**Proposition 1 (matched institutions).** At either symmetric access profile $(a,a)$, contributions and outside participation are independent of $\mu$, with $n_{Hi}=Mh/(Z+2la)$ and $n_{Li}=Mla/(Z+2la)$. Efforts, qualities, prices and profits at that profile also match across institutions. The asymmetric gap is equation (2).

**Proof.** The denominators in (1) coincide when $a_i=a_j$, cancelling $\mu$. At $(F,S)$ pooled $H$ contributions are equal across firms, leaving $d+Mwl/(Z+l)=\delta_P$. With separate catchments the difference is $d+M(vh+wl)/(Z+2l)-Mvh/Z=\delta_S$. The mixture is affine in $\mu$. Lemma 1 supplies the continuations. $\square$

**Proposition 2 (strict reversal).** Suppose $\mathcal H$ holds and

$$\delta_S<0<\delta_P,\qquad 0\leq k<A\delta_P-C\delta_P^2.\tag{R}$$

Then segmentation ($\mu=0$) has unique access equilibrium $(S,S)$ and pooling ($\mu=1$) has unique equilibrium $(F,F)$, each in strict dominant strategies. These are unique subgame-perfect firm outcomes, allowing independent mixing. Pooling's equilibrium customer quality and surplus are lower by $-\delta_S>0$. Internal effort and prices are unchanged; profit per firm falls by $k$, strictly if $k>0$. Total active contribution rises.

**Proof.** From (3), gains from opening against rival $S$ and $F$ are respectively

$$g_S(\delta)=A\delta+C\delta^2-k,\qquad g_F(\delta)=A\delta-C\delta^2-k.\tag{5}$$

On $\mathcal H$, $|\delta|\leq D_{\max}<A/(2C)=(B-2)/(3c)$. If $\delta=\delta_S<0$, then $A+C\delta>A/2>0$, making $g_S<0$; $g_F<0$ as well. If $\delta=\delta_P>0$, (R) makes $g_F>0$ and $g_S\geq g_F>0$. Strict dominance excludes all other pure and independent mixed access equilibria. At symmetric profiles, (3) gives $e_i=1/(3c)$, $p_i=t$, $q_i=1/2$ and $\pi_i=K-ka_i$. By Proposition 1, the quality change from $(S,S)$ to $(F,F)$ across institutions is $d+M(vh+wl)/(Z+2l)-Mvh/Z=\delta_S$. Customers retain the same choices and prices, so each one's utility and aggregate customer surplus change by $\delta_S$. Total active contribution changes from $2Mh/Z$ to $M(2h+2l)/(Z+2l)$, increasing by $2Mlo/[Z(Z+2l)]>0$. $\square$

The comparison separates allocation levels from strategic incentives. Under segmentation an opening firm dilutes its own high-value maintenance and loses relative quality. With pooling, both firms lose equal amounts of $H$ work at an asymmetric profile. The opener retains the new $L$ output and direct access benefit, gaining a relative advantage. When both open, the relative advantage disappears while both products lose valuable maintenance. No compensating equilibrium effort increase occurs because their quality difference remains zero in this covered market.

The strict positive-primitive region is nonempty and open. Take $M=h=l=o=v=t=c=1$, $w=1/10$, $d=1/50$, $k=1/200$, $E=3/5$, $V=4$. Then $\delta_S=-7/75$ and $\delta_P=9/200$. The six margins in (H), in displayed order, are $7$, $23/75$, $56/25$, $19/75$, $1$ and $727/1800$; the pooled opening margin $A\delta_P-C\delta_P^2-k=5869/490000$ is positive. All functions are continuous with positive denominators; every strict inequality persists in an ordinary Euclidean neighborhood of this point. Table 1 summarizes this synthetic illustration, not empirical estimates.

| Quantity | Segmented equilibrium $(S,S)$ | Pooled equilibrium $(F,F)$ |
|:--|--:|--:|
| Total active contribution | $2/3$ | $4/5$ |
| Community maintenance per firm $z_i$ | $1/3$ | $11/50$ |
| Effective customer quality $Q_i$ | $2/3$ | $43/75$ |
| Internal effort; price | $1/3$; $1$ | $1/3$; $1$ |
| Profit per firm | $4/9$ | $4/9-1/200$ |

**Table 1. More participation and lower customer quality in the exact illustration**

## Fixed Outside Opportunities and Limits

Exact symmetric matching depends on pooling outside opportunities. To separate that restriction from reversal itself, consider a different institution: each contributor retains exactly one outside alternative of weight $o/2$ while becoming eligible for both codebases. Set $Z^*=2h+o/2$, $\delta^*=d+Mwl/(Z^*+l)$, and $D^*=\max(|\delta_S|,|\delta^*|)$.

**Proposition 3 (fixed outside opportunity).** Replace $D_{\max}$ in (H) by $D^*$. If $\delta_S<0<\delta^*$, $k<A\delta^*-C(\delta^*)^2$, and $d+M(vh+wl)/(Z^*+2l)-Mvh/Z<0$, segmented $(S,S)$ and pooled $(F,F)$ are again unique access equilibria and the latter has lower customer quality. Symmetric allocations generally do not match across these institutions.

**Proof.** Local allocations remain unchanged. The pooled denominator becomes $Z^*+l(a_i+a_j)$, so pooled $H$ output still cancels in an asymmetric comparison, giving $\delta^*$. Lemma 1 and equation (5) apply with $D^*$. The actual cross-institution symmetric quality change is precisely the proposition's last inequality; symmetric effort and prices coincide. At the illustration, $\delta^*=17/350<D^*=7/75$, the smaller opening gain is $479389/36015000>0$, and cross-institution quality changes by $-31/450$. All inequalities persist locally. The within-pooled quality change is instead $-61/450$ and is a different comparison. $\square$

The harm requires $d<Ml(2vh-wZ)/[Z(Z+2l)]$. If $w\geq2vh/Z$, the maintenance loss disappears; sufficiently large direct benefits $d$ also remove it. If $w=d=0$, then $\delta_P=0$ and pooled opening gains equal $-k$, so strict full-opening dominance fails. High opening costs violate (R). Vanishing contributor mass or task weight, or a very large outside weight, removes the contributor-generated wedge; these limiting observations do not extend the continuation formulas beyond (H). Intermediate mobility can have asymmetric or mixed access equilibria, so endpoint uniqueness does not imply uniqueness at every mobility level. A supplementary alternative-demand calculation failed strict dominance when an effort bound became active; it supplies no global robustness theorem. Proposition 3 is the focused boundary result established here.

## Discussion

### Theoretical Contribution

The result adds a bounded access-and-allocation mechanism to IS research on software maintenance competition. Relative to Mallipeddi et al. (2024), it unpacks a community-effort input into voluntary choices across modules and rival codebases. Relative to endogenous-contribution and licensing models (August et al., 2013, 2018, 2021), it changes technical eligibility while holding licensing and cross-codebase spillovers fixed. The matched comparison identifies how off-equilibrium diversion can reverse access incentives without changing the outcomes of either symmetric profile. Business stealing, modularity and finite attention remain inherited concepts; their task-composition consequence under the stated institution is the contribution.

### Theoretical Implications

Participation and customer-valued maintenance are distinct outcomes. More contributors doing more work is insufficient to infer product improvement when private task returns differ from customer productivity. The comparison also shows why governance institutions belong inside an openness model: which opportunities become jointly eligible matters to deviation incentives, even if symmetric observed allocations coincide. A concrete next question is whether task steering or endogenous private returns break the cancellation that creates $\delta_P$; another is whether dynamic contributor entry of the kind studied by Athey and Ellison (2014) offsets dilution. Arbitrary taste correlation, endogenous populations and weaker product substitution remain unresolved, rather than implied extensions. The fixed-outside result preserves reversal but deliberately gives up matching.

### Practical Implications

For maintainers of competing products that already expose important code, the diagnostic is to assess the composition and source of new contributions, including maintenance displaced from both codebases. Module-level customer value and contributor appeal need separate measurement; raw participation alone cannot answer the access decision. This is not a calibrated recommendation to close code. The model excludes wages, integration bottlenecks, code reuse, entry and many licensing effects. It also does not measure total welfare: contributors weakly benefit from larger feasible menus while customers can lose, and outside-activity utility matters. Lower profit at the pooled equilibrium does not establish a merger remedy or a social optimum. Empirical tests would need to identify the opportunity institution and displacement channel before using this mechanism to explain actual access policies.

### Limitations

The analysis establishes a possibility within a static, specified institution. Fixed contributor mass, independent Gumbel tastes and private returns unaffected by quality or others' effort restrict the allocation mechanism; correlated preferences, entry and dynamic feedback could alter diversion. Exact symmetric matching requires pooling two genuinely distinct outside opportunities with the codebases. The fixed-outside theorem preserves reversal only under its own conditions and gives up that matching. The sufficient continuation domain and endpoint access comparisons do not establish results for effort corners, low reservation values or every intermediate mobility level. Licensing changes, code spillovers, wages, integration bottlenecks and entry are excluded, limiting transfer to other software ecosystems. The exact illustration is synthetic and has no empirical calibration, so it establishes neither prevalence nor effect sizes in practice. Finally, customer surplus is not total welfare: contributor and outside-activity utility preclude a general welfare conclusion or a general recommendation to restrict openness.

## References

Athey, S., & Ellison, G. (2014). Dynamics of open source movements. *Journal of Economics & Management Strategy, 23*(2), 294–316. https://doi.org/10.1111/jems.12053

August, T., Chen, W., & Zhu, K. (2021). Competition among proprietary and open-source software firms: The role of licensing in strategic contribution. *Management Science, 67*(5), 3041–3066. https://doi.org/10.1287/mnsc.2020.3674

August, T., Shin, H., & Tunca, T. I. (2013). Licensing and competition for services in open source software. *Information Systems Research, 24*(4), 1068–1086. https://doi.org/10.1287/isre.2013.0486

August, T., Shin, H., & Tunca, T. I. (2018). Generating value through open source: Software service market regulation and licensing policy. *Information Systems Research, 29*(1), 186–205. https://doi.org/10.1287/isre.2017.0726

Casadesus-Masanell, R., & Llanes, G. (2011). Mixed source. *Management Science, 57*(7), 1212–1230. https://doi.org/10.1287/mnsc.1110.1353

Kumar, V., Gordon, B. R., & Srinivasan, K. (2011). Competitive strategy for open source software. *Marketing Science, 30*(6), 1066–1078. https://doi.org/10.1287/mksc.1110.0669

Mallipeddi, R. R., Demirezen, E. M., Kumar, S., & Gopal, R. D. (2024). Dynamics of competition on openness strategies and software maintenance. *MIS Quarterly, 48*(3), 1239–1262. https://doi.org/10.25300/MISQ/2023/17063

Soundy, J., Wang, C., Stevens, C., & Chan, H. (2021). Game-theoretic analysis of effort allocation of contributors to public projects. In *Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence* (pp. 405–411). https://doi.org/10.24963/ijcai.2021/57
