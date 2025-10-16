day = "Mon"
match day:
    case "Mon" | "Tue" | "Wed" | "Thu" | "Fri":
        print("WeekDay")
    case "Sat" | "Sun":
        print("Weekend")
    case _:
        print("Invalid Day")



def http_status(code):
    match code:
        case 200:
            print("Ok")
        case 400:
            print("Bad Request")
        case 404:
            print("Not Found")
        case 500:
            print("Internel Server Error")
        case _:
            print("Unknown Status")

http_status(200)
http_status(400)
http_status(404)
http_status(45)