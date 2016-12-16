from tree_node import dNode
from avl_tree import AVLTree

class WAVLTree(AVLTree):
	def __init__(self):
		AVLTree.__init__(self)
	
	def _insert(self, val, node):
		if node==None:
			return dNode(val, None, None, 1)
		else:
			if node.val>val:
				node.left=self._insert(val, node.left)
				return self._insert_rotate(node, node.left, node.right)
			elif node.val<val:
				node.right=self._insert(val, node.right)
				return self._insert_rotate(node, node.right, node.left)
			else:
				return node
	
	def _remove(self, val, node):
		if node==None:
			return None
		else:
			if node.val==val:
				if node.left!=None and node.right!=None:
					closest=self._find_leftmost(node.right)
					temp=closest.val
					closest.val=node.val
					node.val=temp
					node.right=self._remove(val, node.right)
					return self._remove_rotate(node, \
						node.right, node.left)
				elif node.left!=None:
					return node.left
				elif node.right!=None:
					return node.right
				else:
					return None
			elif node.val<val:
				node.right=self._remove(val, node.right)
				self.set_depth(node)
				return self._remove_rotate(node, node.right,\
					node.left)
			else:
				node.left=self._remove(val, node.left)
				self.set_depth(node)
				return self._remove_rotate(node, node.left,\
					node.right)

		

	def _insert_rotate(self, parent, target, sibling):
		rd=self._rank_diff(parent, target)
		if rd==0:
			rs=self._rank_diff(parent, sibling)
			if rs==1:
				parent.depth+=1
				return parent
			elif rs>=2:
				return self._trinode_rotate(parent)		
		return parent
	
	def _remove_rotate(self, parent, target, sibling):
		rd=self._rank_diff(parent, target)
		if rd==2:
			return parent
		elif rd==3:
			rs=self._rank_diff(parent, sibling)
			if rs==2:
				parent.depth-=1
				return parent
			else:
				return self._trinode_rotate(parent)
		return parent

	def _rank_diff(self, np, nq):
		return self._depth(np)-self._depth(nq)

	def _depth(self, node):
		if node==None:
			return 0
		else:
			return node.depth			
	
	def printR(self, node):
                if node!=None:
                        self.print(node.left)
                        print("*"*node.depth, node.val)
                        self.print(node.right)


if __name__=="__main__":
	w=WAVLTree()
	w.insert(1)
	w.insert(2)
	w.insert(3)
	w.insert(4)
	w.insert(5)
	w.insert(9)
	w.insert(8)
	w.insert(11)
	w.insert(10)
	w.remove(11)
	w.remove(8)
	w.printR(w.root)
	print()
	w.print(w.root)

