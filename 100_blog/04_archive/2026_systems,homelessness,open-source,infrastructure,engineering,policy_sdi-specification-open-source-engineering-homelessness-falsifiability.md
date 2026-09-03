<!--t A Falsifiable Open-Source Specification for Ending Homelessness t-->
<!--d An independent researcher has published four working papers proposing a modular infrastructure framework for chronic homelessness, with pre-committed failure metrics and an open invitation to falsify the model. d-->
<!--tag systems,homelessness,open-source,infrastructure,engineering,policy tag-->
<!--image https://bikepaths.org/blog/content/images/webp/modern_commercial_glass_tower.webp image-->

The California State Auditor released a report in 2024 examining five of the state's largest homelessness programs. The findings were not what the agencies running those programs wanted to hear, but they were also more complicated than the headlines suggested. Two of the five programs were found likely cost-effective. The other three could not be evaluated at all because the administering agencies had failed to collect the data necessary to determine whether the money had produced any measurable outcome. The auditor did not conclude that spending on homelessness fails. The auditor concluded that California cannot demonstrate whether most of its spending works because the measurement infrastructure does not exist.

That distinction matters for everything that follows in this post, because the framework described here was designed specifically to close that measurement gap.

A previous post on this site described the structural failure of American homelessness policy as an infinite loop, a software metaphor where a recursive coding error consumes every resource fed into the machine without producing any output. That metaphor was drawn from a set of four working papers written by independent researcher Charles Joseph DiBella and published on SSRN between January and April of 2026. The papers are not peer-reviewed journal articles. They are self-published working papers, and the distinction is worth stating plainly because transparency about the status of the research is central to what makes the project unusual.

The foundational paper, posted in January 2026, reviews Housing First research and international comparators including Finland before proposing a modular three-layer framework as an alternative architecture. The subsequent papers develop the relational, economic, and governance layers of the model in sequence. A companion repository on GitHub collects the full specification, a verification matrix, a risk register, and a set of municipal pilot gating criteria into a single open-source package licensed under Creative Commons.

**What Makes This Different**

The most distinctive feature of the framework is not its policy content but its accountability structure. DiBella has pre-committed to a set of eleven measurable claims, and each claim carries a proposed threshold, a measurement method, a validation timeline, and a defined failure condition. The framework proposes measuring biological stabilization against a threshold of 72 hours for 90 percent of residents. It proposes measuring cooperative wage rates against a threshold of 85 percent of local market entry wages over rolling quarterly windows. These are not validated findings drawn from empirical data. They are proposed metrics that a future pilot would need to test, and the framework is explicit about the fact that it has not yet generated the prospective data required to validate any of them.

This pre-commitment to falsifiability is what separates the project from a conventional policy proposal. Many housing programs define their success metrics after deployment, which allows administrators to adjust the definition of success to match whatever outcomes the program actually produces. The SDI framework locks its metrics before the first facility opens, which means a failed pilot cannot be rebranded as a successful one without directly contradicting the published specification.

**The Three-Layer Stack**

The architecture is built as a proposed sequential dependency, meaning that each layer would need to be fully active before the next layer begins. The working papers argue that running the layers in parallel or skipping one entirely would undermine the causal chain the model depends on, though this claim remains untested.

The first layer proposes converting surplus commercial real estate into biologically secure stabilization environments through master lease arrangements rather than multi-year construction projects. The shift to remote work left large commercial buildings sitting partially empty across many American cities, and the framework treats this surplus capacity as infrastructure that could potentially be activated faster than new construction. The working papers estimate activation within 180 days, though actual timelines would depend heavily on local building codes, zoning requirements, and the physical condition of the specific properties involved. The papers acknowledge that office-to-residential conversion carries significant regulatory and structural challenges that vary by municipality.

The second layer proposes grouping residents into small cohorts of approximately seven people, guided by a trained peer mentor at a ratio of one mentor for every seven residents. The working paper supporting this layer cites research showing that housing retention rates drop significantly when individuals are placed into isolated rooms with no relational continuity, though the specific cohort size and mentor ratio are proposed parameters rather than empirically validated optima.

The third layer proposes building cooperative micro-businesses inside the stabilization facility, creating an internal employment bridge for residents whose work histories contain the long gaps that chronic homelessness produces. The framework then proposes using a Medicaid waiver to underwrite the first twelve months of independent market-rate housing for graduating residents. Whether a state Medicaid program would approve this kind of waiver application, and whether the waiver funding would be sufficient to cover market-rate rents in high-cost cities, are open questions that the papers identify but cannot resolve without a live pilot generating actual cost data.

**Why Open Source**

Traditional policy research travels through a pipeline that progressively strips technical precision from the original work. A researcher publishes findings, a think tank condenses them into a brief, a staffer inserts selected phrases into draft legislation, and the final policy document often bears limited resemblance to the original analysis. Publishing the full specification on GitHub does not solve this problem entirely, but it does create a permanent, version-controlled reference point that anyone can compare against whatever legislative language eventually emerges.

The repository includes a contribution guide that invites systems engineers, econometricians, urban planners, clinical directors, and Medicaid waiver architects to audit the framework from their respective domains. The governance model proposes a permanent separation between the systems architect who controls the technical core and the executive operations team responsible for capital procurement and municipal deployment. Whether this split-authority structure would survive contact with real institutional politics is an open question the papers raise but cannot answer in advance.

**The Gating Criteria**

The framework publishes a set of gating criteria that a municipality would need to meet before deployment begins. A city that cannot demonstrate surplus capacity activation, auditable infrastructure verification, capital routing isolation, and cooperative sovereignty would not qualify under the proposed terms.

The auditable infrastructure requirement proposes that every funded stabilization unit carry GPS indexing and real-time digital verification so that a dormant unit cannot be counted as active. This targets a measurement problem the papers call the Ghost Asset Problem, where the reported number of funded housing units in a city exceeds the actual number of verified beds available on any given night.

The capital routing requirement proposes that Medicaid waiver funding designated for the Tenancy Bridge Guarantee be legally isolated from general municipal budgets. The papers argue that without this firewall, transition funding is vulnerable to being swept into other spending priorities during fiscal shortfalls.

**Where the Work Stands**

The framework is currently a proposal backed by four self-published working papers. The theoretical arc is complete, and the next phase would require deployment of one physical facility to generate the prospective empirical data needed to test the combined three-layer mechanism. The papers identify One California Plaza in downtown Los Angeles as a proposed pilot site, a surplus commercial tower near the densest concentration of chronic unsheltered homelessness in the city.

No pilot site has been secured. No funding has been committed. No Medicaid waiver has been filed. The work is at the stage where a first test could be designed and funded, and where the pre-committed verification thresholds at 90, 180, and 365 days would provide the data necessary to determine whether the model works, needs revision, or should be abandoned.

The pre-commitment to those failure conditions is what makes the framework worth examining, because a proposal that defines the terms of its own falsification before asking for a dollar of public money is making a fundamentally different kind of claim than a program that defines success after the money has already been spent.

The four working papers are available on [SSRN](https://papers.ssrn.com/sol3/cf_dev/AbsByAuth.cfm?per_id=7627029) and the full specification is published at [Systemic Dignity Infrastructure](https://github.com/bikepaths/sdi-specification).
