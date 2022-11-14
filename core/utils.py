from os import name as os_name, system as terminal


information = {
    "name": "Maktab File Store",
    "description": "...",
    "version": "1.0.0",
}


def about_us():
    print(
        f"""Store name : {information["name"]}
Description : {information["description"]}
Version : {information["version"]}
"""
    )


def salam(name):
    print("Hello ", name)


def clear():
    terminal('cls' if os_name.lower() == 'nt' else 'clear')
