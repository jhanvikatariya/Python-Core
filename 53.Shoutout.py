import win32com.client as win
speaker=win.Dispatch('SAPI.Spvoice')
l1=['Bhumi','Dev','Naitik']
for i in l1:
    print('shoutout to'+i)
for name in l1:
    names=name.split()
    shouttout=f'Hello{names[0]}'
    speaker.speak(shouttout)
print('shout out for all guys')