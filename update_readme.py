import os
import re
import subprocess
from datetime import datetime

if __name__ == "__main__":
  cwd = os.getcwd()
  
  # collect unhidden directories
  directories = sorted([
    f for f in os.listdir()
    if os.path.isdir(os.path.join(cwd, f))
    and not f.startswith(".")
  ])

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

      # get creation date from git
      dates_str = subprocess.run([
        "git", "log",
        "--pretty=format:%cs",
        os.path.join(path, file),
      ], stdout=subprocess.PIPE)
      dates = [d for d in dates_str.stdout.decode('utf-8').split("\n") if d]
      if dates:
        date = re.match(r'.*(\d\d\d\d-\d\d-\d\d).*', dates[-1]).groups()[0]
      else:
        date = datetime.fromtimestamp(os.path.getmtime(os.path.join(path, file))).strftime("%Y-%m-%d")
      
      entries.append({
        "path": os.path.join(directory, file),
        "heading": heading,
        "date": date
      })

    topics.append({ "heading": directory, "entries": entries })

  # build readme file
  readme_file = os.path.join(cwd, "README.md")
  readme_list = []
  with open(readme_file) as f:
    for line in f:
      readme_list.append(line)
      if line.startswith("<!-- entries: start -->"):
        break
    
    readme_list.append("\n")
    
    for topic in topics:
      readme_list.append(f"## {topic['heading']}\n\n")
      for entry in topic["entries"]:
        readme_list.append(f"- [{entry['heading']}]({entry['path']}) - {entry['date']}\n")
      readme_list.append("\n")

  # write to readme file
  with open(readme_file, "w") as f:
    f.write("".join(readme_list)) 
