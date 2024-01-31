import requests
import json
import os

webhook = "??"

def send_message_to_discord(text,name,pfp):
      data = {'content': text, 'username': name, 'avatar_url': pfp}
      requests.post(webhook, json=data)
      print (" \n",text) 
      print (f"👆Sent by {name}\n")


def send_photo_to_discord(text,name,pfp): 
        payload_json = {"username": name,
                "avatar_url": pfp,
                "content": text,
                "embeds": [{"image": {"url": "attachment://photo.png"}}]
                }
        
        files = {'file': ('photo.png', open("/home/tony/Desktop/comms/photo.png", 'rb'), 'image/png')}
        requests.post(webhook,
        files=files, data={'payload_json': json.dumps(payload_json)})
        print (f"Image by {name} sent")


def send_doc_to_discord(text,name,pfp,savepath): 
        payload_json = {"username": name,
                        "avatar_url": pfp,
                        "content": text
                        }
        files = {'file': (savepath.split("/")[-1], open(savepath, 'rb'), 'application/octet-stream')}
        requests.post(webhook,
        files=files, data={'payload_json': json.dumps(payload_json)})
        print (f"Document sent by {name}")
        os.remove (savepath) 


def send_mp4_to_discord(text,name,pfp,savepath):
        payload_json = {"username": name,
                        "avatar_url": pfp,
                        "content": text
                        }
        files = {'file': (savepath.split("/")[-1], open(savepath, 'rb'), 'video/mp4')}
        requests.post(webhook,
        files=files, data={'payload_json': json.dumps(payload_json)})
        print (f"Video sent by {name}")
        os.remove (savepath) 


thread_to_thread = {None : 1192173947945504830, # general
                    2 : 1192179909355913216, # DAO props
                    3 : 1192180476685848708, # Content Machine
                    4 : 1200136232949260298, # fud killing
                    5 : 1192180256136777829, # Meeting & calls 
                    6 : 1192180119201140787, # Social Media 
                    32 : 1192180352953880597,# Charter Ideas
                    1385 : 1200136620368732240, # Weekly planner
                    968 : 1200136468971126826, # discord revamp
                    777 : 1200136386414641152 # project updates
                    } 

