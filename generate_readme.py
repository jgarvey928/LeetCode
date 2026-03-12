import os
import re

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

def get_difficulty_from_readme(folder_path):
    """Opens the README.md inside the problem folder and extracts the difficulty."""
    readme_path = os.path.join(folder_path, 'README.md')
    
    # If for some reason the README doesn't exist, return the default grey icon
    if not os.path.exists(readme_path):
        return "⚪ TBD"
        
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            # Read the entire file content because the HTML might be all on one line
            content = f.read()
            
            # Check for HTML tags first (what your extension uses)
            # We also check for Markdown just in case older problems use it
            if '<h3>Easy</h3>' in content or '## Easy' in content:
                return "🟢 Easy"
            elif '<h3>Medium</h3>' in content or '## Medium' in content:
                return "🟠 Medium"
            elif '<h3>Hard</h3>' in content or '## Hard' in content:
                return "🔴 Hard"
    except Exception:
        # If there's any error reading the file, safely pass to the default return below
        pass
        
    return "⚪ TBD" # Default grey icon if it couldn't find the difficulty or hit an error

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
        
        # 🕵️‍♂️ DYNAMICALLY FETCH DIFFICULTY!
        # The script looks for <h3>Medium</h3> inside the folder's README.
        difficulty = get_difficulty_from_readme(d)

        # Add the row to our single table
        table_rows.append(f"| {num} | {name} | {difficulty} | [View]({link}) |")

    # Combine all rows
    table_content = '\n'.join(table_rows)
    
    # Insert the table into the template
    readme_content = README_TEMPLATE.format(table_content=table_content)

    # Overwrite the main README.md entirely, destroying any manually added sections from the extension
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    main()
