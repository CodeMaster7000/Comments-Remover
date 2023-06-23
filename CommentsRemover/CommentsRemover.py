with open("File1.py") as fp:
    contents=fp.readlines()
open_bracket_counter=0
close_bracket_counter=0 
decreasing_counter=0   

for number in range(len(contents)):
    if "#" in contents[number-decreasing_counter]:
        if contents[number-decreasing_counter].startswith("#"):
            contents.remove(contents[number-decreasing_counter])
            decreasing_counter+=1 
        else:  
            newline=""  
            for character in contents[number-decreasing_counter]:
                if character=="(":
                    open_bracket_counter+=1
                    newline+=character
                elif character==")":
                    close_bracket_counter+=1
                    newline+=character
                elif character=="#" and open_bracket_counter==close_bracket_counter:
                    break
                else:
                    newline+=character
            contents.remove(contents[number-decreasing_counter])     
            contents.insert(number-decreasing_counter,newline)   

with open("File2.py","w") as fp:
    fp.writelines(contents)
