''' - Main function - JJ McCauley - '''

import timeit
from uninformedsearch import bfs
from uninformedsearch import dfs
from uninformedsearch import ucs

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

# BFS
execution_time = timeit.timeit(lambda: bfs(cities, True, True), number=1)
print("Execution time: ", execution_time, " seconds")

# DFS
execution_time = timeit.timeit(lambda: dfs(cities, True, True), number=1)
print("Execution time: ", execution_time, " seconds")

# UCS
execution_time = timeit.timeit(lambda: ucs(cities, True, True), number=1)
print("Execution time: ", execution_time, " seconds")