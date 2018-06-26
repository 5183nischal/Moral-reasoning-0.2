import glob, os, pickle
import math


def extractor(n=1):
    #n is number of opinions from each year"
    filename = "paragraphs/"
    datafiles = sorted(glob.glob(filename + "para_????"))
    test_files = []
    year = []
    cases_per_year = []
    y = 1891
    case_names = []
    for d in datafiles:
        sentences = sorted(glob.glob(d + "/*.pkl"))
        for i, sentence in enumerate(sentences):
            if i >= n:
                break
            myfile = loadDataset(sentence) 
            test_files.append(myfile)
            year.append(y)
            #adding case no and judge no.
            case_n = ""
            flag = False
            for j in sentence:
            	if j == "X":
            		flag = True
            	if j == "_":
            		flag = False
            	if j == ".":
            		flag = False
            	if flag == True:
            		case_n += j
            case_names.append(case_n)

            myfile.close()
        cases_per_year.append(len(sentences))
        y += 1
    return test_files, year, cases_per_year, case_names

a,b,c,d = extractor()
print(a, d)

