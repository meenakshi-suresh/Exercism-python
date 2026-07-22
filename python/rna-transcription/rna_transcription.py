"""This module provides a function to transcribe a DNA strand into its corresponding RNA strand.
The transcription process involves replacing each nucleotide in the DNA strand 
with its complementary RNA nucleotide:
- Guanine (G) is transcribed to Cytosine (C)
- Cytosine (C) is transcribed to Guanine (G)
- Thymine (T) is transcribed to Adenine (A)
- Adenine (A) is transcribed to Uracil (U)
Non-nucleotide characters in the input DNA strand remain unchanged.
Example:
    >>> to_rna("GCTA")
    'CGAU'
    >>> to_rna("AGCTAGC")
    'UCGAUCG'
    >>> to_rna("XYZ")
    'XYZ'
"""
def to_rna(dna_strand):
    """Transcribes a given DNA strand into its corresponding RNA strand.

    Args:
        dna_strand (str): A string representing the DNA strand.

    Returns:
        str: A string representing the transcribed RNA strand.
    """
    # Create a translation table for DNA to RNA transcription
    translation_table = str.maketrans("GCTA", "CGAU")
    return dna_strand.translate(translation_table)
