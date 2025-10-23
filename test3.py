

def about_me():
    me = {
        "first": "Dave",
        "last": "Smith",
        "Age": "45",
        "address": {
            "street": "Bishopsicamore",
            "number": "4200",
            "city": "ranchocoocamunga",
            "zip" : "765421",
        }
    }
    
    print(me)
    
    # read values
    print(me["first"] +" " + me["last"])
    print(f"I'm {me['Age']} years old")
    
    # read the address
    # print(me["address"]["street"])
    
    address = me["address"]
    street = address["street"]
    num = address["number"]
    city = address["city"]
    zip = address["zip"]
    print(street)
    
    # a) Return to: street #numb, city, zip.
    print(f"Return to:{street} #{num}, {city}, {zip}.")
    
    
    
    
    
    
    
    
# fn calls
about_me()