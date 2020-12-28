from ..database import redis_db

CHAR_SET = tuple("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def encode(num: int):
    if not isinstance(num, int):
        raise TypeError("The type of num should be int, while %s got." % type(num))
    if num == 0:
        return CHAR_SET[0]

    res = []
    length = len(CHAR_SET)
    while num:
        num, remain = divmod(num, length)
        res.append(CHAR_SET[remain])
    
    return "".join(reversed(res))

def short_url(url: str):
    num = int(redis_db.incr("url_count"))
    token = encode(num)
    return token
    