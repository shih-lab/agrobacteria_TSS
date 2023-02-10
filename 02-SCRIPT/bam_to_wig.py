import subprocess
from tqdm import tqdm 
from glob import glob
import os

IN="../../02-OUTPUT/03-ALIGN/02-SEGEMEHL"
for seq in tqdm(glob(f"{IN}/*_sorted.bam")):
    handle = seq.split(".bam")[0]
    #print(handle)
    os.system(f'perl ./make_proper_wig.pl {handle}.bam + > {handle}_forward.wig')
    os.system(f'perl ./make_proper_wig.pl {handle}_reverse.bam - > {handle}_reverse.wig')
