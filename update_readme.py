import os
import requests
import shutil

ROOT_DIR = "./LeetCode"
LEETCODE_API = "https://leetcode.com/graphql"

def get_problem_difficulty(title_slug):
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

def get_problem_number_and_slug(title_slug):
    query = {
        "query": """
        query getQuestionDetail($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId
            titleSlug
          }
        }
        """,
        "variables": {"titleSlug": title_slug}
    }
    try:
        response = requests.post(LEETCODE_API, json=query)
        data = response.json()
        q = data["data"]["question"]
        return f"{q['questionFrontendId']}-{q['titleSlug']}"
    except Exception:
        return None

def filename_to_slug(filename):
    name = os.path.splitext(filename)[0]
    return name.replace("_", "-").replace(" ", "-").lower()

def reorganize_repo():
    moved_count = 0
    for root, _, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith((".java", ".py", ".cpp")):
                slug = filename_to_slug(file)
                folder_name = get_problem_number_and_slug(slug)
                if folder_name:
                    new_folder = os.path.join(ROOT_DIR, folder_name)
                    os.makedirs(new_folder, exist_ok=True)
                    old_path = os.path.join(root, file)
                    new_path = os.path.join(new_folder, file)
                    if old_path != new_path:
                        print(f"Moving {old_path} → {new_path}")
                        shutil.move(old_path, new_path)
                        moved_count += 1
    print(f"✅ Reorganized repo: moved {moved_count} files into numbered folders.")

def generate_table(sort_by="difficulty"):
    problems = []
    count = 1
    for root, _, files in os.walk(ROOT_DIR):
        folder = os.path.basename(root)
        if "-" in folder:  # only numbered folders
            for file in files:
                if file.endswith((".java", ".py", ".cpp")):
                    problem_name = os.path.splitext(file)[0].replace("_", " ")
                    slug = folder.split("-", 1)[1]  # use slug from folder name
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

    if sort_by == "name":
        problems.sort(key=lambda x: x["name"].lower())
    elif sort_by == "difficulty":
        order = {"Easy": 1, "Medium": 2, "Hard": 3, "TBD": 4}
        problems.sort(key=lambda x: order.get(x["difficulty"], 99))

    table_header = "| # | Problem Name | Difficulty | Solution Link | Problem Link |\n|---|---------------|------------|---------------|--------------|\n"
    rows = [
        f"| {i+1} | {p['name']} | {p['difficulty']} | {p['solution']} | {p['problem']} |"
        for i, p in enumerate(problems)
    ]
    return table_header + "\n".join(rows)

def main():
    reorganize_repo()  # first fix repo structure
    table_content = generate_table(sort_by="difficulty")

    readme_content = f"""# 📘 Data Structures & Algorithms (DSA)

![Repo Size](https://img.shields.io/github/repo-size/arpan0408/dsa?color=blue&label=Repo%20Size)
![Stars](https://img.shields.io/github/stars/arpan0408/dsa?style=social)
![Forks](https://img.shields.io/github/forks/arpan0408/dsa?style=social)
![LeetCode Profile](https://img.shields.io/badge/LeetCode-arpan0408-orange?logo=leetcode)
![Top Language](https://img.shields.io/github/languages/top/arpan0408/dsa?color=yellow&logo=java)
![Last Commit](https://img.shields.io/github/last-commit/arpan0408/dsa?color=green&logo=github)

---

## 📋 Solved Problems Table

{table_content}

---
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

    print("✅ README.md updated with solved problems table (sorted by difficulty)!")

if __name__ == "__main__":
    main()
