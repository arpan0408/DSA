import os

def generate_table():
    table_header = "| # | Problem Name | Difficulty | Solution Link |\n|---|---------------|------------|---------------|\n"
    rows = []
    count = 1

    # Walk through repo and auto-detect solutions
    for root, _, files in os.walk("./LeetCode"):
        for file in files:
            if file.endswith(".java") or file.endswith(".py") or file.endswith(".cpp"):
                problem_name = file.replace(".java", "").replace(".py", "").replace(".cpp", "")
                difficulty = "TBD"  # You can enhance this by mapping filenames to difficulty
                solution_link = f"[Solution]({os.path.join(root, file)})"
                rows.append(f"| {count} | {problem_name} | {difficulty} | {solution_link} |")
                count += 1

    return table_header + "\n".join(rows)

def main():
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

## 📋 Solved Problems Table

{generate_table()}

---

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

if __name__ == "__main__":
    main()
