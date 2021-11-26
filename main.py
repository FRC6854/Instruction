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
{}{}{}Experimental | Do not currently use with decimals 

"""

ratio = 10

for i in front.splitlines():
    print(i.format("\u001b[36m", "\u001b[34m", "\u001b[1m\u001b[31m"))

print("{}File: {}".format("\u001b[34m", "\u001b[0m"), end="")

file_path = input()

print("{}Line per second: {}".format("\u001b[34m", "\u001b[0m"), end="")
ratio = int(input())

if os.path.exists(file_path):
    with open(file_path) as f:
        data = f.read()
    
    past = []
    past_split = [0, 0]
    bakery = ""
    for i, data in tqdm(enumerate(data.splitlines()), desc="Converting File"):
        coords = data.split(",")
        if data != past:
            bakery += f"{i*ratio} goto {float(coords[0])-float(past_split[0])} {float(coords[1])-float(past_split[1])}\n"
        past = data
        past_split = data.split(",")
    
    print("{}Extracted file: ".format("\u001b[34m"), end="")

    with open(input(), "w") as f:
        f.write(bakery)