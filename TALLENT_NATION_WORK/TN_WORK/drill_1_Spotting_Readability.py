# Python is famous for its high-level readability, meaning its code often looks close to standard English. 

# Review these two ways to check if a crumb tray is full:
#* **Option A:** `IF READ_SENSOR_REG_0x04 > 0.85 THEN TRIGGER_ALARM_LIGHT`
# * **Option B:** `if crumb_tray.is_full(): toaster.trigger_warning_light()`

# **Your Task:**
# Identify which option represents Python's focus on human-friendly readability.
# 1. Inside the `best_option` method, replace the empty string with either `"A"` or `"B"`.
# 2. Ensure you use a capitalized letter inside the string quotes.

class Readability:
    def best_option(self):
        # Replace the empty string with the correct option letter
        return "B"


def test_readability():
    # Do not modify this testing wrapper
    reader = Readability()
    return reader.best_option()

def solution():
    return test_readability()