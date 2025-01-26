ans = ""
string = "ab"

def solve(ans,string):
    if len(string) == 0:
        print(ans)
        return
    
    output1 = ans
    output2 = ans
    output1 +=  string[0].upper()
    solve(output1,string[1:])
    output2 += string[0]
    solve(output2,string[1:])

    return

solve(ans,string)