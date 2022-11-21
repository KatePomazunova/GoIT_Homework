import re



contacts = {}  


def add(text):

    phone_number = re.findall(r"\d+", text)[-1]
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    contacts[phone_name] =  phone_number
    result = "Number added. Something else?"
    return result


def change(text):
    
    phone_number = re.findall(r"\d+", text)[-1]
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    old_phone_number = contacts[phone_name] 
    contacts[phone_name] =  phone_number
    result = f"{phone_name}\'s number {old_phone_number} changed to {phone_number}. Something else?"
    return result


def end(text):

    result = "Good bye!"
    return result
    

def hello(text):

    result = "How can I help you?"
    return result


def input_error(funk):
      
    def inner(*args,**kwargs):  

        try:
            funk()
        except KeyError: 
            print("This name does not exist.")
            main()
        except IndexError:
            print("Did not receive a name or number.")
            main()
        except:
            print("Option entered incorrectly.")
            main()

    return inner


def phone(text):
    
    phone_name = re.findall(r"[a-z]+", text, flags=re.IGNORECASE)[1].title()
    result = contacts[phone_name]
    return result


def show_all(text):

    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()


@input_error
def main():

    start = True

    while start:

        access = False
        entered_text = input()
        
        for key in user_command.keys():
            if bool(re.search(key, entered_text, flags=re.IGNORECASE)):
                
                access = True
                print(user_command[key](entered_text))

                if key in ["exit","good bye","close"]:
                    start = False  
                break
      
        if not access:
            print("Option entered incorrectly...")
               
      
user_command = {
    "add": add,
    "change": change,
    "exit": end,
    "good bye": end,
    "close": end,
    "hello": hello,
    "phone": phone,
    "show all": show_all,
}


if __name__ == "__main__":
    main()


