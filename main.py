import os, sys
try:
    from tqdm import tqdm
except ImportError:
    sys.exit("Install Requirements")

front = """
{}██╗░░░██╗{}██╗██╗░░██╗██╗███╗░░██╗░██████╗░
{}██║░░░██║{}██║██║░██╔╝██║████╗░██║██╔════╝░
{}╚██╗░██╔╝{}██║█████═╝░██║██╔██╗██║██║░░██╗░
{}░╚████╔╝{}░██║██╔═██╗░██║██║╚████║██║░░╚██╗
{}░░╚██╔╝{}░░██║██║░╚██╗██║██║░╚███║╚██████╔╝
{}░░░╚═╝{}░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚═════╝░
{}{}Instruction System translator for 2D CSV
{}{}{}Experimental

"""

ratio = 10

for i in front.splitlines():
    print(i.format("\u001b[36m", "\u001b[34m", "\u001b[1m\u001b[31m"))

print("{}File: {}".format("\u001b[34m", "\u001b[0m"), end="")

file_path = input()

print("{}Line per second: {}".format("\u001b[34m", "\u001b[0m"), end="")
ratio = int(input())

if os.path.exists(file_path):
    with open("test.csv") as f:
        data = f.read()
    
    past = []
    bakery = ""
    for i, data in tqdm(enumerate(data.splitlines()), desc="Converting File"):
        coords = data.split(",")
        if data != past:
            bakery += f"{i*ratio} goto {coords[0]} {coords[1]}\n"
        past = data
    
    print("{}Extracted file: ".format("\u001b[34m"), end="")

    with open(input(), "w") as f:
        f.write(bakery)