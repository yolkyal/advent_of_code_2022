def dijkstra(graph, source, target):
	dist = {}
	for vertex in graph:
		dist[vertex] = 10000000
	dist[source] = 0

	endpoints = {(source)}
	while len(endpoints) > 0:
		u = (None, 10000000)
		for vertex in endpoints:
			dist_v = dist[vertex]
			if dist_v < u[1]:
				u = (vertex, dist_v)
		u = u[0]
		
		endpoints.remove(u)
		if u == target:
			return dist[u]
		
		for v in [(u[0]+1, u[1]), (u[0], u[1]+1), (u[0]-1, u[1]), (u[0], u[1]-1)]:
			if v in graph and ord(graph[v]) - ord(graph[u]) <= 1:
				alt = dist[u] + 1
				if alt < dist[v]:
					dist[v] = alt
					endpoints.add(v)


graph = {}
start = ''
end = ''
with open(0) as f:
	for row, line in enumerate(f):
		for col, val in enumerate(list(line.strip())):
			if val == 'S':
				start = (row, col)
				graph[start] = 'a'
			elif val == 'E':
				end = (row, col)
				graph[end] = 'z'
			else:
				graph[(row, col)] = val

solution = dijkstra(graph, start, end)

print(solution)