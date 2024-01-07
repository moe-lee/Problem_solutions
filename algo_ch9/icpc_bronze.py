latino = { 'a' : 'as', 'i' : 'ios', 'y' : 'ios', 'l' : 'les', 'n' : 'anes', 'o': 'os', 'r' : 'res', 't' : 'tas', 'u' : 'us', 'v' : 'ves', 'w' : 'was'}
keylist = list(latino.keys())

def processInput(s) :
    org = bytearray(s.encode())
    if org[-1] == ord('e') and org[-2] == ord('n') :
        org[-2] = ord('a')
        org[-1] = ord('n')
        org.append(ord('e'))
        org.append(ord('s'))
    else :
        attachment = latino.get(chr(org[-1]), chr(org[-1])+'us')
        org[-1] = ord(attachment[0])
        for i in range(1, len(attachment)) :
            org.append(ord(attachment[i]))
            
    print(org.decode())
    
def main() :
    n = int(input())

    for i in range(n) :
        org = input()
        processInput(org)


main();