# Naam: Luc Hengeveld
# Datum: 1-1-2021


def main():
    """
    Output:
        - Print header en of de bijbehorende sequentie dna is
    """
    bestand = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna.fna"
    headers, seqs = lees_inhoud(bestand)

    zoekwoord = input("Geef een zoekwoord op: ")
    for i in range(len(headers)):
        if zoekwoord in headers[i]:
            print("Header:", headers[i])
            check_is_dna = is_dna(seqs[i])
            if check_is_dna:
                print("Sequentie is DNA")
                knipt(seqs[i])
            else:
                print("Sequentie is geen DNA. Er is iets fout gegaan.")


def lees_inhoud(bestands_naam):
    """
    Parameters:
        - bestands_naam - naam van het bestand
    Output:
        - headers - lijst met headers
        - seqs - lijst met sequenties
    """
    bestand = open(bestands_naam)
    headers = []
    seqs = []
    seq = ""
    for line in bestand:
        line = line.strip()
        if ">" in line:
            if seq != "":
                seqs.append(seq)
                seq = ""
            headers.append(line)
        else:
            seq += line.strip()
    seqs.append(seq)
    return headers, seqs


def is_dna(seq):
    """
    Parameters:
        - seq - sequentie uit de seqs lijst dat wordt meegegeven in de main
    Output:
        - dna - boolean wat aangeeft of de sequentie wel of niet dna is
    """
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a + t + c + g
    if total == len(seq):
        dna = True
    return dna


def knipt(alpaca_seq):
    """
    Parameters:
        - alpaca_seq - sequentie uit de seqs lijst dat wordt meegegeven in main
    Output:
        - Print welke enzymen knippen in de sequentie
    """
    bestand = open("enzymen.txt")
    for line in bestand:
        naam, seq = line.split(" ")
        seq = seq.strip().replace("^", "")
        if seq in alpaca_seq:
            print(naam, "knipt in sequentie")


main()
