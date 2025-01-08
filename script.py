import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Simulated Data for Energy Consumption Patterns
data = {
    "Department": ["Production", "Logistics", "Administration", "R&D", "Maintenance"],
    "Energy Consumption (kWh)": [5000, 3000, 2000, 4000, 3500],
    "Cost ($)": [750, 450, 300, 600, 525],
    "Efficiency (%)": [85, 75, 90, 80, 78]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Bar Chart: Energy Consumption by Department
plt.figure(figsize=(10, 6))
sns.barplot(x="Department", y="Energy Consumption (kWh)", data=df, palette="Blues")
plt.title("Energy Consumption by Department")
plt.ylabel("Energy Consumption (kWh)")
plt.xlabel("Department")
plt.tight_layout()
plt.show()

# Scatter Plot: Cost vs. Energy Consumption
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Cost ($)", y="Energy Consumption (kWh)", hue="Department", data=df, s=100, palette="muted")
plt.title("Cost vs. Energy Consumption")
plt.xlabel("Cost ($)")
plt.ylabel("Energy Consumption (kWh)")
plt.tight_layout()
plt.show()

# Heatmap: Correlation Analysis
# Select only numeric columns for correlation
numeric_df = df.select_dtypes(include=["number"])
plt.figure(figsize=(8, 5))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Between Metrics")
plt.tight_layout()
plt.show()

# Save mock dataset for dashboard
mock_data_path = "mock_energy_consumption_data.csv"
df.to_csv(mock_data_path, index=False)
print(f"Mock dataset saved to {mock_data_path}")
