import requests


def send_data_to_server(addr, user, image):
    
    fileName = image.replace("\\", "/").split("/")[-1].split(".")
    
    multipart_form_data = {
        'image1': (fileName[0], open(image, 'rb'), "image/"+fileName[1]),
        'user': ('', user),
    }

    response = requests.post(addr, files=multipart_form_data)

    return(response.status_code)


test1 = send_data_to_server(input("Address: "), input("User: "), input("Image: "))


print(test1)
input();