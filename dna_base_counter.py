# DNA Base Counter
# A simple script to count the occurrence of each nucleotide base (A, T, G, C)
# in a given DNA sequence. Useful as a first step in sequence analysis
# and quality checking before alignment or phylogenetic analysis.

def count_bases(sequence):
    """
    Takes a DNA sequence as input and returns a count of each base.
    """
    sequence = sequence.upper()  # convert to uppercase for consistency

    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

    return counts


def gc_content(counts, total_length):
    """
    Calculates GC content (%) - an important metric in molecular biology
    since GC-rich regions affect DNA stability and PCR conditions.
    """
    gc_count = counts["G"] + counts["C"]
    gc_percentage = (gc_count / total_length) * 100
    return round(gc_percentage, 2)


# Example DNA sequence (you can replace this with your own sequence)
dna_sequence = "ATGCGATACGGCTTAACGTGCATGCCGATCGTAGCTAGCTGATCG"

# Run the analysis
base_counts = count_bases(dna_sequence)
total_length = len(dna_sequence)
gc_percent = gc_content(base_counts, total_length)

# Display results
print("DNA Sequence Analysis")
print("----------------------")
print(f"Sequence length: {total_length} bases")
print(f"Base counts: {base_counts}")
print(f"GC content: {gc_percent}%")
