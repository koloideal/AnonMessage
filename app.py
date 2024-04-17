from quart import Quart, render_template, request, flash
from utils_func.message_to_user import main
import configparser
import os
from utils_func.data_to_database import to_database
import datetime
from telethon.errors.rpcerrorlist import UsernameInvalidError, MessageIdsEmptyError
import logging

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

            if not data['username'] and text:

                raise TypeError

            if not text and data['username']:

                raise MessageIdsEmptyError(request)

            if not text and not data['username']:

                raise IndexError

            username = data['username'] if data['username'][0] != '@' else data['username'][1:]

            await main(text, username)

            date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")

        except (ValueError, UsernameInvalidError) as e:

            logging.warning('\n\n')

            logging.error(e.__class__.__name__, exc_info=True)

            logging.warning('\n\n')

            await flash('Пользователь не найден', category='flash_err')

        except IndexError:

            logging.warning('\n\n')

            logging.error('IndexError', exc_info=True)

            logging.warning('\n\n')

            await flash('Поля ввода пустые', category='flash_err')

        except MessageIdsEmptyError:

            logging.warning('\n\n')

            logging.error('MessageIdsEmptyError', exc_info=True)

            logging.warning('\n\n')

            await flash('Пустое сообщение', category='flash_err')

        except TypeError:

            logging.warning('\n\n')

            logging.error('UsernameIsEmptyError', exc_info=True)

            logging.warning('\n\n')

            await flash('Пустой юзернейм', category='flash_err')

        else:

            to_database(user_ip, username, date)

            await flash('Сообщение отправлено', category='flash_ok')

    return await render_template('base.html')

if __name__ == '__main__':

    logging.basicConfig(level=logging.WARNING, filename="secret_data/logs.log", encoding='utf-8',
                        format="%(asctime)s %(levelname)s %(message)s")

    app.run(debug=True)
