import random
wordslist = ["conversation","neighbor","fireplace","careful","eye","doctor","does",6,"speak","tone","paragraph","triangle","from","melted",10,"practice","nearby","means","nails","aware","additional",8,"cap","triangle","settle","sheet","magic","dropped","paragraph",4,"time","several","barn","rays","rhythm","until","past","dream",12,"trunk","breathing","struck","either","general","throughout","than","friend",20,"shut","balance","discussion","support","graph","signal","adult","yesterday","park","round","tears","corner","subject","produce",16,"brief","long","goes","breathing","better","provide","whom","faster","night",4,"fix","age","foreign","food","flame","hurry","else",1,"right","rush","town","empty","certainly","quick","box","poor","took","breeze","understanding",17,"living","make","spell","wore","education","diagram","different","add",5,"six","dry","news","to","driving","degree","captain","coach","further","then",2,"cool","huge","caught","several","east",13,"noted","thrown","floor","shelf",19]
count = 0
sum = 0
print("Enter the number of entries needed in the input file:")
entries = input()
entries = int(entries)
while(count < entries):
    f = open("input.txt", "a")
    select = random.choice(wordslist)
    if type(select) == int:
        if(sum + select >= count):
            continue
        elif(prevIsInt):
            continue
        else:
            sum += select
            line = str(select) + "\n"
            prevIsInt = True
    else:
        line = "$" + select + " " + str(random.randint(1,15)) + "\n"
        prevIsInt = False
    f.write(line)
    count += 1
f.write(str(random.randint(1,20)) + "\n" + "STOP")



