INSERT_REEL = "INSERT INTO reels (id, upload_time, likes_count, play_count, comment_count, caption, video_url, upload, strength) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

GET_BEST_REEL = "SELECT * FROM reels WHERE upload = False ORDER BY strength DESC LIMIT 1;"

UPDATE_REEL = "UPDATE reels SET upload = True WHERE id = %s;"

GET_REEL = "SELECT * from reels WHERE id = %s;"

DELETE_CURRENT= "DELETE FROM reels;"