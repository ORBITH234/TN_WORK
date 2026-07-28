class Toaster:
    def warm_pastry(self):
        # Replace the 0s with the correct settings for a pastry
        heat_level = 1
        timer_seconds = 60
        
        return heat_level, timer_seconds


def test_toaster():
    # Do not modify this testing wrapper
    my_toaster = Toaster()
    return list(my_toaster.warm_pastry())

def solution():
    return test_toaster()