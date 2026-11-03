* THIS PROJECT IS CURRENTLY INCOMPLETE *

=== STATUS ===
In its current status, this program can show a protein's:
- primary structure
- aminoacid composition (both absolute and relative)
- molecular weight
- isoelectric point
- hydrophobicity

=== HOW TO DOWNLOAD/INSTALL ===
1) Click on the "<> Code" button and select "Download ZIP".
2) Extract the downloaded archive.
3) Open a terminal in the extracted folder and execute:
   (on Windows:) "python -m venv venv", followed by: "venv/Scripts/activate", followed by: "pip install -r requirements.txt".
   (on MacOS:) "python3 -m venv venv", followed by: "source venv/bin/activate", followed by: "pip install -r requirements.txt".
   (on Linux:) "python3 -m venv venv", followed by: "source venv/bin/activate", followed by: "pip install -r requirements.txt".

=== HOW TO USE ===
1) Download the sequence you want to analyze (in FASTA format) from a public database like UniProt.
2) Rename the sequence as "s.fasta" and move into the program's directory.
3) Execute "ProPred.sh" in a terminal.

=== CONTENTS ===
- mainscript.py The current main script
- README.txt    This file (not necessary)
- ProPred.sh    The main executable file
- s.fasta       Test sequence (not necessary)
- s2.fasta      Another test sequence (not necessary)

=== OTHER ===
- This project relies on the "biopython" library
