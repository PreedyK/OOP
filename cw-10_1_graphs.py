import matplotlib.pyplot as plt
import numpy as np

x = np.array(["c1", "c2", "c3", "c4"])
y = np.array([24, 98, 47, 68])

print("Mean: ", np.mean(y))
print("Median: ", np.median(y))
print(np.std(y))

plt.xlabel("Courses")
plt.ylabel("Grades")

plt.plot(x,y)
plt.show()


mylabels = ["a1", "a2", "a3", "a4"]
plt.pie(y, labels=mylabels)
plt.show()


x = np.array(["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"])
y = np.array([21, 19, 24, 17, 16, 25, 24, 22, 21, 21])

plt.plot(x, y)
plt.show()

mylabels = ["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"]
plt.pie(y, labels=mylabels)
plt.show()

x = np.array(["2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020"])
y = np.array([21, 19, 24, 17, 16, 25, 24, 22, 21, 21])
plt.scatter(x,y)
plt.show()