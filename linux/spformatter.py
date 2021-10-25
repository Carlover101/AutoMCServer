import time

print("The Server.properties file changes how the server runs and generates worlds.")
time.sleep(2)
YD = input("Would you like to customize this file or leave it as the default values? (Custom/Default)")

if YD.lower() == "default":
  print("Setting to default...")
  time.sleep(1)
  print("Done")
  exit()

elif YD.lower() == "custom":
  sprot = input("How large would you like the player spawn protection to be? (16 is default) ")
  mtick = input("What would you like the max tick timeout to be? (0 = never; 60000 is default) ")
  qport = input("Which port would you like to run the query on? (25565 is default) ")
  genst = input("What generators setting would you like to add? (leave blank if you want to skip) ")
  syncw = input("What would you like to set sync-chunk-writes to? (true/false; default is true) ").lower()
  fgame = input("Would you like to force the gamemode? (true/false; default is false) ").lower()
  alnet = input("Would you like to enable the nether? (true/false; default is true) ").lower()
  enwht = input("Would you like to enforce the whitelist? (true/false; default is false) ").lower()
  gamem = input("What would like to set the gamemode to? (survival/creative/adventure; defualt is survival) ").lower()
  bctop = input("Would you like to broadcast the console commands to operators? (true/false; default is true) ").lower()
  enque = input("Would you like to enable the query? (true/false; default is false) ").lower()
  pidlt = input("What would you like to set the player idle timeout to be? (0 = never; default is 0) ")
  diffc = input("What would you like to set the difficulty to? (easy/normal/hard; default is easy) ").lower()
  spmon = input("Would you like to enable monster spawning? (true/false; default is true) ").lower()
  brtop = input("Would you like to broadcast rcon to ops? (true/false; default is true) ").lower()
  operm = input("What would like to set the operator permission level to? (1/2/3/4; default is 4) ")
  enpvp = input("Would you like to enable pvp? (true/false; default is true) ").lower()
  enbrp = input("What would you like to set the entity broadcast range percentage to? (0-100; default is 100) ")
  ensnp = input("Would you like to enable snoopers? (true/false) ").lower()
  lvlty = input("What would like to set the level type to? (flat/default; default is default) ").lower()
  hrdcr = input("Would you like to set the world to hardcore? (true/false; default is false) ").lower()
  estat = input("Would you like to enable status? (true/false; default is true) ").lower()
  encmb = input("Would you like to enable command blocks? (true/false; default is false) ").lower()
  mxplr = input("What would you like to set the max player count to? (0-9999999; default is 20) ")
  netct = input("What would you like to set the network compression threshold to? (0-1500; default is 256) ")
  ressh = input("What would you like to set the resource pack sha1 to? (paste here; default is blank) ")
  mxwsz = input("What would you like to set the mac world size to? (0-29999984; default is 29999984) ")
  fnprl = input("What would you like to set the function permission level to? (1-2; default is 2) ")
  rcnpt = input("What would you like to set the rcon port to? (default is 25575) ")
  srvpt = input("What would you like to set the server port to? (default is 25565) ")
  debug = input("Would you like to turn on debug? (true/false; default is true) ").lower()
  srvip = input("What would like to set the server ip address to? (if you do not know, leave this blank) ")
  spnpc = input("Would you like to enable the spawning of npcs? (true/false; default is true) ").lower()
  alflt = input("Would you like to enable flight? (true/false; default is false) ").lower()
  lvlnm = input("What would you like to name the world file? (default is world) ")
  vdist = input("What would you like to set the player view distance to? (2-64; default is 10) ")
  respk = input("What would you like to set the resource pack to? (paste a link here; default is blank) ")
  spnan = input("Would you like to turn animal spawning on? (true/false; default is true) ").lower()
  wtlst = input("Would you like to enable whitelist? (true/false; default is false) ").lower()
  rconp = input("What would you like to set the rcon password to? (paste or type here; default is blank) ")
  gnstc = input("Would you like to turn structure generation on? (true/false; default is true) ").lower()
  mxbhi = input("What would you like to set the maximum build hight to? (0-256; default is 256) ")
  onmde = input("Would you like to set online mode on? (true/false; default is true) ").lower()
  lvlsd = input("What would you like to set the world seed to? (paste here; default is blank) ")
  usntp = input("Would you like to use native transport? (true/false; default is true) ").lower()
  prepc = input("Would you like to prevent proxy connections? (true/false; default is false) ").lower()
  enjmx = input("Would you like to enable jmx monitoring? (true/false; default is false) ").lower()
  enrcn = input("Would you like to enable rcon? (true/false; default is false) ").lower()
  smotd = input("What would you like to set the message of the day to? (paste or type it here; default is 'A Minecraft Server') ")

time.sleep(2)
sp = open("server.properties","w+")

sp.write("#Minecraft server properties\n")
if sprot == "" or sprot.isnumeric() == False:
    sp.write("spawn-protection=16\n")
    print("spawn-protection set equal to 16")
    time.sleep(.5)
else:
    sp.write(f"spawn-protection={sprot}\n")
    print(f"spawn-protection set equal to {sprot}")
    time.sleep(.5)

if mtick == "" or mtick.isnumeric() == False:
    sp.write("max-tick-time=60000\n")
    print("max-time-time set equal to 60000")
    time.sleep(.5)
else:
    sp.write(f"max-tick-time={mtick}\n")
    print(f"max-tick-time set equal to {mtick}")
    time.sleep(.5)

if qport == "" or qport.isnumeric() == False:
    sp.write("query.port=25565\n")
    print("query.port set equal 25565")
    time.sleep(.5)
else:
    sp.write(f"query.port={qport}\n")
    print(f"query.port set equal to {qport}")
    time.sleep(.5)

if genst == "":
    sp.write("generator-settings=\n")
    print("generator-settings set equal to ")
    time.sleep(.5)
else:
    sp.write(f"generator-settings={genst}\n")
    print(f"generator-settings set equal to {genst}")
    time.sleep(.5)

if syncw != "true" or "false":
    sp.write("sync-chunk-writes=true\n")
    print("sync-chunk-wirtes set equal to true")
    time.sleep(.5)
else:
    sp.write(f"sync-chunk-writes={syncw}\n")
    print(f"sync-chunk-writes set equal to {syncw}")
    time.sleep(.5)

if fgame != "true" or "false":
    sp.write("force-gamemode=false\n")
    print("force-gamemode set equal to false")
    time.sleep(.5)
else:
    sp.write(f"force-gamemode={fgame}\n")
    print(f"force-gamemode set equal to {fgame}")
    time.sleep(.5)

if alnet != "true" or "false":
    sp.write("allow-nether=true\n")
    print("allow-nether set to true")
    time.sleep(.5)
else:
    sp.write(f"allow-nether={alnet}\n")
    print(f"allow-nether set to {alnet}")
    time.sleep(.5)

if enwht != "true" or "false":
    sp.write("enforce-whitelist=false\n")
    print("enforce-whitelist set to false")
    time.sleep(.5)
else:
    sp.write(f"enforce-whitelist={enwht}\n")
    print(f"enforce-whitelist set to {enwht}")
    time.sleep(.5)

if gamem != "survival" or "creative" or "adventure":
    sp.write("gamemode=survival\n")
    print("gamemode set to easy")
    time.sleep(.5)
else:
    sp.write(f"gamemode={gamem}\n")
    print(f"gamemode set to {gamem}")
    time.sleep(.5)

if bctop != "true" or "false":
    sp.write("broadcast-console-to-ops=true\n")
    print("broadcast-console-to-ops set equal to true")
    time.sleep(.5)
else:
    sp.write(f"broadcast-console-to-ops={bctop}\n")
    print(f"broadcast-console-to-ops set equal to {bctop}")
    time.sleep(.5)

if enque != "true" or "false":
    sp.write("enable-queue=false\n")
    print("enable-queue set to false")
    time.sleep(.5)
else:
    sp.write(f"enable-queue={enque}\n")
    print(f"enable-queue set to {enque}")
    time.sleep(.5)

if pidlt == "" or pidlt.isnumeric() == "false":
    zero = "0"
    sp.write(f"player-idle-timeout={zero}\n")
    print("player-idle-timeout set to 0")
    time.sleep(.5)
else:
    sp.write(f"player-idle-timeout={pidlt}\n")
    print(f"player-idle-timeout set to {pidlt}")
    time.sleep(.5)

if diffc != "easy" or "normal" or "hard":
    sp.write("difficulty=easy\n")
    print("difficulty set to easy")
    time.sleep(.5)
else:
    sp.write(f"difficulty={diffc}\n")
    print(f"difficulty set to {diffc}")
    time.sleep(.5)

if spmon != "true" or "false":
    sp.write("spawn-monsters=true\n")
    print("spawn-monsters set to true")
    time.sleep(.5)
else:
    sp.write(f"spawn-monsters={spmon}\n")
    print(f"spawn-monsters set to {spmon}")
    time.sleep(.5)

if brtop != "true" or "false":
    sp.write("broadcast-rcon-to-ops=true\n")
    print("broadcast-rcon-to-ops set to true")
    time.sleep(.5)
else:
    sp.write(f"broadcast-rcon-to-ops={brtop}\n")
    print(f"broadcast-rcon-to-ops set to {brtop}")
    time.sleep(.5)

if operm == "" or operm.isnumeric() == "false" or operm >= "5":
    sp.write(f"op-permission=4 \n")
    print(f"op-permission set to 4")
    time.sleep(.5)
else:
    sp.write(f"op-permission={operm}\n")
    print(f"op-permission set to {operm}")
    time.sleep(.5)

if enpvp != "true" or "false":
    sp.write("pvp=true\n")
    print("pvp set to true")
    time.sleep(.5)
else:
    sp.write(f"pvp={enpvp}")
    print(f"pvp set to {enpvp}")
    time.sleep(.5)

if enbrp == "" or enbrp.isnumeric() == "false" or enbrp > 101:
    sp.write("entity-broadcast-range-percentage=100\n")
    print("entity-broadcast-range-percentage set to 100")
    time.sleep(.5)
else:
    sp.write(f"entity-broadcast-range-percentage={enbrp}\n")
    print(f"entity-broadcast-range-percentage set to {enbrp}")
    time.sleep(.5)

if ensnp != "true" or "false":
    sp.write("snooper-enabled=true\n")
    print("snooper-enables set to true")
    time.sleep(.5)
else:
    sp.write(f"snooper-enabled={ensnp}\n")
    print(f"snooper-enabled set to {ensnp}")
    time.sleep(.5)

if lvlty != "default" or "flat":
    sp.write("level-type=default\n")
    print("level-type set to default")
    time.sleep(.5)
else:
    sp.write(f"level-type={lvlty}\n")
    print(f"level-type set to {lvlty}")
    time.sleep(.5)

if hrdcr != "true" or "false":
    sp.write("hardcore=false\n")
    print("hardcore set to false")
    time.sleep(.5)
else:
    sp.write(f"hardcore={hrdcr}\n")
    print(f"hardcore set to {hrdcr}")
    time.sleep(.5)

if estat != "true" or "false":
    sp.write("enable-status=true\n")
    print("enable-status set to true")
    time.sleep(.5)
else:
    sp.write(f"enable-status={estat}\n")
    print(f"enable-status set to {estat}")
    time.sleep(.5)

if encmb != "true" or "false":
    sp.write("enable-command-block=false\n")
    print("enable-command-block set to false")
    time.sleep(.5)
else:
    sp.write(f"enable-command-block={encmb}\n")
    print(f"enable-command-block set to {encmb}")
    time.sleep(.5)

if mxplr == "" or mxplr.isnumeric() == "false" or mxplr > "9999999":
    sp.write("max-players=20\n")
    print("max-players set to 20")
    time.sleep(.5)
else:
    sp.write(f"max-players={mxplr}\n")
    print(f"max-players set to {mxplr}")
    time.sleep(.5)

if netct == "" or netct.isnumeric() == "false" or netct > 1500:
    sp.write("network-compression-threshold=256\n")
    print("network-compression-threshold set to 256")
    time.sleep(.5)
else:
    sp.write(f"network-compression-threshold={netct}\n")
    print(f"network-compression-threshold set to {netct}")

if ressh == "":
    sp.write("resource-pack-sha1=\n")
    print("resource-pack-sha1 set to ")
    time.sleep(.5)

else:
    sp.write(f"resource-pack-sha1={ressh}\n")
    print(f"resource-pack-sha1 set to {ressh}")
    time.sleep(.5)

if mxwsz == "" or mxwsz.isnumeric() == "false" or mxwsz > "29999984":
    sp.write("max-world-size=29999984\n")
    print("max-world-size set to 29999984")
    time.sleep(.5)
else:
    sp.write(f"max-world-size={mxwsz}\n")
    print(f"max-world-size set to {mxwsz}")
    time.sleep(.5)

if fnprl != "1" or "2":
    sp.write("function-permission-level=2\n")
    print("function-permission-level set to 2")
    time.sleep(.5)
else:
    sp.write(f"function-permission-level={fnprl}\n")
    print(f"function-permission-level set to {fnprl}")
    time.sleep(.5)

if rcnpt == "" or rcnpt.isnumeric() == "false":
    sp.write("rcon.port=25575\n")
    print("rcon.port set to 25575")
    time.sleep(.5)
else:
    sp.write(f"rcon.port={rcnpt}\n")
    print(f"rcon.port set to {rcnpt}")
    time.sleep(.5)

if srvpt == "" or srvpt.isnumeric() == "false":
    sp.write("server-port=25565\n")
    print("server-port set to 25565")
    time.sleep(.5)
else:
    sp.write(f"server-port={srvpt}\n")
    print(f"server-port set to {srvpt}")
    time.sleep(.5)

if debug != "true" or "false":
    sp.write("debug=false\n")
    print("debug set to false")
    time.sleep(.5)
else:
    sp.write(f"debug={debug}\n")
    print(f"debug set to {debug}")
    time.sleep(.5)

if srvip == "":
    sp.write("server-ip=\n")
    print("server-ip set to ")
    time.sleep(.5)
else:
    sp.write(f"server-ip={srvip}\n")
    print(f"server-ip set to {srvip}")
    time.sleep(.5)

if spnpc != "true" or "false":
    sp.write("spawn-npcs=true\n")
    print("spawn-npcs set to true")
    time.sleep(.5)
else:
    sp.write(f"spawn-npcs={spnpc}\n")
    print(f"spawn-npcs set to {spnpc}")
    time.sleep(.5)

if alflt != "true" or "false":
    sp.write("allow-flight=false\n")
    print("allow-flight set to false")
    time.sleep(.5)
else:
    sp.write(f"allow-flight={alflt}\n")
    print(f"allow-flight set to {alflt}")
    time.sleep(.5)

if lvlnm == "":
    sp.write("level-name=world\n")
    print("level-name set to world")
    time.sleep(.5)
else:
    sp.write(f"level-name={lvlnm}\n")
    print(f"level-name set to {lvlnm}")
    time.sleep(.5)

if vdist == "" or vdist.isnumeric() == "false" or vdist > 32:
    sp.write("view-distance=10\n")
    print("view-distance set to 10")
    time.sleep(.5)
else:
    sp.write(f"view-distance={vdist}\n")
    print(f"view-distance set to {vdist}")
    time.sleep(.5)

if respk == "":
    sp.write("resource-pack=\n")
    print("resource-pack set to ")
    time.sleep(.5)
else:
    sp.write(f"resource-pack={respk}\n")
    print(f"resource-pack set to {respk}")
    time.sleep(.5)

if spnan != "true" or "false":
    sp.write("spawn-animals=true\n")
    print("spawn-animals set to true")
    time.sleep(.5)
else:
    sp.write(f"spawn-animals={spnan}\n")
    print(f"spawn-animals set to {spnan}")
    time.sleep(.5)

if wtlst != "true" or "false":
    sp.write("white-list=false\n")
    print("white-list set to false")
    time.sleep(.5)
else:
    sp.write(f"white-list={wtlst}\n")
    print(f"white-list set to {wtlst}")
    time.sleep(.5)

if rconp == "":
    sp.write("rcon.password=\n")
    print("rcon.password set to ")
    time.sleep(.5)
else:
    sp.write(f"rcon.password={rconp}\n")
    print(f"rcon.password set to {rconp}")
    time.sleep(.5)

if gnstc != "true" or "false":
    sp.write("generate-structures=true\n")
    print("generate-structures set to true")
    time.sleep(.5)
else:
    sp.write(f"generate-structures={gnstc}\n")
    print(f"generate-structures set to {gnstc}")
    time.sleep(.5)

if mxbhi == "" or mxbhi.isnumeric() == "false" or mxbhi > 256:
    sp.write("max-build-height=256\n")
    print("max-build-height set to 256")
    time.sleep(.5)
else:
    sp.write(f"max-build-height={mxbhi}\n")
    print(f"max-build-height set to {mxbhi}")
    time.sleep(.5)

if onmde != "true" or "false":
    sp.write("online-mode=true\n")
    print("online-mode set to true")
    time.sleep(.5)
else:
    sp.write(f"online-mode={onmde}\n")
    print(f"online-mode set to {onmde}")
    time.sleep(.5)

if lvlsd == "":
    sp.write("level-seed=\n")
    print("level-seed set to ")
    time.sleep(.5)
else:
    sp.write(f"level-seed={lvlsd}\n")
    print(f"level-seed set to {lvlsd}")
    time.sleep(.5)

if usntp != "true" or "false":
    sp.write("use-native-transport=true\n")
    print("use-native-transport set to true")
    time.sleep(.5)
else:
    sp.write(f"use-native-transport={usntp}\n")
    print(f"use-native-trasport set to {usntp}")
    time.sleep(.5)

if prepc != "true" or "false":
    sp.write("prevent-proxy-connections=false\n")
    print("prevent-proxy-connections set to false")
    time.sleep(.5)
else:
    sp.write(f"prevent-proxy-connections={prepc}\n")
    print(f"prevent-proxy-connections set to {prepc}")
    time.sleep(.5)

if enjmx != "true" or "false":
    sp.write("enable-jmx-monitoring=false\n")
    print("enable-jmx-monitoring set to false")
    time.sleep(.5)
else:
    sp.write(f"enable-jmx-monitoring={enjmx}\n")
    print(f"enable-jmx-monitoring set to {enjmx}")
    time.sleep(.5)

if enrcn != "true" or "false":
    sp.write("enable-rcon=false\n")
    print("enable-rcon set to false")
    time.sleep(.5)
else:
    sp.write(f"enable-rcon={enrcn}\n")
    print(f"enable-rcon set to {enrcn}")
    time.sleep(.5)

if smotd == "":
    sp.write("motd=A Minecraft Server")
    print("motd set to A Minecraft Server")
    time.sleep(.5)
else:
    sp.write(f"motd={smotd}")
    print(f"motd set to {smotd}")
    time.sleep(.5)
