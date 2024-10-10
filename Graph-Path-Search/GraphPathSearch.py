''' - Main function - JJ McCauley - '''

import timeit
from uninformedsearch import uninformedsearch

cities = {
    'Buffalo': {'Boston': 450, 'Pittsburg': 219},
    'Boston': {'Buffalo': 450, 'New York': 216},
    'Pittsburg': {'Buffalo': 219, 'New York': 370, 
                  'Philadelphia': 304, 'Baltimore': 248},
    'New York': {'Pittsburg': 370, 'Philadelphia': 94},
    'Philadelphia': {'New York': 94, 'Pittsburg': 304,
                     'Baltimore': 101, 'Salisbury': 138},
    'Baltimore': {'Pittsburg': 248, 'Philadelphia': 101,
                  'Salisbury': 117, 'Washington DC': 45},
    'Washington DC': {'Baltimore': 45, 'Salisbury': 116,
                      'Richmond': 110},
    'Salisbury': {'Philadelphia': 138, 'Baltimore': 117,
                  'Washingtom DC': 116, 'Norfolk': 132},
    'Richmond': {'Washington DC': 110, 'Norfolk': 93},
    'Norfolk': {'Richmond': 93, 'Salisbury': 132}
}

# Getting start and end cities from user
startCity = input("Enter Start City: ")
while startCity not in cities:
    startCity = input("ERROR - Start City not found. Please try again: ")
endCity = input("Enter End City: ")
while endCity not in cities:
    endCity = input("ERROR - End city not found. Please try again: ")

# Create uninformedsearch object to use searches in module
s = uninformedsearch()

# Breadth First Search
execution_time1 = timeit.timeit(lambda: s.bfs(cities, startCity, endCity, pr_path=True, pr_totDist=True), number=1)
print("Execution time: ", execution_time1)

# Depth First Search
execution_time2 = timeit.timeit(lambda: s.dfs(cities, startCity, endCity, pr_path=True, pr_totDist=True), number=1)
print("Execution time: ", execution_time2)

# Uniform Cost Search
execution_time3 = timeit.timeit(lambda: s.ucs(cities, startCity, endCity, pr_path=True, pr_totDist=True), number=1)
print("Execution time: ", execution_time3)