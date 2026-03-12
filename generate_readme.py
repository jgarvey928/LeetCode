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

| # | Problem Name | Difficulty | Link to Solution | Topics |
|---|---|:---:|---|---|
{table_content}
"""

def get_existing_topics():
    """Scans the current README to extract topics from BOTH the existing table and the extension's footer."""
    topic_map = {}
    if not os.path.exists('README.md'):
        return topic_map

    try:
        with open('README.md', 'r', encoding='utf-8') as f:
            content = f.read()
            
            # 1. RESCUE PREVIOUSLY SAVED TOPICS FROM OUR CLEAN TABLE
            for line in content.split('\n'):
                if line.startswith('|') and '[View]' in line:
                    parts = line.split('|')
                    if len(parts) >= 6:
                        num = parts[1].strip()
                        topics = parts[5].strip()
                        if topics and topics != "N/A":
                            topic_map[num] = [t.strip() for t in topics.split(',')]

            # 2. GRAB NEW TOPICS FROM THE EXTENSION'S MESSY FOOTER
            if '' in content:
                topics_section = content.split('')[1]
                if '' in topics_section:
                    topics_section = topics_section.split('')[0]
                
                sections = topics_section.split('## ')
                for section in sections[1:]:
                    lines = section.strip().split('\n')
                    if not lines:
                        continue
                    
                    current_topic = lines[0].strip()
                    
                    # Match [XXXX- to find problem numbers
                    problem_ids = re.findall(r'\[(\d{4})-', section)
                    
                    for pid in problem_ids:
                        if pid not in topic_map:
                            topic_map[pid] = []
                        if current_topic not in topic_map[pid]:
                            topic_map[pid].append(current_topic)
    except Exception:
        pass
    return topic_map

def get_difficulty_from_readme(folder_path):
    """Opens the README.md inside the problem folder and extracts the difficulty."""
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
    # 1. Grab all topics before we overwrite the file
    topic_map = get_existing_topics()

    # 2. Find all problem directories
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
        
        # 3. Get the topics we safely recorded. Join them, or use N/A if missing.
        if num in topic_map and topic_map[num]:
            topics_list = ", ".join(topic_map[num])
        else:
            topics_list = "N/A"

        table_rows.append(f"| {num} | {name} | {difficulty} | [View]({link}) | {topics_list} |")

    table_content = '\n'.join(table_rows)
    
    # 4. Generate the clean README content
    readme_content = README_TEMPLATE.format(table_content=table_content)

    # Overwrite the main README.md entirely
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)

if __name__ == "__main__":
    main()
