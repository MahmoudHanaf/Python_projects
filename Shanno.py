
class Char:
    
    #__init__. It's what we use to define the initialisation of an object.
    def __init__(self, name, freq):
        self._name = name
        self._freq = freq
        self._code = ""
     
    #__lt__(self, other) Defines the behaviour of the less-than operator <
    def __lt__(self, other):
        return True if self._freq < other.get_freq() else False
    
    #Defines the behaviour of the equality operator ==
    def __eq__(self, other):
        return True if self._name == other.get_name() and self._freq == other.get_freq() else False


  #The __str__ method in Python represents the class objects as a string – it can be used for classes.
  #The __str__ method should be defined in a way that is easy to read and outputs all the members of the class.
    def __str__(self):
        return "{0}\t {1}\t {2}".format(self._name, str(self._freq), self._code)
    
   #we can say that class Char is an iterable object because we implemented it with __iter__.
   #Method __iter__ returns an iterator.
    def __iter__(self):
        return self
    
    #to get the name of current object
    def get_name(self):
        return self._name
    
    #to get frequency of current object
    def get_freq(self):
        return self._freq
    
    #to get the code of current object
    def get_code(self):
        return self._code
    
    #to append current code to previous codes of current object
    def append_code(self, code):
        self._code += str(code)

    
def find_middle(lst):
    
    if len(lst) == 1 :  return None
    
    s = k = b =0
    
    for p in lst :
        s += p.get_freq()
    s /=2
    
    for p in range(len(lst)):
        k += lst[p].get_freq()
        
        if k == s : return p
        elif k >s :
            j =len(lst) -1
            
            while b <s :
                 b +=lst[j].get_freq()
                 j -=1
            return p if abs(s - k) < abs(s - b) else j
    
    

def shannon_fano(lst):
    
    middle = find_middle(lst)
    if middle is None: return #return nothing if it isn't middle
    
    for i in lst[: middle + 1]: #range(0,middle+1)
        i.append_code(0) #append 0 to the specific symbols in range
        
    shannon_fano(lst[: middle + 1]) #call the function again 

    for i in lst[middle + 1:]: #range(middle+1,the end)
        i.append_code(1)  #append 0 to the specific symbols in range
        
    shannon_fano(lst[middle + 1:]) ##call the function again to complite the codes
         
        

def output():

    lst=list()
    lst.append(Char('A', 0.22))
    lst.append(Char('B', 0.28))
    lst.append(Char('C', 0.15))
    lst.append(Char('D', 0.30))
    lst.append(Char('E', 0.05))
    

    
    lst.sort(reverse=True) #sorting DC
    shannon_fano(lst) #CALL shanon_fano() fun 
    print('char','freq','code')
    for c in lst: #for loop to print all objects of list with codes
     print(c)


output() #calling output()function to get results



            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
                
    
            
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

