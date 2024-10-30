# Roman Rodriguez
# CSCI 128 - Section J
# Assessment 10
# References: Jesse Paulsen
# Time: 30 minutes

def dna_to_rna(sequence:str) -> str:
    rnaseq = ""
    for i in range(len(sequence)):
        if sequence[i] == "A":
            rnaseq += "U"
        elif sequence[i] == "T":
            rnaseq += "A"
        elif sequence[i] == "G":
            rnaseq += "C"
        elif sequence[i] == "C":
            rnaseq += "G"
    
    return rnaseq

def parse_file_into_acids(filename:str) -> list:
    contents = []
    with open(filename, "r") as file:
        for i in file:
            contents.append(i.split())

    return contents

if __name__ == "__main__":
    codonData = input("CODONS_FILENAME> ")
    seqData = input("SEQUENCES_FILENAME> ")
    output = input("OUTPUT_FILENAME> ")

    masterList = []
    codons = parse_file_into_acids(codonData)

    with open(seqData, "r") as seqs:
        for i in seqs:
            substring = ""
            if i != "DONE":
                oneSeq = i.strip()
                substring = substring + oneSeq + " "
                rnaSeq = dna_to_rna(oneSeq)
                startInd = rnaSeq.index("AUG")
                while True:
                    currentCodon = rnaSeq[startInd:startInd+3]
                    if currentCodon == "UAA" or currentCodon == "UAG" or currentCodon == "UGA":
                        break
                    for i in range(len(codons)):
                        if currentCodon == codons[i][0]:
                            substring += codons[i][2]
                    startInd += 3       
                substring += "\n"
                masterList.append(substring)             

    f = open(output, "w")
    for i in range(len(masterList)):
        f.write(masterList[i])            
    f.close()
