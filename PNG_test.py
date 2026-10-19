import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Malgun Gothic"
steps = [4610, 5553, 6042, 5536, 9780]
days = ['월', '화', '수', '목', '금']

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(days, steps)

for i, p in enumerate(steps):
 ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
xytext=(0, 8), ha="center")
ax.set_title("월 ~ 금 활동 걸음수")
fig.savefig("my_first_chart.png")