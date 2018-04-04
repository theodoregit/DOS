import requests as req
count = 2
print("request are sent")
while(1 == 1):
    res = req.get("http://localhost:9000/dict/dictionary?word=POTTEEN")
    #print(res.text)
    #count -= 1

