#!/usr/bin/env python3
"""
New calibration method for pH sensors.
Uses temperature compensation.
"""

def calibrate_ph(raw_ph, temperature):
    """Apply temperature compensation to pH readings."""
    # Temperature compensation formula
    temp_coefficient = 0.003
    reference_temp = 25.0

    corrected_ph = raw_ph + temp_coefficient * (temperature - reference_temp)

    return round(corrected_ph, 2)

# Test the function
if __name__ == "__main__":
    test_ph = 7.5
    test_temp = 20.0
    print(f"Raw pH: {test_ph}")
    print(f"Temperature: {test_temp}°C")
    print(f"Corrected pH: {calibrate_ph(test_ph, test_temp)}")
