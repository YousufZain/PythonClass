from pytube import YouTube
link = input("Enter Your YouTube URL : ")
yt = YouTube(link)
videos = yt.streams.all()
    #this will stream all the format available for the video
video = list(enumerate(videos))
    #this will be index the all format in the list starting with zero
for i in video:
        print(i)
        ##this will print all the availabel formate of video with proper index
print("enter the desired option to download the formate ")
dn_option = int(input("Enter the option : "))
#Ask user that which format he wanted to download
dn_video = videos[dn_option]
dn_video.download() #for the downlaoding video
print("Download Successfull")