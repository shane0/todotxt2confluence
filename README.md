# todotxt2confluence
a cronjob to interface todo.txt android app with confluence using dropbox (if you're confluence is on a private network)

This is something I used in a situation where I was using confluence wiki at work and confluence was only hosted internally

I was also  working on the road at the time and using gina tripani's todo.txt android app on my phone for tasks

I wanted to keep my coworkers updated on my progress and priorities while on the road, so I used this script, to do this you'd need todo.txt on your phone, it uses a text file in dropbox, then at work where confluence is hosted run this python script as a cronjob on a linux box

If you're lucky confluence is in a dmz and you can just use their mobile app, but either way if you're an ascii, dropbox or todo.txt fan you could adjust this in a variety of situations to use todo.txt and confluence together 
