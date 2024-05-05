#multiprocessing
#make a folder named files
import multiprocessing
import requests
def downloadFile(url,name):
    print(f'Started downloading {name}')
    response=requests.get(url)
    open(f'files/file{name}.jpg','wb').write(response.content)
    print(f'Finished Downloading {name}')
url='https://picsum.photos/2000/3000'
pros=[]
if __name__=='__main__':
    for i in range(5):
        p=multiprocessing.Process(target=downloadFile,args=[url,i])
        p.start()
        pros.append(p)
        
    for p in pros:
        p.join()