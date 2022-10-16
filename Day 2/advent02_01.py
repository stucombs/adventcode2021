# forward X increases the horizontal position by X units.
# down X increases the depth by X units.
# up X decreases the depth by X units.

FILE = 'positions.txt';

rf = open(FILE);
arrPos = [];
# strip newline, add line to array for easier indexing
for line in rf.readlines():
	line = line.strip();
	arrPos.append(line);
rf.close();

X=0;
Y=0;
for pos in arrPos:
	if 'forward' in pos:
		X+=int(pos[-1]);
	elif 'down' in pos:
		Y+=int(pos[-1]);
	elif 'up' in pos:
		Y-=int(pos[-1]);

# print(f"[HORIZONTAL]: {X}");
# print(f"[DEPTH] {Y}");
print(f"ANSWER: {Y*X}");