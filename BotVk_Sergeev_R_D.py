from vkbottle.bot import Bot,Message
TOKEN = "vk1.a.-x2xCSdQlJgrcYgPElTjm2twqVMLFzDEZ_4Zv9csQGNOT36hkqmFrcnnNfwWxW2TudfkhX2p_IDLtd-IKpCDNlu3M9_DH65-TwaTvw2qZmdnq7qzzaugbIHI0MrP_Oqyn1Fcm0YT_N_Fv2zq25HIJoYCjOUGykCn5dIHbpdDzAlaStHhE83yr9jxrlPlH5mu9Z3eOA57b0ouCIaK9atsow"

bot=Bot(TOKEN) 
# комманда старт\
@bot.on.message(text="/start")
async def start_handler(message:Message):
    await message.answer("Привет я бот в ВКонтакте")
    #ответ на любое сообщение "привет"
@bot.on.message(text="Привет")
async def hi_handler(message:Message):
    user_id=message.from_id
    await message.answer(f"И тебе привет {user_id}")
#обработка отсального текста
@bot.on.message()
async def any_message(message:Message):
    text=message.text
    user_id=message.from_id
    if text:
        await message.answer(f"Ты написал {text}, молодец {user_id}") 