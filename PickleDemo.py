import pickle

myList = ['a', 'b', 'c', 'd']

with open('datafile.txt', 'wb') as fh:
    pickle.dump(myList, fh)

with open('datafile.txt', 'rb') as fh:
    unpickledList = pickle.load(fh)

print(unpickledList)

x = pickle.dumps(['Paul', 21, 7, 1966])
y = pickle.loads(x)
print(y)

this_int = 55
this_string = 'oh my goodness'
my_dict_of_lists = {
    'a': [1, 2, 3],
    'b': [4, 5, 6]
}
query_results = [('joe', 22, 'clerk'), ('pete', 34, 'salesman')]
with open('datafile2.txt', 'wb') as fh:
    pickle.dump((this_int, this_string, my_dict_of_lists, query_results), fh)
with open('datafile2.txt', 'rb') as fh:
    tup = pickle.load(fh)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])