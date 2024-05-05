import time
import asyncio
import requests


async def func1():
    print('function 1')
    URL='https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg'
    response=requests.get(URL)
    open('instagram.ico','wb').write(response.content)
    
    return 'one'

async def func2():
    print('function 2')
    URL='https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1448-tree-snow-wallpaper-preview.jpg'
    response=requests.get(URL)
    open('instagram2.jpg','wb').write(response.content)
    
    return 'two'

async def func3():
    print('function 3')
    URL='https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg'
    response=requests.get(URL)
    open('instagram3.ico','wb').write(response.content)
    
    return 'three'

async def main():
    #await func1()
    #await func2()
    #await func3()
    #return 3
    
    L=await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    
    print(L)
    #task=asyncio.create_task(func1())
    #await func1()
    #await func2()
    #await func3()
    
asyncio.run(main())