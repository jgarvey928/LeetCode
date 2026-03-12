import os
import re

# We break these tags apart mathematically so browsers CANNOT hide them when you copy-paste!
TOPIC_START = "<" + "!---LeetCode Topics Start-->"
TOPIC_END = "<" + "!---LeetCode Topics End-->"

# Notice the {TOPIC_START} at the bottom. This safely injects the tags.
README_TEMPLATE = f"""# 🚀 LeetCode Solutions

Welcome to my **LeetCode** repository! This repository contains my personal solutions to various LeetCode problems. It serves as a log of my progress in improving my algorithmic thinking, data structure knowledge, and problem-solving skills.

## 📁 Repository Structure

Each problem has its own dedicated directory, named in the format `XXXX-problem-name` (where `XXXX` is the LeetCode problem number).

## 💡 Goals
- Consistently practice coding challenges.
- Optimize solutions for better Time and Space complexities.
- Explore different approaches for the same problem (e.g., Iterative vs. Recursive, Dynamic Programming vs. Greedy).

## 📊 Problems Solved

Here is a list of the problems currently solved in this repository:

| # | Problem Name | Difficulty | Link to Solution | Topics |
|---|---|:---:|---|---|
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
            if len(parts) >= 6:
                num = parts[1].strip()
                topics = parts[5].strip()
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
        
        if num in topic_map and topic_map[num]:
            topics_list = ", ".join(topic_map[num])
        else:
            topics_list = "N/A"

        table_rows.append(f"| {num} | {name} | {difficulty} | [View]({link}) | {topics_list} |")

    table_content = '\n'.join(table_rows)
    
    # We use .format() to inject the rows into the {{table_content}} placeholder safely
    readme_content = README_TEMPLATE.format(table_content=table_content)

    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    main()
