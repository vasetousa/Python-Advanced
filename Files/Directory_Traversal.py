import os
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

files = next(os.walk(input()))    # reads the files in the current directory -> "."
by_extentions = {}
for file in files:
    ext = file.split(".")[-1]
    if ext not in by_extentions:
        by_extentions[ext] = []
    by_extentions[ext].append(file)
with open(desktop, 'w') as output:
    for ext in sorted(by_extentions.keys()):
        files = sorted(by_extentions[ext])
        print(f".{ext}", file=output)
        print(f".{ext}\n")

        for file in files:
            print(f'---{file}')
            print(f'---{file}', file=output)
