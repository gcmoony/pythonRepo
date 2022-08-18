def stripSeparator(itemAdd, separator, replacement = False, replacementSymbol = ":"):
    itemAdd =  itemAdd.split(separator)
    string = ""
    for item in itemAdd:
        if(replacement):
            string += item + replacementSymbol
        else:
            string += item
    if(replacement):
        # To strip the last separator off
        string = string[0:-1]
    return string

def stripSeparatorHelper():
    item = input("Item with character separators: ")
    separator = input("Current separator (i.e. '-', ':', etc.): ")
    response = ""
    while(response.lower() != 'y' and response.lower() != 'n'):
        response = str(input("Would you like a different separator? [y / n]: "))
    if(response == "y"):
        print("What would you like as the new separator?")
        response = input("New separator (i.e. '-', ':', '1', 'v', etc.: ")
        return(stripSeparator(item, separator, True, response))
    else:
        return stripSeparator(item, separator)

def main(): 
    print("New formatted item:", stripSeparatorHelper())

if __name__ == "__main__":
    main()