import random
import unittest

class Department:
    def __init__(self, name, users, threat_scores):
        self.name = name
        self.users = users
        self.threat_scores = threat_scores

    def calc_mean(self):
        return sum(self.threat_scores) / len(self.threat_scores) if self else 0


class Company:
    def __init__(self, departments):
        self.departments = departments

    def aggregatedThreatScore(self):
        total_weighted_score = 0

        for dep in self.departments:
            mean_score = dep.calc_mean()
            weighted_score = mean_score
            total_weighted_score += weighted_score
    
        return total_weighted_score


class TestCompanyThreatScore(unittest.TestCase):
    def test_oneHighMean(self):
        users = 10

        engineering = Department("Engineering", users=users, threat_scores=[random.randint(20, 30) for _ in range(users)])
        marketing = Department("Marketing", users=users, threat_scores=[random.randint(20, 30) for _ in range(users)])
        finance = Department("Finance", users=users, threat_scores=[random.randint(20, 30) for _ in range(users)])
        hr = Department("HR", users=users, threat_scores=[random.randint(20, 30) for _ in range(users)])
        science = Department("Science", users=users, threat_scores=[random.randint(80, 90) for _ in range(users)])
        
        company = Company([engineering, marketing, finance, hr, science])
    
        aggregated_score = company.aggregatedThreatScore()

        print("One separtment has a high threat score, others low", aggregated_score)
    
    def test_sameMean(self):
        users = 10

        engineering = Department("Engineering", users=users, threat_scores=[random.randint(30, 35) for _ in range(users)])
        marketing = Department("Marketing", users=users, threat_scores=[random.randint(30, 35) for _ in range(users)])
        finance = Department("Finance", users=users, threat_scores=[random.randint(30, 35) for _ in range(users)])
        hr = Department("HR", users=users, threat_scores=[random.randint(30, 35) for _ in range(users)])
        science = Department("Science", users=users, threat_scores=[random.randint(30, 35) for _ in range(users)])
        
        company = Company([engineering, marketing, finance, hr, science])
    
        aggregated_score = company.aggregatedThreatScore()

        print("All departments have quite same threat scores", aggregated_score)
    
    def test_sameMeanOneHigh(self):
        users = 10

        engineering = Department("Engineering", users=users, threat_scores=[22,30,25,29,22,24,26,24,28,30])
        marketing = Department("Marketing", users=users, threat_scores=[23,27,25,26,27,28,26,24,29,25])
        finance = Department("Finance", users=users, threat_scores=[20,18,24,20,17,14,17,90,18,22])#Finance department has 1 user with very high threat score
        hr = Department("HR", users=users, threat_scores=[25,24,28,26,27,26,28,25,29,22])
        science = Department("Science", users=users, threat_scores=[23,28,26,27,25,28,27,25,28,23])
        
        company = Company([engineering, marketing, finance, hr, science])
    
        aggregated_score = company.aggregatedThreatScore()

        print("All departments has the same mean(26) threat score", aggregated_score)

    def test_differentUsers(self):
        users_Eng = 22
        users_mark = 33
        users_finance = 44
        users_hr = 55
        users_science = 66 

        engineering = Department("Engineering", users=users_Eng, threat_scores=[random.randint(0, 90) for _ in range(users_Eng)])
        marketing = Department("Marketing", users=users_mark, threat_scores=[random.randint(0, 90) for _ in range(users_mark)])
        finance = Department("Finance", users=users_finance, threat_scores=[random.randint(0, 90) for _ in range(users_finance)])
        hr = Department("HR", users=users_hr, threat_scores=[random.randint(0, 90) for _ in range(users_hr)])
        science = Department("Science", users=users_science, threat_scores=[random.randint(0, 90) for _ in range(users_science)])
        
        company = Company([engineering, marketing, finance, hr, science])
    
        aggregated_score = company.aggregatedThreatScore()

        print("All departments has the different number of users", aggregated_score)

if __name__ == "__main__":
    unittest.main()
