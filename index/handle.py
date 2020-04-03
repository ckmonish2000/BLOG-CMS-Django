def handle_uploaded_file(f):  
    with open('index/media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
    x=f'index/media/{f.name}'
    return x