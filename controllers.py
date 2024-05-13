def insert_reel(db,query,data):
    mycursor = db.cursor()
    val = (data["id"], data["upload_time"], data["like_count"], data["play_count"], data["comment_count"], data["caption"], data["video_url"], False, data["strength"])
    mycursor.execute(query, val)
    db.commit()

    return "done"

def get_best_reel(db,query):
    mycursor = db.cursor()
    mycursor.execute(query) 
    data = mycursor.fetchall()  
    return data

def update_reel(db,query,id):
    mycursor = db.cursor()
    value = (id,)
    mycursor.execute(query,value)
    db.commit()   
    return "done"

def get_reel(db, query, id):
    mycursor = db.cursor()
    value = (id,)  
    mycursor.execute(query, value)
    data = mycursor.fetchall()  

    return len(data) == 1  

