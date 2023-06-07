Action for sending files to Telegram using the [MTProto API](https://docs.pyrogram.org/topics/mtproto-vs-botapi), i.e. you can send files up to 2 GiB.
# Usage
Send a file with a caption message
```yaml
steps:
  - name: Send file to telegram with MTProto API
    uses: mnicolas94/telegram-file-uploader@main
    with:
      session-name: ${{ secrets.TELEGRAM_SESSION }}
      api-id: ${{ secrets.TELEGRAM_API_ID }}
      api-hash: ${{ secrets.TELEGRAM_API_HASH }}
      bot-token: ${{ secrets.TELEGRAM_TOKEN }}
      chat-id: ${{ secrets.TELEGRAM_CHAT_ID }}
      file-path: <path/to/file>
      message: This is a file sent with MTProto API
      cache-session: 'true'
      reply-request: 'The build size is bigger than 50 MB. Please, reply to this message to give me permission to send you the file'
      wait-for-permission-time: 300
```
# Input variables

* session-name: the name for the Pyrogram session. Could be anything, but should be always the same for the same use case.

* api-id: id of your telegram app. Visit https://my.telegram.org/apps to get one. More info in [Pyrogram setup](https://docs.pyrogram.org/start/setup).

* api-hash: hash of yout telegram app. Same as the previous input.

* bot-token: the token of the bot that will send the file.

* chat-id: the chat id you want to send the file to.

* file-path: the file's path you want to send.

* message: [optional] a message caption.

* cache-session: [optional] Default value is 'false'. Set to 'true' to cache the Pyrogram session data file. If set to 'false' or the first time you use this action you will receive a reply request message in Telegram to allow the bot to send messages through the MTProto API. More info in https://docs.pyrogram.org/topics/storage-engines. WARNING: the session data file stores credentials that could be compromised if you cache it in a public repository, use it with care, more info in https://docs.github.com/en/actions/using-workflows/caching-dependencies-to-speed-up-workflows.

* reply-request: [optional] Message sent when the bot has not yet met the chat, or the session is not cached.

* wait-for-permission-time: [optional] Defaults to 300. Seconds to wait for a reply when asking for permission. See two previous variables description.

