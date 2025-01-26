
string = "abc"
ans = ""

ans += string[0]
string = string[1:]

def perm_spaces(ans,string):
    if len(string) == 0:
        print(ans)
        return
    op1 = ans
    op2 = ans
    op1 += string[0]
    perm_spaces(op1,string[1:])
    op2 += " " + string[0]
    perm_spaces(op2,string[1:])

perm_spaces(ans,string)
    