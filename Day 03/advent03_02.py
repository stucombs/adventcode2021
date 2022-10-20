# To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, 
# and keep only numbers with that bit in that position. 
# If 0 and 1 are equally common, keep values with a 1 in the position being considered.

# To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, 
# and keep only numbers with that bit in that position. 
# If 0 and 1 are equally common, keep values with a 0 in the position being considered.
FILE = 'diagnostics.txt';

# get input from file into array
rf = open(FILE);
arr_bins = [];
# strip newline, add line to array for easier indexing
for line in rf.readlines():
	line = line.strip();
	arr_bins.append(line);
rf.close();

arr_bins = [
'00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010',
];

o2_rate='';
co_rate='';
idx=0;
bit_len = len(arr_bins[0]);

arr_bins_copy = arr_bins[:];
while idx < bit_len:
	one=0;
	zero=0;	
	for num in arr_bins:
		if num[idx] == '0':
			zero+=1;
		elif num[idx] == '1':
			one+=1;
	if one > zero:
		for num in arr_bins[:]:
			if num[idx] == '0' and len(arr_bins) > 1:
				arr_bins.remove(num);
		for num in arr_bins_copy[:]:
			if num[idx] == '1' and len(arr_bins_copy) > 1:
				arr_bins_copy.remove(num);

	elif zero > one:
		for num in arr_bins[:]:
			if num[idx] == '1' and len(arr_bins) > 1:
				arr_bins.remove(num);
		for num in arr_bins_copy[:]:
			if num[idx] == '0' and len(arr_bins_copy) > 1:
				arr_bins_copy.remove(num);

	elif zero == one:
		for num in arr_bins[:]:
			if num[idx] == '0' and len(arr_bins) > 1:
				arr_bins.remove(num);
		for num in arr_bins_copy[:]:
			if num[idx] == '1' and len(arr_bins_copy) > 1:
					arr_bins_copy.remove(num);
	# print(f"At Index {idx}: ");
	print("ARRAY ONE");
	print(arr_bins);
	print("ARRAY TWO");
	print(arr_bins_copy);
	idx+=1;

o2_rate = int(arr_bins[0],2);
co_rate = int(arr_bins_copy[0],2);

print(f"[O2] {o2_rate}");
print(f"[CO2] {co_rate}");

print(f"[ANSWER] {o2_rate * co_rate}");
# 674412 == too low!
# RUN FOR CO2 RATE

# Keep only numbers selected by the bit criteria for the type of rating value
#  for which you are searching. Discard numbers which do not match the bit criteria.
# If you only have one number left, stop; this is the rating value for which you are searching.
# Otherwise, repeat the process, considering the next bit to the right.

# Finally, to find the life support rating, 
# multiply the oxygen generator rating (23) by the CO2 scrubber rating (10) to get 230.