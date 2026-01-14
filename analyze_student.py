"""
Project Title : Automated Student Performance Analysis System
Developed By  : Shyam
Course        : CSE
Purpose       : Internship Automation Project
"""
import pandas as pd

# Step 1: Read CSV
df = pd.read_csv("student_data.csv")

# Step 2: Calculate average score
df['Average'] = (
    (df['Quiz1'] + df['Quiz2'] + df['Assignment1'] + df['Assignment2']) / 40 * 40
) + (df['FinalExam'] / 100 * 60)
#calc performance
def classify(avg):
    if avg >= 75:
        return "Excellent"
    elif avg >= 50:
        return "Average"
    else:
        return "Needs Improvement"


df['Performance'] = df['Average'].apply(classify)

# Step 4: Predict At Risk
df['AtRisk'] = df['Average'].apply(lambda x: 1 if x < 50 else 0)

# Step 5: Add Recommendations
def recommend(row):
    rec = []
    if row['Quiz1'] < 6 or row['Quiz2'] < 6:
        rec.append("Practice Quizzes")
    if row['Assignment1'] < 6 or row['Assignment2'] < 6:
        rec.append("Improve Assignments")
    if row['FinalExam'] < 50:
        rec.append("Study Final Exam Topics")
    return ", ".join(rec)

df['Recommendation'] = df.apply(recommend, axis=1)

print("\nFinal Student Analysis:")
print(df)
# Save the final analysis to a CSV (optional professional touch)
df.to_csv("final_student_analysis.csv", index=False)
print("\nFinal table saved as 'final_student_analysis.csv'")

# Optional: show a quick summary
print("\nSummary:")
print("Total Students:", len(df))
print("At Risk Students:", df['AtRisk'].sum())
print("Excellent Students:", len(df[df['Performance']=='Excellent']))
print("Average Students:", len(df[df['Performance']=='Average']))
print("Needs Improvement Students:", len(df[df['Performance']=='Needs Improvement']))
