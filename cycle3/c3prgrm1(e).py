import statistics as s
list1=[20,40,60,40,80,100]
print("mean :",s.mean(list1))
print("median :",s.median(list1))
print("mode :",s.mode(list1))
print("harmonic mean:",s.harmonic_mean(list1))
print("statistics variance:",s.variance(list1))
print()
print("s.median low:",s.median_low([1,3,5,7,9,11,13]))
print("s.median low:",s.median_low([1,3,5,7,9,11]))
print("s.median low:",s.median_low([-12,6.6,-3.4,6,7.1,-9,22]))

