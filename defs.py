def wc_mapper_parallel(document):
     output=[]
     for word in document:
         output.append((word,1))
        
     return output

def wc_reducer_parallel(item):
     output=[]
     (word,counts)=item
     output.append((word,sum(counts)))
     return output