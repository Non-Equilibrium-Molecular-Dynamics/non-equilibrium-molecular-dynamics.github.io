import csv
import os 

def svgtopng(filename):

    filenamepng = filename.replace('.svg','.png')
    cmd = "/snap/bin/inkscape -z -f ./" + filename + " -w 744 -j -e ./" +  filenamepng
    print("Wrinting svg to png " + filename, cmd)
    os.system(cmd)

    return filenamepng

def svgtopdf(filename):

    filenamepdf = filename.replace('.svg','.pdf')
    cmd = "/snap/bin/inkscape -f ./" + filename + " -A ./" +  filenamepdf
    print("Wrinting svg to pdf " + filename, cmd)
    os.system(cmd)

    return filenamepdf

def pngtojpg(filename):

    print("Wrinting png to jpg " + filename)
    filenamejpg = filename.replace('.png','.jpg')
    cmd = "convert " + filename + " " + filenamejpg
    os.system(cmd)

    return filenamejpg

rtrnfrmt = 'pdf'
clean = False

#open basefile
basefile = "name_badges_larger.svg"
f = open(basefile,'r')
filecontents = f.read()
f.close()
newfilecontent = filecontents
i = 1; j = 0
filename = './Badges' + str(j) + '.svg'
with open('Attendees.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        name = ', '.join(row)
        newfilecontent = newfilecontent.replace("Name"+str(i), name)
        i+=1

        #print(i,j,name, filename)

        #Save it as a new svg based on peoples names
        if i > 8:
            print('Writing ' + name + ' to file ', filename)
            g = open(filename, 'w+')
            g.write(newfilecontent)
            g.close()
            i = 1
            #Convert it to jpg
            if rtrnfrmt is 'pdf':
                filename = svgtopdf(filename)
                if clean:
                    os.remove(filename.replace('pdf','svg'))
            elif rtrnfrmt is 'png':
                filename = svgtopng(filename)
                if clean:
                    os.remove(filename.replace('png','svg'))
            elif rtrnfrmt is 'jpg':
                filename = svgtopng(filename)
                filename = pngtojpg(filename)
                if clean:
                    os.remove(filename.replace('jpg','png'))
                    os.remove(filename.replace('jpg','svg'))
            j += 1
            filename = './Badges' + str(j) + '.svg'
            newfilecontent = filecontents


    print('Writing ' + name + ' to file ', filename)
    g = open(filename, 'w+')
    g.write(newfilecontent)
    g.close()
    i = 1
    #Convert it to jpg
    if rtrnfrmt is 'pdf':
        filename = svgtopdf(filename)
        if clean:
            os.remove(filename.replace('pdf','svg'))
    elif rtrnfrmt is 'png':
        filename = svgtopng(filename)
        if clean:
            os.remove(filename.replace('png','svg'))
    elif rtrnfrmt is 'jpg':
        filename = svgtopng(filename)
        filename = pngtojpg(filename)
        if clean:
            os.remove(filename.replace('jpg','png'))
            os.remove(filename.replace('jpg','svg'))

