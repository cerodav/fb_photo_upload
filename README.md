# fb_photo_upload

Please note for the right functioning of this code, please do install the SDK first from :
https://github.com/pythonforfacebook/facebook-sdk

The script is so easy to work out, just plug in your access_token which can be obtained from :
https://developers.facebook.com/tools-and-support/
Please make sure that you have selected publish rights, incase posting photos to wall

And incase if you want to push all the photos to an album : 
1. If you already have an album to which you are willing to push photos, skip steps till 5
2. Choose photos->album->add photos
3. In the dialogue box enter your desired name for album and add a random photo through Fb for now, and hit accept or ready(whatever)
4. Delete this photo, so now you have a plain clear album to push photos into
5. Now bring up your web console (for chrome : Ctrl+Shift+I, for mozilla: Ctrl+U), and then Find (Ctrl+F) the term " album_id="
6. Please copy whatever be the value after 'album_id=' until u reach a '&' i guess, because whatever you have copied is your Album ID
7. Plug these values into the code, and fire it :)

Incase if you simply want to push all the photos to the wall :
1. Just remove teh album path variable in the graph statement (the last line which is not a comment :))

This is not a big deal, just 15 lines of code i guess, thanx to the guy who made this https://github.com/pythonforfacebook/facebook-sdk
