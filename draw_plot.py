import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
cpu = [3.210, 204.985, 819.601, 20488.946]
cpu_gmp = [0.439, 17.472, 70.040, 1744.965]
cuda = [0.451, 11.254, 43.914, 1083.594]

group_labels = ['256', '2048', '4096', '20480']
plt.title('Running time vs. No. of N with Different processors\n')
plt.xlabel('Number of N')
plt.ylabel('Running Time(s)')

# group_labels = ['seq', '1', '4', '8', '16', '32']

# plt.plot(x1, y1, 'r', label='broadcast')
# plt.plot(x2, y2, 'b', label='join')
# plt.xticks(x1, group_labels, rotation=0)

plt.plot(x, cpu, 'r', label='cpu', marker='.')
plt.plot(x, cpu_gmp, 'b', label='cpu-gmp', marker='.')
plt.plot(x, cuda, 'y', label='cuda', marker='.')

# plt.plot(x4, y4, 'b', label='join')
plt.xticks(x, group_labels, rotation=0)

plt.legend(title="Processor", bbox_to_anchor=[0.3, 1])
plt.grid()
plt.savefig("plot.png")
plt.show()
