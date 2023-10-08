import pickle

mp = None

with open('model_pickle','rb') as file:
    mp = pickle.load(file)

COLUMNS = ['buying','maint','doors','persons','lug_boot','safety']
CLASSES = ['Un-Acceptable','Acceptable','Good','Very Good']

# Value Replacements
# buying : ('vhigh','high','med','low') = (1,2,3,4)
# maint : ('vhigh','high','med','low') = (1,2,3,4)
# doors : ('2','3','4','5more') = (1,2,3,4)
# persons : ('2','4','more') = (1,2,3)
# lug_boot : ('small','med','big') = (1,2,3)
# safety : ('low','med','high') = (1,2,3) 
# CLASSES : ('unacc','acc','good','vgood') = (1,2,3,4)


# ans = mp.predict([[4, 4, 4, 3, 3, 3]]) # high end car

# ans = mp.predict([[1, 1, 1, 1, 1, 1]]) # low end car

ans = mp.predict([[3, 3, 3, 2, 2, 2]]) # Avg car


idx = int(str(ans[0])[-2])

print(f'Prediction : {CLASSES[idx-1]}')



