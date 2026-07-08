import re
with open("100_blog/06_data/cefr_b2_dict.txt") as f:
    allowed = set(x.strip().lower() for x in f)
text = """Title: Systemic Dignity: A Practical Alternative to Current Homelessness Strategies
Description: A breakdown of the biological relational and economic steps required to resolve chronic street homelessness.
Tags: society, health, money, infrastructure, mind, systems

Material respect structure, a proposed alternative to current street living strategies, suggests that a dedicated recovery phase focusing on body balance and food rehabilitation is necessary before long-term housing placement. This model uses changed commercial real estate to create safe, small-scale group living places, trying to address the physical and brain trauma of chronic street living.

While American cities spend billions of dollars on street living the visible crisis on the streets continues to get worse every day.

The current political debate is stuck between two ideas where one side demands giving out immediate apartment keys and the other forces criminal camping laws. This ongoing block shows that city leaders are failing because they are making a major order error. A new systems model called material respect structure is the practical alternative. It says that a physical house can not fix a body that has broken down without a dedicated recovery phase.

Traditional programs focus on a roof as the single starting point.

Yet statistics reveal that while places like Finland achieve very high housing retention rates the United States frequently drops below forty percent for the street hardened population. The real difference lies in the physical condition of the person walking through the door.

Years of living on concrete trigger deep physical and brain problems where constant trauma fully ruins regular sleep cycles. Placing a deeply hurt and sick person straight into an isolated apartment frequently leads to extreme anxiety and property failure. This forces them back out onto the street. The material respect model approaches this issue as a physical design challenge by breaking the recovery process into logical body steps that begin with physical balance.

Before long term housing placement ever occurs the system introduces a mandatory step focused on fixing the human body through universal access to thermal safety and intense food rehabilitation.

To reach the street population effectively the entry point of these places operates around the clock with zero behavioral tests. Anyone can walk in to access showers and basic medical care because the design removes the rigid rules that force people to leave their pets or separate from their partners.

Instead of building massive warehouse camps that people avoid because they are loud and dangerous this model cuts places into self governing groups of one hundred and fifty residents. Sociology shows that this number represents the body limit of human trust where people can maintain social safety webs and mutual accountability. Within these smaller groups every resident has a locked room and a dedicated peer worker who helps them build the skills required to transition back into civic life.

Funding this model becomes realistic by taking advantage of a major economic shift involving the commercial real estate fall.

With remote work changing downtown districts many commercial office towers are hitting historic lows and selling at massive discounts. Traditional real estate developers struggle to change these tall buildings into luxury apartments because installing individual plumbing and walls for separate units is impossible. The material respect model takes advantage of the wide open floors of these office buildings by changing the existing architecture into modular group areas. This strategy changes empty concrete structures into self supporting public utilities at a fraction of standard construction costs.

Despite the sound math and the body reasoning behind this idea it has not been adopted because a massive industry of developers and operators profit from managing the ongoing loop of expensive short term camps. Government offices are designed to track basic signs like beds filled rather than complex physical steps like brain balance or physical recovery.

Modern city hall leadership is tied down by slow movement, so a new step will likely require an independent proof of concept funded by a private foundation. Once a single prototype tower shows it can fix street living individuals well and cheap the data will speak for itself.

The empty buildings are already standing in our downtown centers.

The design solution is waiting for a new generation of leaders to implement it."""

words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
bad = [w for w in words if w not in allowed]
print("Bad words left:", set(bad))
