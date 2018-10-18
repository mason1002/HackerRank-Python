import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y20 = [2.268582820892334, 0.4268920421600342, 0.2154300212860107, 0.3706350326538086, 0.257220983505249, 0.5425059795379639]
y100 = [9.689239978790283, 1.789544820785522, 0.6943740844726562, 0.8800060749053955, 1.085325956344604, 1.112133979797363]
y500 = [50.80551314353943, 9.349034786224365, 3.156141042709351, 3.715785980224609, 2.4549400806427, 2.700001001358032]
y1000 = [97.1613028049469, 18.15434384346008, 6.434377908706665, 7.40651798248291, 8.951137065887451, 5.766917943954468]

group_labels = ['seq', '1', '4', '8', '16', '32']
plt.title('Running time vs. Count of Processors with Different Regions\n')
plt.xlabel('Count of Processors')
plt.ylabel('Running Time(s)')

# group_labels = ['seq', '1', '4', '8', '16', '32']

# plt.plot(x1, y1, 'r', label='broadcast')
# plt.plot(x2, y2, 'b', label='join')
# plt.xticks(x1, group_labels, rotation=0)

plt.plot(x, y20, 'r', label='20', marker='.')
plt.plot(x, y100, 'b', label='100', marker='.')
plt.plot(x, y500, 'y', label='500', marker='.')
plt.plot(x, y1000, 'g', label='1000', marker='.')
# plt.plot(x4, y4, 'b', label='join')
plt.xticks(x, group_labels, rotation=0)

plt.legend(title="Vertices", bbox_to_anchor=[0.95, 1])
plt.grid()
plt.savefig("plot.png")
plt.show()
