# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from bs4 import BeautifulSoup
from subprocess import call
import time,random,sys,json,codecs,threading,glob,re,os,urllib,urllib2
from urllib import urlopen
import requests,tempfile

cl = LINETCR.LINE()
cl.login(token='EnboRcQ0yxTx3ljwnvyd.6AZ1bvq+KAa4D/tcvGksdq.+u0zDl0hLLI8a9S5+2uCyCpg15YgAlQ55Ogc8mhoa+g=')
cl.loginResult()

kk = LINETCR.LINE()
kk.login(token='EmIl2Vxdo1LcIwH5qAR4.puzOPEclyQje8cUz6XhsXa.pE1VOTjh6GSa0bok1DxMLmDPTbzlf2wiR9Hj/DXXTrY=')
kk.loginResult()

ki = LINETCR.LINE()
ki.login(token='Em3FdTGjlci8luci4Nf9.jyPfnotv4HnWAfW0dTuBIq.Mipk0c64g+YKjRCwHSEfC6NOdzMPmsb477xfme+yixs=')
kk.loginResult()

kc = LINETCR.LINE()
kc.login(token='EmrlKsAbNwPAtl42fo6a.0ZYvxYaVFI7AnWG7lZ9BcG.KdqeJ5MC4B3cnS8PB47R1kSHrAUsLLE58D0p66Wgeto=')
kc.loginResult()


print ("Login Berhasil")

reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""
]Id︎[
]Mid︎[
]Me︎[
]Mc[
]K on/off[
]Join on/off[
]Group cancelall︎[
]Leave︎ on/off[
]Add on/off[
]Share on/off[
]Removed]all message[
]Confirm[
]Jam on/off[
]Change clock[
]Up[
]Aple[

]Curl[
]Ourl[
]url[
[Ginfo]
]Cancel[
]Gn 「group name」[

[Bye[
]All group[
]Jepit[
]Usir @[
]Pancal @[
]Kill ban[
]Rejeck invite[
]Clear ban[
[Clear[ cancel
[Blockinvite[ on/off
]Mid @[
]Info @[
]Jumpbot[
[Kill 「@」[
]Kasih @[
[Unban 「@」[ By Tag
[Ban︎] Share Contact
[Unban︎[ Share Contact
]Baned @[
]dlmusic[
[Id[
]getlirik[
]getig[
]getimage[
]groupimage[
[Banlist︎[
[Cek ban[
[Invite:「mid」[
[Rename:「name」[
[gift[
[Respo︎n[
[Bot cancel[
[Clone @[
]Back[
]Pap @[
]Sc @[
]Sp @[
[Tagall[
[Mimic: on/off[
]Target @[
]Target Del @[
]Mimic list[

"""
Bots = [cl,ki,kk,kc]
KAC=[cl,ki,kk,kc]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Bots = [mid,Amid,Bmid,Cmid]
admin = ["u8f9d76cfab08132d703f958ce3fa8cc0","ue9acf505543f91a03877e4c25602920d"]
staff = ["u8f9d76cfab08132d703f958ce3fa8cc0","ue9acf505543f91a03877e4c25602920d"]
adminMID = "u8f9d76cfab08132d703f958ce3fa8cc0","ue9acf505543f91a03877e4c25602920d"
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "Protectguest":False,
    "ProtectQR":False,
    "cName":"unknown",
    "blacklist":{},
    "winvite":False,
    "uppoto":False,
    "likefunction":False,
    "welcomemsg":False,
    "Reinvite":False,
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True
    }
wait3 = {
    "copy":False,
    "copy2":"target",
    "target":{}
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }
mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
def yt(query):
    with requests.session() as s:
         isi = []
         if query == "":
             query = "S1B tanysyz"   
         s.headers['user-agent'] = 'Mozilla/5.0'
         url    = 'http://www.youtube.com/results'
         params = {'search_query': query}
         r    = s.get(url, params=params)
         soup = BeautifulSoup(r.content, 'html5lib')
         for a in soup.select('.yt-lockup-title > a[title]'):
            if '&list=' not in a['href']:
                if 'watch?v' in a['href']:
                    b = a['href'].replace('watch?v=', '')
                    isi += ['youtu.be' + b]
         return isi
	
def mention(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print ("[Command] Tag All")
    try:
       cl.sendMessage(msg)
    except Exception as error:
       print (error)
       
def music(songname):
    params = {'songname':songname}
    url = 'http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params)
    r = requests.get(url,verify=False).text
    data = json.loads(r)
    for song in data:
        return song[4]
        
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 3.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass
def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait2['readPoint']:
                    if msg.from_ in wait2["ROM"][msg.to]:
                        del wait2["ROM"][msg.to][msg.from_]
                else:
                    pass
            except:
                pass
        else:
            pass
    except KeyboardInterrupt:
	       sys.exit(0)
    except Exception as error:
        print (error)
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return
def findMusic(to,song):
    params = {'songname':song}
    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
    data = r.text
    data = data.encode('utf-8')
    data = json.loads(data)
    for song in data:
        ki.sendText(to,"This Your Music.\n\nJudul: " + song[0] + "\nWaktu: " + song[1] + "\nLink: " + song[3] + "\nDownload: " + song[4])
    

def findLyric(to,song):
    params = {'songname':song}
    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
    data = r.text
    data = data.encode('utf-8')
    data = json.loads(data)
    for song in data:
        ki.sendText(to,"Lyrics Of " + song[0] + ":\n\n"+ song[5])

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        if op.type == 11:
           if wait["ProtectQR"] == True:
               if op.param2 not in admin:
                   G = cl.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   cl.kickoutFromGroup(op.param1,[op.param2])
                   cl.updateGroup(G)
        if op.type == 11:
            if op.param2 not in admin:
                G.preventJoinByTicket = True
                return
            cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nPlease don't play qr")
            print ("Update group")
        if op.type == 13:
           if wait["Protectguest"] == True:
               if op.param2 not in admin:
                  cl.cancelGroupInvitation(op.param1,[op.param3])
  	     
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 15:
            if wait["Reinvite"] == True:
                try:
                    ki.inviteIntoGroup(op.param1, [op.param2])
                except:
                    random.choice(KAC).inviteIntoGroup(op.param1, [op.param2])
        if op.type == 17:
	   #if wait["welcomemsg"] == True:
              if op.param2 not in Bots:
                 ginfo = cl.getGroup(op.param1)
                 cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\nwelcome to group\n"+ str(ginfo.name))
#------fungsi protect yg membatalkan undangan grup----------
        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                try:
                    cl.kickoutFromGroup(op.param1, op.param2)
                except:
                    cl.kickoutFromGroup(op.param1, op.param3)
     	   
        #if op.type == 17:
              #ginfo = cl.getGroup(op.param1)
              #cl.sendText(op.param1,"Selamat Datang Di Grup " + str(ginfo.name))
        if op.type == 17:
            if op.param3 in wait["blacklist"]:
                try:
                    cl.kickoutFromGroup(op.param1, op.param3)
                except:
                    cl.kickoutFromGroup(op.param1, op.param3)
        if op.type == 19:
                    if op.param3 in admin:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        random.choice(KAC).inviteIntoGroup(op.param1,admin)

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加し�����す。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    ki.updateGroup(G)
                    Ti = ki.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
        if op.type == 19:
                if op.param2 not in admin:
                    try:
                        gs = cl.getGroup(op.param1)
                        gs = ki.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return


                    except Exception:
                        print (e)


        if op.type == 11:
                if op.param2 not in admin:
                    try:
                        gs = cl.getGroup(op.param1)
                        gs = ki.getGroup(op.param1)
                        targets = [op.param2]
                        for target in targets:
                           try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                           except:
                            return


                    except Exception as e:
                        print (e)

        #if op.type == 19:
            #if op.param2 not in admin:
                  #G = cl.getGroup(op.param1)
                  #G.preventJoinByTicket = False
                  #cl.updateGroup(G)
                  #Ti = cl.reissueGroupTicket(op.param1)
                  #ki.acceptGroupInvitationByTicket(op.param1,Ti)
                  #ki.kickoutFromGroup(op.param1,[op.param2])
    	     	  #wait["blacklist"][op.param2] = True
                  #ki.leaveGroup(op.param1)
                  #G.preventJoinByTicket = True
                  #cl.updateGroup(G)
                  #pass
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.from_ in admin and wait3["copy"] == True and wait3["copy2"] == "me" and "Ccopy" not in msg.text:
                    for i in range(1):
                        cl.sendText(msg.to,msg.text)
                        wait3["copy"] = False
                    wait3["copy"] = True
            elif msg.from_ in wait3["target"] and wait3["copy"] == True and wait3["copy2"] == "target":
                    for i in range(1):
                     text = msg.text
            	     if text is not None:
                        cl.sendText(msg.to,msg.text)
                    else:
                        if msg.contentType == 7:
            			msg.contentType = 7
            			msg.text = None
            			msg.contentMetadata = {
            			"STKID": "6",
            			"STKPKGID": "1",            						"STKVER": "100" }
            			cl.sendMessage(msg)
            #elif msg.contentType == 13:
            			#msg.contentType = 13
            			#msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
            			#cl.sendMessage(msg)
            			wait3["copy"] = False
            			wait3["copy"] = True
                            
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "":
        	       if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")

            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
            cl.like(url[25:58], url[66:], likeType=1001)
            cl.comment(url[25:58], url[66:],"like\nlike\ndan\nLike")
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               if wait["uppoto"] == True:
                  if msg.from_ in admin:
                        target = msg.contentMetadata["mid"]
                        contact = cl.getContact(target)
                        X = contact.displayName
                        profile = cl.getProfile()
                        profile.displayName = X
                        cl.updateProfile(profile)
                        cl.sendText(msg.to, "done")
                        P = contact.pictureStatus
                        cl.updateProfilePicture(P)
               if wait["winvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 ki.sendText(msg.to,"-> " + _name + " udah d dlam\nplease cek!!!")
                                 break
                             elif invite in wait["blacklist"]:
                                 ki.sendText(msg.to,"Sorry, " + _name + " On Blacklist")
                                 ki.sendText(msg.to,"unban dulu vrohh !, \n➡Unban: " + invite)
                                 break
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     ki.findAndAddContactsByMid(target)
                                     ki.inviteIntoGroup(msg.to,[target])
                                     ki.sendText(msg.to,"done vrohh \n➡" + _name +"\n Telah tercyduk....😉")
                                     wait["winvite"] = False
                                     break
                                 except:
                                     try:
                                         ki.findAndAddContactsByMid(invite)
                                         ki.inviteIntoGroup(op.param1,[invite])
                                         wait["winvite"] = False
                                     except:
                                         try:
                                             ki.findAndAddContactsByMid(invite)
                                             ki.inviteIntoGroup(op.param1,[invite])
                                             wait["winvite"] = False
                                             ki.sendText(msg.to,"done vrohh...\n➡" + _name)
                                             break
                                         except:
                                            try:
                                                 cl.findAndAddContactsByMid(invite)
                                                 cl.inviteIntoGroup(op.param1,[invite])
                                                 wait["winvite"] = False
                                                 cl.sendText(msg.to,"done vroh\n➡" + _name)
                                                 break
                                            except:
                                                 ki.sendText(msg.to,"Negative, Error detected")
                                                 wait["winvite"] = False
                                                 break

               elif wait["contact"] == True:
                    msg.contentType = 0
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"「 Name 」 :\n" + msg.contentMetadata["displayName"] + "\n「 Mid 」 :\n" + msg.contentMetadata["mid"] + "\n「 Status 」 :\n" + contact.statusMessage + "\n「 Profile 」 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n「 Cover 」 :\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"「 Name 」 :\n" + contact.displayName + "\n「 Mid 」 :\n" + msg.contentMetadata["mid"] + "\n「 Status 」 :\n" + contact.statusMessage + "\n「 Profile 」 :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n「 Cover 」 :\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
               if msg.from_ in mid:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            
            elif 'Yt ' in msg.text:
	      if msg.from_ in admin:
                try:
                    textToSearch = (msg.text).replace('Yt ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    cl.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    cl.sendText(msg.to,"Could not find it")
            elif "music " in msg.text.lower():
                if msg.from_ in admin:
                   try:
                       song = msg.text[7:]
                       findMusic(msg.to, song)
                   except:
                       cl.sendText(msg.to,"Error...")
            elif "lyric " in msg.text.lower():
                if msg.from_ in admin:
                   try:
                       song = msg.text[7:]
                       findLyric(msg.to, song)
                   except:
                      cl.sendText(msg.to,"Error...")
            elif "Contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
            elif msg.text in ["Mimic on"]:
                    if wait3["copy"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic On")
                    else:
                    	wait3["copy"] = True
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic On")
                        else:
    	                	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Mimic off"]:
                    if wait3["copy"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Already on")
                        else:
                            cl.sendText(msg.to,"Mimic Off")
                    else:
                    	wait3["copy"] = False
                    	if wait["lang"] == "JP":
                    		cl.sendText(msg.to,"Mimic Off")
                        else:
	                    	cl.sendText(msg.to,"Already on")
            elif msg.text in ["Target list"]:
                        if wait3["target"] == {}:
                            cl.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in wait3["target"]:
                                mc += "✔️ "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if wait3["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                wait3["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                wait3["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic change to target")
                            else:
                                cl.sendText(msg.to,"I dont know")
            elif "Target @" in msg.text:
                        target = msg.text.replace("Target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                wait3["target"][t] = True
                            cl.sendText(msg.to,"Target added")
            elif "Del target @" in msg.text:
                        target = msg.text.replace("Del target @","")
                        gc = cl.getGroup(msg.to)
                        targets = []
                        for member in gc.members:
                            if member.displayName == target.rstrip(' '):
                                targets.append(member.mid)
                        if targets == []:
                            cl.sendText(msg.to, "User not found")
                        else:
                            for t in targets:
                                del wait3["target"][t]
                            cl.sendText(msg.to,"Target deleted")               
            elif "Copy " in msg.text:
                if msg.from_ in admin:
                 targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        contact = cl.getContact(target)
                        X = contact.displayName
                        profile = cl.getProfile()
                        profile.displayName = X
                        cl.updateProfile(profile)
                        cl.sendText(msg.to, "Success...")
                        #---------------------------------------
                        Y = contact.statusMessage
                        lol = cl.getProfile()
                        lol.statusMessage = Y
                        cl.updateProfile(lol)
                        #---------------------------------------
                        P = contact.pictureStatus
                        cl.updateProfilePicture(P)
                    except Exception as e:
                        cl.sendText(msg.to, "Failed!")
                        print (e)
            
            
            elif "create " in msg.text:
               if msg.from_ in admin:    
                midd = msg.text.replace("create ","")
                ki.findAndAddContactsByMid(midd)
                ki.createGroup(midd)
            elif "CreatGroup @" in msg.text:
              if msg.from_ in admin:
                print "[Command]dp executing"
                _name = msg.text.replace("CreatGroup @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                for target in g.Name:                                                      
                    ki.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            ki.createGroup(msg.to, target)
                            ki.sendText(msg.to, "sukses")
                        except:
                            pass
                print ("[Command]stel cover executed")
            elif msg.text.lower() == 'responsename':
              if msg.from_ in admin or staff:
                profile = ki.getProfile()
                text = profile.displayName + "􀜁􀅔"
                ki.sendText(msg.to, text)
                profile = kk.getProfile()
                text = profile.displayName + "􀜁􀅔"
                kk.sendText(msg.to, text)
                profile = kc.getProfile()
                text = profile.displayName + "􀜁􀅔"
                kc.sendText(msg.to, text)
            elif msg.text.lower() == 'bye':
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"􀜁􀇔􏿿Bye Bye 􀄃􀈡􏿿 "  +  str(ginfo.name)  + "")
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                    except:
                        pass    
            elif "Sp @" in msg.text:
                if msg.from_ in admin:
                   _name = msg.text.replace("Sp @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = cl.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except Exception as e:
                               cl.sendText(msg.to, str(e))
            elif "Sc @" in msg.text:
                if msg.from_ in admin:
                    _name = msg.text.replace("Sc @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                contact = cl.getContact(target)
                                cu = cl.channel.getCover(target)
                                path = str(cu)
                                cl.sendImageWithURL(msg.to, path)
                            except Exception as e:
                               cl.sendText(msg.to, str(e))
            elif ("Gn " in msg.text):
               if msg.from_ in mid:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("dlmusic " in msg.text):
                songname = msg.text.replace("dlmusic ","")
                params = {"songname": songname}
                r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    abc = song[3].replace('https://','http://')
                    cl.sendText(msg.to, "Judul: " + song[0].encode('utf-8') +"" + "\n" + "Durasi: " + song[1].encode('utf-8') +"" + "\n" + "Link: " + song[4].encode('utf-8'))
                    cl.sendText(msg.to, "Tunggu sebentar, loading VN")
                    cl.sendAudioWithURL(msg.sto, abc)

            elif "getlirik " in msg.text:
                songname = msg.text.replace("getlirik ","")
                params = {"songname": songname}
                r=requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data=r.text
                data=json.loads(data)
                for song in data:
                    songz = song[5].encode('utf-8')
                    lyric = songz.replace('ti:','Judul - ')
                    lyric = lyric.replace('ar:','Artis - ')
                    lyric = lyric.replace('al:','Album - ')
                    lyric = lyric.replace('by:','')
                    removeString = "[1234567890.:]"
                    for char in removeString:
                        lyric = lyric.replace(char,'')
                    cl.sendText(msg.to,lyric)
            elif "gimage " in msg.text:
                search = msg.text.replace("gimage ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    cl.sendText(msg.to,"Silahkan tunggu...")
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
#-----------------------------------------------------------)
            elif "getig " in msg.text:
                    try:
                    	instagram = msg.text.replace("getig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        text = "Name : "+namaIG+"\nBiography :\n"+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nMedia : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"\nUsername : "+usernameIG+""
                        cl.sendImageWithURL(msg.to, profileIG)
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
            elif "Kick " in msg.text:
               if msg.from_ in mid:
                midd = msg.text.replace("Kick ","")
                msg.to = midd
                msg.contentType = 9
                msg.contentMetadata={'STKPKGID': '8588',
                                                 'PRDTYPE': 'STICKER',
                                                 'MSGTPL': '3'}
                msg.text = None
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
     	        cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
                ki.sendMessage(msg)
       	       print ("spam berjalan")
                                
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Removed" in msg.text:
               if msg.from_ in mid:
                  try:
                     cl.removeAllMessages(op.param2)
                     cl.sendText(msg.to, " all pesan telah di hapus")
                     print ("sukses hapus")
                  except:
                      pass
            elif "Invite " in msg.text:
               if msg.from_ in mid:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            
            elif msg.text in ["Back"]:
                    try:
                       cl.updateProfilePicture(backup.pictureStatus)
                       cl.updateProfile(backup)
                       cl.sendText(msg.to, "Profile telah kembali...")
                    except Exception as e:
                       cl.sendText(msg.to, str(e))
            
            
            elif "Clone @" in msg.text:
                     _name = msg.text.replace("Clone @","")
                     _nametarget = _name.rstrip('  ')
                     gs = cl.getGroup(msg.to)
                     targets = []
                     for g in gs.members:
                         if _nametarget == g.displayName:
                             targets.append(g.mid)
                     if targets == []:
                         cl.sendText(msg.to, "Target Not Found")
                     else:
                         for target in targets:
                             try:
                                cl.cloneContactProfile(target)
                                cl.sendText(msg.to, "Succes")
                             except Exception as error:
                                 print (error)
            
            elif ("Pancal " in msg.text):
               if msg.from_ in mid:
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           cl.kickoutFromGroup(msg.to,[target])
                       except:
                           cl.sendText(msg.to,"Error")
            elif msg.text in ["Uppoto"]:
            	if msg.from_ in admin:
                 wait["uppoto"] = True
                 cl.sendText(msg.to,"send contact 😉")
            elif msg.text in ["Jepit"]:
            	if msg.from_ in admin:
                 wait["winvite"] = True
                 cl.sendText(msg.to,"send contact 😉")
            elif "Usir " in msg.text:
                  if msg.from_ in admin:
                       ulti0 = msg.text.replace("Usir ","")
                       ulti1 = ulti0.lstrip()
                       ulti2 = ulti1.replace("@","")
                       ulti3 = ulti2.rstrip()
                       _name = ulti3
                       gs = cl.getGroup(msg.to)
                       ginfo = cl.getGroup(msg.to)
                       gs.preventJoinByTicket = False
                       cl.updateGroup(gs)
                       invsend = 0
                       Ticket = cl.reissueGroupTicket(msg.to)
                       ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                       time.sleep(0.2)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    ki.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"TerCYDUC Vrohh")
                                    ki.sendText(msg.to,"Done, See u :*")
                                    ki.leaveGroup(msg.to)
                                    gs = cl.getGroup(msg.to)
                        	    gs.preventJoinByTicket = True
                        	    cl.updateGroup(gs)
                                    gs.preventJoinByTicket(gs)
                        	    cl.updateGroup(gs)
            elif msg.text in ["Reject invite"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"All invitations have been rejected")
                    else:
                        cl.sendText(msg.to,"Done")
            
            elif "Hajar " in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                   except:
                      pass
            elif msg.text in ["Jumpbot"]:
              if msg.from_ in mid:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                cb = ""
                cb2 = "" 
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)
                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""
                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"
                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    cl.sendMessage(msg)
                except Exception as error:
                    print (error)
            elif msg.text in ["All group"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n"
                            except:
                                h += "Error!"
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "|[Total Groups]| : " + total)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "[" + groups.name + "]\n -+GroupID : " + i + "\n -+Members : " + members + "\n -+MembersPending : " + pendings + "\n -+Creator : " + groups.creator.displayName + "\n"
                            except:
                                j += "Error!"
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "|[Total Groups Invited]| : " + totals)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")
            
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
            
            elif msg.text in ["æ„›ã®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["Gift2"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["Gift3"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["Gift4"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                kc.sendMessage(msg)
            elif "Kasih " in msg.text:
                  if msg.from_ in mid:
                       nk0 = msg.text.replace("Kasih ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           cl.sendText(msg.to,"contact tak terdeteksi....")
                           pass
                       else:
                           for target in targets:
                                try:
                                   cl.findAndAddContactsByMid(target)
                                   msg.to = target
                                   msg.contentType = 9
                                   msg.contentMetadata={'STKPKGID': '8588',
                                                 'PRDTYPE': 'STICKER',
                                                 'MSGTPL': '3'}
                                   msg.text = None
                                   cl.sendMessage(msg)
       	                           print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"done gift")
                                    ki.sendText(msg.to,"thanks")
            if msg.text in ["cancel","Cancel"]:
               if msg.from_ in mid:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            if msg.text in ["Ourl","Link on"]:
               if msg.from_ in mid:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            if msg.text in ["Curl","Link off"]:
               if msg.from_ in mid:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text.lower() in ["upot on"]:
                if msg.from_ in admin:
                    if wait["uppoto"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"uppoto ON😉")
                        else:
                            cl.sendText(msg.to,"uppoto on😉")
                    else:
                        wait["uppoto"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"uppoto already on")
                        else:
                            cl.sendText(msg.to,"already on")
            elif msg.text.lower() in ["upot off"]:
                if msg.from_ in admin:
                    if wait["uppoto"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"upoto off...*-* ")
                        else:
                            cl.sendText(msg.to,"uppoto off")
                    else:
                        wait["uppoto"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"uppoto already off")
                        else:
                            cl.sendText(msg.to,"uppoto off")
            elif "Id" == msg.text:
                cl.sendText(msg.to,msg.to)
            elif ("Baned " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
            
            elif "Block @" in msg.text:
                if msg.toType == 2:
                    print "[block] OK"
                    _name = msg.text.replace("Block @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                           targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to, "Not Found...")
                    else:
                        for target in targets:
                            try:
                               cl.blockContact(target)
                               cl.sendText(msg.to, "Success block contact~")
                            except Exception as e:
                               print (e)
            elif msg.text in["Blocklist"]:
                blockedlist = cl.getBlockedContactIds()
                cl.sendText(msg.to, "Please wait...")
                kontak = cl.getContacts(blockedlist)
                num=1
                msgs="User Blocked List\n"
                for ids in kontak:
                    msgs+="\n%i. %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n\nTotal %i blocked user(s)" % len(kontak)
                cl.sendText(msg.to, msgs)
            elif msg.text in ["TL:"]:
                tl_text = msg.text.replace("TL:","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            elif msg.text in ["Clear ban"]:
               if msg.from_ in mid:
                wait["blacklist"] = {}
                cl.sendText(msg.to, "all banlist removed😉")
            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Auto like:on"]:
			  if msg.from_ in admin:
			    if wait["likefunction"] == True:
				   if wait["lang"] == "JP":
				      cl.sendText(msg.to,"turning on auto like")
				   else:
				      cl.sendText(msg.to,"turning on auto like")
			    else:
				   wait["likefunction"] = True
				   if wait["lang"] == "JP":
					    cl.sendText(msg.to,"auto like have been enable")
				   else:
					    cl.sendText(msg.to,"auto like have been enable")
			
	    elif msg.text in ["Auto like:off"]:
	          if msg.from_ in admin:
			     if wait["likefunction"] == False:
				    if wait["lang"] == "JP":
				       cl.sendText(msg.to,"turning off auto like")
				    else:
				       cl.sendText(msg.to,"turning off auto like")
	        	     else:
				    wait["likefunction"] = False
				    if wait["lang"] == "JP":
					   cl.sendText(msg.to,"auto like have been disable")
				    else:
					   cl.sendText(msg.to,"auto like have been disable")
            elif msg.text in ["Auto welcome:on"]:
	          if msg.from_ in admin:
			     if wait["welcomemsg"] == True:
				    if wait["lang"] == "JP":
				       cl.sendText(msg.to,"turning on auto welcome")
				    else:
				       cl.sendText(msg.to,"turning on auto welcome")
			     else:
				    wait["welcomemsg"] = True
				    if wait["lang"] == "JP":
					    cl.sendText(msg.to,"auto welcome have been enable")
				    else:
					    cl.sendText(msg.to,"auto welcome have been enable")
						
	    elif msg.text in ["Auto welcome:off"]:
		         if msg.from_ in admin:
			        if wait["welcomemsg"] == False:
				       if wait["lang"] == "JP":
				          cl.sendText(msg.to,"turning off auto welcome")
				       else:
				          cl.sendText(msg.to,"turning off auto welcome")
			        else:
				       wait["welcomemsg"] = False
				       if wait["lang"] == "JP":
					      cl.sendText(msg.to,"auto welcome have been disable")
				       else:
					      cl.sendText(msg.to,"auto welcome have been disable")
            elif msg.text in ["Blockinvite on"]:
                if wait["Protectguest"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done.....")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done.....")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Blockinvite off"]:
                if wait["Protectguest"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"protect Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectguest"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"protect Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect on"]:
              if msg.from_ in mid:
                if wait["ProtectQR"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Please...do not open qr!!!")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Please...do not open qr!!")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect off"]:
              if msg.from_ in mid:
                if wait["ProtectQR"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Free....update group")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["ProtectQR"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Free....update group")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Rein on","invite on"]:
                if wait["Reinvite"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"awas limit😂")
                        print "[Command]Join on executed"
                    else:
                        ki.sendText(msg.to,"awas limit...")
                        print "[Command]Join on executed"
                else:
                    wait["Reinvite"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Rein om")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"gagal.....")
                        print "Join on executed"
            elif msg.text in ["Rein off","invite off"]:
                if wait["Reinvite"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Reinvite Off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto Rein Off")
                        print "[Command]Join off executed"
                else:
                    wait["Reinvite"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done...")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Done.....")
                        print "[Command]Join off executed"
            elif msg.text.lower() in ["winvite on"]:
                if msg.from_ in admin:
                    if wait["winvite"] == True:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"winvite ON😉")
                        else:
                            cl.sendText(msg.to,"Winvite on😉")
                    else:
                        wait["winvite"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Winvite already on")
                        else:
                            cl.sendText(msg.to,"already on")
            elif msg.text.lower() in ["winvite off"]:
                if msg.from_ in admin:
                    if wait["winvite"] == False:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"winvite off...*-* ")
                        else:
                            cl.sendText(msg.to,"winvite off")
                    else:
                        wait["winvite"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"winvite already off")
                        else:
                            cl.sendText(msg.to,"winvite off")
            elif msg.text in ["Contact on"]:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["é€£çµ¡å…ˆ:ã‚ªãƒ•","K off","Contact off","é¡¯ç¤ºï¼šé—œ"]:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done ")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•åƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•åƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»ã€‚è¦æ—¶å¼€è¯·æŒ‡å®šäººæ•°å‘é€")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Set"]:
                md = ""
                if wait["uppoto"] == True: md+="[*] Upfoto : on\n"
                else: md+=" Upfoto : off\n"
                if wait["Reinvite"] == True: md+="[*] Reinvite : on\n"
                else: md+=" Reinvite : off\n"
                if wait["Protectguest"] == True: md+="[*] Block Invite on\n"
                else: md+="Block Invite off\n"
                if wait["winvite"] == True: md+="[*] Winvite : on\n"
                else: md+="[*] Winvite : off\n"
                if wait["ProtectQR"] == True: md+="[*] Protect Qr on\n"
                else: md+="Protect qr off\n"
                if wait["contact"] == True: md+="[*] Contact : on\n"
                else: md+=" Contact : off\n"
                if wait["autoJoin"] == True: md+="[*] Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+="[*] Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+="[*] Auto leave : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+="[*] Share : on\n"
                else:md+=" Share : off\n"
                if wait["autoAdd"] == True: md+="[*] Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+="[*] Comment : on\n"
                else:md+="[*] Comment : off\n"
                cl.sendText(msg.to,md)
            
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•å€™èªžç¢ºèª"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")

            
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    cl.sendText(msg.to,"already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"done")
            
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    cl.sendText(msg.to,"already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"done")
            
#-----------------------------------------
            
            if msg.text.lower() in ["tagall"]:
                group = cl.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    cl.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "Done : " + str(jml) +  " Members"
                cnt.to = msg.to
                cl.sendMessage(cnt)
            
#---------------------------------------
            elif msg.text in ["Change clock "]:
                n = msg.text.replace("Change clock ","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
            elif msg.text in ["Up"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam Update")
                else:
                    cl.sendText(msg.to,"Please turn on the name clock")
            elif msg.text in ["Groupku","Glist"]:
       	         gid = cl.getGroupIdsJoined()
    	         h = ""
    	         for i in gid:
     	          h += "[⭐] %s \n" % (cl.getGroup(i).name + " | Members : " + str(len (cl.getGroup(i).members)))
    	         cl.sendText(msg.to, "☆「Group List」☆\n"+ h +"Total Group : " +str(len(gid)))
#---------------Cek Sider---------------
	    elif msg.text == "Point":
                      cl.sendText(msg.to, "rec sider..😉")
                      try:
                       del wait2['readPoint'][msg.to]
                       del wait2['readMember'][msg.to]
                      except:
                               pass
                      now2 = datetime.now()
                      wait2['readPoint'][msg.to] = msg.id
                      wait2['readMember'][msg.to] = ""
                      wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                      wait2['ROM'][msg.to] = {}
                      print (wait2)

            elif msg.text == "Sider":
                if msg.to in wait2['readPoint']:
                   if wait2["ROM"][msg.to].items() == []:
                      chiya = ""
                   else:
                      chiya = ""
                      for rom in wait2["ROM"][msg.to].items():
                         print (rom)
                         chiya += rom[1] + "\n"

		   cl.sendText(msg.to, "Jumlah Reader...😉%s\nread terbaru😉\n%s\nread time\n[%s]"  % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
       	        else:
		   cl.sendText(msg.to, "Please input Point to rec sider..😉")
#-----------------Cek Sider---------------------
            elif msg.text in ["Groupku"]:
       	         gid = cl.getGroupIdsJoined()
    	         h = ""
    	         for i in gid:
     	          h += "[⭐] %s \n" % (cl.getGroup(i).name + " | Members : " + str(len (cl.getGroup(i).members)))
    	         cl.sendText(msg.to, "☆「Group List」☆\n"+ h +"Total Group : " +str(len(gid)))

#----------------------------------------------------------------
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
#----------------------------------------------------------
            elif "Piuwits" in msg.text:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        #ki2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        print "kicker ok"
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
            elif "Balik" in msg.text:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        #ki2.leaveGroup(msg.to)
                        #kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["Kill"]:
               if msg.from_ in mid:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Fuck You")
                        cl.sendText(msg.to,"Fuck You")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
            if "Clean" in msg.text:
               if msg.from_ in mid:
                if msg.toType == 2:
                    print ("ok")
                    _name = msg.text.replace("Cleanse","")
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Just some casual cleansing ô")
                    ki.sendText(msg.to,"Group cleansed.")
                    cl.sendText(msg.to,"Fuck You All")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                        ki.sendText(msg.to,"Not found.")
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[cl,ki]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                ki.sendText(msg,to,"Group cleanse")
                                cl.sendText(msg,to,"Group cleanse")
                                ki.sendText(msg,to,"Group cleanse")

            
            elif "Blacklist @ " in msg.text:
               if msg.from_ in mid:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Succes")
                                except:
                                    cl.sendText(msg.to,"error")
#----------------------------------------

            elif "Bc " in msg.text:
				bctxt = msg.text.replace("Bc ","")
				cl.sendText(msg.to,(bctxt))
				#kk.sendText(msg.to,(bctxt))
				#kc.sendText(msg.to,(bctxt))

            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                cl.sendText(msg.to, "Progress...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                #ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                #kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                #kc.sendText(msg.to, "%sseconds" % (elapsed_time))

#------------------------------------------------------------------
            
            elif msg.text in ["Ban"]:
               if msg.from_ in mid:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
                #ki.sendText(msg.to,"send contact")
                #kk.sendText(msg.to,"send contact")
                #kc.sendText(msg.to,"send contact")
            elif msg.text in ["Unban"]:
               if msg.from_ in mid:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
                #ki.sendText(msg.to,"send contact")
                #kk.sendText(msg.to,"send contact")
                #kc.sendText(msg.to,"send contact")
            elif msg.text in ["Banlist"]:
               if msg.from_ in mid:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"nothing")
                    #ki.sendText(msg.to,"nothing")
                    #kk.sendText(msg.to,"nothing")
                    #kc.sendText(msg.to,"nothing")
                else:
                    cl.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    #ki.sendText(msg.to,mc)
                    #kk.sendText(msg.to,mc)
                    #kc.sendText(msg.to,mc)
            
            if msg.text in ["Kill ban"]:
               if msg.from_ in mid:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        #ki.sendText(msg.to,"There was no blacklist user")
                        #kk.sendText(msg.to,"There was no blacklist user")
                        #kc.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        cl.kickoutFromGroup(msg.to,[jj])
                        #ki.kickoutFromGroup(msg.to,[jj])
                        #kk.kickoutFromGroup(msg.to,[jj])
                        #kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #ki.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #kk.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    #kc.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
               if msg.from_ in mid: 
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            if "random:" in msg.text:
               if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random:","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif msg.text.lower() in ["aple"]:
                if msg.from_ in admin:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.2)
                        G = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        ki.updateGroup(G)
                        print ("[Command] Join")
                        G.preventJoinByTicket(G)
                        ki.updateGroup(G)
            elif msg.text.lower() in ["bye"]:
                if msg.toType == 2:
                  if msg.from_ in staff:
                    print ("[Command] Bye")
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to, "Terima Kasih")
                        kk.leaveGroup(msg.to, "Jangan Lupa Add Saya")
                        kc.leaveGroup(msg.to, "Assalamulaikum")
                    except:
                        pass
            elif msg.text in ["Mayhem"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print ("ok")
                    _name = msg.text.replace("Mayhem","")
                    gs = cl.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    #gs = kr.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    cl.sendText(msg.to,"「 Mayhem 」\nMayhem is STARTING♪\n' abort' to abort♪")
                    ki.sendText(msg.to,"「 Mayhem 」\n46 victims shall yell hul·la·ba·loo♪\nˌ/hələbəˈlo͞o,ˈhələbəˌlo͞o/")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak ditemukan")
                    else:
                        for target in targets:
                            if not target in Bots:
                                try:
                                   klist=[ki,cl,kk,kc]
                                   kicker=random.choice(klist)
                                   kicker.kickoutFromGroup(msg.to,[target])
                                   print (msg.to,[g.mid])
                                except:
                                   ki.sendText(msg.to,"Mayhem done")
            elif "unban " in msg.text:
                if msg.from_ in staff:
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    targets = []
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del wait["blacklist"][target]
                            f=codecs.open('st2__b.json','w','utf-8')
                            json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                            cl.sendText(msg.to,"Done Unbanned")
                            print ("[Command] Unbannad")
                        except:
                            pass
            elif "Recover" in msg.text:
		thisgroup = ki.getGroups([msg.to])
		Mids = [contact.mid for contact in thisgroup[0].members]
		mi_d = Mids[:33]
		ki.createGroup("Recover", mi_d)
		cl.sendText(msg.to,"Success recover")
            elif msg.text in ["Restart"]:
		if msg.from_ in admin:
		    cl.sendText(msg.to, "Restarting.....")
		    restart_program()
		    print ("@Restart")
		else:
		    cl.sendText(msg.to, "No Access")
            elif "Pap @" in msg.text:          
                   _name = msg.text.replace("Pap @","")
                   _nametarget = _name.rstrip('  ')
                   gs = cl.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       cl.sendText(msg.to,"Contact not found")
                   else:
                       for target in targets:
                           try:
                               contact = cl.getContact(target)
                               path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                               cl.sendImageWithURL(msg.to, path)
                           except:
                               pass            
            elif "Groupimage" in msg.text:
            	  group = cl.getGroup(msg.to)
                  cl.sendText(msg.to,"Gambar Grup :\n=> http://dl.profile.line-cdn.net/" + group.pictureStatus)
           #=================================Add mimic==========================
            elif ("mimic:add " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            cl.sendText(msg.to,"Target ditambahkan")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            pass
#=================================Del mimic==========================
            elif ("mimic:del " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            cl.sendText(msg.to,"Target dihapuskan")
                            cl.sendMessageWithMention(msg.to,target)
                            break
                        except:
                            pass
#=================================Mimic status==========================
            elif "mimic " in msg.text:
                if msg.from_ in admin:
                    cmd = msg.text.replace("mimic ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            cl.sendText(msg.to,"Mimic sudah on")
                        else:
                            cl.sendText(msg.to,"Mimic sudah on")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            cl.sendText(msg.to,"Mimic sudah off")
                        else:
                            cl.sendText(msg.to,"Mimic sudah off")
                            
            elif msg.text in ["Mlist"]:
                if wait2["target"] == {}:
                    cl.sendText(msh.to,"Nothing")
                else:
                    mc = "Target copy user\n"
                    mids = []
                    for s in range(len(wait2["target"])):
                        mids.append(wait2["target"][s])
                        cmids = cl.getContact(mids)
                    for x in range(len(cmids)):
                        mc += "\n["+str(x)+"]"+cmids[x].disiplayName
                        cl.sendText(msg.to,mc)
#==============================================================================
        if op.type == 26:
            msg = op.message
            if msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#===============================================================================
            elif msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                text = msg.text
                if text is not None:
                    cl.sendText(msg.to,text)
                else:
                    if msg.contentType == 7:
                        msg.contentType = 7
                        msg.text = None
                        msg.contentMetadata = {
                                             "STKID": "6",
                                             "STKPKGID": "1",
                                             "STKVER": "100" }
                        cl.sendMessage(msg)
                    elif msg.contentType == 13:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': msg.contentMetadata["mid"]}
                        cl.sendMessage(msg)
#================================================================================= 
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・" + Name
                        wait2['ROM'][op.param1][op.param2] = "・" + Name
                else:
                    cl.sendText
            except:
                pass


        if op.type == 59:
            print (op)
  	      
        
    except Exception as error:
        print (error)
#-----------------------------------------------
def autolike():
            for zx in range(0,20):
                hasil = ki.activity(limit=20)
                if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
                    try:    
                        kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                        kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By line:://ti/p/~edolveak")
                        ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                        ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like By line:://ti/p/~edolveak")
                        print ("DiLike")
                    except:
                            pass
                else:
                        print ("Sudah DiLike")
            time.sleep(500)
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

       
def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

