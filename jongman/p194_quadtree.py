def reverse_tree(string,idx=0):
    head = string[idx]
    if head == 'b' or head == 'w':
        return head
    idx += 1
    upper_left = reverse_tree(string,idx)
    idx += len(upper_left)
    upper_right = reverse_tree(string,idx)
    idx += len(upper_right)
    lower_left = reverse_tree(string,idx)
    idx += len(lower_left)
    lower_right = reverse_tree(string,idx)
    return 'x'+lower_left+lower_right+upper_left+upper_right
    
for t in range(1,int(input())+1):
    tree = str(input())
    print(reverse_tree(tree))