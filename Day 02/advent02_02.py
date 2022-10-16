FILE = 'positions.txt';

# get input as text into array
rf = open(FILE);
arrPos = [];
# strip newline, add line to array for easier indexing
for line in rf.readlines():
	line = line.strip();
	arrPos.append(line);
rf.close();

# begin problem
X=0;
Y=0;
AIM=0;

for pos in arrPos:
	if "forward" in pos:
		X+=int(pos[-1]);
		Y+=( AIM * int(pos[-1]) );
	elif "down" in pos:
		AIM+=int(pos[-1]);
	elif "up" in pos:
		AIM-=int(pos[-1]);

# print(f"[HORIZONTAL]: {X}");
# print(f"[DEPTH]: {Y}");
# print(f"[AIM]: {AIM}");
print(f"[ANSWER]: {X*Y}");