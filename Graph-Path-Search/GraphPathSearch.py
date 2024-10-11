''' - Main function - JJ McCauley - '''

import timeit
from uninformedsearch import uninformedsearch

# Added an addEdge function for expandability
def addEdge(city1: str, city2: str, weight: int):
    if city1 not in cities:
        cities[city1] = {}
    if city2 not in cities:
        cities[city2] = {}
    # Add the edge from city 1 to city 2
    cities[city1][city2] = weight
    # Add the edge from city 2 to city 1
    cities[city1][city2] = weight

# Hardcoding the provided cities graph
cities = {
    'Buffalo': {'Boston': 450, 'Pittsburg': 219},
    'Boston': {'Buffalo': 450, 'New York': 216},
    'Pittsburg': {'Buffalo': 219, 'New York': 370, 
                  'Philadelphia': 304, 'Baltimore': 248},
    'New York': {'Pittsburg': 370, 'Philadelphia': 94},
    'Philadelphia': {'New York': 94, 'Pittsburg': 304,
                     'Baltimore': 101, 'Salisbury': 138},
    'Baltimore': {'Pittsburg': 248, 'Philadelphia': 101,
                  'Washington DC': 45, 'Salisbury': 117},
    'Washington DC': {'Baltimore': 45, 'Salisbury': 116,
                      'Richmond': 110},
    'Salisbury': {'Philadelphia': 138, 'Baltimore': 117,
                  'Washington DC': 116, 'Norfolk': 132},
    'Richmond': {'Washington DC': 110, 'Norfolk': 93},
    'Norfolk': {'Richmond': 93, 'Salisbury': 132}
}

# Getting start and end cities from user
'''
startCity = input("Enter Start City: ")
while startCity not in cities:
    startCity = input("ERROR - Start City not found. Please try again: ")
endCity = input("Enter End City: ")
while endCity not in cities:
    endCity = input("ERROR - End city not found. Please try again: ")
'''
# Hardcoded for debugging purposes
startCity = 'Boston'
endCity = 'Salisbury'

# Create uninformedsearch object to use searches in module
s = uninformedsearch()

# Breadth First Search
execution_time1 = timeit.timeit(lambda: s.bfs(cities, startCity, endCity, pr_path=True, pr_totDist=True), number=1)
print("Execution time for BFS: ", round((1000000 * execution_time1), 3), " microseconds\n")

# Depth First Search
execution_time2 = timeit.timeit(lambda: s.dfs(cities, startCity, endCity, pr_path=True, pr_totDist=True), number=1)
print("Execution time for DFS: ", round((1000000 * execution_time2), 3), " microseconds\n")

# Uniform Cost Search
execution_time3 = timeit.timeit(lambda: s.ucs(cities, startCity, endCity, pr_path=True, pr_totDist=True), number=1)
print("Execution time for UCS: ", round((1000000 * execution_time3), 3), " microseconds\n")