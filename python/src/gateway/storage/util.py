import pika, json


def upload(f, fs, channel, access):
    try:
        fid = fs.put(f)
    except Exception as err:
        print(err)
        return str(err), 500
    
    message = {
        'video_id': str(fid),
        'mp3_id': None,
        'username': access['user'],

    }

    try:
        channel.publish(
            exchange='',
            routing_key='video',
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            )
        )
    except Exception as err:
        print(err)
        fs.delete(fid)
        return str(err), 500
