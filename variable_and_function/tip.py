def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    d = str(d)
    d_str = d.lstrip('$')
    return float(d_str)
    

def percent_to_float(p): 
    p = str(p)
    p_str = p.rstrip('%')
    p_int = int(p_str)/100
    return float(p_int)
    
    
    
main() 