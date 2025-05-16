def login_hold_edit(email,password):


    with open('login_hold.txt', 'w') as f:
        f.write('{}'.format(email))
        f.write("\n")
        f.write("{}".format(password))

def login_hold_fetch():
    with open('login_hold.txt', 'r') as f:
        value1 = f.readline().strip()
        value2 = f.readline().strip()
    return value1,value2

def db_type_write(ctype):
    with open("database_type.txt","w") as f:
        f.write('{}'.format(ctype))

def db_type_read():
    with open("database_type.txt", "r") as f:
        val=f.readline()
    return val