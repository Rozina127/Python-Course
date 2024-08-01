################    file reading from day23.txt file    ######################
with open("day23.txt") as file:
    filecontent=file.read()
    print (filecontent) 
    
################    file writting in day23.txt file    ######################      
with open("day23.txt" , mode="a") as file:
    file.write("\nShe likes programming.")
    
    
    
    