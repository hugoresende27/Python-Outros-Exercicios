from time import sleep
import emoji
print ("\033[7m=\033[m"*100)
print ("\033[7mFOGO ARTIFÍCIO\033[m")
print (emoji.emojize(":thumbs_up:"))

for x in range (10,-1,-1):
    print ("\033[37;41mCONTAGEM --> {} \033[m".format(x),emoji.emojize(":face_screaming_in_fear:"))
    sleep(0.2)

print (emoji.emojize(":fireworks:"*130))
