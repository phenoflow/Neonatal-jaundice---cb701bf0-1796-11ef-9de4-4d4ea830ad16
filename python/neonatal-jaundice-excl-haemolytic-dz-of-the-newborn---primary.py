# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"Qyu5800","system":"readv2"},{"code":"Q433800","system":"readv2"},{"code":"Q434200","system":"readv2"},{"code":"Q433300","system":"readv2"},{"code":"Q432.00","system":"readv2"},{"code":"Q433600","system":"readv2"},{"code":"Q433500","system":"readv2"},{"code":"Q430000","system":"readv2"},{"code":"Q436200","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('neonatal-jaundice-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["neonatal-jaundice-excl-haemolytic-dz-of-the-newborn---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["neonatal-jaundice-excl-haemolytic-dz-of-the-newborn---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["neonatal-jaundice-excl-haemolytic-dz-of-the-newborn---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)