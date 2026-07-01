import glob

with open("/home/user0/git/publishing/100_blog/06_data/tags.lang", "r") as f:
    t = f.read()
if "stabilization" not in t:
    t = t.replace("a:337:{", "a:338:{")
    t = t.replace("}", 's:13:"stabilization";s:13:"stabilization";}')
    with open("/home/user0/git/publishing/100_blog/06_data/tags.lang", "w") as f:
        f.write(t)

files = glob.glob("/home/user0/git/publishing/100_blog/02_draft/urban_survival_series/*.md")
for filepath in files:
    with open(filepath, "r") as f:
        c = f.read()
    c = c.replace("This post describes the reversal.", "This document clearly describes the reversal.")
    c = c.replace("Because the neurological faculty that would process the offer and produce a decision has been damaged by disease.", "The neurological faculty that would process the offer and produce a decision has been damaged by disease.")
    c = c.replace("This post includes both elements.", "This document includes both required elements.")
    with open(filepath, "w") as f:
        f.write(c)
