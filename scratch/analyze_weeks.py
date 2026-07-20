import os
import re

content_dir = r"c:\Users\ADMIN\OneDrive\Máy tính\WorkShopAWS\content\1-Worklog"
weeks = sorted([d for d in os.listdir(content_dir) if os.path.isdir(os.path.join(content_dir, d))])

out_path = r"c:\Users\ADMIN\OneDrive\Máy tính\WorkShopAWS\scratch\weeks_report.txt"

with open(out_path, "w", encoding="utf-8") as out:
    for w in weeks:
        vi_path = os.path.join(content_dir, w, "_index.vi.md")
        en_path = os.path.join(content_dir, w, "_index.md")
        
        vi_title = "None"
        en_title = "None"
        vi_objectives = []
        en_objectives = []
        
        if os.path.exists(vi_path):
            with open(vi_path, "r", encoding="utf-8") as f:
                content = f.read()
                title_match = re.search(r'title:\s*"(.*?)"', content)
                if title_match:
                    vi_title = title_match.group(1)
                # Find lines starting with * under objectives
                obj_match = re.search(r'### Mục tiêu.*?:(.*?)###', content, re.DOTALL)
                if obj_match:
                    vi_objectives = [line.strip("* ").strip() for line in obj_match.group(1).strip().split("\n") if line.strip().startswith("*")]
                    
        if os.path.exists(en_path):
            with open(en_path, "r", encoding="utf-8") as f:
                content = f.read()
                title_match = re.search(r'title:\s*"(.*?)"', content)
                if title_match:
                    en_title = title_match.group(1)
                obj_match = re.search(r'### Week.*?Objectives:(.*?)###', content, re.DOTALL)
                if obj_match:
                    en_objectives = [line.strip("* ").strip() for line in obj_match.group(1).strip().split("\n") if line.strip().startswith("*")]
                    
        out.write(f"Directory: {w}\n")
        out.write(f"  VI Title: {vi_title}\n")
        out.write(f"  EN Title: {en_title}\n")
        out.write(f"  VI Obj: {vi_objectives[:2]}\n")
        out.write(f"  EN Obj: {en_objectives[:2]}\n")
        out.write("-" * 40 + "\n")
