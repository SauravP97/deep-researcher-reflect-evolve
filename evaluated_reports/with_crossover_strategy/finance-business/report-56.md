# Is there a general method for solving a first-price sealed-bid auction with two bidders who have independent private values drawn from different distributions (i.e., ex-ante asymmetric bidders)?

# Deep Research Report: A General Method for Solving Asymmetric First-Price Sealed-Bid Auctions

## Executive Summary

This report addresses the existence and nature of a general method for solving first-price sealed-bid auctions with two bidders whose private values are drawn from different distributions (ex-ante asymmetry). The research confirms that a general method does exist, centered on establishing and solving a system of coupled first-order ordinary differential equations (ODEs) derived from each bidder's utility maximization problem.

While a universal closed-form solution for all possible distributions is not available due to the complexity of this system, the theoretical framework is well-established. Analytical solutions have been derived for specific cases, most notably when bidders' values are drawn from different uniform distributions.

The equilibrium that arises from this asymmetry exhibits several key characteristics that diverge from the symmetric case. The "weak" bidder (whose values are drawn from a stochastically dominated distribution) bids more aggressively than the "strong" bidder. This leads to an inefficient allocation, where the bidder with the highest private value does not always win. Furthermore, this dynamic causes a failure of the Revenue Equivalence Theorem; under these asymmetric conditions, the first-price auction can generate strictly greater expected revenue for the seller than a second-price auction.

## Key Findings

### The Foundational Symmetric Model

To understand the asymmetric case, it is essential to first establish the method for the symmetric case, where `N` bidders draw their independent private values from a common distribution `F(v)`. The solution concept is the Bayesian Nash Equilibrium (BNE), where each bidder's strategy is a best response to the strategies of all other bidders.

A risk-neutral bidder with value `v` chooses a bid `b` to maximize their expected utility, which is their surplus (`v - b`) multiplied by their probability of winning. The BNE bidding strategy `b(v)` is found by solving the first-order condition of this maximization problem. The general solution is given by the integral formula:

`b(v) = v - ∫[0,v] (F(x)/F(v))^(N-1) dx`

For the specific case of a uniform distribution on [0,1], where `F(v) = v`, this simplifies to a linear bidding strategy: `b(vi) = ((N-1)/N) * vi`. This foundational model provides the core mathematical tools and intuition for approaching the more complex asymmetric problem.

### Equilibrium Bidding Behavior in Asymmetric Auctions

When bidders are asymmetric, their equilibrium bidding strategies are interdependent, reflecting the characteristics of their opponent. Research and experimental studies have identified a consistent pattern in this behavior:

*   **Aggressive Weak Bidder:** The "weak" bidder (whose value distribution is stochastically dominated by the "strong" bidder's) tends to bid more aggressively than the "strong" bidder [https://www.researchgate.net/publication/222430966_Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental_Study, https://www.researchgate.net/publication/332700175_Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental_Study]. This means that for a given value, the weak bidder "shades" their bid less than the strong bidder does. This aggressive strategy is a best response to the presence of a stronger competitor [https://www.isid.ac.in/~dmishra/topicsdoc/maskin_riley.pdf].

*   **Interdependent Strategies:** In the resulting BNE, each bidder's bid function is continuous, strictly increasing, and depends on the characteristics of both their own and their rival's value distribution [https://academic.oup.com/restud/article/90/2/852/6628599, https://brocku.ca/repec/pdf/0504.pdf].

### Auction Outcomes and Allocative Inefficiency

The bidding behavior described above directly impacts the auction's outcome and its economic efficiency.

*   **Win Probabilities:** As a direct result of their more aggressive bidding, the weak bidder wins more frequently in a first-price auction than they would in a second-price auction, where the highest-value bidder always wins. Conversely, the strong bidder wins less often than they would in a second-price auction [https://brocku.ca/repec/pdf/0504.pdf].

*   **Allocative Inefficiency:** Unlike symmetric auctions, which are known to be efficient (the item is allocated to the bidder with the highest willingness-to-pay), asymmetric first-price auctions are generally inefficient [http://waehrer.net/HRWEfficiency.pdf]. The weak bidder's aggressive strategy can lead them to win the auction even when the strong bidder holds a higher private value. This misallocation of the good is a hallmark of asymmetric first-price auctions.

### Failure of the Revenue Equivalence Theorem

A central finding in auction theory is the Revenue Equivalence Theorem, which states that under symmetric conditions, various standard auction formats (including first-price and second-price) yield the same expected revenue for the seller. However, this theorem fails when bidders are asymmetric [https://www.csef.it/WP/wp712.pdf].

*   **Increased Revenue in First-Price Auctions:** The aggressive bidding by the weak bidder to overcome their ex-ante disadvantage drives up the final price. Consequently, the seller's expected revenue in a first-price auction with asymmetric bidders can be strictly greater than the revenue from a second-price auction under the same conditions [https://eprints.ugd.edu.mk/23178/1/dushko+,mico+paper+ISCTBL2019.pdf, https://econtheory.org/?f=4555]. In some settings, a sequential first-price auction can generate even higher revenue than a simultaneous one [https://www.academia.edu/113518531/Pre_Auction_Offers_in_Asymmetric_First_Price_and_Second_Price_Auctions].

## Detailed Analysis

### The General Method: A System of Coupled Differential Equations

The core of the general method for solving a two-bidder asymmetric first-price auction lies in formulating each bidder's utility maximization problem and deriving the first-order conditions. Let the bidders be "Strong" (S) and "Weak" (W), with value distributions `FS` and `FW`, probability density functions `fS` and `fW`, and inverse bid functions `bS⁻¹(b)` and `bW⁻¹(b)`.

The strong bidder's problem is to choose a bid `b` to maximize their expected payoff:
`max b FW(b⁻¹W(b))(tS − b)`

Here, `FW(b⁻¹W(b))` represents the strong bidder's probability of winning, which is the probability that the weak bidder's value is less than the value required for the weak bidder to place a bid of `b`.

Taking the first-order condition for each bidder's maximization problem yields the following system of two coupled ordinary differential equations:

1.  **For the strong bidder (S):** `fW(b⁻¹W(b)) / FW(b⁻¹W(b)) * (b⁻¹W)′(b) = 1 / (b⁻¹S(b) − b)`
2.  **For the weak bidder (W):** `fS(b⁻¹S(b)) / FS(b⁻¹S(b)) * (b⁻¹S)′(b) = 1 / (b⁻¹W(b) − b)`

Solving this system, along with appropriate boundary conditions (e.g., that the highest possible bids must be the same), yields the inverse bid functions, which characterize the BNE. While the research logs confirm this system as the central analytical tool, they did not contain a step-by-step derivation from the initial utility function.

### Analytical Solutions for the Asymmetric Uniform Case

Although solving the system of ODEs is generally intractable for arbitrary distributions, explicit, closed-form analytical solutions have been found for the case where two bidders' values are drawn from different uniform distributions [https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf, https://ore.exeter.ac.uk/articles/journal_contribution/Asymmetric_first-price_auctions_with_uniform_distributions_Analytic_solutions_to_the_general_case/29721242].

For instance, one study provides the explicit inverse bid function for bidder 1 (`v1(b)`) in an auction with a binding minimum bid `m`, where values are drawn from `[v1, v1]` and `[v2, v2]`:

*   `v1(b) = v1 + (m − v1)(m − v2) / (b − v2 − c3(b − m)θ(b + m − v1 − v2)1−θ)`

The constants in this equation depend on the parameters of the value distributions [http://www.ma.huji.ac.il/~zamir/documents/Uniform_fulltext.pdf]. The existence of such formulas, though complex, confirms that the general method can yield concrete solutions in specific, well-defined scenarios.

### Existence and Uniqueness of Equilibrium

The existence of a BNE has been established more broadly, even for auctions with more than two asymmetric bidders [https://www.scilit.com/publications/42b0523eb54bbcbde933215bdf27f972]. The existence proofs often rely on perturbation methods, showing that the equilibrium in an auction with asymmetric supports can be seen as the limit of equilibria from a series of "close" auctions with common supports [https://www.sciencedirect.com/science/article/pii/S0899825624000848].

While existence is generally assured, uniqueness is guaranteed only under certain conditions, such as for two bidders with atomless distributions or when distributions have a mass point at the lower end of their support [https://www.scilit.com/publications/42b0523eb54bbcbde933215bdf27f972].

## Conclusion & Outlook

There is a well-defined general method for solving first-price sealed-bid auctions with two asymmetric bidders. The method involves setting up and solving a system of coupled differential equations that describe each bidder's optimal bidding strategy. However, the mathematical complexity of this system means that analytical, closed-form solutions are only available for specific cases, such as when value distributions are uniform.

The analysis of the asymmetric equilibrium reveals significant departures from the symmetric model. The weak bidder's aggressive bidding strategy leads to allocative inefficiency but can increase the seller's expected revenue beyond what would be achieved in a second-price auction. This failure of the Revenue Equivalence Theorem is a critical insight for auction design, suggesting that sellers facing asymmetric bidders may prefer the first-price format.

The outlook for this field involves further exploration of conditions for unique equilibria and the development of numerical and computational methods to solve for bidding strategies when analytical solutions are not feasible [https://dl.acm.org/doi/abs/10.1145/3736252.3742487].

## References

[http://waehrer.net/HRWEfficiency.pdf](http://waehrer.net/HRWEfficiency.pdf)

[http://www.columbia.edu/~yc2271/files/publications/chekim.pdf](http://www.columbia.edu/~yc2271/files/publications/chekim.pdf)

[http://www.ma.huji.ac.il/~zamir/documents/Uniform_fulltext.pdf](http://www.ma.huji.ac.il/~zamir/documents/Uniform_fulltext.pdf)

[https://academia.edu/113518531/Pre_Auction_Offers_in_Asymmetric_First_Price_and_Second_Price_Auctions](https://academia.edu/113518531/Pre_Auction_Offers_in_Asymmetric_First_Price_and_Second_Price_Auctions)

[https://academic.oup.com/restud/article/90/2/852/6628599](https://academic.oup.com/restud/article/90/2/852/6628599)

[https://brocku.ca/repec/pdf/0504.pdf](https://brocku.ca/repec/pdf/0504.pdf)

[https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf](https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf)

[https://dl.acm.org/doi/abs/10.1145/3736252.3742487](https://dl.acm.org/doi/abs/10.1145/3736252.3742487)

[https://econtheory.org/?f=4555](https://econtheory.org/?f=4555)

[https://economics.stackexchange.com/questions/6808/system-of-differential-equations-asymmetric-first-price-auction](https://economics.stackexchange.com/questions/6808/system-of-differential-equations-asymmetric-first-price-auction)

[https://eprints.ugd.edu.mk/23178/1/dushko+,mico+paper+ISCTBL2019.pdf](https://eprints.ugd.edu.mk/23178/1/dushko+,mico+paper+ISCTBL2019.pdf)

[https://hal.science/hal-01313412v1/document](https://hal.science/hal-01313412v1/document)

[https://onlinelibrary.wiley.com/doi/10.1155/2021/5592402](https://onlinelibrary.wiley.com/doi/10.1155/2021/5592402)

[https://ore.exeter.ac.uk/articles/journal_contribution/Asymmetric_first-price_auctions_with_uniform_distributions_Analytic_solutions_to_the_general_case/29721242](https://ore.exeter.ac.uk/articles/journal_contribution/Asymmetric_first-price_auctions_with_uniform_distributions_Analytic_solutions_to_the_general_case/29721242)

[https://papers.ssrn.com/sol3/papers.cfm?abstract_id=930518](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=930518)

[https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf](https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf)

[https://www.csef.it/WP/wp712.pdf](https://www.csef.it/WP/wp712.pdf)

[https://www.isid.ac.in/~dmishra/topicsdoc/maskin_riley.pdf](https://www.isid.ac.in/~dmishra/topicsdoc/maskin_riley.pdf)

[https://www.researchgate.net/publication/222430966_Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental_Study](https://www.researchgate.net/publication/222430966_Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental_Study)

[https://www.researchgate.net/publication/228319685_Linear_Bid_in_Asymmetric_First-Price_Auctions](https://www.researchgate.net/publication/228319685_Linear_Bid_in_Asymmetric_First-Price_Auctions)

[https://www.researchgate.net/publication/303019838_Asymmetric_information_about_rivals'_types_Existence_of_equilibrium_in_first-price_auction](https://www.researchgate.net/publication/303019838_Asymmetric_information_about_rivals'_types_Existence_of_equilibrium_in_first-price_auction)

[https://www.researchgate.net/publication/332700175_Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental_Study](https://www.researchgate.net/publication/332700175_Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental_Study)

[https://www.sciencedirect.com/science/article/abs/pii/S0165176511002473](https://www.sciencedirect.com/science/article/abs/pii/S0165176511002473)

[https://www.sciencedirect.com/science/article/pii/S0899825607000188](https://www.sciencedirect.com/science/article/pii/S0899825607000188)

[https://www.sciencedirect.com/science/article/pii/S0899825624000848](https://www.sciencedirect.com/science/article/pii/S0899825624000848)

[https://www.scilit.com/publications/42b0523eb54bbcbde933215bdf27f972](https://www.scilit.com/publications/42b0523eb54bbcbde933215bdf27f972)

## Citations 
- https://economics.stackexchange.com/questions/14412/derivation-of-equilibrium-strategy-in-1st-price-auction
- https://hanzhezhang.github.io/teaching/Chicago_ECON207/207sol_auction.pdf
- http://www.econport.org/content/handbook/auctions/auctionsexperiments/auctionsbneandfirstprice.html
- https://homepages.math.uic.edu/~marker/stat473-F14/auctions.pdf
- https://cs.brown.edu/courses/cs1951k/lectures/2020/first_price_BNE.pdf
- https://files.webservices.illinois.edu/8224/jmp_kwanghyunkim_181104.pdf
- https://cs.brown.edu/courses/cs1951k/lectures/2020/first_price_auctions.pdf
- https://www.econgraphs.org/explanations/game/auctions/first_price_auctions
- https://onlinelibrary.wiley.com/doi/10.1155/2021/5592402
- https://www.chegg.com/homework-help/questions-and-answers/consider-first-price-sealed-bid-auction-n-1-bidders-bidders-private-values-independent-uni-q107300834
- https://economics.stackexchange.com/questions/6808/system-of-differential-equations-asymmetric-first-price-auction
- https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf
- https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf
- http://www.ma.huji.ac.il/~zamir/documents/Uniform_fulltext.pdf
- https://users.ssc.wisc.edu/~dquint/econ805%202007/econ%20805%20lecture%209.pdf
- https://web.stanford.edu/~jdlevin/Econ%20286/Auctions.pdf
- https://onlinelibrary.wiley.com/doi/10.1155/2021/5592402
- http://www.ma.huji.ac.il/~zamir/documents/Uniform_fulltext.pdf
- https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf
- https://ore.exeter.ac.uk/articles/journal_contribution/Asymmetric_first-price_auctions_with_uniform_distributions_Analytic_solutions_to_the_general_case/29721242
- https://ideas.repec.org/p/huj/dispap/dp432.html
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=930518
- https://www.researchgate.net/publication/228319685_Linear_Bid_in_Asymmetric_First-Price_Auctions
- https://www.sciencedirect.com/science/article/pii/S0899825624000848
- https://academic.oup.com/restud/article/90/2/852/6628599
- https://onlinelibrary.wiley.com/doi/10.1155/2021/5592402
- https://www.csef.it/WP/wp712.pdf
- https://www.researchgate.net/publication/228319685_Linear_Bid_in_Asymmetric_First-Price_Auctions
- https://www.cirje.e.u-tokyo.ac.jp/research/workshops/micro/documents/March20.pdf
- http://www.ma.huji.ac.il/~zamir/documents/Uniform_fulltext.pdf
- https://onlinelibrary.wiley.com/doi/10.1155/2021/5592402
- https://brocku.ca/repec/pdf/0504.pdf
- http://www.columbia.edu/~yc2271/files/publications/chekim.pdf
- https://www.sciencedirect.com/science/article/abs/pii/S0165176511002473
- https://hal.science/hal-01313412v1/document
- https://capcp.la.psu.edu/wp-content/uploads/sites/11/2020/07/NumericalSolutions.pdf
- http://waehrer.net/HRWEfficiency.pdf
- https://www.researchgate.net/publication/222430966_Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental_Study
- https://econ.biu.ac.il/sites/econ/files/shared/riedp_6-15.pdf
- https://www.researchgate.net/publication/332700175_Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental_Study
- https://www.academia.edu/23104056/Bidding_Behavior_in_Asymmetric_Auctions_An_Experimental
- https://brocku.ca/repec/pdf/0504.pdf
- https://www.researchgate.net/publication/303019838_Asymmetric_information_about_rivals'_types_Existence_of_equilibrium_in_first-price_auction
- https://dl.acm.org/doi/abs/10.1145/3736252.3742487
- https://www.scilit.com/publications/42b0523eb54bbcbde933215bdf27f972
- https://www.sciencedirect.com/science/article/pii/S0899825624000848
- https://ideas.repec.org/p/ecl/stabus/2057.html
- https://www.sfu.ca/~idudnyk/Auctions_Part2_Revenue_Equivalence.pdf
- https://elischolar.library.yale.edu/cgi/viewcontent.cgi?article=2531&context=cowles-discussion-paper-series
- https://www.sciencedirect.com/science/article/pii/S0899825607000188
- https://www.mdc.e.u-tokyo.ac.jp/wp/wp-content/uploads/2025/05/Asymmetric-Auctions-with-Resale.pdf
- https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf
- https://eprints.ugd.edu.mk/23178/1/dushko+,mico+paper+ISCTBL2019.pdf
- https://www.academia.edu/113518531/Pre_Auction_Offers_in_Asymmetric_First_Price_and_Second_Price_Auctions
- https://www.isid.ac.in/~dmishra/topicsdoc/maskin_riley.pdf
- https://carnehl.github.io/SRPS.pdf
- https://onlinelibrary.wiley.com/doi/10.1155/2021/5592402
- https://www.mdpi.com/2073-4336/13/5/62
- https://econtheory.org/?f=4555
- https://quizlet.com/gb/626946194/economics-of-auctions-midterm-flash-cards/
- https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4905549