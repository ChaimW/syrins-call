#---------------------------------------
#   Import Libraries
#---------------------------------------
import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

#---------------------------------------
#	Script Information
#---------------------------------------
ScriptName = "Syrin's Call"
Description = "Control Syrinscape Effects from Chat"
Creator = "Chaim Weinberg (IrrationalDM)" 
Website = "https://www.twitch.tv/IrrationalDM"
Version = "0.2"
# ---------------------------------------
#	Set Variables
# ---------------------------------------
# ---------------------------------------
#	Dictionaries
# ---------------------------------------
import links
# ---------------------------------------
#	Functions
# ---------------------------------------
def trigger(player,type,id):
	return
def callFantasyMood(name):
    syrinscapeCall = os.path.join("syrinscape-fantasy:moods/{}/play/").format(links.fantasyMoods[name])
    os.startfile(syrinscapeCall)
    return
def callFantasyElement(name):
    syrinscapeCall = os.path.join("syrinscape-fantasy:elements/{}/play/").format(links.fantasyElements[name])
    os.startfile(syrinscapeCall)
    return
def callSciFiMood(name):
    syrinscapeCall = os.path.join("syrinscape-sci-fi:moods/{}/play/").format(links.scifiMoods[name])
    os.startfile(syrinscapeCall)
    return
def callSciFiElement(name):
    syrinscapeCall = os.path.join("syrinscape-sci-fi:elements/{}/play/").format(links.scifiElements[name])
    os.startfile(syrinscapeCall)
    return
def silence(name):
	os.startfile("syrinscape-fantasy:moods/Y3VzdG9tLW1vb2RzOjpTaWxlbmNl/play/")
	os.startfile("syrinscape-fantasy:moods/Y3VzdG9tLW1vb2RzOjpTaWxlbmNl/play/")
	os.startfile("syrinscape-sci-fi:moods/Y3VzdG9tLW1vb2RzLXNjaS1maTo6U2lsZW5jZQ/play/")
	os.startfile("syrinscape-sci-fi:moods/Y3VzdG9tLW1vb2RzLXNjaS1maTo6U2lsZW5jZQ/play/")
	os.startfile("curl https://www.syrinscape.com/online/frontend-api/stop-all/")
	return
def Parse(parseString, userid, username, targetid, targetname, message):
    if "$SILENT" in parseString:
		silence("secret")
		return parseString.replace("$SILENT","")
    if "$SFE" in parseString:
        start = '$SFE('
        end = ')'
        uri = (parseString.split(start))[1].split(end)[0]
        callFantasyElement(uri)
        param = "$SFE({})".format(uri)
        return parseString.replace(param,"")
    if "$SFM" in parseString:
        start = '$SFM('
        end = ')'
        uri = (parseString.split(start))[1].split(end)[0]
        callFantasyMood(uri)
        param = "$SFM({})".format(uri)
        return parseString.replace(param,"")
    if "$SSE" in parseString:
        start = '$SSE('
        end = ')'
        uri = (parseString.split(start))[1].split(end)[0]
        callSciFiElement(uri)
        param = "$SSE({})".format(uri)
        return parseString.replace(param,"")
    if "$SSM" in parseString:
        start = '$SSM('
        end = ')'
        uri = (parseString.split(start))[1].split(end)[0]
        callSciFiMood(uri)
        param = "$SSM({})".format(uri)
        return parseString.replace(param,"")
    return parseString
#---------------------------------------
#	Initialize Data / Load Only
#---------------------------------------
def Init():
    return
def Execute(data):
    return
def Tick():
    return
