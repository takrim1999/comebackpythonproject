import subprocess

records = []
done_list = []
def display():
    print("Welcome to Todo List App")
    print("funtions: 'add','show','edit','delete','check'")
    print("To exit type 'exit'")
    return True

def clear():
    subprocess.run("clear")
    display()
    print("")
    return True

def show(records,done_list):
    if records:
        print("Your list:")
        for i in range(len(records)):
            print(f"{i+1}. {records[i]} {done_list[i]}")
    else:
        print("List is Empty!")
        print("")
        return False
    print("")
    return True

def add(records,done_list):
    show(records,done_list)
    record = input("Add to your list(type 'exit' to stop): ")
    if record == "exit":
        return False
    records.append(record)
    done_list.append("")
    return True

def done(records,done_list):
    flag = show(records,done_list)
    if not flag:
        return "empty"
    id = input("record id(type 'exit' to stop): ")
    if id.lower()=="exit":
        return False
    try:
        id = int(id)
        done_list[id-1] = "done"
    except:
        print("Invalid Id\nTry Again")
    return True

def edit(records,done_list):
    flag = show(records,done_list)
    if not flag:
        return "empty"
    id = input("record id: ")
    if id.lower()=="exit":
        return False
    try:
        id = int(id)
        records[id-1] = input(f"{records[id-1]}:")
        choice = input("edit checking?(Y/N): ")
        if choice.lower() == "y"|"yes":
            choice2 = input("'check' or 'uncheck': ")
            if choice2.lower() == "check":
                done_list[id-1] = "done"
            elif choice2.lower() == "uncheck":
                done_list[id-1] = ""
        else:
            pass
    except:
        print("Invalid Id\nTry Again")
    return True



def remove(records,done_list):
    flag = show(records,done_list)
    if not flag:
        return "empty"
    id = input("record id(type 'exit' to stop): ")
    if id.lower()=="exit":
        return False
    try:
        id = int(id)
        records.pop(id-1)
        done_list.pop(id-1)
    except:
        print("Invalid Id\nTry Again")
    return True


clear()
while True:
    result = input("> ")
    match result.lower():
        case "exit":
            break
        case "show":
            clear()
            show(records,done_list)
        case "add":
            while True:
                clear()
                flag = add(records,done_list)
                if not flag:
                    break
            clear()
            show(records,done_list)
        case "delete":
            while True:
                clear()
                flag = remove(records,done_list)
                if flag!=True:
                    break
            clear()
            show(records,done_list)
            if flag == "empty":
                print("Unable to delete records!")
                print("")
        case "check":
            while True:
                clear()
                flag = done(records,done_list)
                if flag!=True:
                    break
            clear()
            show(records,done_list)
            if flag == "empty":
                print("Unable to check records!")
                print("")
        case "edit":
            clear()
            flag = edit(records,done_list)
            show(records,done_list)
            if flag == "empty":
                print("Unable to edit records!")
                print("")

        case others:
            print(f"No keyword like {others}")