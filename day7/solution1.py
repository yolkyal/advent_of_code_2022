class TreeNode:
	def __init__(self, parent):
		self.parent = parent
		self.size = 0
		self.children = {}
	
	def full_size(self):
		child_size = sum([child.full_size() for child in self.children.values()])
		return self.size + child_size


root_node = TreeNode(None)
cur_node = root_node
with open(0) as f:
	next(f)
	for line in f:
		line = line.strip()
		if line[0:4] == '$ cd':
			path = line[5:]
			if path == '..':
				cur_node = cur_node.parent
			else:
				cur_node = cur_node.children[line[5:]]
		elif line[0:4] == '$ ls':
			continue
		elif line[0:3] == 'dir':
			cur_node.children[line[4:]] = TreeNode(cur_node)
		elif line[0] != '$':
			cur_node.size += int(line.split()[0])


full_sizes = []
def get_all_full_sizes(node):
	global full_sizes
	for child in node.children.values():
		get_all_full_sizes(child)
	full_sizes.append(node.full_size())


get_all_full_sizes(root_node)

result = sum([s for s in full_sizes if s <= 100000])
print(result)