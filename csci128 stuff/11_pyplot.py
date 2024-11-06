# Roman Rodriguez
# CSCI 128 - Section J
# Assessment 11
# References: No one
# Time: 30 minutes

import matplotlib.pyplot as plt

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

def create_amino_histogram(plot_name:str, aminos:list) -> None:
    plt.hist(aminos)
    plt.xlabel("Amino Acid Abbreviations")
    plt.ylabel("Counts")
    plt.title("Histogram of Amino Acids")
    plt.savefig(f"{plot_name}")

def create_GC_scatter(plot_name:str, gc_ratios:list, sequence_lengths:list) -> None:
    plt.scatter(gc_ratios, sequence_lengths)
    plt.xlabel("GC Content Ratio")
    plt.ylabel("Sequence Length")
    plt.title("Scatterplot of Sequence Length vs GC Content")
    plt.savefig(f"{plot_name}")

def create_base_lineplot(plot_name:str, sequence:str) -> None:
    aLst = []; aCnt = 0
    tLst = []; tCnt = 0
    gLst = []; gCnt = 0
    cLst = []; cCnt = 0
    for i in range(len(sequence)):
        if sequence[i] == "A":
            aCnt += 1
        elif sequence[i] == "T":
            tCnt += 1
        elif sequence[i] == "G":
            gCnt += 1
        elif sequence[i] == "C":
            cCnt += 1
        ratioA = aCnt / (i + 1)
        ratioT = tCnt / (i + 1)
        ratioG = gCnt / (i + 1)
        ratioC = cCnt / (i + 1)
        aLst.append(ratioA)
        tLst.append(ratioT)
        gLst.append(ratioG)
        cLst.append(ratioC)
    
    print(aLst)
    plt.plot(range(1, len(sequence) + 1), aLst, label="A")
    plt.plot(range(1, len(sequence) + 1), tLst, label="T")
    plt.plot(range(1, len(sequence) + 1), gLst, label="G")
    plt.plot(range(1, len(sequence) + 1), cLst, label="C")
    plt.legend(loc="best")
    plt.xlabel("Location in Sequence")
    plt.ylabel("Ratio Per Base")
    plt.title("Line Plot of Base Ratios")
    plt.savefig(f"{plot_name}")

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
