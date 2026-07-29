<!--mos MoS_Analytical_OVP.md mos-->
<!--t The Anatomy of the Singular Prototype: Scaling SDI to the Dunbar Baseline t-->
<!--d The minimum viable SDI deployment requires 85,000 square feet and a community ceiling of 150 people, of which 38 are permanent staff and 112 are residents. This post derives both numbers from biological and operational first principles. d-->
<!--tag society,systems,infrastructure,technology,logistics,economics tag-->
<!--image https://bikepaths.org/blog/content/images/webp/urban_municipal_concrete_plaza_1785223126473.webp image-->

Most government programs that address homelessness begin with a negotiation. A city council sits in a room, looks at the budget, and asks how much money is available. Then it designs a program that fits inside that budget. If the budget is small, the program is small. If the budget disappears next year, the program disappears with it. The Systemic Dignity Infrastructure does not work this way. It begins with a different question. It asks what a human body requires to stay alive, and then it builds the program around that answer. The budget conversation happens afterward.

This distinction matters because human biology is not negotiable. A person living on the street loses weight. The digestive system starts to fail after weeks of inconsistent nutrition. Infections that a healthy immune system would fight off in days become permanent conditions. The body loses its ability to regulate temperature, which means a cold night that a housed person sleeps through can kill an unsheltered person. These are not opinions about what homeless people deserve. These are measurements of how the human body works. The Systemic Dignity Infrastructure treats them as engineering constraints, the same way a bridge engineer treats the tensile strength of steel. You cannot argue a steel beam into holding more weight than physics allows, and you cannot argue a starving human body into surviving without calories.

Because the system begins with biology instead of budgets, it operates as an open-source engineering specification. The word "open-source" comes from the software industry. It means that the blueprints, the design rules, and the working logic are published for anyone to read, copy, and implement. No single company or government owns the specification. Any city, any nonprofit, any hospital system can download the plans and build a deployment. The reason for making it open-source is a practical admission that no single organization has the money, the expertise, and the political authority to build these systems alone, rather than a matter of idealism. A hospital knows how to deliver medical care but does not know how to acquire real estate. A real estate developer knows how to buy buildings but does not know how to route Medicaid funding. A city government controls zoning laws but has no clinical staff. The open-source model allows each of these specialists to contribute their piece without any one of them owning the whole puzzle.

Yet the open-source model carries a non-negotiable rule. The specialists who cooperate on the logistics cannot change the biological baseline. A real estate analyst can propose a cheaper building in a different neighborhood. A Medicaid administrator can restructure how reimbursement claims flow through the billing system. These are logistical adjustments, and they are welcome. What no participant can do is propose removing the medical intake floor to save money, or cutting the food supply from three meals a day to one. Those changes would violate the biological specification, and the system treats such a violation the same way a bridge engineer treats removing a load-bearing column. The bridge falls down.

The next constraint comes from a British scientist named Robin Dunbar. Dunbar spent decades studying primates, including humans, and he focused on the size of the neocortex. The neocortex is the outer layer of the brain, the wrinkled part visible in photographs. It handles social processing. It tracks faces, remembers names, stores emotional history with other people, and predicts how someone will behave based on past interactions. Dunbar found that the size of this brain region correlates with the maximum number of stable social relationships a species can maintain. For humans, that number is 150. This is not an approximation. Dunbar published this figure in 1992, and three decades of subsequent research across military units, corporate organizations, and village populations have confirmed it repeatedly.

The number 150 means something specific. It means that when a group of humans exceeds 150 members, the individuals inside that group can no longer recognize one another by sight. They stop knowing who is trustworthy and who is dangerous. They stop resolving conflicts through personal familiarity and start requiring rules, enforcement officers, and surveillance cameras. The group shifts from a community to an institution. Anyone who has lived in a large apartment complex has experienced a version of this. You do not know your neighbors. You do not know who belongs in the hallway and who does not. The building compensates for that anonymity by installing security cameras and hiring a doorman. The SDI specification avoids this failure by capping every residential cluster at 150 people. The specification calls this cluster a Dunbar Pod.

Inside one Dunbar Pod, every resident is known by name. Staff members recognize every face. When a resident stops appearing for meals, someone notices within hours, not weeks. When a conflict arises between two residents, the staff already knows both individuals, their histories, their triggers, and their patterns. This consequence of brain architecture operates as a structural limitation rather than a management philosophy. Groups smaller than 150 can self-police through mutual recognition. Groups larger than 150 cannot.

Scaling a deployment down to the smallest possible size that still functions without compromise means supporting one Dunbar Pod and nothing less. One Pod contains 150 people total. The question that has to be answered before any blueprints are drawn is whether "150 people" means 150 residents, or whether the staff members who work inside the building every day also count toward that number.

The answer matters enormously for the budget. Dunbar's research was not limited to friendships or peer relationships. His cognitive limit applies to any stable social relationship where a person tracks another individual by name, face, and behavioral history. A nurse who knows 40 residents by their medication schedules, their triggers, and their family situations has consumed 40 Dunbar slots. Those 40 residents each know that nurse by name and face in return. The relationship is mutual and it consumes cognitive capacity on both sides. When an SDI building operates as a genuine community rather than an institution, the staff and the residents are part of the same social network. The 150 limit therefore applies to the combined total of residents and permanent on-site staff.

This creates the first min/max optimization problem in the specification. The number of residents that a deployment can house is not 150. The number of residents is 150 minus the minimum number of staff required to run a 24-hour, seven-day-a-week, year-round clinical and operational facility.

That minimum staff number is not a guess. It is a calculation. Any position that must be filled around the clock requires 4.2 full-time equivalent workers to cover three daily shifts across seven days, after accounting for days off, vacation time, and sick leave. The SDI clinical and operational model requires, at minimum, the following roles present on-site at all times: two registered nurses to cover the clinical floor and intake screening, one security and floor monitor per wing to cover resident safety, one kitchen worker to prepare and serve the three daily meals, and one facilities worker to maintain the building systems. Beyond the continuous roles, daytime operations require one physician or psychiatrist on-site, one social worker and case manager, one administrative intake coordinator, one building supervisor, and one veterinary technician to manage the animal kennel during morning and afternoon feeding windows.

Converting these roles to full-time equivalents at the 4.2 multiplier for continuous positions and 1.0 for daytime-only positions produces the following staffing model.

| Role | Per Shift | Coverage | Multiplier | FTE |
|---|---|---|---|---|
| Registered Nurses | 2 | 24/7 | 4.2 | 8 |
| Security / Floor Monitors | 2 | 24/7 | 4.2 | 8 |
| Kitchen Workers | 2 | 24/7 | 4.2 | 8 |
| Facilities Workers | 1 | 24/7 | 4.2 | 4 |
| Physicians | 1 | Daytime + On-Call | 2.0 | 2 |
| Social Worker / Case Manager | 1 | Daytime | 1.0 | 1 |
| Intake Coordinator | 1 | Daytime | 1.0 | 1 |
| Building Supervisor | 1 | Daytime | 1.0 | 1 |
| Veterinary Technician | 1 | Daytime | 1.0 | 1 |
| **Total** | | | | **38** |

These 38 permanent staff members consume 38 Dunbar slots.

Subtracting 38 staff from the community ceiling of 150 produces the resident count: 112 people per Dunbar Pod. That is the number the building is sized for. Any operator who houses 150 residents and then hires a clinical staff on top of that figure creates a community of 188 people, which is 38 people beyond the cognitive limit, and the Dunbar effect collapses.

The private residential rooms are called Asset Limited Modular Units. Each unit provides 150 square feet of private, lockable living space for one person. That is a room roughly 10 feet wide and 15 feet long. It contains a bed, a desk, personal storage, and enough floor space to move without feeling caged. Multiply 150 square feet by 112 residents, and the residential component requires 16,800 square feet. That number accounts only for the private rooms. It does not include hallways, stairwells, elevators, or common areas on the residential floors.

The remaining program spaces serve specific functions in the stabilization pipeline, which is the sequence of operations that moves a person from the street into permanent stability.

The first component is the Ground Floor Intake Airlock. When a new resident arrives from the street, they do not walk up to a reception desk and fill out paperwork. They enter a controlled medical environment on the ground floor. In this space, medical staff perform a health screening. They check for tuberculosis, lice, scabies, open wounds, and acute psychiatric emergencies. They provide a shower, clean clothing, and a first meal. The Airlock exists because a person arriving from the street carries biological risks that cannot be introduced into a shared living environment without screening. This is the same infection-control logic that hospitals use when admitting patients from emergency rooms, not a moral judgment about hygiene.

The second component is the veterinary kennel. A significant percentage of unhoused individuals own pets, primarily dogs. These animals serve as emotional support, physical warmth during cold nights, and personal security. Traditional shelters ban animals, which means a person who owns a dog will refuse shelter and stay on the street. The SDI specification treats this refusal as a design failure in the shelter, not a character flaw in the person. The veterinary kennel occupies a dedicated section of the lower floors. It provides kenneling, veterinary medical care, feeding, and supervised interaction time so that residents can visit their animals daily without the animals occupying the residential floors.

The third component is the Possessions Vault. People who live on the street accumulate possessions. Shopping carts, bicycles, tents, sleeping bags, boxes of personal documents, clothing, tools, and sentimental items fill their immediate environment. Traditional shelters either ban these possessions or store them in garbage bags that get lost or stolen. The SDI specification provides a warehouse-scale vault in the lower levels of the building. Each resident receives a locked storage unit. Their belongings are catalogued and protected. The Vault exists because a person who enters a program and loses everything they own will leave that program. The loss of possessions triggers the same psychological destabilization as the loss of housing itself.

The fourth component is the clinical node. Doctors, nurses, psychiatrists, addiction counselors, and social workers operate on-site inside the building. Residents do not travel to external appointments at hospitals across the city. The clinical staff comes to them. This arrangement exists because the population entering the system carries a disease burden that external appointment systems cannot handle. A person with untreated diabetes, an infected foot wound, untreated psychosis, and no identification cannot navigate a city bus system to reach a clinic five miles away, check in with a receptionist, wait in a lobby for two hours, and return home. The clinical node removes every one of those barriers by placing the medical staff inside the same building where the person sleeps.

These four program components account for the spaces that residents and intake staff interact with directly. Running a 24-hour building requires a second layer of infrastructure that operates entirely out of sight. This layer does not touch the pipeline, but the pipeline cannot run without it.

| Component | Function | Square Feet |
|---|---|---|
| Commercial Kitchen and Cold Storage | Cooking line, walk-in refrigerator, walk-in freezer, dry goods, dishwashing | 3,000 |
| Laundry Facility | Commercial washers and dryers processing linens and clothing for 112 residents | 1,500 |
| Mechanical / Electrical / HVAC Plant | Air handling, electrical switchgear, plumbing, backup generator | 4,000 |
| Staff Offices, Break Rooms, Lockers | Administrative workspace and rest areas for 38 workers | 3,000 |
| Loading Dock and Waste Handling | Food deliveries, medical supplies, laundry and waste outbound | 1,500 |
| Server Room and Communications Hub | Network infrastructure, building automation, data systems | 500 |
| **Total Back-of-House** | | **13,500** |

Adding 13,500 square feet to the 71,500 square feet of program space produces a minimum building footprint of 85,000 gross square feet for a single pod.

The physical shape of this 85,000 square feet is flexible. One option is horizontal. An abandoned big-box retail store, the kind vacated when a chain like Sears or Kmart closes, provides a single-story floorplate large enough to contain the full deployment on one level. The ceilings in these buildings are typically 20 to 30 feet high, which accommodates mezzanine construction for the residential floors above the ground-level services. The second option is vertical. A mid-rise commercial office tower of five floors, each floor measuring roughly 17,000 square feet, stacks the functions on top of one another. The Airlock, loading dock, and mechanical plant occupy the ground floor. The Vault, kennel, and laundry occupy the second floor. The clinical node, staff offices, and kitchen occupy the third floor. The residential units for 112 residents occupy floors four and five.

What the physical shape cannot do is shrink below 85,000 square feet without breaking the pipeline. If a city council eliminates the back-of-house to save money, the kitchen closes, the laundry stops, the building loses power backup during storms, and the clinical node cannot receive medical supply deliveries. The residents are housed but not fed, clothed, or treated. The pipeline produces the same failure it would produce if the building were never built.

The single-pod prototype is not the economically optimal deployment. The back-of-house infrastructure, the kitchen, the laundry, the mechanical plant, the loading dock, and the server room serve the whole building regardless of how many pods occupy the residential floors. Stacking two or three Dunbar Pods inside one tower amortizes that fixed overhead cost across a larger number of residents without requiring additional fixed infrastructure. The constraint on this stacking is cognitive isolation. For the Dunbar effect to hold inside each pod, the residents of one pod cannot share social space with the residents of another. A shared dining hall defeats the architecture. A shared elevator lobby where residents of all pods mix defeats it. The ground-floor infrastructure can serve the whole building because residents do not spend their social time there. The residential floors, the common areas, and the dining rooms must remain separated, one set per pod.

This splits the staffing model into variable and fixed categories. Variable staff, such as nurses and floor monitors, must remain dedicated to a single pod to maintain the social network. Fixed staff, such as facilities technicians and kitchen workers, operate largely outside the intimate pod network and scale efficiently across the whole building. 

A vertical tower combining three pods represents the probable economic optimum. Beyond three pods, the logistical friction of preventing resident cross-contamination in elevators and intake airlocks becomes impossible to manage.

| Metric | Single Pod Prototype | Three-Pod Tower |
|---|---|---|
| Total Residents | 112 | 336 |
| Variable Staff (Dedicated) | 19 FTE (1 pod) | 57 FTE (3 pods) |
| Fixed Staff (Shared) | 19 FTE | 28 FTE |
| Total Staff | 38 FTE | 85 FTE |
| Gross Square Footage | 85,000 sq ft | 185,000 sq ft |
| Fixed Cost Amortization | Baseline | Optimized |

The 85,000 square foot figure and the 112 resident ceiling are the engineering baselines for the singular prototype. They are not targets to negotiate from. They are the floor below which the specification refuses to operate.

