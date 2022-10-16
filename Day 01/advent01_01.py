FILE = 'depths.txt';

rf = open(FILE);
arrNums = [];
# strip newline, add line to array for easier indexing
for line in rf.readlines():
	line = line.strip();
	arrNums.append(line);
rf.close();

increase_count=0;
i=0;
while i < len(arrNums):
	if i > 0:
		if int(arrNums[i]) > int(arrNums[i-1]):
			increase_count+=1;
	i+=1;

print(f"ANSWER: {increase_count}");
