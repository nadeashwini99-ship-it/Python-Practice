print("===== RESUME KEYWORD CHECKER =====")

resume = input("Paste your resume text here:\n").lower()

job_role = input("\nEnter job role: ").lower()

skills = {
    "python": ["python", "programming"],
    "web development": ["html", "css", "javascript"],
    "database": ["sql", "mysql"],
    "tools": ["git", "github"],
    "communication": ["communication", "teamwork"]
}

required_keywords = []

if "python" in job_role:
    required_keywords = [
        "python", "sql", "git", "problem solving"
    ]

elif "web" in job_role:
    required_keywords = [
        "html", "css", "javascript", "git"
    ]

elif "data" in job_role:
    required_keywords = [
        "python", "sql", "excel", "data analysis"
    ]

else:
    required_keywords = [
        "communication", "teamwork", "python", "sql"
    ]

found = []
missing = []

for keyword in required_keywords:
    if keyword in resume:
        found.append(keyword)
    else:
        missing.append(keyword)

print("\n===== ANALYSIS RESULT =====")

print("\nKeywords Found:")
for keyword in found:
    print("✔", keyword)

print("\nKeywords Missing:")
for keyword in missing:
    print("✘", keyword)

score = (len(found) / len(required_keywords)) * 100

print("\nResume Match Score:", round(score, 2), "%")

if score >= 75:
    print("Good match! Your resume matches many keywords.")
elif score >= 50:
    print("Average match. Consider adding relevant skills.")
else:
    print("Low match. Improve your resume with relevant skills.")
