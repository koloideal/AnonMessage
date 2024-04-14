from quart import Quart, render_template, request, flash
from message_to_user import main
from telethon.errors.rpcerrorlist import PeerIdInvalidError, UsernameInvalidError
import configparser

config = configparser.ConfigParser()

config.read('config.ini')


app = Quart(__name__)
app.config["SECRET_KEY"] = config['Quart']['SECRET_KEY']


@app.route('/', methods=['GET', 'POST'])
async def contact():

    if request.method == 'POST':

        try:

            data = await request.form

            text = data['text']

            username = data['username'] if data['username'][0] != '@' else data['username'][1:]

            await main(text, username)

        except (PeerIdInvalidError, UsernameInvalidError, ValueError):

            await flash('Not sent', category='flash_err')

        else:

            await flash('Sent', category='flash_ok')

    return await render_template('base.html')


if __name__ == '__main__':

    app.run(debug=True)
