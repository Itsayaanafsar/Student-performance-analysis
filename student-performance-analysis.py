import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance.csv')
plt.style.use('ggplot')

# 1) Average score per subject
avg_scores = df[['math score', 'reading score', 'writing score']].mean()

plt.figure(figsize=(8,5))
avg_scores.plot(kind='bar', color = ['skyblue', 'salmon', 'lightgreen'])
plt.title('Average Subject Scores', fontsize=14, fontweight='bold')
plt.xlabel('Subjects')
plt.ylabel('Average Score')
plt.tight_layout()
plt.xticks(rotation=0)
plt.grid(linestyle="--",alpha=0.3)
plt.ylim(0, 100)
plt.savefig("avg_scores.png", dpi=200)
plt.show()

# 2) Histogram of Math scores
plt.figure(figsize=(8,5))
plt.hist(df["math score"], bins=20, color="purple", alpha = 0.8)
plt.title("Math Score Distribution", fontsize=14, fontweight='bold')
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.grid(linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("math_histogram.png", dpi=200)
plt.show()

# 3) Scatter plot: Reading vs Writing
plt.figure(figsize=(8,5))
plt.scatter(df["reading score"], df["writing score"], color="teal", alpha=0.6, s=50)
plt.title("Reading vs Writing Scores", fontsize=14, fontweight='bold')
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.grid(linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("reading_vs_writing.png", dpi=200)
plt.show()

# 4) Pie chart: Test preparation completed or not
prep_counts = df["test preparation course"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(prep_counts, labels=prep_counts.index, autopct="%1.1f%%",startangle=90, wedgeprops={'edgecolor': 'white'}, colors=["orange","lightblue"])
plt.title("Test Preparation Course Completion", fontsize=14, fontweight='bold')
plt.tight_layout()
plt.savefig("prep_pie.png", dpi=200)
plt.show()