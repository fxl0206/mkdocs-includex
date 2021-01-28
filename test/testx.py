import os
import sys
import csv 

TPLX='\
|    | animal_1   | animal_2   |\n\
|---:|:-----------|:-----------|\n\
|  0 | elk        | dog        |\n\
|  1 | pig        | quetzal    |'

def parseCsv(path):
    cmd_str = ''
    with open(path,encoding= 'gbk')as f:
        f_csv = csv.reader(f)
        line = 0
        for row in f_csv :
            curRow='|'
            for col in row:
                curRow=curRow+col+"|"
            if line == 0 :
                hsp='|'
                for col in row:
                    hsp=hsp+":---"+"|"
                curRow=curRow+"\n"+hsp
            cmd_str=cmd_str+"\n"+curRow
            line=line+1
        return cmd_str
#主机名|IP|端口|用户|密码
#---|---|---|---|---
#www.hubx.site|10.19.83.188|线下|archapp|线下
def main(argv):
    path=os.path.splitext("1.txt")[-1]
    print(path)
    print(parseCsv("./hosts-info.csv"))
    print(TPLX)


if __name__ == "__main__":
   main(sys.argv[1:])