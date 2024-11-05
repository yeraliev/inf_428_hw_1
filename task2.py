import random
import unittest

class Department:
    def __init__(self, name, importance, users, threat_scores):
        self.name = name
        self.importance = importance
        self.users = users
        self.threat_scores = threat_scores

    def calc_mean(self):
        return sum(self.threat_scores) / len(self.threat_scores) if self else 0


class Company:
    def __init__(self, departments):
        self.departments = departments

    def aggregatedThreatScore(self):
        total_weighted_score = 0
        total_importance = 0

        for dep in self.departments:
            mean_score = dep.calc_mean()
            weighted_score = mean_score * dep.importance
            total_weighted_score += weighted_score
            total_importance += dep.importance

        if total_importance == 0:
            return 0

        aggregated_score = total_weighted_score / total_importance

        return aggregated_score


class TestCompanyThreatScore(unittest.TestCase):
    def test_noOutliners(self):
        users_Eng = 22
        users_mark = 33
        users_finance = 44
        users_hr = 55
        users_science = 66 

        engineering = Department("Engineering", importance=1, users=users_Eng, threat_scores=[random.randint(20, 50) for _ in range(users_Eng)])
        marketing = Department("Marketing", importance=2, users=users_mark, threat_scores=[random.randint(20, 50) for _ in range(users_mark)])
        finance = Department("Finance", importance=3, users=users_finance, threat_scores=[random.randint(20, 50) for _ in range(users_finance)])
        hr = Department("HR", importance=4, users=users_hr, threat_scores=[random.randint(20, 50) for _ in range(users_hr)])
        science = Department("Science", importance=5, users=users_science, threat_scores=[random.randint(20, 50) for _ in range(users_science)])
        
        company = Company([engineering, marketing, finance, hr, science])
    
        aggregated_score = company.aggregatedThreatScore()

        print("Aggregated score (no outliners)", aggregated_score)
    
    def test_meanThread(self):
        users_Eng = 22
        users_mark = 33
        users_finance = 44
        users_hr = 55
        users_science = 66 

        engineering = Department("Engineering", importance=1, users=users_Eng, threat_scores=[random.randint(30, 35) for _ in range(users_Eng)])
        marketing = Department("Marketing", importance=2, users=users_mark, threat_scores=[random.randint(30, 35) for _ in range(users_mark)])
        finance = Department("Finance", importance=3, users=users_finance, threat_scores=[random.randint(30, 35) for _ in range(users_finance)])
        hr = Department("HR", importance=4, users=users_hr, threat_scores=[random.randint(30, 35) for _ in range(users_hr)])
        science = Department("Science", importance=5, users=users_science, threat_scores=[random.randint(30, 35) for _ in range(users_science)])
        
        company = Company([engineering, marketing, finance, hr, science])
    
        aggregated_score = company.aggregatedThreatScore()

        print("Mean threat score are NOT far from each other", aggregated_score)
    
    def test_equalUsers(self):
        users = 10

        engineering = Department("Engineering", importance=1, users=users, threat_scores=[random.randint(0, 90) for _ in range(users)])
        marketing = Department("Marketing", importance=2, users=users, threat_scores=[random.randint(0, 90) for _ in range(users)])
        finance = Department("Finance", importance=3, users=users, threat_scores=[random.randint(0, 90) for _ in range(users)])
        hr = Department("HR", importance=4, users=users, threat_scores=[random.randint(0, 90) for _ in range(users)])
        science = Department("Science", importance=5, users=users, threat_scores=[random.randint(0, 90) for _ in range(users)])
        
        company = Company([engineering, marketing, finance, hr, science])
    
        aggregated_score = company.aggregatedThreatScore()

        print("Similiar number of users", aggregated_score)

    def test_equalImportance(self):
        users_Eng = 22
        users_mark = 33
        users_finance = 44
        users_hr = 55
        users_science = 66 

        engineering = Department("Engineering", importance=1, users=users_Eng, threat_scores=[random.randint(0, 90) for _ in range(users_Eng)])
        marketing = Department("Marketing", importance=1, users=users_mark, threat_scores=[random.randint(10, 90) for _ in range(users_mark)])
        finance = Department("Finance", importance=1, users=users_finance, threat_scores=[random.randint(10, 90) for _ in range(users_finance)])
        hr = Department("HR", importance=1, users=users_hr, threat_scores=[random.randint(10, 90) for _ in range(users_hr)])
        science = Department("Science", importance=1, users=users_science, threat_scores=[random.randint(10, 90) for _ in range(users_science)])
        
        company = Company([engineering, marketing, finance, hr, science])
    
        aggregated_score = company.aggregatedThreatScore()

        print("All departments has the same importance", aggregated_score)

if __name__ == "__main__":
    unittest.main()