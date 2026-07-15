import re

with open('/home/user0/files/oakhaven_framework_paper.md', 'r') as f:
    text = f.read()

# Eliminate dashes and semicolons
text = text.replace('—', ', ').replace('–', ' to ').replace(';', ',')

lines = text.split('\n')
new_lines = []
started_prose = False

for line in lines:
    # Skip initial empty lines or the main title
    if not started_prose:
        if line.startswith('# Freedom, Security'):
            continue
        if line.startswith('## Abstract'):
            continue
        if line.strip() == '':
            continue
        started_prose = True
    
    if line.startswith('#'):
        heading_text = line.lstrip('#').strip()
        new_lines.append(f"**{heading_text}**")
    else:
        new_lines.append(line)

body = '\n'.join(new_lines)

metadata = """<!--t Freedom, Security, Equality, and Order: A Framework for Understanding Modern Policy Conflict t-->
<!--d This paper examines how modern societies balance freedom, security, equality, and order through six areas of public policy. d-->
<!--tag society,freedom,security,equity,policy,conflict tag-->
<!--image https://bikepaths.org/blog/content/images/webp/scales_shield_chain_grid.webp image-->

"""

final_text = metadata + body

out_path = '/home/user0/git/bikepaths/blog/society/image/scheduled/2026-07-18-06-00-00_society,freedom,security,equity,policy,conflict_freedom-security-equality-and-order.md'

with open(out_path, 'w') as f:
    f.write(final_text)

print(f"Generated {out_path}")
