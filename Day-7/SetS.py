# Sets are implemented using hash tables in Python.
# This provides O(1) average time complexity for lookups and insertions.
# Overall complexity for union/intersection is linear O(N) relative to the set sizes,
# which is optimal for unsorted data.

aida_roll_no = {70, 71, 72, 73, 74, 75, 76}  # Removed duplicate 73
aidb_roll_no = {70, 63, 72, 79, 74, 86, 76}

print("aida_roll_no:\n", aida_roll_no)

# Using '|' operator for union
print("union of aid a & b:\n", aida_roll_no | aidb_roll_no)

# Using '&' operator for intersection
# Python automatically optimizes this to iterate over the smaller set
print("intersection of aid a & b:\n", aida_roll_no & aidb_roll_no)
