# visualize.py
# Loads employee data, counts 'Operations' frequency, prints it,
# and creates a histogram / bar chart of department distribution (savess chart.png),
# and writes a self-contained visualization.html embedding the PNG and script.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Load data
df = pd.read_csv("data.csv")

# Calculate frequency count for "Operations" department
ops_count = (df['department'] == 'Operations').sum()
print(f"Operations department frequency count: {ops_count}")

# Create histogram / bar chart of department distribution
plt.figure(figsize=(6,6))
sns.countplot(data=df, y='department', order=df['department'].value_counts().index, palette='Set2')
plt.title('Department Distribution (n={})'.format(len(df)))
plt.xlabel('Count')
plt.ylabel('Department')
plt.tight_layout()

# Save figure to PNG
plt.savefig("chart.png", dpi=150)
plt.close()

# Create an HTML file embedding the PNG as base64 and include the script (for verification)
with open("chart.png", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

# Read this script's content to include in the HTML (for transparency)
with open("visualize.py", "r", encoding="utf-8") as f:
    script_text = f.read()

html = f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Department Distribution</title></head>
<body>
<h2>Department Distribution (All employees)</h2>
<p>Operations department frequency count: <strong>{ops_count}</strong></p>
<img src="data:image/png;base64,{img_b64}" alt="Department distribution chart" style="max-width:512px; width:90%; height:auto;"/>
<hr/>
<h3>Python script used (visualize.py)</h3>
<pre>{script_text}</pre>
<p>Contact: 24f2005647@ds.study.iitm.ac.in</p>
</body>
</html>"""

with open("visualization.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved chart.png and visualization.html. Done.")
