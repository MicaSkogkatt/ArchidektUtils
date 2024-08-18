# Path to the export from Archidekt.
# The export should *not* contain the DateAdded column,
# since that one is allowed to be different for two mergable entries
inputfile = "placeholder1.csv"
# Where you want your output-csv
outputfile = "placeholder2.csv"

# Get all lines for processing
with open(inputfile, 'r') as file:
    lines = file.readlines()

# Setup before looping through
output_lines = []
idx_to_check = list(range(len(lines)))
idx_to_ignore = []
merged = 0

# Loop through all entries,
# unless a match have already been found for the row, try to match it against all subsequent rows
for idx in idx_to_check:
    if idx in idx_to_ignore:
        # This row has already been merged with a previous row, skip
        continue
    new_row = lines[idx] # What will be written to the new file, if no merge occurs it will be written as is
    search_for = lines[idx].split(",", 1)
    quantity = search_for[0]  # The amount
    pattern = search_for[1]  # The row without "Quantity"
    for idy in range(idx+1,len(lines)):  # Going through all subsequent rows
        line = lines[idy].split(",", 1)
        if line[1] == pattern:  # Match found!
            # Do the merge! (aka update quantity)
            quantity = int(quantity) + int(line[0])
            new_row = str(quantity) + "," + pattern
            # Printout to inform user
            print('Merging')
            print("Entry " + str(idx) + ": " + str(search_for))
            print("Entry " + str(idy) + ": " + str(line))
            print('>>')
            print(new_row)
            # Mark it so it isn't duplicated
            idx_to_ignore.append(idy)
            # This is just to give user the stats
            merged = merged + 1
    # Add to pending output
    output_lines.append(new_row)

# Write to output-file
with open(outputfile, 'w') as file:
    file.write(''.join(str(i) for i in output_lines))

print("Done, merged " + str(merged) + " rows")
