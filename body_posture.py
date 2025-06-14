import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("accelerometer\\final_data1.csv")  # Loading the CSV file

label_map = {
    0: "Sleeping",
    1: "Standing",
    2: "Sitting",
    3: "Running",
    4: "Forward Bending",
    5: "Backward Bending"
}
df["posture_name"] = df["label"].map(label_map)  # Map numeric labels to posture names

plt.figure(figsize=(15, 12)) #Plotting

plt.subplot(3, 1, 1)
plt.plot(df['index'], df['Ax1'], label='Ax1') 
plt.plot(df['index'], df['Ay1'], label='Ay1')
plt.plot(df['index'], df['Az1'], label='Az1')
plt.title('Sensor 1 Accelerations')
plt.xlabel('Time (index)')
plt.ylabel('Acceleration')
plt.legend() # Sensor 1

plt.subplot(3, 1, 2)
plt.plot(df['index'], df['Ax2'], label='Ax2')
plt.plot(df['index'], df['Ay2'], label='Ay2')
plt.plot(df['index'], df['Az2'], label='Az2')
plt.title('Sensor 2 Accelerations')
plt.xlabel('Time (index)')
plt.ylabel('Acceleration')
plt.legend() # Sensor 2

plt.subplot(3, 1, 3)
plt.plot(df['index'], df['label'], color='black', label='Posture Label')
plt.yticks(list(label_map.keys()), list(label_map.values()))
plt.title('Posture Labels Over Time')
plt.xlabel('Time (index)')
plt.ylabel('Posture')
plt.legend()  # Posture Labels

plt.tight_layout()
plt.show()