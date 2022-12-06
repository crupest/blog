#! /usr/bin/env python3

import os
from os.path import *
from subprocess import run
import sys
from rich.prompt import Confirm
from rich.console import Console

script_dir = dirname(__file__)
project_dir = normpath(dirname(script_dir))
posts_dir = join(project_dir, "content", "posts")

console = Console()

if len(sys.argv) == 1:
    to_do = Confirm.ask(
        "You don't specify post name to generate. Do you want me to detect and process all?", console=console)
    if not to_do:
        exit(0)
    files = [f[:-len(".docx")]
             for f in os.listdir(posts_dir) if f.endswith(".docx") and not f.startswith('~$')]
    console.print("Will process:")
    for file in files:
        console.print(file, style="magenta")
else:
    files = sys.argv[1:]
    for file in files:
        if not isfile(join(posts_dir, f"{file}.docx")):
            console.print(f"[magenta]{file}[/] not found.", style="red")
            exit(1)

for file in files:
    run(["pandoc", join(posts_dir, f"{file}.docx"),
        "-o", join(posts_dir, f"{file}.docx.md")], check=True)

    if not exists(join(posts_dir, f"{file}.md")):
        run(["hugo", "new", join(posts_dir, f"{file}.md")], check=True)

    with open(join(posts_dir, f"{file}.md"), "r") as f:
        content = f.read()

    first_occur = content.find("---")
    if first_occur == -1:
        console.print(f"Front matter not found.", style="red")
        exit(2)
    second_occur = content.find("---", first_occur + 3)
    if second_occur == -1:
        console.print("Front matter not found.", style="red")
        exit(2)

    front_matter = content[:second_occur + 3]

    with open(join(posts_dir, f"{file}.docx.md"), "r") as f:
        new_content = front_matter + "\n" + f.read()

    with open(join(posts_dir, f"{file}.md"), "w") as f:
        f.write(new_content)
