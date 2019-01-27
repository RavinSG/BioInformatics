gene_file = 'Salmonella_enterica.txt'
import deamination as deamin
from matplotlib import pyplot as plt


def clean_file():
    with open(gene_file, 'r', encoding='utf-8') as file:
        genome = ''
        for line in file:
            genome += line.strip()

    out = 'Salmonella_enterica_clean.txt'
    file = open(out, 'w', encoding='utf-8')
    file.write(genome)


cleaned = open('Vibrio_cholerae.txt', 'r', encoding='utf-8')
genome = ''
for line in cleaned:
    genome = line

count, min_loc = deamin.skew(genome)
plt.plot(count)
print(min_loc)

plt.show()
ori_posible = min_loc[0]
box_range = [ori_posible - 250, ori_posible + 250]

pos_DNAa_box = genome[box_range[0]: box_range[1]]
deamin.k_mers_d_mismatches(pos_DNAa_box, 9, 1)
