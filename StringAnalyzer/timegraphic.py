import matplotlib.pyplot as plt

lines = [10000, 100000, 1000000]
linesn = [0.1, 1, 10]
_RegEx = [0.030254840850830078, 0.27523016929626465, 2.707456588745117]
_SMC = [0.5280139446258545, 5.248928070068359, 53.19554615020752]
_PLY = [0.3620951175689697, 3.3886730670928955, 35.02669358253479]

plt.title('Зависимость времени обработки от кол-ва строк')
plt.xlabel('Кол-во строк, шт * 10^5')
plt.ylabel('Время, с')
plt.grid()

#fig, ax = plt.subplots()

plt.plot(linesn, _RegEx, label='RegEx')
plt.plot(linesn, _SMC, label='SMC')
plt.plot(linesn, _PLY, label='PLY')



plt.legend()

plt.show()