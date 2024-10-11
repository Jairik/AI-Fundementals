''' - Defining the search functions - 
        JJ McCauley - 10/9/24 '''

'''Parameters for all search functions in this module: 
    cities- Dict of dicts (graph)
    start- String city to start from
    end- String target city to end at
    pr_path- Boolean for printing the path
    pr_totDist- Boolean for printing the total distance of pat'''
        
import heapq  # Simplified UCS implementation


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
        stack = [(start, 0, [start])]
        visited = set()
        while stack:
            current, current_distance, path = stack.pop()
            if current == end: # Check if current city is target
                    if pr_path:
                        print(" -> ".join(path))
                    if pr_totDist:
                        print("Total DFS Distance: ", current_distance)
                    return
            if current not in visited:
                visited.add(current)
                # Check each neighbor and it's weight
                for neighbor, weight in reversed(cities[current].items()):
                    if neighbor not in visited:
                        stack.append((neighbor, current_distance + weight, path + [neighbor]))
                        
    
    
    '''Uniform Cost Search'''
    def ucs(self, cities: dict[str, dict[str, int]], start: str, end: str, pr_path: bool, pr_totDist: bool):
        queue = [(start, 0, [])]
        visited = set()
        while queue:
            # Pop the city with the smallest cost
            current, current_distance, path = heapq.heappop(queue)
            if current in visited:  # If city already visited, skip to next one
                continue 
            visited.add(current)
            path = path + [current]
            if current == end:
                if pr_path:
                    print(" -> ".join(path))
                if pr_totDist:
                    print("Total UCS Distance: ", total_distance)
                    return
            # Expand neighbors
            for neighbor, weight in cities[current].items():
                if neighbor not in visited:
                    total_distance = current_distance + weight
                    heapq.heappush(queue, (neighbor, total_distance, path))
                    
            