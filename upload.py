import argparse
import asyncio
from pyrogram import Client
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message


def parse_arguments():
    parser = argparse.ArgumentParser("telegram file uploader")
    parser.add_argument("-s", dest="session_name", type=str)
    parser.add_argument("-ai", dest="api_id", type=str)
    parser.add_argument("-ah", dest="api_hash", type=str)
    parser.add_argument("-t", dest="bot_token", type=str)
    parser.add_argument("-ch", dest="chat_id", type=str)
    parser.add_argument("-f", dest="file_path", type=str)
    parser.add_argument("-m", dest="message", required=False, default="", type=str)
    parser.add_argument("--wait-permission", dest="wait_permission", action="store_true")
    parser.add_argument("--wait-time", dest="wait_time", required=False, default=300, type=int)
    return parser.parse_args()


async def wait_message_from_chat(app, chat_id):
    received_message_future = asyncio.get_running_loop().create_future()

    @app.on_message()
    async def my_handler(client, message: Message):
        # print("message received...")
        sending_chat_id = message.chat.id
        if sending_chat_id == chat_id:
            # print("its the same id...")
            received_message_future.set_result(True)
        # else:
            # print("its a different id...")
    await received_message_future


async def main():
    args = parse_arguments()
    session_name = args.session_name
    api_id = args.api_id
    api_hash = args.api_hash
    bot_token = args.bot_token
    chat_id = int(args.chat_id)
    file_path = args.file_path
    message = args.message
    wait_permission = args.wait_permission
    wait_time = args.wait_time

    app = Client(session_name, api_id=api_id, api_hash=api_hash, bot_token=bot_token)
    async with app:
        send_message = True
        if wait_permission:
            # print("waiting time or message...")
            wait_message_task = asyncio.create_task(wait_message_from_chat(app, chat_id))
            wait_timeout_task = asyncio.create_task(asyncio.sleep(wait_time))

            tasks = {wait_message_task, wait_timeout_task}

            # wait for timeout or message from chat to get permission
            done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

            # print("cancelling pending tasks...")
            for task in pending:
                task.cancel()

            if wait_timeout_task in done:
                # print("timed out")
                send_message = False
        if send_message:
            # print("sending message...")
            try:
                await app.send_document(chat_id=chat_id, document=file_path, caption=message)
            except PeerIdInvalid:
                print("ERROR")
        # else:
        #     print("not sending message...")


if __name__ == '__main__':
    asyncio.run(main())
