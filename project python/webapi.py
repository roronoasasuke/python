import json
with open('webapi.json', 'r') as file:
    data = json.load(file)

    if data.get('success') and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        email = user_data["login"]["email"]
        password = user_data["login"]["password"]
        country = user_data["location"]["country"]
        city = user_data["location"].get("city","not specified")
        state = user_data["location"].get("state","not specified")
        action = user_data["anime"]["action"]
        adventure = user_data["anime"].get("adventure","not specified")
        psycho = user_data["anime"].get("psycho","not specified")

        print('Username:',username)
        print('Email:',email)
        print('Password:',password)
        print('Country:',country)
        print('City:',city)
        print('State:',state)
        print('Action Animes:',action)
        print('Adventure Animes:',adventure)
        print('Psychotic Animes:',psycho)
    else:
        print('404 data not found')    
