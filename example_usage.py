"""
Example usage of the process_uci_format function
"""

import pandas as pd
from process_uci_format import process_uci_format

# Example: Create a sample dataframe similar to UCI format
sample_data = {
    'Date': ['16/12/2006', '16/12/2006', '16/12/2006'],
    'Time': ['17:24:00', '17:25:00', '17:26:00'],
    'Global_active_power': [4.216, 5.360, 5.374],
    'Global_reactive_power': [0.418, 0.436, 0.498],
    'Voltage': [234.840, 233.630, 233.290],
    'Global_intensity': [18.400, 23.000, 23.000],
    'Sub_metering_1': [0.000, 0.000, 0.000],
    'Sub_metering_2': [1.000, 1.000, 2.000],
    'Sub_metering_3': [17.000, 16.000, 17.000]
}

df_sample = pd.DataFrame(sample_data)
print("Original DataFrame:")
print(df_sample)
print("\n" + "="*50 + "\n")

# Process the UCI format
processed_df = process_uci_format(df_sample)

if processed_df is not None:
    print("Processed DataFrame (long format):")
    print(processed_df.head())
    print(f"\nShape: {processed_df.shape}")
else:
    print("Processing failed - returned None")

# Example with alternative column names (to test robustness)
print("\n" + "="*50 + "\n")
print("Testing with alternative column names:")

sample_data_alt = {
    'date': ['16/12/2006', '16/12/2006'],
    'time ': ['17:24:00', '17:25:00'],  # Note: space after 'time'
    'GLOBAL_ACTIVE_POWER': [4.216, 5.360],
    'Sub_metering_1': [0.000, 0.000],
    'Sub_metering_2': [1.000, 1.000]
}

df_sample_alt = pd.DataFrame(sample_data_alt)
print("Alternative DataFrame:")
print(df_sample_alt)
print("\n" + "="*30 + "\n")

processed_df_alt = process_uci_format(df_sample_alt)
if processed_df_alt is not None:
    print("Processed DataFrame:")
    print(processed_df_alt.head())
else:
    print("Processing failed")