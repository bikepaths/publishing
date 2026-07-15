import re

FILE_PATH = '/home/user0/git/bikepaths/blog/society/image/scheduled/2026-07-18-06-00-00_society,freedom,security,equity,policy,conflict_freedom-security-equality-and-order.md'

with open(FILE_PATH, 'r') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    # Fix Colons
    if '**Step' in line and ':' in line:
        line = line.replace(':', '.')
    elif ':' in line and not 'http' in line and not '<!--' in line:
        # replace colon acting as hard stop with a period
        line = line.replace(': ', '. ')
    
    # Fix Synthetic Contrasts
    if 'Not identical outcomes for everyone, but a genuine chance' in line:
        line = line.replace('Not identical outcomes for everyone, but a genuine chance', 'A genuine chance')
    if 'is not agreement, but honesty' in line:
        line = line.replace('is not agreement, but honesty', 'is honesty rather than agreement')
    if 'are not only weighing freedom against order, but making different guesses' in line:
        line = line.replace('are not only weighing freedom against order, but making different guesses', 'are weighing freedom against order and making different guesses')
    if 'are not the same kind of cost, and a careful analysis' in line:
        line = line.replace('are not the same kind of cost, and a careful analysis', 'differ in kind, and a careful analysis')
    if 'not simply an obstacle' in line:
        line = line.replace('not simply an obstacle', 'rather than simply an obstacle')
    if 'not just a rule\'s wording' in line:
        line = line.replace('not just a rule\'s wording', 'rather than just a rule\'s wording')
        
    # Fix Banned Words
    line = re.sub(r'\bheavily\b', 'strongly', line, flags=re.IGNORECASE)
    line = re.sub(r'\bcompletely\b', 'entirely', line, flags=re.IGNORECASE)
    line = re.sub(r'\bprecisely\b', 'specifically', line, flags=re.IGNORECASE)
    line = re.sub(r'\bcapacity\b', 'limits', line, flags=re.IGNORECASE)
    line = re.sub(r'\bhowever sympathetic\b', 'no matter how sympathetic', line, flags=re.IGNORECASE)
    line = re.sub(r'\bhowever\b', 'though', line, flags=re.IGNORECASE)
    line = re.sub(r'\bexactly\b', 'specifically', line, flags=re.IGNORECASE)
    line = re.sub(r'\bheavy\b', 'large', line, flags=re.IGNORECASE)
    line = re.sub(r'\bstructurally\b', 'systematically', line, flags=re.IGNORECASE)
    line = re.sub(r'\bexact\b', 'specific', line, flags=re.IGNORECASE)

    new_lines.append(line)

with open(FILE_PATH, 'w') as f:
    f.writelines(new_lines)
