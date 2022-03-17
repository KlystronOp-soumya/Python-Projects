import re
def subst(pattern, replace_str, string):
    #susbstitute pattern and return it
    return re.sub(pattern,replace_str,string)


def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
    #Create pattern Implementation here 
    pattern = r"\sROAD\s?"
    comp_pattern = re.compile(pattern)
    replace_str = r" RD."
    new_address=[]
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address
    for each_addr in addr:
        new_address.append(subst(comp_pattern,replace_str,each_addr))
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address

    return new_address

print(main())