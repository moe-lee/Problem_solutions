from collections import deque as stack

def parse_shortest_path(path) :
    tokens = path.split("/")
    dir_stack = stack()
    if not tokens[0] : dir_stack.append("")
    for t in tokens :
        if dir_stack and t == ".." :
            dir_stack.pop()
        elif t!="." and t :
            dir_stack.append(t)
            
    return "/".join(dir_stack)


if __name__ == "__main__" :
    print(parse_shortest_path("/usr/lib/../test/bin/gcc"))