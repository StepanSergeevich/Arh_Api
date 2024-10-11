from config import host, user, password, db_name
from flask import Flask, request
from flask_restful import Api, Resource
import requests, psycopg2

app = Flask(__name__)
api = Api(app)



class Weather(Resource):
    def post(self):
        get_request = request.get_json()
        latitude = 0
        longitude = 0

        if not get_request:
            return {'message': 'Ошибка: пустой json'}, 400

        try: 
            conntection = psycopg2.connect(host=host, user=user, password=password, database=db_name)

            with conntection.cursor() as cursor:
                cursor.execute(""" SELECT * FROM api_database""")
                data = cursor.fetchall()

                city_found = False
                for elem in data:
                    if elem[0] == get_request.capitalize():
                        latitude = elem[1]
                        longitude = elem[2]
                        city_found = True
                        break
                    
                if not city_found:
                    return{'message': f'Город {get_request} не найден'}, 404
                    
            url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
            response = requests.get(url).json()
            
            temperature = response['current_weather']['temperature']
            windspeed = int(response['current_weather']['windspeed']) / 3.6 

            return {'message': f'{get_request} - {temperature} °C при ветре в {windspeed:.1f} m/s'}

        except Exception as e:
            print(f"Произошла ошибка: {e}")

api.add_resource(Weather, '/weather')

if __name__ == '__main__':
    app.run(debug=True)  












