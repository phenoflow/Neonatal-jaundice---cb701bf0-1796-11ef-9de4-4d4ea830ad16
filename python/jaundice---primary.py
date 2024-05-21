# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"7269.0","system":"readv2"},{"code":"103252.0","system":"readv2"},{"code":"94612.0","system":"readv2"},{"code":"19581.0","system":"readv2"},{"code":"48638.0","system":"readv2"},{"code":"71056.0","system":"readv2"},{"code":"48869.0","system":"readv2"},{"code":"69317.0","system":"readv2"},{"code":"45303.0","system":"readv2"},{"code":"19583.0","system":"readv2"},{"code":"28184.0","system":"readv2"},{"code":"92680.0","system":"readv2"},{"code":"65651.0","system":"readv2"},{"code":"35477.0","system":"readv2"},{"code":"64140.0","system":"readv2"},{"code":"8069.0","system":"readv2"},{"code":"66985.0","system":"readv2"},{"code":"47340.0","system":"readv2"},{"code":"106539.0","system":"readv2"},{"code":"63838.0","system":"readv2"},{"code":"70324.0","system":"readv2"},{"code":"59451.0","system":"readv2"},{"code":"98034.0","system":"readv2"},{"code":"104225.0","system":"readv2"},{"code":"70762.0","system":"readv2"},{"code":"39164.0","system":"readv2"},{"code":"47802.0","system":"readv2"},{"code":"93156.0","system":"readv2"},{"code":"89653.0","system":"readv2"},{"code":"48012.0","system":"readv2"},{"code":"48009.0","system":"readv2"},{"code":"57133.0","system":"readv2"},{"code":"61800.0","system":"readv2"},{"code":"58833.0","system":"readv2"},{"code":"1359.0","system":"readv2"},{"code":"3211.0","system":"readv2"},{"code":"40869.0","system":"readv2"},{"code":"55360.0","system":"readv2"},{"code":"59695.0","system":"readv2"},{"code":"68206.0","system":"readv2"},{"code":"28361.0","system":"readv2"},{"code":"3615.0","system":"readv2"},{"code":"35625.0","system":"readv2"},{"code":"35507.0","system":"readv2"},{"code":"7828.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('neonatal-jaundice-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["jaundice---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["jaundice---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["jaundice---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
