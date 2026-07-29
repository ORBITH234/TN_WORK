
# Drill 4: Reading the Final State
## Instructions

## Programs track states as they change over time. Review this sequence:

## **Starting State:** 
## * Heat Dial: `5`
## * Bread Color: `"WHITE"`

## **Instructions Run:**
## 1. Set Toaster Power to ON.
## 2. Wait 300 seconds.
## 3. Set Toaster Power to OFF. 

## *(Note: A heating time of 300 seconds at Heat Dial 5 will completely incinerate the bread).*

## **Your Task:** 
## Update the `bread_color` variable below by reassigning it to the correct final state string. Choose exactly from one of these options: `"WHITE"`, `"GOLDEN_BROWN"`, or `"BURNT_BLACK"`.





class Simulator:
    def get_final_state(self):
        # Starting State
        bread_color = "WHITE"
        
        # The toaster runs at Level 5 for 300 seconds. 
        # Reassign bread_color to its new state below:
        bread_color = "BURNT_BLACK" 
        
        return bread_color


def test_simulator():
    # Do not modify this testing wrapper
    sim = Simulator()
    return sim.get_final_state()

def solution():
    return test_simulator()