import pickle

fp = open('sample_pickle.dat', 'rb')
n = pickle.load(fp)
n1 = pickle.load(fp)
i = 0
while i < n:
    x = pickle.load(fp)
    print(x)
    i += 1
fp.close()
