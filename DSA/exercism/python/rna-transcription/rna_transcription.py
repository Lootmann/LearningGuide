"""ran_transcription.py

Given a DNA strand, its transcribed RNA strand is formed by replacing
each nucleotide with its complement:

* `G` -> `C`
* `C` -> `G`
* `T` -> `A`
* `A` -> `U`
"""


def to_rna(dna_strand: str) -> str:
    rna = []

    for dna in dna_strand:
        if dna == "G":
            rna.append("C")
        elif dna == "C":
            rna.append("G")
        elif dna == "T":
            rna.append("A")
        else:
            rna.append("U")

    return "".join(rna)
