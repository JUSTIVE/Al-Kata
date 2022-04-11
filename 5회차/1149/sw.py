#%%
n = int(input())
colors = list()
for _ in range(n):
    colors.append(list(map(int, input().split())))

# %%
for i in range(1, n):
    colors[i][0] = colors[i][0] + min(colors[i-1][1], colors[i-1][2])
    colors[i][1] = colors[i][1] + min(colors[i-1][0], colors[i-1][2])
    colors[i][2] = colors[i][2] + min(colors[i-1][1], colors[i-1][0])

print(min(colors[n-1]))


# %%
