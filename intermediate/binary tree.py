class Node:
    def __init__(self,val):
        self.left=None
        self.val=val
        self.right=None

def gen_tree(data,root,i,n):#data,None,0,12
    if i<n and data[i]!=None:
        root=Node(data[i])
        root.left=gen_tree(data,root.left,2*i+1,n)
        root.right=gen_tree(data,root.right,2*i+2,n)
    return root

def preorder(root):
    if root!=None:
        print(root.val,end=" ")
        preorder(root.left)
        preorder(root.right)


data=[1,2,3,4,5,6,7,8,9,10,11,12]
root=None
root=gen_tree(data,root,0,len(data))
preorder(root)