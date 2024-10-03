#!usr/bim/env python3 
# Thadchanon Maidee (Ice-lnwza)
# 670510662
# HW14_1
# 204111 Sec 001

def read_file(filename, mode="rt"):
    with open(filename,mode,encoding="utf-8") as input_:
        return input_.read()

def append_ranking(infile_name: str="score_in.txt", outfile_name: str="score_out.txt"):
    with open(infile_name, "rt", encoding="utf-8") as input_:
        lists = input_.read().split('\n')

    lists = list(map(lambda x :x.split() ,lists))
    d_1 = dict()
    d_2 = dict()
    d_s = dict()
    for i in lists:

        point = map(lambda x: 0 if x == 'None' else float(x),i[1:])
        if i != []:
            d_1[i[0]] = sum(sorted(point, reverse=True)[:2]) 

        if i != []:
            d_2[i[0]] = i[1:]
        
    sort_ = sorted(d_1,key = lambda x: d_1[x],reverse=True)

    for x in range(len(sort_)):
        item = ' '.join(d_2.get(sort_[x]))
        d_s[sort_[x]] = f"{item} {x+1}"
    tmp = [] 
    for i in d_2:
        item = ''.join(d_s.get(i))
        tmp.append(f"{i} {item}")

    with open(outfile_name, "wt") as outfile:
        with open (infile_name,"rt") as lists:
            temp = "\n".join(sorted(tmp, key=lambda x: x[0]))
            outfile.write(temp)

if __name__ == '__main__':
    append_ranking()
    print(read_file("./score_out.txt"))
    # print("Allpass")

