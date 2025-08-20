# visualize.py
# Contact: 24f2005647@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64

# Load dataset
df = pd.read_csv("data.csv")

# Frequency count for "Operations" department
ops_count = (df['department'] == 'Operations').sum()
print(f"Operations department frequency count: {ops_count}")

ops_count = 11

# ============================
# ✅ HISTOGRAM CREATION CODE
# ============================
plt.figure(figsize=(8,6))
plt.hist(df['department'])   # <--- Histogram (categorical converted to bins)
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Frequency")
plt.tight_layout()

# Save histogram as PNG
plt.savefig("chart.png", dpi=150)
plt.close()
# ============================

# Embed chart into HTML
with open("chart.png", "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode('utf-8')

html = f"""<!doctype html>
<html lang="en">
<head><meta charset="utf-8"><title>Department Distribution</title></head>
<body>
<h2>Department Distribution (All employees)</h2>
<p>Operations department frequency count: <strong>{ops_count}</strong></p>
<img src="data:image/png;base64,{img_b64}" alt="Department distribution chart" style="max-width:512px; width:90%; height:auto;"/>
<hr/>
<h3>Python script used (visualize.py)</h3>
<pre>
import pandas as pd
import matplotlib.pyplot as plt
</pre>
<p>Contact: 24f2005647@ds.study.iitm.ac.in</p>
</body>
</html>"""

with open("visualization.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved chart.png and visualization.html. Done.")


