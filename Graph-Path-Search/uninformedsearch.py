''' - Defining the search functions - 
        JJ McCauley - 10/9/24 '''

'''Parameters for all search functions in this module: 
    cities- Dict of dicts (graph)
    start- String city to start from
    end- String target city to end at
    pr_path- Boolean for printing the path
    pr_totDist- Boolean for printing the total distance of pat'''
        
#TODO: BFS+DFS+UCS algorithms implementation

class uninformedsearch:
    
    '''Breadth First Search'''
    def bfs(self, cities: dict[str, dict[str, int]], start: str, end: str, pr_path: bool, pr_totDist: bool):
        visited = [start]
        queue = [start]
        total_distance = 0
        while queue:
            m = queue.pop(0)
            if pr_path and total_distance == 0:
                print(m, end=" ")
            else:
                print("->", m, end=" ")
            if m in cities:
                if m is end:
                    break
                for neighbor in cities[m]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
                        total_distance += cities[m][neighbor]  # Add the cost to total distance
        
        if pr_totDist:
            print("\nTotal BFS Distance: ", total_distance)
    

    
    '''Depth First Search'''
    def dfs(self, cities: dict[str, dict[str, int]], start: str, end: str, pr_path: bool, pr_totDist: bool):
        stack = [start]
        if pr_path:
            print(start, end=" ")
        visited = set()
        total_distance = 0
        while stack:
            current = stack.pop()
            if current == end: # Check if current city is target
                    if pr_totDist:
                        print("\nTotal DFS Distance: ", total_distance)
                    return
            if current not in visited:
                visited.add(current)
                # Check each neighbor and it's weight
                for neighbor, weight in reversed(cities[current].items()):
                    if neighbor not in visited:
                        if pr_path:
                            if pr_path:
                                print("->", neighbor, end=" ")
                        total_distance += weight
                        stack.append(neighbor)
                    
    
    
    
    '''Uniform Cost Search'''
    def ucs(self, cities: dict[str, dict[str, int]], start: str, end: str, pr_path: bool, pr_totDist: bool):
        pass