"""protein_translation.py

Translate RNA sequences into proteins.
"""
from typing import Generator


def is_terminated(protein: str) -> bool:
    return protein in ("UAA", "UAG", "UGA")


def codon_to_protein(protein: str) -> str:
    if protein in ("AUG"):
        return "Methionine"

    if protein in ("UUU", "UUC"):
        return "Phenylalanine"

    if protein in ("UUA", "UUG"):
        return "Leucine"

    if protein in ("UCU", "UCC", "UCA", "UCG"):
        return "Serine"

    if protein in ("UAU", "UAC"):
        return "Tyrosine"

    if protein in ("UGU", "UGC"):
        return "Cysteine"

    if protein in ("UGG"):
        return "Tryptophan"

    return protein


def codons(strand: str) -> Generator:
    for codon in [strand[3 * i : 3 * i + 3] for i in range(len(strand) // 3)]:
        yield codon


def proteins(strand: str) -> list:
    result = []

    for codon in codons(strand):
        if is_terminated(codon):
            return result

        result.append(codon_to_protein(codon))

    return result
