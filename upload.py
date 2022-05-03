import argparse
from pyrogram import Client


def parse_arguments():
    parser = argparse.ArgumentParser("telegram file uploader")
    parser.add_argument("-s", dest="session_name", type=str)
    parser.add_argument("-sh", dest="session_hash", type=str)
    parser.add_argument("-ai", dest="api_id", type=str)
    parser.add_argument("-ah", dest="api_hash", type=str)
    parser.add_argument("-t", dest="bot_token", type=str)
    parser.add_argument("-ch", dest="chat_id", type=str)
    parser.add_argument("-f", dest="file_path", type=str)
    return parser.parse_args()


async def send_document(app, chat_id, file_path):
    async with app:
        await app.send_document(chat_id=chat_id, document=file_path)
        print(await app.export_session_string())


if __name__ == '__main__':
    args = parse_arguments()
    session_name = args.session_name
    session_hash = args.session_hash
    api_id = args.api_id
    api_hash = args.api_hash
    bot_token = args.bot_token
    chat_id = args.chat_id
    file_path = args.file_path

    app = Client(session_name, session_string=session_hash, api_id=api_id, api_hash=api_hash, bot_token=bot_token)
    app.run(send_document(app, chat_id, file_path))

