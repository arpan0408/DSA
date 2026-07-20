import os
import requests

ROOT_DIR = "./LeetCode"
LEETCODE_API = "https://leetcode.com/graphql"

def get_problem_difficulty(title_slug):
    """
    Fetch difficulty from LeetCode GraphQL API using problem slug.
    Example slug: 'two-sum'
    """
    query = {
        "query": """
        query getQuestionDifficulty($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            difficulty
          }
        }
        """,
        "variables": {"titleSlug": title_slug}
    }

    try:
        response = requests.post(LEETCODE_API, json=query)
        data = response.json()
        return data["data"]["question"]["difficulty"]
    except Exception:
        return "TBD"

def filename_to_slug(filename):
    """
    Convert filename like 'TwoSum.java' → 'two-sum'
    """
    name = os.path.splitext(filename)[0]
    slug = name.replace("_", "-").replace(" ", "-").lower()
    return slug

def generate_table(sort_by="difficulty"):
    """
    Generate markdown table of solved problems.
    sort_by can be 'difficulty' or 'name'
    """
    problems = []
    count = 1

    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith((".java", ".py", ".cpp")):
                problem_name = os.path.splitext(file)[0].replace("_", " ")
                slug = filename_to_slug(file)
                difficulty = get_problem_difficulty(slug)

                solution_path = os.path.join(root, file).replace("\\", "/")
                solution_link = f"[Solution]({solution_path})"
                problem_link = f"[Problem](https://leetcode.com/problems/{slug}/)"

                problems.append({
                    "id": count,
                    "name": problem_name,
                    "difficulty": difficulty,
                    "solution": solution_link,
                    "problem": problem_link
                })
                count += 1

    # Sorting logic
    if sort_by == "name":
        problems.sort(key=lambda x: x["name"].lower())
    elif sort_by == "difficulty":
        order = {"Easy": 1, "Medium": 2, "Hard": 3, "TBD": 4}
        problems.sort(key=lambda x: order.get(x["difficulty"], 99))

    # Build table
    table_header = "| # | Problem Name | Difficulty | Solution Link | Problem Link |\n|---|---------------|------------|---------------|--------------|\n"
    rows = [
        f"| {i+1} | {p['name']} | {p['difficulty']} | {p['solution']} | {p['problem']} |"
        for i, p in enumerate(problems)
    ]

    return table_header + "\n".join(rows)

def main():
    # Change sort_by to "name" if you prefer alphabetical order
    table_content = generate_table(sort_by="difficulty")

    readme_content = f"""# 📘 Data Structures & Algorithms (DSA)

![Repo Size](https://img.shields.io/github/repo-size/arpan0408/dsa?color=blue&label=Repo%20Size)
![Stars](https://img.shields.io/github/stars/arpan0408/dsa?style=social)
![Forks](https://img.shields.io/github/forks/arpan0408/dsa?style=social)
![LeetCode Profile](https://img.shields.io/badge/LeetCode-arpan0408-orange?logo=leetcode)
![Top Language](https://img.shields.io/github/languages/top/arpan0408/dsa?color=yellow&logo=java)
![Last Commit](https://img.shields.io/github/last-commit/arpan0408/dsa?color=green&logo=github)

---

## 🚀 About This Repository
- 📂 Organized solutions to popular DSA problems  
- 🧩 Covers arrays, strings, linked lists, trees, graphs, dynamic programming, and more  
- 💡 Clean, maintainable code with comments for clarity  
- 🎯 Goal: Strengthen problem-solving skills and prepare for technical interviews  

---

## 📑 Contents
- Arrays & Strings  
- Linked Lists  
- Stacks & Queues  
- Trees & Graphs  
- Dynamic Programming  
- Miscellaneous  

---

## 🔗 My LeetCode Profile
👉 [LeetCode Profile - arpan0408](https://leetcode.com/arpan0408/)

---

## 📊 LeetCode Stats
![LeetCode Stats](https://leetcard.jacoblin.cool/arpan0408?theme=dark&font=Source%20Sans%20Pro&ext=contest)

---

<!--## 📋 Solved Problems Table

{table_content}

---
-->

## 🛠️ Tech Stack
- Languages: Java, Python, C++  
- Platform: LeetCode, GitHub  
- Tools: VS Code, IntelliJ IDEA  

---

## 📈 Progress Tracking
I regularly update this repo with new problems and solutions.  
Follow along to see my journey of mastering DSA and improving coding interview readiness.

---

## 🤝 Contributing
Suggestions and optimizations are welcome!  
Feel free to open an issue or submit a pull request.

---

## 📜 License
Licensed under the MIT License – free to use for learning and practice.
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ README.md updated with solved problems table (sorted by difficulty)!")

if __name__ == "__main__":
    main()
