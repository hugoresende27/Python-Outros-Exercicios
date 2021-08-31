media={
        "Hugo":20,
        "Rita":15.8,
        "José":18.2,
        "Sara":12.9
    }

print (media)
notas = media.values()
print (notas)
outra_media=sum(notas)/4

print (outra_media)
print ("Media %.2f"%(sum(media.values())/len(media)))