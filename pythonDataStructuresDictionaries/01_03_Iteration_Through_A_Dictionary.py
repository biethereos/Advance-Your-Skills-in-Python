sal_info = dict()
print(sal_info)
sal_info = {'Austin': 911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 89286}
print(sal_info)
if ('Dallas' in sal_info):
    print(sal_info['Dallas'])
else:
    print('not found')
    
for location in sal_info:
    print(sal_info[location])
    
for location in sal_info:
    print(location)