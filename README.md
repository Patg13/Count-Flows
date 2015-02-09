# Count-Flows
Fasta Flows Counting python 3 script / program

Compatibility 
This program has been programmed on Linux Ubuntu 14.04  (Biolinux build)

This program has been made to obtain a flows (454 pyrosequencing) count from a regular fasta file
This porgram is NOT compatible with Illumina or Ion Torrent sequencing technologies

This program can be launch locally or sent to the bin folder (you can remove the .py extension for easier use)

Here the options:

-h   Display Help
-in  Fasta File path (REQUIRED)
-out Output text filename (REQUIRED)
-tech 454 Pyrosequencing Technology Type*

*This program is compatible with 454 pyrosequencing FLX and FLX+
Use "-tech A" for FLX
Use "-tech B" for FLX+

Here's an linux commandline exemple:

./count-flows.py -in Seq.fasta -out Flows_tab.txt -tech B

The output file is a tabulation delimited table of this format:

Sequence_Name flows_count

In case you use a Fasta sequence which contain nucleotide ambiguity (N), the Flows count will be equal to "NA"
