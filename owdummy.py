import json

owdummy = json.loads("""
{  
   "coord":{  
      "lon":-0.13,
      "lat":51.51
   },
   "weather":[  
      {  
         "id":300,
         "main":"n/a",
         "description":"n/a",
         "icon":"09d"
      }
   ],
   "base":"stations",
   "main":{  
      "temp":0,
      "pressure":0,
      "humidity":0,
      "temp_min":0,
      "temp_max":0
   },
   "visibility":10000,
   "wind":{  
      "speed":0,
      "deg":0
   },
   "clouds":{  
      "all":0
   },
   "dt":1485789600,
   "sys":{  
      "type":1,
      "id":5091,
      "message":0.0103,
      "country":"GB",
      "sunrise":1485762037,
      "sunset":1485794875
   },
   "id":2643743,
   "name":"London",
   "cod":200
}
""")
