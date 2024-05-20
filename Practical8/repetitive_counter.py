# provide the sequence
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
def count_repeats(seq):
    count = 0
    pattern = r'GTGTGT|GTCTGT'  # define repeated sequence patterns
    for i in range(0, len(seq), len(pattern)):
        count += seq.count(pattern)
    return count

# calculate and print the total number of repetitive elements
print(f"The total number of repetitive elements is: {count_repeats(seq)}")