import glob, os, pickle
import math


def extractor(n=1):
    #n is number of opinions from each year"
    filename = "paragraphs/"
    datafiles = sorted(glob.glob(filename + "para_????"))
    test_files = []

    for d in datafiles:
        paragraphs = sorted(glob.glob(d + "/*.pkl"))
        for i, para in enumerate(paragraphs):
            if i > n:
                break
            myfile = loadDataset(para) 
            for j in myfile:    
                test_files.append(j)

    return test_files


