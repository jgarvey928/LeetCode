import os
import re

# This is the template for your README. The {table_content} part will be replaced by the script.
README_TEMPLATE = """# 🚀 LeetCode Solutions

Welcome to my **LeetCode** repository! This repository contains my personal solutions to various LeetCode problems. It serves as a log of my progress in improving my algorithmic thinking, data structure knowledge, and problem-solving skills.

## 📁 Repository Structure

Each problem has its own dedicated directory, named in the format `XXXX-problem-name` (where `XXXX` is the LeetCode problem number).

## 📊 Problems Solved

Here is a list of the problems currently solved in this repository:

| # | Problem Name | Link to Solution |
|---|---|---|
{table_content}

---
*Happy Coding! 💻*
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

        # Add the row to our table
        table_rows.append(f"| {num} | {name} | [View]({link}) |")

    # Combine all rows
    table_content = '\n'.join(table_rows)
    
    # Insert the table into the template
    readme_content = README_TEMPLATE.format(table_content=table_content)

    # Overwrite the README.md with the new content
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    main()
