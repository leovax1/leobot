import discord
import asyncio
import urllib.request
arabL=['ي','و','ه','ن','م','ل','ك','ق','ف','غ','ع','ظ','ط','ش','س','ز','ر','ذ','د','خ','ح','ج','ث','ت','ب','ا','ص',' ',]
englishL=['y','o','h','n','m','l','k','9','f','gh','3','th','ta','sh','s','z','r','dh','d','kh','7','j','th','t','b','a','sa',' ']

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = "https://www.youtube.com/user/oNEMoTEK/videos"#edit meeeeee to vid link if channle
headers={'User-Agent':user_agent,} 
def checkForDub(data):
    word=[]
    for line in data:
        if line+data[data.index(line)-1] in englishL:
            word.append(arabL[englishL.index(line+data[data.index(line)+1])])
        elif line in englishL:
            word.append(arabL[englishL.index(line)])
    return word
        
TOKEN = 'MzE1ODI3NzY1NTE1NjQ5MDI2.DZqmfQ.WqPiBuCfgmjuZ420hoxEkJKgpeM'

client = discord.Client()



async def newV():
 await client.wait_until_ready()
 lastvid='/watch?v=y8CGvpigFUw&t'
 channel = discord.Object(id='304307420623142912')
 while True:
  request=urllib.request.Request(url,None,headers)
  response = urllib.request.urlopen(request)
  dataYT= str(response.read())
  dataYT =dataYT.split('>')
  for line in dataYT:
    if 'href="/watch?v' in line:
       data=line.split('"')
       for line in data:
           if '/watch?v' in line:
               videolink=line
       if lastvid!=videolink:
        lastvid=videolink
        print(lastvid)
        msg='https://www.youtube.com'+videolink
        await client.send_message(channel, msg)
        await asyncio.sleep(30)
        break;
       else:
              await asyncio.sleep(30)
              break;


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    
    if message.content.startswith('!'):
        data=list(message.content)
        msg=checkForDub(data)
        await client.send_message(message.channel, ''.join(msg))
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(newV())
client.run(TOKEN)
