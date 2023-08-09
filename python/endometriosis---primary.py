# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"7E0D800","system":"readv2"},{"code":"BBL1.11","system":"readv2"},{"code":"K50..00","system":"readv2"},{"code":"K500000","system":"readv2"},{"code":"K500100","system":"readv2"},{"code":"K500200","system":"readv2"},{"code":"K506.00","system":"readv2"},{"code":"K50z.00","system":"readv2"},{"code":"12175.0","system":"med"},{"code":"16143.0","system":"med"},{"code":"19266.0","system":"med"},{"code":"19682.0","system":"med"},{"code":"20194.0","system":"med"},{"code":"22007.0","system":"med"},{"code":"22662.0","system":"med"},{"code":"30091.0","system":"med"},{"code":"3432.0","system":"med"},{"code":"36805.0","system":"med"},{"code":"36930.0","system":"med"},{"code":"37392.0","system":"med"},{"code":"41735.0","system":"med"},{"code":"42092.0","system":"med"},{"code":"42424.0","system":"med"},{"code":"48222.0","system":"med"},{"code":"49603.0","system":"med"},{"code":"499.0","system":"med"},{"code":"50464.0","system":"med"},{"code":"50518.0","system":"med"},{"code":"50544.0","system":"med"},{"code":"56751.0","system":"med"},{"code":"60097.0","system":"med"},{"code":"60784.0","system":"med"},{"code":"61192.0","system":"med"},{"code":"62982.0","system":"med"},{"code":"63232.0","system":"med"},{"code":"63749.0","system":"med"},{"code":"66361.0","system":"med"},{"code":"67137.0","system":"med"},{"code":"68037.0","system":"med"},{"code":"69931.0","system":"med"},{"code":"70854.0","system":"med"},{"code":"71993.0","system":"med"},{"code":"94268.0","system":"med"},{"code":"9492.0","system":"med"},{"code":"97045.0","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('endometriosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["endometriosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["endometriosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["endometriosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
