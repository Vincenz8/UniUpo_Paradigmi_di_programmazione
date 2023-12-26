# standard Libraries
from collections import namedtuple

Tree = namedtuple(typename='Tree', field_names=['data', 'sx', 'dx'], defaults=[None] * 3)


def is_leaf(tree: Tree):
	return tree.sx is None and tree.dx is None


def get_depth(tree):
	if is_leaf(tree): return 0
	return 1 + max([get_depth(subtree) for subtree in tree[1:] if subtree])


def pp_tree(tree: Tree) -> None:
	if tree is not None:
		if is_leaf(tree):
			print(tree.data, end='')
		else:
			print('(', end='')
			pp_tree(tree.sx)
			print(tree.data, end='')
			pp_tree(tree.dx)
			print(')', end='')
	

def depth_n(tree: Tree, lv: int):
	if tree is not None:
		if lv == 0:
			return [tree.data]
		else:
			if not is_leaf(tree):
				return depth_n(tree.sx, lv - 1) + depth_n(tree.dx, lv - 1)
			
	return []


def eleva(a: int, b: int) -> int:
	if b == 0:
		return 1
	else:
		return a * eleva(a, b - 1)
	

def main():
	optree1 = Tree('*',
	               Tree('+',
	                    Tree(7),
	                    Tree(4)),
	               Tree('-',
	                    Tree(7),
	                    Tree(4))
	               )

	pp_tree(optree1)
	print(f"\ndepth_n: {depth_n(optree1, 1)}")
	print(f"depth_n: {depth_n(optree1, 2)}")
	print(f"3 ^ 3 = {eleva(3, 3)}")
	print("max_prof non implementata")
	print("fold_left_ic non implementata")
	
	
if __name__ == "__main__":
	main()
