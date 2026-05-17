# Chapter Two: The Contractor State

Muneeb and Sohaib Akhter deleted ninety‑six U.S. databases in fifty‑six minutes. Their credentials should have been revoked at termination. First, understand the political economy that gave them access: the federal contractor state. This is not just individual malfeasance. Outsourcing federal IT created blind spots where accountability vanished when most needed.

The brothers were brilliant hackers, but they exploited a system that favoured continuous operation over quick security responses. The party holding access had no incentive to revoke it fast. The paying party could not easily verify revocation.

The architecture stems from the 1996 Clinger‑Cohen Act, also called the Information Technology Management Reform Act. It responded to Y2K anxieties, labeling federal IT as bloated and obsolete. The law introduced Chief Information Officers and private‑sector metrics, urging agencies to outsource.

Clinger‑Cohen did more than suggest outsourcing; it built a bureaucratic framework that made outsourcing often obligatory for agencies seeking reform compliance.

GAO reports show that by the early 2000s outsourcing became the dominant model for federal IT. Agencies stopped maintaining large in‑house developer teams. Instead, they awarded multi‑year, multi‑hundred‑million‑dollar contracts to firms like Leidos, SAIC, CGI Federal, and Accenture.

These contractors designed, built, operated, and secured the networks, databases, and applications behind veterans’ benefits, tax processing, and national security intel. The logic: private firms could deliver IT services more efficiently and at lower cost, scaling expertise with mission demands.

Less attention was paid to accountability when the wires connecting service delivery to consequences were cut. FOIA reports reveal a shift in performance measurement and rewards.

Under the legacy federal workforce, security failures were direct. An administrator who failed to patch could face discipline, and a supervisor ignoring an escalation could be terminated. Their employment was tied to the agency, and performance reviews included security compliance.

Under the contractor model, especially firm‑fixed‑price or time‑and‑materials contracts, incentives inverted. Contractors were paid to keep systems running, close tickets, and meet uptime SLAs. These agreements did not measure intrusion detection speed or access revocation rigor.

A contractor whose monitoring flagged an insider threat faced a dilemma. Escalating the alert could trigger a costly incident review, threatening uptime guarantees. Downplaying the anomaly kept metrics green. The structure rewarded the latter.

OIG reports show this dynamic codified in contracts between prime contractors and federal agencies. Missing uptime targets incurs immediate, quantifiable penalties. Missing security SLAs yields speculative, long‑term consequences, often unenforced.

In essence, contracts paid for the illusion of security while measuring only availability. Congressional hearings note the subcontractor cascade endemic to federal IT. A prime contractor may subcontract thirty percent of work to regional specialists, who may further outsource niche functions.

By the time work reaches the individual running SQL queries, four or five layers separate the federal agency from the employee with keyboard access. Each layer adds markup, reporting requirements, and incentives to obscure problems that could reflect poorly on performance.

Audits of subcontractor performance by the prime were rare; agency‑level audits rarer still. The result: no single entity had full visibility into who could access what, and no entity had a strong financial incentive to find out.

GAO data indicates that about seventy‑five percent of federal IT spending went to contracts for services, operations, and maintenance. In high‑impact areas like database administration, contractor share often exceeded eighty‑five percent. Privileged access holders were far more likely to be contractor badge holders than federal civil servants.

Personnel vetting, monitoring, and off‑boarding protocols for contractors were private policies, not federal rules. FOIA reports on IRS IT modernization contracts highlight misaligned background checks. Contractors often use a seven‑year lookback, ignoring older convictions.

The Akhter brothers’ 2015 guilty pleas fell just outside this window when they were hired in 2023. A seven‑year check in early 2024 would show a clean record.

Thus, agencies contract out not just labor but the responsibility for knowing who that labor is, yet retain ultimate liability for their actions.

When a contractor employee is terminated, off‑boarding depends on the contractor’s internal policies and speed. Even if SLAs promise “immediate” deactivation, the financial consequence of delay is negligible compared to penalties for missing uptime guarantees.

Consequently, access revocation becomes a low priority, an administrative afterthought rather than a security imperative. This was precisely the failure that enabled the Akhter operation.

On February 18, 2025, Muneeb Akhter’s termination meeting ended around 4:50 p.m. Federal standards require automatic disabling of accounts within fifteen minutes. Instead, his credentials stayed active for nearly an hour, allowing the deletion of ninety‑six databases and exfiltration of thousands of files.

The paying agency had no real‑time way to verify revocation. The contractor had no financial reason to treat it as urgent.

Closing this gap requires re‑engineering incentives that govern federal IT outsourcing. One approach: tie contractor payments to security outcomes, withholding fees until independent auditors confirm access revocation timelines meet federal standards. Another: impose liquidated damages for delayed deactivation equal to uptime penalties.

A third approach: mandate real‑time sharing of access logs between contractors and agencies, enabling continuous verification that only active employees retain privileges.

A fourth approach: bring high‑risk functions like privileged access management back in‑house or under hybrid models where federal employees retain oversight authority.

These solutions are costly and complex, requiring contract rewrites, retraining, and trade‑offs between cost, speed, and security.

The Akhter case shows the current model already carries a cost measured in deleted databases, exfiltrated personal records, and eroded public trust.

Recognizing that the architecture itself is the root cause is the first step toward designing a system where the door does not remain open long enough for a determined actor to walk through it, and if they do, an alarm sounds before they reach the database.