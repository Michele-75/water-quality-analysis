# Visualize water quality trends
library(ggplot2)
library(dplyr)

# Read processed data
data <- read.csv("data/processed/sensors_2024_clean.csv")

# Create time series plot
ggplot(data, aes(x = as.POSIXct(paste(date, time)), y = pH, color = station_id)) +
  geom_line() +
  geom_point() +
  labs(title = "pH Levels by Station",
       x = "Date/Time",
       y = "pH") +
  theme_minimal()
