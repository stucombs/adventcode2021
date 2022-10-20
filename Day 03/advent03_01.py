FILE = 'diagnostics.txt';

# get input from file into array
rf = open(FILE);
arr_bins = [];
# strip newline, add line to array for easier indexing
for line in rf.readlines():
	line = line.strip();
	arr_bins.append(line);
rf.close();

g_rate=''; # 5 bit number
e_rate='';
arr_bits = [];# <-- needs to be 2D array

# create sub array for length of each number
for d in range(len(arr_bins[0])):
	arr_bits.append([]);

# fill sub arrays with corresponding bits
for num in arr_bins:
	for i,bit in enumerate(num):
		arr_bits[i].append(bit);

for arr in arr_bits:
	z=0;
	o=0;
	for bit in arr:
		if bit == '0':
			z+=1;
		else:
			o+=1;
	if z > o:
		g_rate += '0';
		e_rate += '1';
	else:
		g_rate += '1';
		e_rate += '0';

gamma = int(g_rate,2);
epsilon = int(e_rate,2);

print(gamma * epsilon);