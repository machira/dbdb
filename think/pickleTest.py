import pickle, pprint

data1 = {'a':[1,2.0,3,4+6j],
	'b':('string',u'Unicode string'),
	'c':None}

selfref_list = [1,2,3]
selfref_list.append(selfref_list)

output = open('data.pkl','wb')

pickle.dump(data1, output)

pickle.dump(selfref_list, output, -1)
output.close()

pkl_file = open('data.pkl','rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

