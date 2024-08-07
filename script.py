
import os
from datetime import datetime
import query
import controllers
import time

# --------------------------------------------------------------------------------------------------------------------

CURRENT_DIR = os.getcwd() + os.sep
DOWNLOAD_DIR = CURRENT_DIR + 'downloads' + os.sep
UPLOAD_DIR=DOWNLOAD_DIR+'video.mp4'
THUMBNAIL_DIR=DOWNLOAD_DIR+'video.mp4.jpg'
accounts= [ "sarcastic_us",
                "idiotic.trolls",
                "trolls_official",
                "_naughtysociety",
                "ghantaa",
                "daily_over_dose",
                "trollscasm",
                "log.kya.sochenge",
            ]
# --------------------------------------------------------------------------------------------------------------------

def time_difference_in_minutes(dt1):
    dt2 = datetime.now(dt1.tzinfo)
    diff_seconds = (dt2 - dt1).total_seconds()
    diff_minutes = diff_seconds / 60
    
    return diff_minutes

# --------------------------------------------------------------------------------------------------------------------

def get_reels(api,db):
    for acc in accounts:

        user_id = api.user_id_from_username(acc)
        medias = api.user_clips(user_id,6)
        
        for i in medias:
            data = {
            "id" : i.id,
            "upload_time" : i.taken_at,
            "like_count" : i.like_count,
            "play_count" : i.play_count,
            "comment_count" : i.comment_count,
            "caption" : str(i.caption_text),
            "video_url" : str(i.video_url),
            "strength" : (((i.like_count +  i.comment_count)*10000)/time_difference_in_minutes(i.taken_at))
            }

            check = controllers.get_reel(db,query.GET_REEL,data["id"])

            if (check) :
                continue
            else :
                controllers.insert_reel(db,query.INSERT_REEL,data)

    return "done"


# --------------------------------------------------------------------------------------------------------------------

def upload_reels(api,db):
    print("Trying to upload")
    reels = controllers.get_best_reel(db,query.GET_BEST_REEL)
    print("reel data",reels)
    
    for reel in reels:
        CAPTION = reel[5]
        VIDEO_URL = reel[6]
        api.video_download_by_url(VIDEO_URL,filename='video',folder=DOWNLOAD_DIR) 
        media = api.clip_upload(
        UPLOAD_DIR,
        CAPTION
        )
        controllers.update_reel(db, query.UPDATE_REEL, reel[0])

        os.remove(UPLOAD_DIR)
        os.remove(THUMBNAIL_DIR)

    return "done"

# --------------------------------------------------------------------------------------------------------------------


def main(api,database,request):
    
    

    

    # --------------------------------------------------------------------------------------------------------------------

    print("starting")
    # while True:
    #     upload_reels(api,database)
    #     print("video uploaded 1, sleeping for 30 mins")
    #     time.sleep(1800)
    #     upload_reels(api,database)
    #     print("video uploaded 2, sleeping for 30 mins")
    #     time.sleep(1800)
    #     get_reels(api,database)
    #     print("scrapping done, sleeping for 5 mins ")
    #     time.sleep(300)
    # return "done"

