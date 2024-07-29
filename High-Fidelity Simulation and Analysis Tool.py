import numpy as np
import matplotlib.pyplot as plt

# Parameters
dt = 0.01  # time step
t = np.arange(0, 10, dt)  # time array
x = np.zeros_like(t)  # position array
v = np.zeros_like(t)  # velocity array

# Initial conditions
x[0] = 0
v[0] = 1

# Simulation loop
for i in range(1, len(t)):
    a = -0.1 * v[i-1]  # example acceleration: simple damping
    v[i] = v[i-1] + a * dt
    x[i] = x[i-1] + v[i-1] * dt

# Plot results
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Position vs Time')
plt.xlabel('Time [s]')
plt.ylabel('Position [m]')

plt.subplot(2, 1, 2)
plt.plot(t, v)
plt.title('Velocity vs Time')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')

plt.tight_layout()
plt.show()
