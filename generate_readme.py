import os
import re

# 🎯 ADD NEW PROBLEMS HERE!
# Just add the 4-digit number and the colored difficulty icon.
# If a number is missing, the script will just put "⚪ TBD" for it.
DIFFICULTIES = {
    "0002": "🟠 Medium",
    "0006": "🟠 Medium",
    "0007": "🟠 Medium",
    "0009": "🟢 Easy",
    "0013": "🟢 Easy",
    "0014": "🟢 Easy",
    "0021": "🟢 Easy",
    "0026": "🟢 Easy",
    "0027": "🟢 Easy",
    "0080": "🟠 Medium",
    "0088": "🟢 Easy",
    "0121": "🟢 Easy",
    "0169": "🟢 Easy",
    "0595": "🟢 Easy",
    "1603": "🟢 Easy",
    "1791": "🟢 Easy",
    "1916": "🔴 Hard",
    "2383": "🟢 Easy"
}

README_TEMPLATE = """# 🚀 LeetCode Solutions

Welcome to my **LeetCode** repository! This repository contains my personal solutions to various LeetCode problems. It serves as a log of my progress in improving my algorithmic thinking, data structure knowledge, and problem-solving skills.

## 📁 Repository Structure

Each problem has its own dedicated directory, named in the format `XXXX-problem-name` (where `XXXX` is the LeetCode problem number).

## 💡 Goals
- Consistently practice coding challenges.
- Optimize solutions for better Time and Space complexities.
- Explore different approaches for the same problem (e.g., Iterative vs. Recursive, Dynamic Programming vs. Greedy).

## 📊 Problems Solved

Here is a list of the problems currently solved in this repository:

| # | Problem Name | Difficulty | Link to Solution |
|---|---|:---:|---|
{table_content}
"""

def main():
    # Find all directories that match the pattern "4 digits followed by a hyphen"
    dirs = [d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'^\d{4}-', d)]
    # Sort them numerically
    dirs.sort()

    table_rows = []
    for d in dirs:
        # Split "0002-add-two-numbers" into "0002" and "add-two-numbers"
        parts = d.split('-', 1)
        num = parts[0]
        
        # Capitalize the words for a clean problem name
        name_parts = parts[1].split('-')
        name = ' '.join(word.capitalize() for word in name_parts)
        
        link = f"./{d}"
        
        # Look up the difficulty in our dictionary above. Default to "⚪ TBD" if not found.
        difficulty = DIFFICULTIES.get(num, "⚪ TBD")

        # Add the row to our single table
        table_rows.append(f"| {num} | {name} | {difficulty} | [View]({link}) |")

    # Combine all rows
    table_content = '\n'.join(table_rows)
    
    # Insert the table into the template
    readme_content = README_TEMPLATE.format(table_content=table_content)

    # Overwrite the README.md entirely, destroying any manually added sections from the extension
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    main()
