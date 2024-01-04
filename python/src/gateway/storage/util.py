import pika, json


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception:
        return 'internal server error', 500
    
    message = {
        'video_id': str(fid),
        'mp3_id': None,
        'username': access['username'],

    }

    try:
        channel.basic.publish(
            exchange='',
            routing_key='video',
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.spec.PERSISTENT_DELIVERY_MODE,
            )
        )
    except:
        fs.delete(fid)
        return 'internal server error', 500