import unittest

def Cal_Gpa(marks):

    if 1 <= marks <50:
        return "F"

    elif 50 <= marks < 60:
        return "B"

    elif 60 <= marks <70:
        return "A-"

    elif 70 <= marks <80:
        return "A"

    elif 80 <= marks <=100:
        return "A+"

    else:
        return "F"

class TestGPA(unittest.TestCase):
    def test_cal(self):
        self.assertEqual(Cal_Gpa(0),"F")
        self.assertEqual(Cal_Gpa(49),"F")
        self.assertEqual(Cal_Gpa(50),"B")
        self.assertEqual(Cal_Gpa(59), "B")
        self.assertEqual(Cal_Gpa(60),"A-")

class TestCGPA(unittest.TestCase):
    def test_cal(self):
        self.assertEqual(Cal_Gpa(69) ,"A-")
        self.assertEqual(Cal_Gpa(70),"A")
        self.assertEqual(Cal_Gpa(79),"A")
        self.assertEqual(Cal_Gpa(80),"A+")
        self.assertEqual(Cal_Gpa(100),"A+")

if __name__ == '__main__':
    unittest.main()