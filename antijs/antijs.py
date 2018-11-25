# all of this data is copied from creator production PrankBots
# don't forget to always support the prabkbots channel
# SUBSCRABE HERE https://bit.ly/2xbVxlh
# MY ID LINE :: http://line.me/ti/p/~Adiputra.95
# Copy Righ :: http://github.com/Aprank
# Country :: INDONESIA.
# Area :: BOGOR.
#___SCRIPT PYTHON 3____
# GET INSTALED IN MODULE FROM VPS IT IS IN REPOSIYORIES
#*Acil Creator
# DI SUBSCRABE CHANNEL NYA JIKA BOT LINE UPDATE PASTI DI KABARIN DI CHANNELNYA
#VERSI VPS.

from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess,asyncio
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
_session = requests.session()
botStart = time.time()
"""
 1 SELFBOT ONLY PENAMBAHAN 1 BOT DAN 1 ANTI JS
"""
settingsOpen = codecs.open("PrankBots.json","r","utf-8")
PrankBots = json.load(settingsOpen)
settingsOpen = codecs.open("Abouts.json","r","utf-8")
Abouts = json.load(settingsOpen)
me = LINE(PrankBots["selfbot"])
me.log(str(me.authToken))
channelToken = me.getChannelResult()
bot1 = LINE(PrankBots["bot1"])
Java_script = LINE(PrankBots["java_script"])
me.log('all ready')
Java_scriptRanger = Java_script.profile.mid
Java_scriptProfile = Java_script.getProfile()
Java_scriptSettings = Java_script.getSettings()
BotRanger = bot1.profile.mid
BotRangerProfile = bot1.getProfile()
BotRangerSettings = bot1.getSettings()
meM = me.profile.mid
meProfile = me.getProfile()
meSettings = me.getSettings()
oepoll = OEPoll(me)
Owner = PrankBots["owner"]
Acil = [meM,BotRanger,Java_scriptRanger,Owner]
Stiles = "│™│ "
respontags = {
    "Auto_text": "\nYes I'am Here"
}
Sid={
    "Tar":{},
    "Red":{},
    "Reason":{}
}
mid = me.getProfile().mid
PrankBots["myProfile"]["displayName"] = meProfile.displayName
PrankBots["myProfile"]["statusMessage"] = meProfile.statusMessage
cont = me.getContact(meM)
PrankBots["myProfile"]["pictureStatus"] = meProfile.pictureStatus
coverId = me.getProfileDetail()["result"]["objectId"]
apikey_com = "u0ac948397fbc732bd3bc5ca273faa698"
coverId = me.getProfileDetail()["result"]["objectId"]
PrankBots["myProfile"]["coverId"] = coverId
Extr = me.getContact(apikey_com).displayName
def backupData():
    try:
        backup = PrankBots
        f = codecs.open('PrankBots.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = Abouts
        f = codecs.open('Abouts.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        ErrorX(error)
        return False
def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@PrankBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
def Run_Xp():
    print ("RESTART")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
Devert = "My name is "+cont.displayName+"\nMy git your bots"
def Run_Xx():
    print ("BOT KEMBALI AKTIF")
    backupData()
    python = sys.executable
    os.execl(python, python, *sys.argv)
mulai = time.time()
def Musik(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+me.getContact(meM).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': me.getContact(meM).statusMessage if me.getContact(meM).statusMessage != '' else 'creator By meMots |ID LINE|\nadiputra.95', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': me.getContact(meM).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.me.me/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+meM,'MSG_SENDER_NAME':  me.getContact(meM).displayName,}
    return me.sendMessage(to, me.getContact(meM).displayName, contentMetadata, 19)
def ErrorX(text):
    me.log("data: " + str(text))
    time_ = datetime.now()
    with open("Data.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
def sendMeention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@PrankBots "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    me.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        ErrorX(error)
        me.sendMessage(to, "Error\n\n" + str(error))
extras = Stiles+"Creator:by "+Extr+"\n"
def RunTheRun(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,7,25)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = me.getAllContactIds()
        gid = me.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        h = me.getContact(meM)
        me.reissueUserTicket()
        My_Id = "http://line.me/ti/p/"+me.getUserTicket().id
        text += mention+"WAKTU : "+datetime.strftime(timeNow,'%H:%M:%S')+" INDONESIA\n\nMY GROUP : "+str(len(gid))+"\n\nMY FRIEND: "+str(len(teman))+"\n\nTIME VPS : In "+hari+"\n\nᴄʀᴇᴀᴛᴏʀ ʙʏ : ᴘʀᴀɴᴋʙᴏᴛs. ʟɪɴᴇ ᴠᴇʀ.8.14.2\n\nTANGGAL : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n\nTIME RUN : \n • "+bot+"\n\nMY TOKEN : "+str(me.authToken)+"\n\nMY MID : "+h.mid+"\n\nMY ID LINE : "+My_Id
        me.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        me.sendMessage(to, "Error :\n" + str(error))
def SqL_R(text):
    R_SQL = text.lower()
    if PrankBots["key"] == True:
        if R_SQL.startswith(PrankBots["text"]):
            PrankBotsData = R_SQL.replace(PrankBots["text"],"")
        else:
            PrankBotsData = "Undefined command"
    else:
        PrankBotsData = text.lower()
    return PrankBotsData
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 26 or op.type == 25:
            msg = op.message
            Id = msg.id
            R = msg.to or to
            D = msg._from
            Proses_message = msg.text
            if Proses_message == "Active" or Proses_message == "active":
                if D in Owner or D in meM:
                    PrankBots["bot"] = True
                    me.sendMessage(R,"Bot active")
                    me.sendMessage(R,"Already Ok "+me.getContact(D).displayName)
                    PrankBots["Conection"] = R
                    Run_Xx()
                    
            if Proses_message == "Non active" or Proses_message == "non active":
                print ("NOTIF BOT NON ACTIVE")
                if D in Owner or D in meM:
                    PrankBots["bot"] = False
                    me.sendMessage(R,"Bot Non Active")
                    me.sendMessage(R,"Ok I'am Turn down "+me.getContact(D).displayName)
                
        if op.type == 25 or op.type == 26:
          if PrankBots["bot"] == True:
            msg = op.message
            text = msg.text
            Id = msg.id
            R = msg.to or to
            D = msg._from
            Gr = op.param1
            OperPrankBotsData = PrankBots["text"].title()
            if PrankBots["key"] == False:
                 OperPrankBotsData = ''
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if D != me.profile.mid:
                        to = D
                    else:
                        to = R
                elif msg.toType == 1:
                    to = R
                elif msg.toType == 2:
                    to = R
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        PrankBotsData = SqL_R(text)
                        if PrankBotsData == Abouts["1"]:
                          if D in Owner or D in meM:
                            Res= extras+Stiles+Abouts["0"]+"\n"
                            Res+= Stiles+"1. "+OperPrankBotsData+Abouts["1"]+"\n"
                            Res+= Stiles+"2. "+OperPrankBotsData+Abouts["2"]+"\n"
                            Res+= Stiles+"3. "+OperPrankBotsData+Abouts["3"]+"\n"
                            Res+= Stiles+"4. "+OperPrankBotsData+Abouts["4"]+"\n"
                            Res+= Stiles+"5. "+OperPrankBotsData+Abouts["5"]+"\n"
                            Res+= Stiles+"6. "+OperPrankBotsData+Abouts["6"]+"\n"
                            Res+= Stiles+"7. "+OperPrankBotsData+Abouts["7"]+"\n"
                            Res+= Stiles+"8. "+OperPrankBotsData+Abouts["8"]+" *porn\n"
                            Res+= Stiles+"9. "+OperPrankBotsData+Abouts["9"]+" *judul\n"
                            Res+= Stiles+"10. "+OperPrankBotsData+Abouts["10"]+" *tags\n"
                            Res+= Stiles+"11. "+OperPrankBotsData+Abouts["11"]+"\n"
                            Res+= Stiles+"12. "+OperPrankBotsData+Abouts["12"]+" *txt/txt/txt\n"
                            Res+= Stiles+"13. "+OperPrankBotsData+Abouts["13"]+" *text\n"
                            Res+= Stiles+"14. "+OperPrankBotsData+Abouts["14"]+"\n"
                            Res+= Stiles+"15. "+OperPrankBotsData+Abouts["15"]+"\n"
                            Res+= Stiles+"16. "+OperPrankBotsData+Abouts["16"]+"\n"
                            Res+= Stiles+"17. "+OperPrankBotsData+Abouts["17"]+"\n"
                            Res+= Stiles+"18. "+OperPrankBotsData+Abouts["18"]+"\n"
                            Res+= Stiles+"19. "+OperPrankBotsData+Abouts["19"]+" *tags\n"
                            Res+= Stiles+"20. "+OperPrankBotsData+Abouts["20"]+" *tags\n"
                            Res+= Stiles+"21. "+OperPrankBotsData+Abouts["21"]+" *tags\n"
                            Res+= Stiles+"22. "+OperPrankBotsData+Abouts["22"]+" *tags\n"
                            Res+= Stiles+"23. "+OperPrankBotsData+Abouts["23"]+" *tags\n"
                            Res+= Stiles+"24. "+OperPrankBotsData+Abouts["24"]+" *tags\n"
                            Res+= Stiles+"25. "+OperPrankBotsData+Abouts["25"]+" *text\n"
                            Res+= Stiles+"26. "+OperPrankBotsData+Abouts["26"]+" *01-02-1995\n"
                            Res+= Stiles+"27. "+OperPrankBotsData+Abouts["27"]+" *id ig\n"
                            Res+= Stiles+"28. "+OperPrankBotsData+Abouts["28"]+" *id smule\n"
                            Res+= Stiles+"29. "+OperPrankBotsData+Abouts["29"]+"\n"
                            Res+= Stiles+"30. "+OperPrankBotsData+Abouts["30"]+" *text\n"
                            Res+= Stiles+"31. "+OperPrankBotsData+Abouts["31"]+" *text\n"
                            Res+= Stiles+"32. "+OperPrankBotsData+Abouts["32"]+"\n"
                            Res+= Stiles+"33. "+OperPrankBotsData+Abouts["33"]+" *text\n"
                            Res+= Stiles+"34. "+OperPrankBotsData+Abouts["34"]+"\n"
                            Res+= Stiles+"35. "+OperPrankBotsData+Abouts["35"]+"\n"
                            Res+= Stiles+"36. "+OperPrankBotsData+Abouts["36"]+"\n"
                            Res+= Stiles+"37. "+OperPrankBotsData+Abouts["37"]+"\n"
                            Res+= Stiles+"38. "+OperPrankBotsData+Abouts["38"]+"\n"
                            Res+= Stiles+"39. "+OperPrankBotsData+Abouts["39"]+"\n"
                            Res+= Stiles+"40. "+OperPrankBotsData+Abouts["40"]+"\n"
                            Res+= Stiles+"41. "+OperPrankBotsData+Abouts["41"]+"\n"
                            Res+= Stiles+"42. "+OperPrankBotsData+Abouts["42"]+"\n"
                            Res+= Stiles+"43. "+OperPrankBotsData+Abouts["43"]+"\n"
                            Res+= Stiles+"44. "+OperPrankBotsData+Abouts["44"]+"\n"
                            Res+= Stiles+"45. "+OperPrankBotsData+Abouts["45"]+"\n"
                            Res+= Stiles+"46. "+OperPrankBotsData+Abouts["46"]+"\n"
                            Res+= Stiles+"47. "+OperPrankBotsData+Abouts["47"]+"\n"
                            Res+= Stiles+"48. "+OperPrankBotsData+Abouts["48"]+"\n"
                            Res+= Stiles+"49. "+OperPrankBotsData+Abouts["49"]+"\n"
                            Res+= Stiles+"50. "+OperPrankBotsData+Abouts["50"]+"\n"
                            Res+= Stiles+"51. "+OperPrankBotsData+Abouts["51"]+"\n"
                            Res+= Stiles+"52. "+OperPrankBotsData+Abouts["52"]+"\n"
                            Res+= Stiles+"53. "+OperPrankBotsData+Abouts["53"]+"\n"
                            Res+= Stiles+"54. "+OperPrankBotsData+Abouts["54"]+"\n"
                            Res+= Stiles+"55. "+OperPrankBotsData+Abouts["55"]+"\n"
                            Res+= Stiles+"56. "+OperPrankBotsData+Abouts["56"]+"\n"
                            Res+= Stiles+"57. "+OperPrankBotsData+Abouts["57"]+"\n"
                            Res+= Stiles+"58. "+OperPrankBotsData+Abouts["58"]+"\n"
                            Res+= Stiles+"59. "+OperPrankBotsData+Abouts["59"]+"\n"
                            Res+= Stiles+"60. "+OperPrankBotsData+Abouts["60"]+"\n"
                            Res+= Stiles+"61. "+OperPrankBotsData+Abouts["61"]+"\n"
                            Res+= Stiles+"62. "+OperPrankBotsData+Abouts["62"]+"\n"
                            Res+= Stiles+"63. "+OperPrankBotsData+Abouts["63"]+"\n"
                            Res+= Stiles+"64. "+OperPrankBotsData+Abouts["64"]+"\n"
                            Res+= Stiles+"65. "+OperPrankBotsData+Abouts["65"]+"\n"
                            Res+= Stiles+"66. "+OperPrankBotsData+Abouts["66"]+"\n"
                            Res+= Stiles+"67. "+OperPrankBotsData+Abouts["67"]+" [invite bot]\n"
                            Res+= Stiles+"68. "+OperPrankBotsData+Abouts["68"]+" [bot leave]\n"
                            Res+= Stiles+"69. "+OperPrankBotsData+Abouts["69"]+"\n"
                            Res+= Stiles+"70. "+OperPrankBotsData+Abouts["70"]+"\n"
                            Res+= Stiles+"71. "+OperPrankBotsData+Abouts["76"]+"\n"
                            Res+= Stiles+"72. "+OperPrankBotsData+Abouts["71"]+" [delete blacklist]\n"
                            Res+= Stiles+"73. "+OperPrankBotsData+Abouts["72"]+"\n"
                            Res+= Stiles+"74. "+OperPrankBotsData+Abouts["73"]+" @ [self bot kick target]\n"
                            Res+= Stiles+"75. "+OperPrankBotsData+Abouts["74"]+" @ [bot kick target]\n"
                            Res+= Stiles+"76. "+OperPrankBotsData+Abouts["75"]+"\n"
                            Res+= Stiles+"_____CHECK BOT______\n"
                            if PrankBots["Add"] == True: Res+= Stiles+" autoadd->『on』\n"
                            else: Res+= Stiles+" autoadd->『off』\n"
                            if PrankBots["Shared"] == True: Res+= Stiles+" shared->『on』\n"
                            else: Res+= Stiles+" shared->『off』\n"
                            if PrankBots["Join"] == True: Res+= Stiles+" autojoin->『on』\n"
                            else: Res+= Stiles+" autojoin->『off』\n"
                            if PrankBots["Read"] == True: Res+= Stiles+" autoread->『on』\n"
                            else: Res+= Stiles+" autoread->『off』\n"
                            if PrankBots["Unsend"] == True: Res+= Stiles+" unsend->『on』\n"
                            else: Res+= Stiles+" unsend->『off』\n"
                            if PrankBots["Wc"] == True: Res+= Stiles+" welcome->『on』\n"
                            else: Res+= Stiles+" welcome->『off』\n"
                            if PrankBots["Respon"] == True: Res+= Stiles+" respon->『on』\n"
                            else: Res+= Stiles+" respon->『off』\n"
                            Protection = ""
                            a = 0
                            gid = PrankBots["PROTECT"]
                            for group in gid:
                                a = a + 1
                                end = '\n'
                                pli = Stiles + str(a) + ". " +me.getGroup(group).name
                            Res += Stiles+"━━━━━p̲̅r̲̅o̲̅t̲̅e̲̅c̲̅t̲̅ g̲̅r̲̅o̲̅u̲̅p̲̅━━━━━━"+Protection+"\n"+Stiles+"━━━━ %s DI PROTECT ━━━━\n" %(str(len(PrankBots["PROTECT"])))
                            Res += Stiles+"____________________\n"
                            Res += Stiles+"______SelfName______\n"+Stiles+meProfile.displayName+"\n"
                            me.sendContact(R,apikey_com)
                            me.sendMessage(R, str(Res)+Stiles+"Subcrabe my Channel\n"+Stiles+" https://bit.ly/2xbVxlh")
                        if PrankBotsData == Abouts["2"]:
                          if D in Owner or D in meM:
                            try:
                                me.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                me.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                me.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                me.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                me.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                bot1.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                bot1.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                bot1.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                bot1.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                bot1.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                Java_script.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                Java_script.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                Java_script.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                Java_script.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                Java_script.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                Musik(R)
                                RunTheRun(apikey_com, D, "_______RESULT______\n")
                            except:Musik(R)
                        if PrankBotsData == Abouts["3"]:
                          if D in Owner or D in meM:
                            me.reissueUserTicket()
                            My_Id = me.profile.displayName + "My id Line: http://line.me/ti/p/" + me.getUserTicket().id
                            me.sendMessage(R,My_Id)
                        if PrankBotsData == Abouts["4"]:
                          if D in Owner or D in meM:
                            me.leaveGroup(R)
                        if PrankBotsData == Abouts["5"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            cu = me.getProfileCoverURL(D)          
                            path = str(cu)
                            me.sendImageWithURL(R, path)
                        if PrankBotsData == Abouts["6"]:
                          if D in Owner or D in meM:
                            result = requests.get("http://jadwalnonton.com/")
                            data = BeautifulSoup(result.content, 'html5lib')
                            hasil = "_______CINEMA______\nType : Movie List Today\n"
                            no = 1
                            for dzin in data.findAll('div', attrs={'class':'col-xs-6 moside'}):
                                hasil += "\n\n{}. {}".format(str(no), str(dzin.find('h2').text))
                                hasil += "\n     Link : {}".format(str(dzin.find('a')['href']))
                                no = (no+1)
                            me.sendMessage(R, str(hasil))
                        if PrankBotsData == Abouts["7"]:
                          if D in Owner or D in meM:
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get('http://api-1cak.herokuapp.com/random')
                                data = r.text
                                data = json.loads(data)
                                img = data["img"]
                                me.sendMessage(R,"━═| Daftar cakcak |═━\n━═| Title: %s\n━═| Link: %s\n━═| Id: %s\n━═| Votes: %s\n━═| NSFW: %s\n━═| [ Finish ] |═━" %(str(data["title"].replace('FACEBOOK Comments', ' ')), str(data["url"]), str(data["id"]), str(data["votes"]), str(data["nsfw"])))
                        if PrankBotsData.startswith(Abouts["8"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            kata = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                try:
                                    r = web.get("https://api.redtube.com/?data=redtube.Videos.searchVideos&output=json&search={}".format(urllib.parse.quote(kata)))
                                    data = r.text
                                    data = json.loads(data)
                                    ret_ = "━═Bokep inimah"
                                    no = 1
                                    anu = data["videos"]
                                    if len(anu) >= 20:
                                        for s in range(20):
                                            hmm = anu[s]
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    else:
                                        for s in anu:
                                            hmm = s
                                            title = hmm['video']['title']
                                            duration = hmm['video']['duration']
                                            views = hmm['video']['views']
                                            link = hmm['video']['embed_url']
                                            ret_ += "\n━═ {}. \nTitle ━═ {}\nDurasi ━═ {}\nViews ━═ {}\nLink ━═ {}".format(str(no), str(title), str(duration), str(views), str(link))
                                            no += 1
                                    me.sendMessage(R, str(ret_))
                                except:
                                    me.sendMessage(R, "Tidak ditemukan")
                        if PrankBotsData.startswith(Abouts["9"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            title = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get("http://www.omdbapi.com/?t="+title+"&y=&plot=full&apikey=4bdd1d70")
                                data=r.text
                                data=json.loads(data)
                                hasil = "╭━━═════[ Hasil pencarian film]"
                                hasil += "\nInformasi ━═| " +str(data["Title"])+ " (" +str(data["Year"])+ ")"
                                hasil += "\nPlot ━═| " +str(data["Plot"])
                                hasil += "\nDirector ━═| " +str(data["Director"])
                                hasil += "\nActors ━═| " +str(data["Actors"])
                                hasil += "\nRelease ━═| " +str(data["Released"])
                                hasil += "\nGenre ━═| " +str(data["Genre"])
                                hasil += "\nTimer ━═| " +str(data["Runtime"])
                                img = data["Poster"]
                                me.sendImageWithURL(R,img)
                                me.sendMessage(R,hasil)
                        if PrankBotsData.startswith(Abouts["10"]):
                          if D in Owner or D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = me.getContact(key1)
                            me.findAndAddContactsByMid(key1)
                            me.sendMessage(R, "teman di tambahkan")
                        if PrankBotsData == Abouts["11"]:
                          if D in Owner or D in meM:
                            me.sendMessage(R, "Selesai.!!")
                            PrankBots["Conection"] = R
                            Run_Xp()
                        if PrankBotsData.startswith(Abouts["12"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            txt = teks.split("/")
                            bag1 = txt[0]
                            bag2 = txt[1]
                            bag3 = txt[2]
                            angka = ["1","2","3","4","5"]
                            latar = random.choice(angka)
                            nomor = ["1","2","3","4"]
                            background = random.choice(nomor)
                            url = "https://ari-api.herokuapp.com/retro?bg="+latar+"&txt="+background+"&text1="+bag1+"&text2="+bag2+"&text3="+bag3
                            me.sendImageWithURL(R, url)
                        if PrankBotsData.startswith(Abouts["13"]):
                          if D in Owner or D in meM:
                            separate = text.split(" ")
                            teks = text.replace(separate[0] + " ","")
                            url = "https://ari-api.herokuapp.com/led?text="+teks+"&sign=PB"
                            me.sendImageWithURL(R, url)
                        if PrankBotsData == Abouts["14"]:
                          if D in Owner or D in meM:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            me.sendMessage(R, "━━━━━╦RUNTIME BOTS╦━━━━━\n ┣━╦[ {}".format(str(runtime)))
                        if PrankBotsData == Abouts["15"]:
                          if D in Owner or D in meM:
                            start = time.time()
                            me.sendMessage(R, "gooo...")
                            elapsed_time = time.time() - start
                            me.sendMessage(R,format(str(elapsed_time)))
                        if PrankBotsData == Abouts["16"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendMessage(R,h.mid)
                        if PrankBotsData == Abouts["17"]:
                          if D in Owner or D in meM:
                            contact = me.getContact(D)
                            cover = me.getProfileCoverURL(D)
                            result = "╔══[ Details Profile ]"
                            result += "\n╠ Display Name : {}".format(contact.displayName)
                            result += "\n╠ Mid : {}".format(contact.mid)
                            result += "\n╠ Status Message : {}".format(contact.statusMessage)
                            result += "\n╠ Picture Profile : http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus)
                            result += "\n╠ Cover : {}".format(str(cover))
                            result += "\n╚══[ Finish ]"
                            me.sendImageWithURL(R, "http://dl.profile.line-cdn.net/{}".format(contact.pictureStatus))
                            me.sendImageWithURL(R, str(cover))
                            me.sendMessage(R, str(result))
                        if PrankBotsData == Abouts["18"]:
                          if D in Owner or D in meM:
                            h = me.getContact(D)
                            me.sendVideoWithURL(R,"http://dl.profile.line-cdn.net/" + h.pictureStatus + "/vp")
                        if PrankBotsData.startswith(Abouts["19"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                me.sendMessage(R, str(ret_))
                        if PrankBotsData.startswith(Abouts["20"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus
                                    me.sendImageWithURL(R, str(path))
                        if PrankBotsData.startswith(Abouts["21"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.me.naver.jp/" + me.getContact(ls).pictureStatus + "/vp"
                                    me.sendVideoWithURL(R, str(path))
                        if PrankBotsData.startswith(Abouts["22"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Namanya\n{}".format(str(contact.displayName)))
                        if PrankBotsData.startswith(Abouts["23"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    me.sendMessage(R, "Status kontak\n\n{}".format(str(contact.statusMessage)))
                        if PrankBotsData.startswith(Abouts["24"]):
                          if D in Owner or D in meM:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = me.getContact(ls)
                                    mi_d = contact.mid
                                    me.sendContact(R, mi_d)
                        if PrankBotsData.startswith(Abouts["25"]):
                          if D in Owner or D in meM:
                            me.sendMessage(R, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(PrankBots["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                me.sendMessage(R, str(ret_))
                        if PrankBotsData.startswith(Abouts["26"]):
                          if D in Owner or D in meM:
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━═════[CREATOR PRANKBOTS]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                        if PrankBotsData.startswith(Abouts["27"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(PrankBots["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                me.sendImageWithURL(R, text1[0])
                                me.sendMessage(R, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")
                        if PrankBotsData.startswith(Abouts["28"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            me.sendMessage(R, "ini id smulenya kak\n" + smule)
                        if PrankBotsData == Abouts["29"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                members = [mem.mid for mem in group.members]
                                me.acquireGroupCallRoute(R)
                                me.inviteIntoGroupCall(R, contactIds=members)
                                me.sendMessage(R, "Berhasil")
                        if PrankBotsData.startswith(Abouts["30"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'id'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("hasil.mp3")
                            me.sendAudio(R,"hasil.mp3")
                        if PrankBotsData.startswith(Abouts["31"]):
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                X = me.getGroup(R)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                me.updateGroup(X)
                        if PrankBotsData == Abouts["32"]:
                          if D in Owner or D in meM:
                            me.removeAllMessages(op.param2)
                            me.sendMessage(R, "Chat deleted")
                        if PrankBotsData.startswith(Abouts["33"]):
                          if D in Owner or D in meM:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = me.groups
                            for group in groups:
                                sendMessageWithFooter(group, "╭━━━━━╦BroadCast by Self╦━━━━━╮\n{}".format(str(txt))+"\nDont forget to Subscrabe :D\nChannel : https://bit.ly/2xbVxlh")
                            me.sendMessage(R, "Berhasil broadcast ke {} group".format(str(len(groups))))
                        if PrankBotsData == Abouts["34"]:
                          if D in Owner or D in meM:
                            groups = me.groups
                            ret_ = "╭━━━━━══[ Group List ]══━━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = me.getGroup(gid)
                                ret_ += "\n┣═ {}. {} ┣═Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]════━━━━━".format(str(len(groups)))
                            me.sendMessage(R, str(ret_))
                        if PrankBotsData == Abouts["35"]:
                          if D in Owner or D in meM:
                            contactlist = me.getAllContactIds()
                            kontak = me.getContacts(contactlist)
                            num=1
                            msgs="╭━━━━━══[ Friend List ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Friend Result ]══━━━━━\nTotal : %i" % len(kontak)
                            me.sendMessage(R, msgs)
                        if PrankBotsData == Abouts["36"]:
                          if D in Owner or D in meM:
                            blockedlist = me.getBlockedContactIds()
                            kontak = me.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━━══[ Friend Block ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Block Result ]══━━━━━\nBlock Total : %i" % len(kontak)
                            me.sendMessage(R, msgs)
                        if PrankBotsData == Abouts["37"]:
                          if D in Owner or D in meM:
                            me.sendMessage(R, "━━━━══[Pembuat Grup]══━━━━")
                            group = me.getGroup(R)
                            GS = group.creator.mid
                            me.sendContact(R, GS)
                            me.sendMessage(R, "━━━━══━━╩━━══━━━━")
                        if PrankBotsData == Abouts["38"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n┣═ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    me.sendMessage(R, str(ret_))
                        if PrankBotsData == Abouts["39"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                if msg.toType == 2:
                                    group = me.getGroup(R)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        me.sendMessage(R, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        me.sendMessage(R, str(ret_))
                        if PrankBotsData == Abouts["40"]:
                          if D in Owner or D in meM:
                            if D in meM:
                                group = me.getGroup(R)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://me.me/R/ti/g/{}".format(str(me.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭━━━━══[ Group Info ]"
                                ret_ += "\n┣═Nama Group : {}".format(str(group.name))
                                ret_ += "\n┣═ID Group : {}".format(group.id)
                                ret_ += "\n┣═Pembuat : {}".format(str(gCreator))
                                ret_ += "\n┣═Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n┣═Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣═━━━Kode Qr/Link━━━═"
                                ret_ += "\n┣═Group Ticket : {}".format(gTicket)
                                ret_ += "\n┣═Group Qr : {}".format(gQr)
                                ret_ += "\n╰━━━━══[ CREATOR PRANKBOT]"
                                me.sendImageWithURL(R, path)
                                me.sendMessage(R, str(ret_))
                        if PrankBotsData == Abouts["41"]:
                          if D in Owner or D in meM:
                            group = me.getGroup(R)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            me.sendImageWithURL(R, path)
                        if PrankBotsData == Abouts["42"]:
                          if D in Owner or D in meM:
                            gid = me.getGroup(R)
                            me.sendMessage(R, "Name group\n" + gid.name)
                        if PrankBotsData == Abouts["43"]:
                          if D in Owner or D in meM:
                            gid = me.getGroup(R)
                            me.sendMessage(R,gid.id)
                        if PrankBotsData == Abouts["44"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    ticket = me.reissueGroupTicket(R)
                                    me.sendMessage(R, "https://me.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "https://me.me/R/ti/g/{}".format(str(ticket)))
                        if PrankBotsData == Abouts["45"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == False:
                                    me.sendMessage(R, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil membuka Qr")
                        if PrankBotsData == Abouts["46"]:
                          if D in Owner or D in meM:
                            if msg.toType == 2:
                                group = me.getGroup(R)
                                if group.preventedJoinByTicket == True:
                                    me.sendMessage(R, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    me.updateGroup(group)
                                    me.sendMessage(R, "Berhasil menutup Qr")
                        if PrankBotsData == Abouts["47"]:
                          if D in Owner or D in meM:
                            PrankBots["Add"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["48"]:
                          if D in Owner or D in meM:
                            PrankBots["Add"] = False
                            me.sendMessage(R, "Already ff")
                        if PrankBotsData == Abouts["49"]:
                          if D in Owner or D in meM:
                            PrankBots["Join"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["50"]:
                          if D in Owner or D in meM:
                            PrankBots["Join"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["51"]:
                          if D in Owner or D in meM:
                            PrankBots["Read"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["52"]:
                          if D in Owner or D in meM:
                            PrankBots["Read"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["53"]:
                          if D in Owner or D in meM:
                            PrankBots["Unsend"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["54"]:
                          if D in Owner or D in meM:
                            PrankBots["Unsend"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["55"]:
                          if D in Owner or D in meM:
                            PrankBots["Wc"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["56"]:
                          if D in Owner or D in meM:
                            PrankBots["Wc"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["57"]:
                          if D in Owner or D in meM:
                            PrankBots["Shared"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["58"]:
                          if D in Owner or D in meM:
                            PrankBots["Shared"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["59"]:
                          if D in Owner or D in meM:
                            PrankBots["Respon"] = True
                            me.sendMessage(R, "Already on")
                        if PrankBotsData == Abouts["60"]:
                          if D in Owner or D in meM:
                            PrankBots["Respon"] = False
                            me.sendMessage(R, "Already off")
                        if PrankBotsData == Abouts["61"]:
                          if D in Owner or D in meM:
                                try:
                                    del Sid['Red'][R]
                                    del Sid['Reason'][R]
                                    del Sid['Tar'][R]
                                except:
                                    pass
                                Sid['Red'][R] = Id
                                Sid['Reason'][R] = ""
                                Sid['Tar'][R]=True
                                me.sendMessage(R, "di aktifkan untuk grup\n"+g.name)
                        if PrankBotsData == Abouts["62"]:
                          if D in Owner or D in meM:
                            if R in Sid['Red']:
                                Sid['Tar'][R]=False
                                me.sendMessage(R, "Daftar yang terlihat\n"+Sid['Reason'][msg.to])
                                me.sendMessage(R, "Already off")
                            else:
                                me.sendMessage(R, "aktifkan dulu beb")
                        if PrankBotsData == Abouts["63"]:
                         if D in Owner or D in meM:
                          group = me.getGroup(R)
                          Rmem = [contact.mid for contact in group.members]
                          Dmem = len(Rmem)//20
                          try:                          	
                              for mentionMembers in range(Dmem+1):
                                  no = 0
                                  ret_ = "\n╔════════════"
                                  dataMid = []
                                  for dataMention in group.members[mentionMembers*20 : (mentionMembers+1)*20]:
                                      dataMid.append(dataMention.mid)
                                      no += 1
                                      ret_ += "\n╠. @!".format(str(no))
                                  ret_ += "\n╚══════════════".format(str(len(dataMid)))
                                  sendMeention(R, ret_, dataMid)
                          except Exception as Ewe:
                              print(Ewe)
                        if PrankBotsData == Abouts["64"]:
                          if D in Owner or D in meM:
                            try:
                                PrankBots["Shared"] = True
                                PrankBots["Add"] = True
                                PrankBots["Join"] = True
                                PrankBots["Wc"] = True
                                PrankBots["Read"] = True
                                PrankBots["Unsend"] = True
                                me.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                me.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                me.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                me.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                me.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                bot1.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                bot1.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                bot1.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                bot1.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                bot1.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                Java_script.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                Java_script.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                Java_script.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                Java_script.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                Java_script.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                me.sendMessage(R,"SETTING ALL IN ONLINE")
                            except:me.sendMessage(R,"SETTING ALL IN ONLINE")
                        if PrankBotsData == Abouts["65"]:
                          if D in Owner or D in meM:
                            try:
                                PrankBots["Shared"] = False
                                PrankBots["Add"] = False
                                PrankBots["Join"] = False
                                PrankBots["Wc"] = False
                                PrankBots["Read"] = False
                                PrankBots["Unsend"] = False
                                me.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                me.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                me.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                me.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                me.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                bot1.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                bot1.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                bot1.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                bot1.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                bot1.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                Java_script.findAndAddContactsByMid("ub0842532a31b9d99856cf2590b17d33f")
                                Java_script.findAndAddContactsByMid("udfaf52176415b46cb445ae2757ec85f3")
                                Java_script.findAndAddContactsByMid("u17a086ccff618e754588a1108335867f")
                                Java_script.findAndAddContactsByMid("uc8dc5352066b6a344bde3c07b0fe04ea")
                                Java_script.findAndAddContactsByMid("ub9c30fd47257ec4337ee777657b4df66")
                                me.sendMessage(R,"SETTING ALL IN OFFLINE")
                            except:me.sendMessage(R,"SETTING ALL IN OFFLINE")
                        if PrankBotsData == Abouts["66"]:
                          if D in Owner or D in meM:
                            RunTheRun(R, D, "_______RESULT______\n")
                        if PrankBotsData == Abouts["67"]:
                          if D in Owner or D in meM:
                              PASUKAN = [BotRanger,Java_scriptRanger]
                              try:
                                 me.inviteIntoGroup(R,PASUKAN)
                                 bot1.acceptGroupInvitation(R)
                              except:
                                 P = me.getGroup(R)
                                 P.preventedJoinByTicket = False
                                 invsend = 0 #INI PERLU JIKA PAKAI COMMAND
                                 Targ = me.reissueGroupTicket(R)
                                 bot1.acceptGroupInvitationByTicket(R,Targ)
                                 bot1.findAndAddContactsByMid(Java_scriptRanger)
                                 bot1.inviteIntoGroup(R,[Java_scriptRanger])
                        if PrankBotsData == Abouts["68"]:
                          if D in Owner or D in meM:
                            try:
                              bot1.cancelGroupInvitation(R,[Java_scriptRanger])
                              bot1.leaveGroup(R)
                            except:
                              bot1.leaveGroup(R)
                        if PrankBotsData == Abouts["69"]:
                          if D in Owner or D in meM:
                              if R in PrankBots["PROTECT"]:
                                  me.sendMessage(R,"Sudah on")
                                  bot1.sendMessage(R,"Sudah on")
                              else:
                                  PrankBots["PROTECT"][R] = True
                                  me.sendMessage(R,"Already on..")
                                  bot1.sendMessage(R,"Already on..")
                        if PrankBotsData == Abouts["70"]:
                          if D in Owner or D in meM:
                              if R in PrankBots["PROTECT"]:
                                  me.sendMessage(R,"Already off")
                                  bot1.sendMessage(R,"Already off")
                                  del PrankBots["PROTECT"][R]
                              else:
                                  me.sendMessage(R,"Belum di protect")
                                  bot1.sendMessage(R,"ok siap")
                        if PrankBotsData == Abouts["76"]:
                            if D in Owner or D in meM:
                                thanks = ""
                                a = 0
                                Ban = PrankBots["blacklist"]
                                for Crott in Ban:
                                    a = a + 1
                                    end = '\n'
                                    thanks += "\n┣|" + str(a) + ". " +me.getContact(Crott).displayName
                                me.sendMessage(R, "━━━━━━━╦℘̰̰̈́ґ̰̰̈́∂̰̰̈́η̰̰̈́к̰̰̈́в̰̰̈́❍̰̰̈́т̰̰̈́ѕ̰̰̈́╦━━━━━━━\n━━━━━daftar blacklist━━━━━━"+thanks+"\n┣━━━━━━★p̲̅r̲̅a̲̅n̲̅k̲̅b̲̅o̲̅t̲̅s̲̅★━━━━━━━\nTOTAL ADA %s BLACKLIST" %(str(len(PrankBots["blacklist"]))))
                        if PrankBotsData == Abouts["71"]:
                          if D in Owner or D in meM:
                              PrankBots["blacklist"] = {}
                              me.sendMessage(R, "delete blacklist success.!!")
                        if PrankBotsData == Abouts["72"]:
                          if D in Owner or D in meM:
                              me.sendMessage(R,meProfile.displayName+"\nSELF READY")
                              bot1.sendMessage(R,BotRangerProfile.displayName+"\nKICKER READY")
                        if PrankBotsData.startswith(Abouts["73"]):
                          if D in Owner or D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = me.getContact(key1)
                            me.kickoutFromGroup(key1)
                        if PrankBotsData.startswith(Abouts["74"]):
                          if D in Owner or D in meM:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = bot1.getContact(key1)
                            bot1.kickoutFromGroup(key1)
                        if PrankBotsData.startswith(Abouts["75"]):
                          if D in Owner or D in meM:
                              if msg.toType == 2:
                                  _name = msg.text.replace(Abouts["75"],"")
                                  P = me.getGroup(R)
                                  P.preventedJoinByTicket = False
                                  me.updateGroup(P)
                                  invsend = 0
                                  Targ = me.reissueGroupTicket(R)
                                  bot1.acceptGroupInvitationByTicket(R,Targ)
                                  targets = []
                                  for g in P.members:
                                      if _name in g.displayName:
                                          targets.append(g.mid)
                                  if targets == []:
                                      me.sendMessage(R, "limit")
                                      bot1.sendMessage(R, "limit juga")
                                  else:
                                      for allmember in targets:
                                          if not allmember in Acil:
                                              try:
                                                  bott=[me,bot1]
                                                  kikil=random.choice(bott)
                                                  kikil.kickoutFromGroup(R,[allmember])
                                              except:
                                                  bot1.sendMessage(R,"sudah limit")
                                                  me.sendMessage(R,"sudah limit")
                                      else:
                                          me.sendMessage(R,"Member kosong.!!")
        if op.type == 26:
          if PrankBots["bot"] == True:
            msg = op.message
            text = msg.text
            Id = msg.id
            R = msg.to or to
            D = msg._from
            if msg.toType == 0 or msg.toType == 2:
                if msg.toType == 0:
                    to = D
                elif msg.toType == 2:
                    to = R
                if PrankBots["Read"] == True:
                    me.sendChatChecked(R, Id)
                if msg.contentType == 0:
                    if text is None:
                        return
                if msg.contentType == 16:
                        if PrankBots["Shared"] == True:
                            try:
                                ret_ = "╔══[ Details Post ]"
                                if msg.contentMetadata["serviceType"] == "GB":
                                    contact = me.getContact(D)
                                    auth = "\n╠ Penulis : {}".format(str(contact.displayName))
                                else:
                                    auth = "\n╠ Penulis : {}".format(str(msg.contentMetadata["serviceName"]))
                                purl = "\n╠ URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://me.me/R/"))
                                ret_ += auth
                                ret_ += purl
                                if "mediaOid" in msg.contentMetadata:
                                    object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                    if msg.contentMetadata["mediaType"] == "V":
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                            murl = "\n╠ Media URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                        ret_ += murl
                                    else:
                                        if msg.contentMetadata["serviceType"] == "GB":
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        else:
                                            ourl = "\n╠ Objek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                    ret_ += ourl
                                if "stickerId" in msg.contentMetadata:
                                    stck = "\n╠ Stiker : https://me.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                    ret_ += stck
                                if "text" in msg.contentMetadata:
                                    text = "\n╠ Tulisan : {}".format(str(msg.contentMetadata["text"]))
                                    ret_ += text
                                ret_ += "\n╚══[ Finish ]"
                                me.sendMessage(R, str(ret_))
                            except Exception as error:
                                logError(error)
                                traceback.print_tb(error.__traceback__)
                if msg.contentType == 0 and D not in meM and msg.toType == 2:
                    if 'MENTION' in msg.contentMetadata.keys()!= None:
                        names = re.findall(r'@(\w+)', text)
                        mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                        mentionees = mention['MENTIONEES']
                        lists = []
                        for mention in mentionees:
                            if meM in mention["M"]:
                                if PrankBots["Respon"] == True:
                                    sendMention(R, D, "\n",respontags["Auto_text"])
                                    me.sendContact(R, D)
                                break
        if op.type == 19 or op.type == 32:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if meM in Kawan:
                print ("SELFBOT DI KICK DARI GRUP")
                if Penjahat in Acil:
                    bot1.findAndAddContactsByMid(Kawan)
                    bot1.inviteIntoGroup(Chanell,[Kawan])
                    me.acceptGroupInvitation(Chanell)
                else:
                    PrankBots["blacklist"][Penjahat] = True
                    try:
                        bot1.findAndAddContactsByMid(Kawan)
                        bot1.inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 1 MENGUNDANG KEMBALI KE GRUP")
                        me.acceptGroupInvitation(Chanell)
                        bot1.kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        print ("SELFBOT DI KICK\nANTI JS BERTINDAK")
                        Java_script.kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        bot1.findAndAddContactsByMid(Java_scriptRanger)
                        bot1.inviteIntoGroup(Chanell,[Java_scriptRanger])
            if BotRanger in Kawan:
                print ("BOT 1 ADA YANG KICK")
                if Penjahat in Acil:
                    me.findAndAddContactsByMid(Kawan)
                    me.inviteIntoGroup(Chanell,[Kawan])
                    bot1.acceptGroupInvitation(Chanell)
                else:
                    PrankBots["blacklist"][Penjahat] = True
                    try:
                        me.findAndAddContactsByMid(Kawan)
                        me.inviteIntoGroup(Chanell,[Kawan])
                        print ("BOT 1 DI INVITE KEMBALI")
                        bot1.acceptGroupInvitation(Chanell)
                        me.kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        print ("BOT 1 DI KICK ANTI JS BERTINDAK")
                        Java_script.kickoutFromGroup(Chanell,[Penjahat])
                        P = Java_script.getGroup(Chanell)
                        P.preventedJoinByTicket = False
                        Java_script.updateGroup(P)
                        LinkQrGroup = Java_script.reissueGroupTicket(Chanell)
                        me.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        bot1.acceptGroupInvitationByTicket(Chanell,LinkQrGroup)
                        Java_script.leaveGroup(Chanell)
                        me.findAndAddContactsByMid(Java_scriptRanger)
                        me.inviteIntoGroup(Chanell,[Java_scriptRanger])
            if Java_scriptRanger in Kawan:
                print ("ANTI JS DI KICK")
                if Penjahat in Acil:
                    bot1.findAndAddContactsByMid(Kawan)
                    bot1.inviteIntoGroup(Chanell,[Kawan])
                else:
                    PrankBots["blacklist"][Penjahat] = True
                    try:
                        bot1.findAndAddContactsByMid(Kawan)
                        bot1.inviteIntoGroup(Chanell,[Kawan])
                        print ("ANTI JS DI INVITE")
                        me.kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        me.findAndAddContactsByMid(Kawan)
                        me.inviteIntoGroup(Chanell,[Kawan])
                        print ("ANTI JS DI INVITE")
                        bot1.kickoutFromGroup(Chanell,[Penjahat])
        if op.type == 19 or op.type == 32:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if Chanell in PrankBots["PROTECT"]:
                if Penjahat in Acil:
                    pass
                else:
                    PrankBots["blacklist"][Penjahat] = True
                    print ("PROTECT BERTINDAK DI GRUP "+me.getGroup(Chanell).name)
                    try:
                        bot1.kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        me.kickoutFromGroup(Chanell,[Prnjahat])
        if op.type == 17:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if Penjahat in PrankBots["blacklist"]:
                print ("BLACKLIST MASUK DI GRUP "+me.getGroup(Chanell).name)
                try:
                    bot1.kickoutFromGroup(Chanell,[Penjahat])
                except:
                    me.kickoutFromGroup(Chanell,[Prnjahat])
            else:pass
        if op.type == 13:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if Kawan in PrankBots["blacklist"]:
                print ("BLACKLIST DI INVITE DI GRUP "+me.getGroup(Chanell).name)
                try:
                    bot1.cancelGroupInvitation(Chanell,[Kawan])
                    me.kickoutFromGroup(Chanell,[Penjahat])
                except:
                    me.cancelGroupInvitation(Chanell,[Kawan])
                    bot1.kickoutFromGroup(Chanell,[Penjahat])
            if Chanell in PrankBots["PROTECT"]:
                if Penjahat in Acil:
                    pass
                else:
                    PrankBots["blacklist"][Penjahat] = True
                    print ("PROTECT BERTINDAK DI GRUP "+me.getGroup(Chanell).name)
                    try:
                        bot1.cancelGroupInvitation(Chanell,[Kawan])
                        me.kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        me.cancelGroupInvitation(Chanell,[Kawan])
                        bot1.kickoutFromGroup(Chanell,[Penjahat])
        if op.type == 11:
            Chanell = op.param1
            Penjahat = op.param2
            Kawan = op.param3
            if Chanell in PrankBots["PROTECT"]:
                if Penjahat in Acil:
                    pass
                else:
                    PrankBots["blacklist"][Penjahat] = True
                    print ("PROTECT BERTINDAK DI GRUP "+me.getGroup(Chanell).name)
                    try:
                        P = me.getGroup(Chanell)
                        P.preventedJoinByTicket = True
                        me.updateGroup(P)
                        bot1.kickoutFromGroup(Chanell,[Penjahat])
                    except:
                        Java_script.acceptGroupInvitation(Chanell)
                        P = bot1.getGroup(Chanell)
                        P.preventedJoinByTicket = True
                        bot1.updateGroup(P)
                        Java_script.kickoutFromGroup(Chanell,[Penjahat])
                        Java_script.leaveGroup(Chanell)
                        me.findAndAddContactsByMid(Java_scriptRanger)
                        me.inviteIntoGroup(Chanell,[Java_scriptRanger])
        if op.type == 13:
            print ("NOTIFIED MEMBER OR SELF JOIN GROUP")
            Gr = op.param1
            if PrankBots["Join"] == True:
                me.acceptGroupInvitation(Gr)
            else:
                pass
        if op.type == 5:
            print ("NOTIFIED ADD CONTACT SELF")
            if PrankBots["Add"] == True:
                me.findAndAddContactsByMid(op.param1)
            sendMention(op.param1, op.param1, "Thanks For add Me ","")
        if op.type == 15:
            Gr = op.param1
            Cj = op.param2
            print ("NOTIFIED CONTACT MEMBER LEAVE TO GROUP")
            if PrankBots["Wc"] == True:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Good bye : {}".format(dia.displayName)
                ms += "In group : {}".format(Gc.name)
                mt = "Why your leave in group {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendMessage(dia,mt)
                me.sendContact(Gr,dia)
        if op.type == 17:
            Gr = op.param1
            Cj = op.param2
            print ("NOTIFIED CONTACT MEMBER JOIN TO GROUP")
            if PrankBots["Wc"] == True:
                Gc = me.getGroup(Gr)
                dia = me.getContact(Cj)
                ms = "Welcome : {}".format(dia.displayName)+" In group : {}".format(Gc.name)
                me.sendMessage(Gr,str(ms))
                me.sendContact(Gr,dia)
        if op.type == 65:
            print ("UNSEND MESSAGE UNSENDER FROM MY SELF")
            if PrankBots["Unsend"] == True:
                Geting = op.param1
                Text_in_Destroy = op.param2
                if Text_in_Destroy in msg_dict:
                    Timer = time.time()
                    Target_Text = me.getContact(msg_dict[Text_in_Destroy]["from"])
                    if "text" in msg_dict[Text_in_Destroy]:
                        StartTimer = Timer - msg_dict[Text_in_Destroy]["waktu"]
                        StartTimer = format_timespan(StartTimer)
                        rat_ = "Timer unsend: {} WIB".format(StartTimer)
                        rat_ += "Text Unsend\n{}".format(msg_dict[Text_in_Destroy]["text"])
                        sendMention(Geting, Target_Text.mid, "Sorry\nMy Resend your Message\n\n", str(rat_))
                        del msg_dict[Text_in_Destroy]
                else:
                    me.sendMessage(Geting,"Detected Unsend")
        if op.type == 55:
            Gr = op.param1
            try:
                if Sid['Tar'][Gr]==True:
                        if Gr in Sid['Red']:
                            Name = me.getContact(op.param2).displayName
                            Np = me.getContact(op.param2).pictureStatus
                            if Name in Sid['Reason'][Gr]:
                                pass
                            else:
                                Sid['Reason'][Gr] += "\n||[ " + Name + " ]||"
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[0] + " " + "\nNah jangan ngintip mulu . . .\nGabung Chat yux ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                    else:
                                        me.sendMessage(Gr, "Hallo.. " + " " + nick[1] + " " + "\nJangan ngintip.. . . .\nMasuk  ayox... ")
                                        me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                                else:
                                    me.sendMessage(Gr, "hallo.. " + " " + Name + " " + "\nJangan ngintip aja\nMasuk gabung chat ya... ")
                                    me.sendImageWithURL(Gr, "http://dl.profile.line-cdn.net/" + Np)
                        else:
                            pass
                else:
                    pass
            except:
                pass
        else:
            pass
    except Exception as error:
        ErrorX(error)
        if op.type == 59:
            print (op)
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
    except Exception as e:
        me.log("DATA: " + str(e))
