import qrcode as qr

img  = qr.make("https://www.youtube.com/watch?v=DBXyJO7ZZfw")
img.save("youtube_channel.png")

