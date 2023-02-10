from tqdm import tqdm
from glob import glob
import os 

IN="../../02-OUTPUT/02-TRIM"
OUT="../../02-OUTPUT/03-ALIGN"
for seq in tqdm(glob(f"{IN}/*-R1-trimmed.fq.gz")):
    if "BV1" in seq:
        ref = f'{OUT}/BV1-C58.idx'
        db = '../../01-INPUT/04-REFERENCE/BV1-C58.fna'
    if "BV2" in seq:
        ref = f'{OUT}/BV2-C16_80.idx'
        db = f'../../01-INPUT/04-REFERENCE/BV2-C16_80.fna'
    if "BV3" in seq:
        ref = f'{OUT}/BV3-T60_94.idx'
        db = f'../../01-INPUT/04-REFERENCE/BV3-T60_94.fna' 

    seq_handle = seq.split('/')[-1].split('.')[0][:-11]
    r1 = seq_handle + "-R1"
    r2 = seq_handle + "-R2"
    print(seq_handle)
    
    os.system(f"time segemehl.x -t 10 -s\
        -i {ref} \
        -d {db} \
        -q {IN}/{r1}-trimmed_filtered.fq.gz \
        -p {IN}/{r2}-trimmed_filtered.fq.gz \
        -o {OUT}/{seq_handle}_filtered.sam")
    
    os.system(f'samtools view --threads 10 -bS {OUT}/{seq_handle}_filtered.sam > {OUT}/{seq_handle}_filtered.bam')
    os.system(f'samtools sort --threads 10 {OUT}/{seq_handle}_filtered.bam -o {OUT}/{seq_handle}_filtered_sorted.bam')
    os.system(f'rm {OUT}/{seq_handle}_filtered.sam')
    os.system(f'rm {OUT}/{seq_handle}_filtered.bam')

    os.system(f"time segemehl.x -t 10 -s\
        -i {ref} \
        -d {db} \
        -q {IN}/{r1}-trimmed.fq.gz \
        -p {IN}/{r2}-trimmed.fq.gz \
        -o {OUT}/{seq_handle}.sam")

    os.system(f'samtools view --threads 10 -bS {OUT}/{seq_handle}.sam > {OUT}/{seq_handle}.bam')
    os.system(f'samtools sort --threads 10 {OUT}/{seq_handle}.bam -o {OUT}/{seq_handle}_sorted.bam')
    os.system(f'rm {OUT}/{seq_handle}.sam')
    os.system(f'rm {OUT}/{seq_handle}.bam')