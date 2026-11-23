import os

os.makedirs("/output", exist_ok=True)

LINE = "I finally organized my life into folders, and now I can't find anything because I named them all 'misc'."

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)