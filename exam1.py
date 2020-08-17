import sys

def deduplicate(dup_str):
    dist_list=[]
    input_list=dup_str.split()
    for i in input_list:
        if i not in dist_list:
            dist_list.append(i)
    return dist_list


def sort(some_list):
    sorted_list=sorted(some_list)
    return sorted_list




def parse(string):
    file=open(string,"r")
    content=file.read()
    file.close()
    dist_list=deduplicate(content)
    sorted_list=sort(dist_list)
    sorted_words= " ".join(sorted_list)
    print(sorted_words)

parse(sys.argv[1])    
