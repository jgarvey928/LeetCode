import os
import re

# We break these tags apart mathematically so browsers CANNOT hide them when you copy-paste!
TOPIC_START = "<" + "!---LeetCode Topics Start-->"
TOPIC_END = "<" + "!---LeetCode Topics End-->"

# Dictionary mapping file extensions to Language names
EXTENSION_MAP = {
    '.py': 'Python',
    '.java': 'Java',
    '.sql': 'SQL',
    '.js': 'JavaScript',
    '.ts': 'TypeScript',
    '.c': 'C',
    '.cpp': 'C++',
    '.cs': 'C#',
    '.go': 'Go',
    '.rb': 'Ruby',
    '.swift': 'Swift',
    '.kt': 'Kotlin',
    '.rs': 'Rust',
    '.php': 'PHP',
    '.sh': 'Shell'
}

# Link to Solution is now the very last column
README_TEMPLATE = f"""<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=006400&center=true&vCenter=true&width=435&lines=🚀+LeetCode+Journey+2024;Solving+one+problem+at+a+time...;Mastering+Algorithms+%26+Data+Structures;Language+of+choice:+Java" alt="Typing SVG" />
</p>

<p align="center">
  <img src="https://leetcode-stats-six.vercel.app/?username=jgarvey928&theme=dark" alt="LeetCode Stats" />
</p>
# 🚀 LeetCode Solutions

Welcome to my **LeetCode** repository! This repository contains my personal solutions to various LeetCode problems. It serves as a log of my progress in improving my algorithmic thinking, data structure knowledge, and problem-solving skills.

## 📁 Repository Structure

Each problem has its own dedicated directory, named in the format `XXXX-problem-name` (where `XXXX` is the LeetCode problem number).

## 💡 Goals
- Consistently practice coding challenges.
- Optimize solutions for better Time and Space complexities.
- Explore different approaches for the same problem (e.g., Iterative vs. Recursive, Dynamic Programming vs. Greedy).

## 📊 Problems Solved

Here is a list of the problems currently solved in this repository:

| # | Problem Name | Difficulty | Language | Topics | Link to Solution |
|---|---|:---:|---|---|---|
{{table_content}}

{TOPIC_START}
{TOPIC_END}
"""

def get_existing_topics():
    """Scans the current README to extract topics line-by-line to prevent formatting crashes."""
    topic_map = {}
    if not os.path.exists('README.md'):
        return topic_map

    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. RESCUE PREVIOUSLY SAVED TOPICS
    for line in content.split('\n'):
        if line.startswith('|') and '[View]' in line:
            parts = line.split('|')
            if len(parts) >= 7:
                num = parts[1].strip()
                # Smart check: smoothly handles the transition from the old column order to the new one
                if '[View]' in parts[5]:
                    topics = parts[6].strip() # Old format
                else:
                    topics = parts[5].strip() # New format
                    
                if topics and topics != "N/A":
                    topic_map[num] = [t.strip() for t in topics.split(',')]

    # 2. PARSE NEW TOPICS FROM THE EXTENSION'S FOOTER
    if TOPIC_START in content and TOPIC_END in content:
        block = content.split(TOPIC_START)[1].split(TOPIC_END)[0]
        
        current_topic = ""
        for line in block.split('\n'):
            line = line.strip()
            
            if line.startswith('## '):
                current_topic = line.replace('##', '').strip()
                
            elif current_topic and line.startswith('|') and '[' in line:
                match = re.search(r'\[(\d{4})-', line)
                if match:
                    pid = match.group(1)
                    if pid not in topic_map:
                        topic_map[pid] = []
                    if current_topic not in topic_map[pid]:
                        topic_map[pid].append(current_topic)
                        
    return topic_map

def get_difficulty_from_readme(folder_path):
    readme_path = os.path.join(folder_path, 'README.md')
    if not os.path.exists(readme_path):
        return "⚪ TBD"
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if '<h3>Easy</h3>' in content or '## Easy' in content:
                return "🟢 Easy"
            elif '<h3>Medium</h3>' in content or '## Medium' in content:
                return "🟠 Medium"
            elif '<h3>Hard</h3>' in content or '## Hard' in content:
                return "🔴 Hard"
    except Exception:
        pass
    return "⚪ TBD"

def get_languages_from_folder(folder_path):
    """Scans the folder for code files and returns a string of the languages used."""
    languages = set()
    try:
        for file in os.listdir(folder_path):
            ext = os.path.splitext(file)[1].lower()
            if ext in EXTENSION_MAP:
                languages.add(EXTENSION_MAP[ext])
    except Exception:
        pass
        
    if not languages:
        return "N/A"
        
    return ", ".join(sorted(list(languages)))

def main():
    topic_map = get_existing_topics()

    dirs = [d for d in os.listdir('.') if os.path.isdir(d) and re.match(r'^\d{4}-', d)]
    dirs.sort()

    table_rows = []
    for d in dirs:
        parts = d.split('-', 1)
        num = parts[0]
        
        name_parts = parts[1].split('-')
        name = ' '.join(word.capitalize() for word in name_parts)
        
        link = f"./{d}"
        difficulty = get_difficulty_from_readme(d)
        languages_list = get_languages_from_folder(d)
        
        if num in topic_map and topic_map[num]:
            topics_list = ", ".join(topic_map[num])
        else:
            topics_list = "N/A"

        # Moved the Link to the very end of the row
        table_rows.append(f"| {num} | {name} | {difficulty} | {languages_list} | {topics_list} | [View]({link}) |")

    table_content = '\n'.join(table_rows)
    
    readme_content = README_TEMPLATE.format(table_content=table_content)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    main()
