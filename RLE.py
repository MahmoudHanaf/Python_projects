
##print("My name is mahmoud")
## this encoding string to be compressed by RLE
def encode(message):
    encode_message =""
    i =0
    
    while(i<= len(message)-1):
        counter =1
        ch =message[i]
        j =i
        
        while(j <len(message)-1):
            if(message[j] == message[j+1]):
                counter +=1
                j=j+1
            else:
                break
        encode_message=encode_message+str(counter)+ch
        i=j+1
    return encode_message
    


encode_message= encode("AAABBDDDDDGGGG")
print(encode_message)
 ## 
## this function to decode string to b compeesed by RLE   

def decode(our_message):
    
    decode_message =""
    i=0
    
    while(i <= len(our_message)-1):
        
        run_count = int(our_message[i])
        run_word =our_message[i+1]
        
    
        for j in range(run_count):
            decode_message = decode_message + run_word
            
        i = i+2
    return decode_message

decode_message = decode("3A5C4B")
print(decode_message)

        
            
            
            
            
            
        
        
    
           
