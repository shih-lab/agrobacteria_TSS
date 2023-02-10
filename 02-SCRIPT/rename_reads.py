import pandas as pd
import os
from glob import glob
from tqdm import tqdm

sample_desc = {'01': '01-C58-BV1-MOPS_glucose-tex_plus',
 '02': '02-C16_80-BV2-MOPS_glucose-tex_plus',
 '03': '03-T60_94-BV3-MOPS_glucose-tex_plus',
 '04': '04-C58-BV1-MOPS_succinate-tex_plus',
 '05': '05-C16_80-BV2-MOPS_succinate-tex_plus',
 '06': '06-T60_94-BV3-MOPS_succinate-tex_plus',
 '07': '07-C58-BV1-PITA_log-tex_plus',
 '08': '08-C16_80-BV2-PITA_log-tex_plus',
 '09': '09-T60_94-BV3-PITA_log-tex_plus',
 '10': '10-C58-BV1-PITA_induced-tex_plus',
 '11': '11-C16_80-BV2-PITA_induced-tex_plus',
 '12': '12-T60_94-BV3-PITA_induced-tex_plus',
 '13': '13-C58-BV1-PITA_stationary-tex_plus',
 '14': '14-C16_80-BV2-PITA_stationary-tex_plus',
 '15': '15-T60_94-BV3-PITA_stationary-tex_plus',
 '16': '16-C58-BV1-MOPS_glucose-tex_minus',
 '17': '17-C16_80-BV2-MOPS_glucose-tex_minus',
 '18': '18-T60_94-BV3-MOPS_glucose-tex_minus',
 '19': '19-C58-BV1-MOPS_succinate-tex_minus',
 '20': '20-C16_80-BV2-MOPS_succinate-tex_minus',
 '21': '21-T60_94-BV3-MOPS_succinate-tex_minus',
 '22': '22-C58-BV1-PITA_log-tex_minus',
 '23': '23-C16_80-BV2-PITA_log-tex_minus',
 '24': '24-T60_94-BV3-PITA_log-tex_minus',
 '25': '25-C58-BV1-PITA_induced-tex_minus',
 '26': '26-C16_80-BV2-PITA_induced-tex_minus',
 '27': '27-T60_94-BV3-PITA_induced-tex_minus',
 '28': '28-C58-BV1-PITA_stationary-tex_minus',
 '29': '29-C16_80-BV2-PITA_stationary-tex_minus',
 '30': '30-T60_94-BV3-PITA_stationary-tex_minus'}

samples = []

for path in glob('/*'):
    file = path.split('/')[-1]
    sample = file.split('-')[1][:2]
    samples.append(sample)
    read = file.split('_')[3]
    desc = sample_desc[sample] + '-' + read
    os.rename(path, 'reads/' + desc + '.fq.gz')
    
for path in tqdm(glob('/*.fq.gz')):
    out_path = path.split('.')[0] + '.fa'
    os.system('seqtk seq -a ' + path + ' > ' + out_path)
    os.system('bzip2 ' + out_path)
    os.system('rm '+ path)
    os.system('rm ' + out_path)