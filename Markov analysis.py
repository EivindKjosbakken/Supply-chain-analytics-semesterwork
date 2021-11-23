import numpy as np


mu_rep = 1/8
failure_rate = 0.005

A = np.array([[-mu_rep, mu_rep, 0], [failure_rate, -failure_rate-mu_rep, mu_rep], [0, failure_rate, -failure_rate]])

t = 0
end_t = 8
dt = end_t / 800
Pt = np.array([0, 0, 1])
pts = []
pts.append(Pt[0])


while t <= end_t:
    t += dt
    Pt = np.dot(Pt, (A*dt + np.identity(3)))
    pts.append(Pt[0])


print(f"Average hours down each day with backup machine is: {np.average(pts)*8}")
