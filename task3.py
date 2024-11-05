import unittest


def time_calc(hour1, hour2):
    difference = abs(hour1 - hour2)
    difference_time = 24 - difference
    return min(difference, difference_time)
    

class testFeatureTransformation(unittest.TestCase):
    def test1(self):
        res = time_calc(23, 1)
        print("Test 23:00 and 1:00:", res)
    
    def test2(self):
        res = time_calc(12, 18)
        print("Test 12:00 and 18:00:", res)
    
    def test3(self):
        res = time_calc(20, 5)
        print("Test 20:00 and 5:00:", res)

if __name__ == "__main__":
    unittest.main()