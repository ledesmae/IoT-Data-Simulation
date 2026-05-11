import random
import time
import pandas as pd

# Function to simulate IoT sensor data
def generate_iot_data(samples=10):

    data = []

    for i in range(samples):

        sensor_id = f"Sensor_{i+1}"

        temperature = round(random.uniform(20.0, 35.0), 2)

        humidity = random.randint(40, 80)

        air_quality = random.randint(50, 300)

        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        data.append([
            sensor_id,
            temperature,
            humidity,
            air_quality,
            timestamp
        ])

        time.sleep(1)

    return pd.DataFrame(
        data,
        columns=[
            "Sensor ID",
            "Temperature (°C)",
            "Humidity (%)",
            "Air Quality Index (AQI)",
            "Timestamp"
        ]
    )

# Generate simulated IoT data
iot_data = generate_iot_data(10)

# Display data
print(iot_data)

# Export to CSV
iot_data.to_csv("iot_data.csv", index=False)

print("CSV file saved successfully!")