# {} shows that the defined item is dictionary
# bunch of key value pairs
# d={'w1:'d1,'k1':'v1' ....}
d={'word':'definition','felony':'crime','chump':'a fool','penace':'self-punishment','fiddle':'cheating'}
d1={'key1':'abc','key2':'bcd','key3':'jhk','key4':'poi'}
print(" directory1", d,"\n","directory2", d1)
print("To get the value of given key  such as key2, felony:print(directoryname[keyname]) ")
print(d1['key2'])
print(d['felony'])

# To add value in dictionary
d1['key5']='new_value'
d1['key6']='another_new_val'

print ("after adding new values",d1)
# to replace a value
d1['key2']='replaced value'
print ("after replacing value in key2",d1)

# to create a list inside dictionary
dict={ 'listname': [2,3,4,5,6],
        'gold':50000,
        'location':'India'}
print("Dictionary with list",dict)
print("length of list inside the dict", len(dict['listname']))
#print("printing selected items from list", dict['listname[0:2]'])
# to delete a KV pairs
del d['word']
print(" directory1 after deletion", d)
