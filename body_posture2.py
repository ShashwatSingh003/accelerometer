import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("accelerometer\\final_data1.csv")

plt.figure(figsize=(10, 4))
plt.plot(df['index'], df['Ax1'], color='red')
plt.title('Ax1 - Sensor 1 (X-axis)')
plt.xlabel('Time (index)')
plt.ylabel('Acceleration')
plt.grid(True)
plt.tight_layout()
plt.show() # Plot Ax1 (Sensor 1 - X Axis)

plt.figure(figsize=(10, 4))
plt.plot(df['index'], df['Ax2'], color='blue')
plt.title('Ax2 - Sensor 2 (X-axis)')
plt.xlabel('Time (index)')
plt.ylabel('Acceleration')
plt.grid(True)
plt.tight_layout()
plt.show() # Plot Ax2 (Sensor 2 - X Axis)

plt.figure(figsize=(10, 4))
plt.plot(df['index'], df['Ay1'], color='green')
plt.title('Ay1 - Sensor 1 (Y-axis)')
plt.xlabel('Time (index)')
plt.ylabel('Acceleration')
plt.grid(True)
plt.tight_layout()
plt.show() # Plot Ay1 (Sensor 1 - Y Axis)

plt.figure(figsize=(10, 4))
plt.plot(df['index'], df['Ay2'], color='orange')
plt.title('Ay2 - Sensor 2 (Y-axis)')
plt.xlabel('Time (index)')
plt.ylabel('Acceleration')
plt.grid(True)
plt.tight_layout()
plt.show() # Plot Ay2 (Sensor 2 - Y Axis)

plt.figure(figsize=(10, 4))
plt.plot(df['index'], df['Az1'], color='purple')
plt.title('Az1 - Sensor 1 (Z-axis)')
plt.xlabel('Time (index)')
plt.ylabel('Acceleration')
plt.grid(True)
plt.tight_layout()
plt.show() # Plot Az1 (Sensor 1 - Z Axis)

plt.figure(figsize=(10, 4))
plt.plot(df['index'], df['Az2'], color='brown')
plt.title('Az2 - Sensor 2 (Z-axis)')
plt.xlabel('Time (index)')
plt.ylabel('Acceleration')
plt.grid(True)
plt.tight_layout()
plt.show() # Plot Az2 (Sensor 2 - Z Axis)