import time


def app():
    lost_found = input('Lost or found? ')
    lost_found = lost_found.lower()
    col_yes = False
    man_yes = False
    obj_yes = False
    if lost_found == 'lost' or lost_found == 'found':
        form = input('Enter your name - ')
        form = form.lower()
        object = input('Enter the object - ')
        object = object.lower()
        manufacturer = input('Enter the brand/company - ')
        manufacturer = manufacturer.lower()
        color = input('Enter the color - ')
        color = color.lower()
    else:
        print('Invalid entry please enter "lost" if you have lost something or "found" if you have found other peoples article ')
        time.sleep(10)
        exit()
    if lost_found == 'lost':
        file = open('objects', 'r')
        for lines in file:
            lines = lines.split()
            if lines[1] == object:
                obj_yes = True
            if lines[2] == manufacturer:
                man_yes = True
            if lines[3] == color:
                col_yes = True
            if col_yes == man_yes == obj_yes is True:
                print(f"{lines[0]} has found your {object} {form}")
                time.sleep(10)
        file.close()
    elif lost_found == 'found':
        file = open('object', 'a')
        file.write(form)
        file.write(object)
        file.write(manufacturer)
        file.write(color)
        print('Ok we have accepted your entry')
        time.sleep(10)
        file.close()



app()
