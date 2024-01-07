from collections import deque as stack

def get_shortes_paths(path) :
    tokens = list(filter(lambda x : x != '.', path.split('/')))
    path_notations = stack()
    for i in tokens :
        if i == '..' :
            if not(path_notations) or path_notations[-1] == '..' :
                path_notations.append('..')
            
            else : path_notations.pop()
        else:
            path_notations.append(i)
    return "/".join(path_notations)
    
if __name__ == "__main__":
    print(get_shortes_paths("../../src/bin/gcc/../java/./././../python/interpreter/codes"))
