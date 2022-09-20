#write a program that asks the size in MB of a file to download, and the speed of an internet link in Mbps, and print the time to download in minutes
filesize = float(input('Input the file size in MB: '))
speed = float(input('Input the link`s speed in Mbps: '))
seconds = filesize / speed
minutes = int(seconds/60)
seconds = seconds%60
print ('Time to download file through link: %.2f minutes ' % (minutes))