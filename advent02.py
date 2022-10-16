FILE = 'assets/depths.txt';

rf = open(FILE);
arrNums = [];
# strip newline, add line to array for easier indexing
for line in rf.readlines():
	line = line.strip();
	arrNums.append(line);
rf.close();

i=0;
increase_count=0;
while i < ( len(arrNums) - 3 ):
	winOne=0;
	winTwo=0;
	winOne = sum([int(arrNums[i]), int(arrNums[i+1]), int(arrNums[i+2])]);
	winTwo = sum([int(arrNums[i+1]), int(arrNums[i+2]), int(arrNums[i+3])]);

	if int(winOne) < int(winTwo):
		increase_count+=1;
	i+=1;

print(f"ANSWER: {increase_count}");