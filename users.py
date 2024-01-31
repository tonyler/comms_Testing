class tony:
    url = "https://cdn.discordapp.com/avatars/817451374811152474/730a8b3fb819b6719dbc30bcdbe82dcb.png?size=2048"
    username = "tøny ⚵"
class papayo: 
    url = "https://cdn.discordapp.com/avatars/933475193236639875/5dfa4a511a312cd8701a1f78fd640fdf?size=1024"
    username = "Papayo"
class camel: 
    url = "https://cdn.discordapp.com/avatars/340813726103896064/0eef9350b82ee76540cadc2eada038a9?size=1024"
    username = "Camel 🐪" 
class max:
    url = "https://cdn.discordapp.com/avatars/318486129571790850/f37fc2f7c2c075b02b3050414365c184?size=1024"
    username = "Max"
class highlander: 
    url = "https://cdn.discordapp.com/avatars/735189796951031920/d61452d19a214905d0da3b6618838953?size=1024"
    username = "Highlander | ChainTools Validator | Juno Communications"

def pfp_retriever(name): 
    if name == tony.username:
        pfp = tony.url
    elif name == papayo.username:
        pfp = papayo.url
    elif name == camel.username:
        pfp = camel.url
    elif name == max.username:
        pfp = max.url
    elif name == highlander.username:
        pfp = highlander.url
    return pfp

     
