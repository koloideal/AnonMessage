from quart import Quart, render_template, request, flash
from utils_func.message_to_user import main
import configparser
import os
from utils_func.data_to_database import to_database
import datetime

config = configparser.ConfigParser()

config.read('secret_data/config.ini')


app = Quart(__name__)
app.config["SECRET_KEY"] = config['Quart']['SECRET_KEY']

os.makedirs('secret_data', exist_ok=True)


@app.route('/', methods=['GET', 'POST'])
async def contact():

    user_ip = request.remote_addr

    if request.method == 'POST':

        try:

            data = await request.form

            text = data['text']

            username = data['username'] if data['username'][0] != '@' else data['username'][1:]

            await main(text, username)

            date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

        except ValueError:

            await flash('Пользователь не найден', category='flash_err')

        except IndexError:

            await flash('Поля ввода пустые', category='flash_err')

        else:

            to_database(user_ip, username, date)

            await flash('Сообщение отправлено', category='flash_ok')

    return await render_template('base.html')


if __name__ == '__main__':

    app.run(debug=True)
