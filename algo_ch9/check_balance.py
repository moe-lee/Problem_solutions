import binarytree

class HeightWithBalanceFlag(object) :
    # balanced : Boolean
    # height : integer
    def __init__(self, balanced, hegith) :
        self.balanced = balanced
        self.height = hegith

def isBalanced(root) :
    if root is None :
        return HeightWithBalanceFlag(True, -1)
    else :
        left_h = isBalanced(root.left)
        right_h = isBalanced(root.right)
        if not(right_h.balanced and left_h.balanced) or (abs(left_h.height - right_h.height) > 1):
            return HeightWithBalanceFlag(False, max(right_h.height, left_h.height) + 1)
        
        return HeightWithBalanceFlag(True, max(right_h.height, left_h.height) + 1)

'''
완전한 부분 트리 중에서 가장 큰 크기를 반환하라.
'''

def isBalanced_app1(root) :
    if root is None :
        # Base case: An empty tree is balanced with a height of -1.
        return HeightWithBalanceFlag(True, -1)
    else :
        # Recursive case: Calculate the heights of the left and right subtrees.
        #print(root)
        left_h = isBalanced_app1(root.left)
        right_h = isBalanced_app1(root.right)
        #print(root.left)
        #print(left_h.balanced, left_h.height)
        
        #print(root.right)
        #print(right_h.balanced, right_h.height)
        # Case analysis

        # Both left and right subtrees are complete => Check if this subtree is complete.
        
        if left_h.balanced and right_h.balanced and left_h.height == right_h.height :
            cnt = -1
            most_right = root.left
            if most_right: cnt+=1
            while most_right and most_right.right is not None :
                most_right = most_right.right
                cnt+=1
            if cnt == right_h.height :
                return HeightWithBalanceFlag(True, right_h.height + 1)
            else :
                return HeightWithBalanceFlag(False, max(right_h.height, left_h.height))
        
        elif left_h.balanced and right_h.balanced and (left_h.height - right_h.height) != 1 :
            return HeightWithBalanceFlag(False, max(left_h.height, right_h.height))
        
        elif (not left_h.balanced and right_h.balanced) or (not right_h.balanced and left_h.balanced):
            return HeightWithBalanceFlag(False, (left_h.height) if left_h.balanced else right_h.height)
        
        elif not left_h.balanced and not right_h.balanced :
            return HeightWithBalanceFlag(False, max(left_h.height, right_h.height))
        
        return HeightWithBalanceFlag(True, left_h.height + 1)

def get_k_balanced_node(root, k, result) :
    if not root : return -1
    

if __name__=="__main__" :
    root = binarytree.build([1,2,3,4,5,6,7,8, 9, None, 11, 12, 13])
    print(root)
    print(isBalanced_app1(root).height)