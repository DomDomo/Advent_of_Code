lines = []

with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def print_paper(paper):
    for line in paper:
        print(line)

    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")

def make_fold(coord, line, paper):
    if coord == "x":
        for y in range(len(paper)):
            paper[y][line] = '-'

        reverse = []
        fold = paper[0].index('-')+1
        for line in paper:
            reverse.append(line[fold:][::-1])
        
        for x in range(len(reverse)):
            for y in range(len(reverse[0])):
                paper[x][y] = "#" if paper[x][y] == "#" or reverse[x][y] == "#" else "."


        new_paper = []
        for line in paper:
            new_paper.append(line[:fold-1])
        
    else:
        paper[line] = ['-'] * int(max_x+1)

        reverse = []
        max_y = len(paper)-1
        for y in range(max_y, 0, -1):
            if paper[y][0] == "-": break
            reverse.append(paper[y])

        for x in range(len(reverse)):
            for y in range(len(reverse[0])):
                paper[x][y] = "#" if paper[x][y] == "#" or reverse[x][y] == "#" else "."

        new_paper = []
        for line in paper:
            if line[0][0] == "-": break
            new_paper.append(line)


    return new_paper

def count_holes(paper):
    holes = 0
    for line in paper:
        holes += line.count("#")

    return holes

blank_line = lines.index("")
coords = [((coord.split(",")[0]), coord.split(",")[1]) for coord in lines[:blank_line]]
folds = [(fold.split("=")[0][-1], fold.split("=")[1]) for fold in lines[blank_line+1:]]
coords = [(int(a), int(b)) for a, b in coords]
folds = [(a, int(b)) for a, b in folds]


xs, ys = zip(*coords)
max_x = max(xs)
max_y = max(ys)



paper = []
for _ in range(max_y+1):
    paper.append(['.'] * int(max_x+1))



for coord in coords:
    x, y = coord
    paper[y][x] = "#"

#print_paper(paper)

for fold in folds:
    coord, line = fold
    paper = make_fold(coord, line, paper)
    #print_paper(paper)
    print(count_holes(paper))

textfile = open("display.txt", "w")
for element in paper:
    textfile.write(" ".join(str(x) for x in element))
    textfile.write("\n")
textfile.close()
