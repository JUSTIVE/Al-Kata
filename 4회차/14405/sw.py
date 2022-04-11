#%%
import re
tmp = re.sub('pi|ka|chu', '', input())
print('YES') if not tmp else print('NO')

