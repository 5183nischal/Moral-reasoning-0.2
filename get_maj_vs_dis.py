import glob, os, pickle
import math


def MajVsDisExtractor():

	filename = "sentences_new/"
	datafiles = sorted(glob.glob(filename + "sent_????"))
	test_files = []
	maj_op = []
	dis_op = []

	d = datafiles[-1]
	sentences = sorted(glob.glob(d + "/*.txt"))

	for i in range(len(sentences)):
		myfile = open(sentences[i],'r')
		data=myfile.read().replace('\n', '')
		if "MajOp" in sentences[i]:
			maj_op.append(data)
		elif "DisOp" in sentences[i]:
			dis_op.append(data)
	
		myfile.close()

	return maj_op, dis_op
