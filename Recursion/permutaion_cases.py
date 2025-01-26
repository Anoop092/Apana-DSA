string = "a1B2"
ans = ""
result =[]
def solve(string,ans,result):
    if len(string) == 0:
        result.append(ans)
        return
    #check wheather the chracter is is numeric
    if string[0].isnumeric():
        ans += string[0]
        solve(string[1:],ans,result)
        return
    # caplitilize the letter
    out1 = ans
    out2 = ans
    out1 += string[0].upper()
    solve(string[1:],out1,result)
    # lowercase letter
    out2 += string[0].lower()
    solve(string[1:],out2,result)
    return
solve(string,ans,result)



