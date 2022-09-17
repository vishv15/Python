# write a programe to print first triagnle 
# *
# **
# ***
# ****
# *****

flash=5
while flash>0:
    count=0
    while count<flash:
        print("*",end='')
        count+=1
    print("")
    flash+=1