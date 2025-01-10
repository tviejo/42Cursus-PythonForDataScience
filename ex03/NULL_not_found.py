def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing:", object, object.__class__)
    elif object.__class__ == float:
        print("Cheese:", object, object.__class__)
    elif object.__class__ == int and object == 0:
        print("Zero:", object, object.__class__)
    elif object.__class__ == str and object == "":
        print("Empty:", object, object.__class__)
    elif object.__class__ == bool and object == False:
        print("False:", object, object.__class__)
    else:
        print("Type not found")
        return(1)
    