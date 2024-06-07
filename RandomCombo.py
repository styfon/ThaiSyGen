import random
#from ToneRuleTest import vow_List_No_Final
#from ToneRuleTest import con_mid

#tone_marks = [")่",")้",")๊",")๋"]
spvow = [")ี",")ิ",")ื",")ั"]

def combo2(con,vow,tone):
    conR = random.choice(con)
    vowR = random.choice(vow)
    lenvow = len(vowR)
    replace = ")"
    index = vowR.find(replace)
    if tone == "":
        return combo(conR,vowR)
    elif lenvow == 2:
         #strtone = tone[0]+tone[1]
         strtone = tone
         if index == 1:
             sy = combo(conR,vowR)
             return sy[1] + replace_character(strtone,sy[1],")")
         elif vowR in spvow: #changed from adding indexes
            return replace_character(strtone,combo(conR,vowR),")")
         else:
             sy = combo(conR,vowR)
             return replace_character(strtone,sy[0],")") + sy[1]
    else:
        #strtone = tone[0]+tone[1]
        strtone = tone
        if vowR[index]+vowR[index+1] in spvow:
            sy = combo(conR,vowR)
            part = sy[index]+sy[index+1]
            wtone = replace_character(strtone,part,")")
            return f'{sy[:index]}{wtone}{sy[index+1:]}'
        else:
            sy = combo(conR,vowR)
            part = sy[index]
            wtone = replace_character(strtone,part,")")
            return f'{sy[:index]}{wtone}{sy[index+1:]}'

def combo(data1,data2):
    if not data1 or not data2:
        return None
    char_to_replace = ")"
    result = replace_character(data2, data1, char_to_replace)
    return result

def replace_character(string1, string2, char_to_replace):
    index = string1.find(char_to_replace)
    if index != -1:
        replaced_string = string1[:index] + string2 + string1[index+1:]
        return replaced_string
    else:
        return string1  # Return the original string if the character is not found
    
#rule14 = combo2(con_mid,vow_List_No_Final,tone_marks[0])
#print(rule14)

