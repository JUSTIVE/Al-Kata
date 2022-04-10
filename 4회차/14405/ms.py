import re
print("YES" if (re.sub(r'pi|ka|chu', r'', input()) == '') else "NO")
