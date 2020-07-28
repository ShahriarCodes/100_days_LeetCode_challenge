nparray1 = ([0, 1, 2, 3]) # Define an array
nparray2 = ([4, 5, 6, 7])
flavor4 = 0
for a, b in zip(nparray1, nparray2):
    flavor4 += a * b
flavor4
