from flask import Flask, Response
from sql_client import Mysql

app = Flask(__name__)


@app.route(f"/vk_id/<user>")
def index(user):
    sql_result = Mysql.get_db_values(Mysql, f"SELECT id from test_users where username = '{user}'")
    try:
        if sql_result[0] is not None:
            sql_id = sql_result[0]["id"]
            return Response(f'{{"vk_id":"{sql_id}"}}', status=200, mimetype="application/json")
    except IndexError:
        return Response("{}", status=404, mimetype="application/json")


if __name__=="__main__":
    app.run(host='192.168.0.11')

