import pika, json, tempfile, os
from bson.objectid import ObjectId
import moviepy.editor


def start(message, fs_videos, fs_mp3s, channel):
    message = json.loads(message)

    # empty temp file
    tf = tempfile.NamedTemporaryFile()
    
    # video contents
    out = fs_videos.get(ObjectId(message['video_id']))
    
    # add video contents to temp file
    tf.write(out.read())
    
    # create audio from temp video file
    audio = moviepy.editor.VideoFileClip(tf.name).audio
    tf.close()

    # write audio to temp file
    tf_path = tempfile.tempfile.gettempdir() + f"/{message['video_id']}.mp3"
    audio.write_audiofile(tf_path)

    # save file to monogdb
    f = open(tf_path, 'rb')
    data = f.read()
    fid = fs_mp3s.put(data)
    f.close()
    os.remove(tf_path)

    # send message to rabbitmq
    message['mp3_id'] = str(fid)

    try:
        channel.basic_publish(
            exchange='',
            routing_key=os.environ.get('MP3_QUEUE'),
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.spec.PERSISTENT_DELIVERY_MODE,
            )
        )
    except Exception:
        fs_mp3s.delete(fid)
        return 'failed to publish message'