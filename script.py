from instagrapi import Client
import os
from datetime import datetime
import query
import db
import controllers

CURRENT_DIR = os.getcwd() + os.sep
DOWNLOAD_DIR = CURRENT_DIR + 'downloads' + os.sep
UPLOAD_DIR=DOWNLOAD_DIR+'video.mp4'


def time_difference_in_minutes(dt1):
    dt2 = datetime.now(dt1.tzinfo)
    diff_seconds = (dt2 - dt1).total_seconds()
    diff_minutes = diff_seconds / 60
    
    return diff_minutes

def get_reels(account,api,db):
    
    user_id = api.user_id_from_username(account)
    medias =client.user_clips(user_id,5)
    
    for i in medias:
        
        data = {
           "id" : i.id,
           "upload_time" : i.taken_at,
           "like_count" : i.like_count,
           "play_count" : i.play_count,
           "comment_count" : i.comment_count,
           "caption" : i.caption_text,
           "video_url" : str(i.video_url),
           "strength" : (((i.like_count +  i.comment_count)*10000)/time_difference_in_minutes(i.taken_at))
        }

        check = controllers.get_reel(db,query.GET_REEL,data["id"])

        if(check) :
            continue
        else :
            controllers.insert_reel(db,query.INSERT_REEL,data)

    upload_reels(api,db)

    return "done"

def upload_reels(api,db):

    reels = controllers.get_best_reel(db,query.GET_BEST_REEL)

    print(reels)
    
    CAPTION = reels[0][5]
    VIDEO_URL = reels[0][6]
     
    client.video_download_by_url(VIDEO_URL,filename='video',folder=DOWNLOAD_DIR) 
    media = api.clip_upload(
    UPLOAD_DIR,
    CAPTION
    )

    os.remove(UPLOAD_DIR)

    return "done"

client = Client()
db = db.db()
client.login('ganje.salamanca','qwerty1234')
medias = get_reels('amrutamokal',client,db) 


# c=1
# for reel in medias:
#     if reel.video_url != None :
#         # client.video_download_by_url(reel.video_url,filename='video'+str(c),folder=DOWNLOAD_DIR)
#         c=c+1
# # upload_reels(client)18:27:20	DELETE FROM reels	Error Code: 1175. You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column.  To disable safe mode, toggle the option in Preferences -> SQL Editor and reconnect.	0.0032 sec
