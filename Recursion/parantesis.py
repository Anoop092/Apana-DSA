ans = ""
result = []
n = 5
open_bracket_count = n
closed_bracket_count = n

def solve(ans,open_bracket_count,closed_bracket_count):
    if open_bracket_count == 0 and closed_bracket_count == 0:
        result.append(ans)
        return
    if open_bracket_count > 0:
        op1 = ans
        op1 += "("
        solve(op1,open_bracket_count-1,closed_bracket_count)
    if closed_bracket_count > open_bracket_count:
        op2= ans
        op2 += ")"
        solve(op2,open_bracket_count,closed_bracket_count-1)
    
solve(ans,open_bracket_count,closed_bracket_count)
print(result)
