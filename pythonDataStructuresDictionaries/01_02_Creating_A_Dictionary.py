sal_info = {'Austin': 91185, 'Boston': 90171}
print(sal_info)
sal_info['Boston'] = 95123
print(sal_info)
sal_info['Atlanta'] = 91234
print(sal_info)
print(len(sal_info))
del sal_info['Atlanta']
print(sal_info)
print(len(sal_info))
# print(sal_info['Atlanta'])
sal_info.clear()
print(sal_info)
print(len(sal_info))
