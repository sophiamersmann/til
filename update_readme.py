import os
from datetime import datetime

if __name__ == "__main__":
  cwd = os.getcwd()
  
  # collect unhidden directories
  directories = [
    f for f in os.listdir()
    if os.path.isdir(os.path.join(cwd, f))
    and not f.startswith(".")
  ]

  # collect entries within directories
  topics = []
  for directory in directories:
    path = os.path.join(cwd, directory)
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    entries = []
    for file in files:
      heading = file
      with open(os.path.join(path, file)) as f:
        for line in f:
          line = line.strip()
          if line.startswith('# '):
            heading = line[1:].strip()
            break
      
      entries.append({
        "path": os.path.join(directory, file),
        "heading": heading,
        "date": datetime.fromtimestamp(os.path.getmtime(os.path.join(path, file))).strftime("%Y-%m-%d")
      })

    topics.append({ "heading": directory, "entries": entries })

  # build readme file
  readme_file = os.path.join(cwd, "README.md")
  readme_list = []
  with open(readme_file) as f:
    for line in f:
      if line.strip().startswith("## "):
        break
      readme_list.append(line)
    
    readme_list.append("\n")
    
    for topic in topics:
      readme_list.append(f"## {topic['heading']}\n\n")
      for entry in topic["entries"]:
        readme_list.append(f"- [{entry['heading']}]({entry['path']}) - {entry['date']}\n")
      readme_list.append("\n")

  # write to readme file
  with open(readme_file, "w") as f:
    f.write("".join(readme_list)) 
