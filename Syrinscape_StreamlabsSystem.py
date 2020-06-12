#---------------------------------------
#   Import Libraries
#---------------------------------------
import os, sys # os allows us to call files and uris, sys allows us to modify path within this frame
sys.path.append(os.path.join(os.path.dirname(__file__), "lib")) # allows 

#---------------------------------------
#	Script Information
#---------------------------------------
ScriptName = "Syrin's Call"
Description = "Control Syrinscape Effects from Chat"
Creator = "Chaim Weinberg (IrrationalDM)" 
Website = "https://www.twitch.tv/IrrationalDM"
Version = "0.2.1-dev"

# ---------------------------------------
#	Set Variables
# ---------------------------------------
onlinePlayer = False # use online or local players
usePlayer = 0 # default, fantasy, sci-fi, boardgame NOTE: the boardgame player is not supported by syrinscape TODO: improve clarity

# ---------------------------------------
#	Dictionaries
# ---------------------------------------
import links,tokens # links is the current uri dictionary,

# ---------------------------------------
#	Functions
# ---------------------------------------
def callFantasyMood(name):
    syrinscapeCall = os.path.join("syrinscape-fantasy:moods/{}/play/").format(links.fantasyMoods[name])  # TODO: Deprecate
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
	if onlinePlayer:
		os.startfile("curl https://www.syrinscape.com/online/frontend-api/stop-all")  # TODO: add aplication key logic
	else:
		if usePlayer == 1 or usePlayer == 0: # 0 is default, 1 is fantasy
			os.startfile("syrinscape-fantasy:moods/Y3VzdG9tLW1vb2RzOjpTaWxlbmNl/play/") # need to call twice to shut off long one-shots
			os.startfile("syrinscape-fantasy:moods/Y3VzdG9tLW1vb2RzOjpTaWxlbmNl/play/")
		if usePlayer == 2 or usePlayer == 0: # 0 is default, 2 is sci-fi
			os.startfile("syrinscape-sci-fi:moods/Y3VzdG9tLW1vb2RzLXNjaS1maTo6U2lsZW5jZQ/play/") # need to call twice to shut off long one-shots
			os.startfile("syrinscape-sci-fi:moods/Y3VzdG9tLW1vb2RzLXNjaS1maTo6U2lsZW5jZQ/play/")
	return
def Parse(parseString, userid, username, targetid, targetname, message):
    if "$SILENT" in parseString:
		silence("secret")
		parseString = parseString.replace("$SILENT","")
    if "$SFE" in parseString:
        start = '$SFE('
        end = ')'
        uri = (parseString.split(start))[1].split(end)[0]
        callFantasyElement(uri)
        param = "$SFE({})".format(uri)
        parseString = parseString.replace(param,"")
    if "$SFM" in parseString:
        start = '$SFM('
        end = ')'
        uri = (parseString.split(start))[1].split(end)[0]
        callFantasyMood(uri)
        param = "$SFM({})".format(uri)
        parseString = parseString.replace(param,"")
    if "$SSE" in parseString:
        start = '$SSE('
        end = ')'
        uri = (parseString.split(start))[1].split(end)[0]
        callSciFiElement(uri)
        param = "$SSE({})".format(uri)
        parseString = parseString.replace(param,"")
    if "$SSM" in parseString:
        start = '$SSM('
        end = ')'
        uri = (parseString.split(start))[1].split(end)[0]
        callSciFiMood(uri)
        param = "$SSM({})".format(uri)
        parseString = parseString.replace(param,"")
	if "$secret1" in parseString: # TODO: delete this function
		parseString = parseString.concat(tokens.discord)
		parseString = parseString.replace("$secret1","")
	if "$secret2" in parseString: # TODO: delete this function
		parseString = parseString.concat(tokens.syrinscape)
		parseString = parseString.replace("$secret2","")
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
