ds = ""
string = "abc"


def print_subsets(ds,string):
    # Base case 
    if len(string) == 0:
        print(ds)
        return
    
    # take character choice
    print_subsets(ds,string[1:])
    ds = ds + string[0]
    print_subsets(ds,string[1:])
    return

print_subsets(ds,string)    
    
    
