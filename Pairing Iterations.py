import itertools

my_string = 'a0:12:90:00:80:43'
mac = my_string.replace(':','')

#Using Join and Zip
[" ".join(pair) for pair in zip(* 2 * [iter(mac)])]

#Using Zip and Slicing
[i+j for i,j in zip(mac[::2], mac[1::2])]

#Using Itertools Join and Zip
si = iter(mac)
[''.join(each) for each in itertools.izip(si, si)]

#Using Itertools Map and Zip
map(''.join, itertools.izip(si, si))

#Output - ['a0', '12', '90', '00', '80', '43']
