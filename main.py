import telebot # импортируем telebot
from secrets import secrets # словарь с токеном из файла secrets.py
import random # для выбора случайного комплимента
# передаём значение переменной с кодом экземпляру бота
bot = telebot.TeleBot('8316990519:AAFA29x7evTvJXCpnoznk2kuazhlswFaoTY')
users = {}



# хендлер и функция для обработки команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(text="Расклады МАК🔮",
                                                     callback_data='save_data')
    button_change = telebot.types.InlineKeyboardButton(text="Тесты📄",
                                                       callback_data='change_data')
    #button_kurs = telebot.types.InlineKeyboardButton(text="Курс📚",
    #                                                   callback_data='kurs_data')
    button_rasskaz = telebot.types.InlineKeyboardButton(text="️Психотерапевтические рассказы⭐️",
                                                      callback_data='rasskaz_data')
    button_medi = telebot.types.InlineKeyboardButton(text="Отзывы❤️",
                                                        callback_data='medi_data')
    button_zapis = telebot.types.InlineKeyboardButton(text="️Записаться на консультацию✏️",
                                                     callback_data='zapis_data')
    keyboard.add(button_save, button_rasskaz, button_change, button_zapis, button_medi, row_width=1  )
    img = 'https://sun9-32.userapi.com/s/v1/ig2/t2Fje7Ezewl5tg0GGaVjCVsJCXVv28lqa0vkZtErcyMAAEAMkOTXRCp4JaaUVvdA2sBCbvwCurfTrXKmJ3NNWv1g.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu&cs=1920x0'
    bot.send_photo(message.chat.id, img, caption='Добро пожаловать в чат-бот психолога Ирины Елисеевой',
                     reply_markup=keyboard)

#Обработчик первой кнопки (расклады МАК)
@bot.callback_query_handler(func=lambda call: call.data == 'save_data')
def save_btn(call):
    message = call.message
    chat_id = message.chat.id
    img = 'https://sun9-12.userapi.com/s/v1/ig2/KNolflLWUHbLhldnNtrTlxHe0vHvKiWOsCrAXmEvWecuQjO6vbFc4zf8GLuJuYua-n1Ok6itw8HDoHBptN9UTfCL.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu&cs=1920x0'
    msg = bot.send_photo(message.chat.id, img, caption='Вы находитесь в разделе раскладов с метафорическими картами')
    bot.send_message(message.chat.id, "<b>Как правильно сформулировать вопрос для МАК-карт?</b> \n1. Говорите от первого лица и сосредоточьтесь на одной конкретной теме - так вы сделаете запрос более личным и четким. \n2. Избегайте вопросов, на которые можно ответить «Да» или «Нет». \n3. Ваш вопрос должен касаться сферы вашего влияния - сфокусируйтесь на том, что можете изменить сами, а не на действиях других людей или внешних обстоятельствах. \nВ итоге хороший запрос звучит так: он про вас, затрагивает одну тему, предполагает развернутый ответ и находится в зоне вашего контроля. Например: «Что поможет мне преодолеть страх публичных выступлений?» ", parse_mode="html")
    bot.send_message(message.chat.id, "Введите ваш запрос для расклада:")
    users[chat_id] = {}
    bot.register_next_step_handler(msg, after_text_2)

#Обработчик рандомной МАК-КАРТЫ
def after_text_2(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                     callback_data='nazad_data')
    keyboard.add(button_nazad)
    m1 = message.text
    file_name = str(message.from_user.last_name) + str(message.from_user.first_name) + ".txt"
    print(file_name)
    f = open(file_name, 'a')
    f.write(message.text + ' ')
    f.close()
    bot.send_message(message.chat.id, "Карта по вашему запросу «"+ str(m1)+"»")
    l1 = 'https://sun9-72.userapi.com/s/v1/ig2/dKnPOuj5xeNhZ6ESXrOVUsiM38yMUVSwQMp3aVW3oVon4nAd0_TDEu_R8x7a330oV9tiEbP8vIGfLQMIPWOd3Sfb.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l2 = 'https://sun9-25.userapi.com/s/v1/ig2/WkoEA95h_bJS-QFYvcGbZuFnkqTanS1p3q3U1EUsT8WQItuvWiLUv5HUBgZgAyAD53zWaEZAz8gRJhSdeUGqJKH-.jpg?quality=95&as=32x38,48x57,72x86,108x129,160x191,240x286,360x429,480x572,540x643,640x762,720x857,896x1067&from=bu&cs=896x0'
    l3 = 'https://sun9-64.userapi.com/s/v1/ig2/4KsW6LIw2kcJfaAABGdTWoXwFzkP5PR2xHf5Ou6VJgoehAe9gzHWEmeQ7zbo3u6ZbbToxxpuInTwWq9DEJSQPrtj.jpg?quality=95&as=32x40,48x60,72x91,108x136,160x202,240x302,360x454,480x605,540x680,640x806,720x907,896x1129&from=bu&cs=896x0'
    l4 = 'https://sun9-87.userapi.com/s/v1/ig2/0L_KF3Vaw0GQDNav2HUobLUC1fz8YOU1V7Epj_d5zqpEOiUybY7_8oU8owl1hOisNhXJArPKar9F3pXPKhy2gCtS.jpg?quality=95&as=32x39,48x58,72x88,108x131,160x195,240x292,360x438,480x584,540x657,640x779,720x876,896x1090&from=bu&cs=896x0'
    l5 = 'https://sun9-26.userapi.com/s/v1/ig2/0suegqNhGeBplExvwtyydF5FdzKnkBeOVrD2rAHyTyv-MNzovILtcWRstz0WImcsKCsbXap6a6LZ5R5EXhD7k0Kv.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l6 = 'https://sun9-70.userapi.com/s/v1/ig2/4RrxdBypOQblT_-de7RUyW0Vf04TE7wHxxdCyJypEdX3DsyQcGo-UY2MUFnt02swSOZD0UM9zrDyAAnyrLvlf8v3.jpg?quality=95&as=32x40,48x60,72x90,108x135,160x201,240x301,360x451,480x602,540x677,640x802,720x902,896x1123&from=bu&cs=896x0'
    l7 = 'https://sun9-70.userapi.com/s/v1/ig2/vXKwH0HaREPDHZiYDyMhvU6s9mCVgWlPG90aKdthi2bA0md2TES1_UsOcYoXHNaF20Np604pV_R6lWza6nHCRsjw.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l8 = 'https://sun9-30.userapi.com/s/v1/ig2/3I5a4fgBdjo7KaWXBd-bkiaLGCQ0QgtUSTLAhx3PNl-TbYN1b79uMLvsRvqt2H9SXk87Ua8OTwpAfGS7UyIG3DSM.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l9 = 'https://sun9-66.userapi.com/s/v1/ig2/y27tojEhH0coNM0plm7hHHFR6PWLvgm0os3Me5C7kOMS1Jl7kZbSj4XeqouIrmSNm820oI3wyzapGLcaIEODjEWM.jpg?quality=95&as=32x40,48x60,72x90,108x134,160x199,240x298,360x448,480x597,540x671,640x796,720x895,896x1114&from=bu&cs=896x0'
    l10 = 'https://sun9-23.userapi.com/s/v1/ig2/Y2F7l9j-tV1in9Jo5TRCBJCCOq4DZkv4M-xxn8YmnyAB28plg6mUain_CBX1NGIz19m89f7i1K9dw2Ph2qJXrUkw.jpg?quality=95&as=32x40,48x60,72x89,108x134,160x198,240x298,360x446,480x595,540x670,640x794,720x893,896x1111&from=bu&cs=896x0'
    l11 = 'https://sun9-9.userapi.com/s/v1/ig2/wSOF4HmzGsAVHt67QM5gp-9vQfCnuDfCi9IeaDmTmueY4ATdpqHUevtVw7CrpO5TPXUQLKlP_EDhcObWt7nrabE4.jpg?quality=95&as=32x38,48x57,72x85,108x128,160x190,240x285,360x427,480x569,540x640,640x759,720x854,894x1060&from=bu&cs=894x0'
    l12 = 'https://sun9-57.userapi.com/s/v1/ig2/J-VWkzPs127FLPqb8PozNRvv2Ts9kxbQ5vK2B_La43GHsi3-p1UmFqhUybpRaIRlDj1-qFl79Xk7_X9zBtjchrMc.jpg?quality=95&as=32x40,48x59,72x89,108x134,160x198,240x297,360x445,480x594,540x668,640x791,720x890,896x1108&from=bu&cs=896x0'
    l13 = 'https://sun9-51.userapi.com/s/v1/ig2/nmlgatBKRscMbGMz3vFIum0wppLMVNvc16ipgrwgRAa7KcwwVq7aaMIaF7MeS2zb21n4pOHMnNJg4_WAmlGjbJyL.jpg?quality=95&as=32x40,48x60,72x90,108x135,160x201,240x301,360x452,480x602,540x677,640x803,720x903,896x1124&from=bu&cs=896x0'
    l14 = 'https://sun9-86.userapi.com/s/v1/ig2/ZmIm-SkI3DOU3P7Rt78vEcxz6NjMCPbX1enFRa1wklrMClMBwutyC_4s9qgpyVPBl_BKVoOZDQpNmnO59dPewtL_.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l15 = 'https://sun9-21.userapi.com/s/v1/ig2/Ke3Jh_PFwhd72Mr0YTUC840qpaW1hCi5EtXxeai1rOrMSrhg5wv13sJvGXpvNI-I9AG_h_q0Tbb6gUYggz_-xbL9.jpg?quality=95&as=32x39,48x59,72x88,108x132,160x196,240x294,360x440,480x587,540x661,640x783,720x881,896x1096&from=bu&cs=896x0'
    l16 = 'https://sun9-35.userapi.com/s/v1/ig2/crSTLthCYz9318vJLgy_nNTJWwbcw3W_9YTnUkD8oLD_uwZ_9jslpNpYuRz9STjZGlqFwMqOyuT9bt0h597eePz0.jpg?quality=95&as=32x39,48x59,72x88,108x132,160x196,240x294,360x440,480x587,540x661,640x783,720x881,896x1096&from=bu&cs=896x0'
    l17 = 'https://sun9-47.userapi.com/s/v1/ig2/lytQRWpzDgusqXEDFXapqfQo6B6xJIjQ-6zPpJPrISAYfFgHBZ8BgUk-EXK1b2Ecyg3w801LBIyp5I84rKjxCVVw.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l18 = 'https://sun9-46.userapi.com/s/v1/ig2/GhV3W0K9ymIFOOInyHmg2MgKXX0ppVlIalh1dXqnjX_nWiK-MClwxPTsqkfCDx_l9lXiO1gC5nUYD9W_807yDzQe.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l19 = 'https://sun9-54.userapi.com/s/v1/ig2/-rY4TyzKBLIHgQcNqZnCaip9477_pmEMQgkf_BeTXG8VR9Uy93jjwQNW1OBTDKujDo-LCAJxQ1a6540WFgE_u4N9.jpg?quality=95&as=32x40,48x60,72x89,108x134,160x199,240x298,360x447,480x596,540x671,640x795,720x894,896x1113&from=bu&cs=896x0'
    l20 = 'https://sun9-14.userapi.com/s/v1/ig2/GBDEIeomkJBoBFVf6gorsU2NnC8OAk3g6ZJgUEJ0l43ymknbg7_jaWoGu4hCZgEa3aht3BWfZcoY7zFKwuKjUx5X.jpg?quality=95&as=32x47,48x71,72x106,108x159,160x235,240x353,360x529,480x705,540x793,640x940,720x1058,1047x1538&from=bu&cs=1047x0'
    l21 = 'https://sun9-3.userapi.com/s/v1/ig2/UVR7RXv_nfT2jlJ_jIuOeXofG_lOfzvi9WfeFVjmy920Qa1EJOiwZBFieCLuZ9vc4dTG-Yz82jfjAJuUa8LITGIj.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l22 = 'https://sun9-54.userapi.com/s/v1/ig2/LEH7loNT8V3zHXLVzniudjfGwkREtVoEb0-_3T-VJ3gJcwk0zacnGcik4Y_MFo23Z9ubZiB1v7FBLCNwccCvW-uL.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l23 = 'https://sun9-55.userapi.com/s/v1/ig2/EO3sGJxUsiIvZ9_azFogUqkUMrLvLGf2iavwkxZAC8MjVA1G7UrDgluA6l-_A6r7_GfVc4zNKrJqpr8108WtQnSs.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l24 = 'https://sun9-72.userapi.com/s/v1/ig2/h1_V2ycQUiiPfUChqo8GrsG3ahdLWEQpMVXHrUGTcI220nP68eEYGAvrZnwLpStNahjfRkGBwaWdEQMMW95BtIYw.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l25 = 'https://sun9-46.userapi.com/s/v1/ig2/7qgUVVFrV0dDux0VwQT2v4f_KlyVhxPuZAol0074JiVsamHNWmO3pNoElmfe-Vcc3Ji4yj23O2M0k1p6y4639IHB.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l26 = 'https://sun9-25.userapi.com/s/v1/ig2/8FgOamm-sl7qHaPGq44KLaDCTdBjahvK_trx2QLFRD_P_o-0EnA7mYRKYqFSmD1HLboCYHuGywIIf80IhsYRct5K.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l27 = 'https://sun9-52.userapi.com/s/v1/ig2/l9mYH_gRZ-Gd42TP46jV_kuEioy4hYxRIxfNsr5e7bmCjW1F2qYGbCnfLaA4nEx9qacorX0scIUkPhurhaxECiP2.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l28 = 'https://sun9-15.userapi.com/s/v1/ig2/fMkDjTVKPGO40fdjvGUDhPPM5CX8V82GBSGf8V4icLBNC3FQ-QPTsyzKW14WFOFZXWJWwvDk5dw1ZJotPYOVjm6J.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l29 = 'https://sun9-68.userapi.com/s/v1/ig2/beQC2K6GA7hcrJTqDYxXULjrBPXKtZ2cElyXCn9PH7qtm9RMsFVMuJX60AjGPKS9W4kBKTceiqKuZ0uyqRIsxouR.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l30 = 'https://sun9-4.userapi.com/s/v1/ig2/13ydiHX03YCB3_fFx9sXcs_rS4B4OQsFkEpUIsNAvUERXikNttiAslz-2R-_dPTn6hH2UrTFykZzzjycIMFqYTbg.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l31 = 'https://sun9-42.userapi.com/s/v1/ig2/MvqJFwwMZARZxgOHzlt4GHAfsQtX99MgyHhTgs_7bBboUodxW4iPZxrNKXM0q70lU8iMfNTcs1Zb7mkArKesIe7m.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l32 = 'https://sun9-66.userapi.com/s/v1/ig2/xaxFLeLiAiJfh2BAoerO9XUApZ0fyd5sTAYufL3I6An_diG88iVctUI1LoKWtDccjkaCjtL1jJX45zqboUYqI6D_.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l33 = 'https://sun9-5.userapi.com/s/v1/ig2/cusysF-9dy7S1R3uJv9IYXEvDNlSv6aUN7UM21PN8X9PPS2LO5K997k9q-UsuKePsIXuSzgHRMEkO2tLpskkEqEF.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l34 = 'https://sun9-29.userapi.com/s/v1/ig2/seDSTGAcJDJJrHGh16Ykr4XPvV7F2iyff6kvFZkozeW0JaUDPvWIsp_zVUTVX5F2jOxKopeNcsSGUARkvIGxDAS7.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l35 = 'https://sun9-2.userapi.com/s/v1/ig2/WULqFznhdHyyC0JxdqQWx9GXVQwlqyZ2-6Z0I3kGT239jDXJ2VXgDoHnPyzEQo7wQ2Ingib9jYfuqlFolZ5uPxTC.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l36 = 'https://sun9-76.userapi.com/s/v1/ig2/B-lNvTUPztQAaRLNnB3V05IO-vt_5JZgg2edfbApgDEmUgC9xgFfkZWOoP2l01MiNcc3Xcyy-0EEz77G5-XfJQGS.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l37 = 'https://sun9-56.userapi.com/s/v1/ig2/3VmvlkuSGgfgjgtLoGwexVRBm56eO54bD7W2G2D8yTxRpDsRS7Bp9O9k_WvKgE6zc3M_QLkJP-TFw1dEvWrw3-uY.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l38 = 'https://sun9-36.userapi.com/s/v1/ig2/6PTzPHMpQY4_ZFf6qG4y7WDcCuGB_jUjpazLAYXRtL95Y7YhQ5S9vj3CXBJxriAi95IJuXe4hM60qyhGCbtaZXDj.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l39 = 'https://sun9-9.userapi.com/s/v1/ig2/JhLHtiuvwSbqjidj_YtVBM7McZrCMJ8fLDM2GL9vGMkwkAkEQLBtmyKKaaNJbWmayGJdiqMCdJ0p58yTOBqpr1zL.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l40 = 'https://sun9-21.userapi.com/s/v1/ig2/r2NSjuj7qwz1cf_uJKVy3GgskSqVtarTWSV87G0xHvG_q9eZb3ZL87T0CvPJ7LbPiOtJLu4Mx1lTPoAglomJXcyB.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,790x1053&from=bu&cs=790x0'
    l41 = 'https://sun9-71.userapi.com/s/v1/ig2/Mha7vNHZax-DNgQaeMFvpNQZlknrBXxt3BrVP-h39pWw-dZw7upeUtU6_MlalhGqJPuKFsNzI04-PJ-vDW_KLYdM.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    l42 = 'https://sun9-29.userapi.com/s/v1/ig2/AsKZ1zqD_PJqYCze3_A2mAwj_bolwGaySB3AK8A9J6cu5InV2UnJWT3r-MZHEroj2OaKYHcGvPdX_TQg_LFMGFTg.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&u=8PtmrzpeSsMnn-RAZyVsatp0gOHgD9OgPhP1FUxZ-Do&cs=896x0'
    img_list = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20, l21, l22, l23, l24, l25, l26, l27, l28, l29, l30, l31, l32, l33, l34, l35, l36, l37, l38, l39, l40, l41, l42]
    img_path = random.choice(img_list)
    bot.send_photo(message.chat.id, img_path)
    '''if img_path == l1:
        bot.send_message(message.chat.id, " ")
    elif img_path == l2:
        bot.send_message(message.chat.id, " ")
    elif img_path == l3:
        bot.send_message(message.chat.id, " ")
    elif img_path == l4:
        bot.send_message(message.chat.id, " ")
    elif img_path == l5:
        bot.send_message(message.chat.id, " ")
    elif img_path == l6:
        bot.send_message(message.chat.id, " ")
    elif img_path == l7:
        bot.send_message(message.chat.id, " ")
    elif img_path == l8:
        bot.send_message(message.chat.id, " ")
    elif img_path == l9:
        bot.send_message(message.chat.id, " ")
    elif img_path == l10:
        bot.send_message(message.chat.id, " ")
    elif img_path == l11:
        bot.send_message(message.chat.id, " ")
    elif img_path == l12:
        bot.send_message(message.chat.id, " ")
    elif img_path == l13:
        bot.send_message(message.chat.id, " ")
    elif img_path == l14:
        bot.send_message(message.chat.id, " ")
    elif img_path == l15:
        bot.send_message(message.chat.id, " ")
    elif img_path == l16:
        bot.send_message(message.chat.id, " ")
    elif img_path == l17:
        bot.send_message(message.chat.id, " ")
    elif img_path == l18:
        bot.send_message(message.chat.id, " ")
    elif img_path == l19:
        bot.send_message(message.chat.id, " ")
    elif img_path == l20:
        bot.send_message(message.chat.id, " ")
    elif img_path == l21:
        bot.send_message(message.chat.id, " ")
    elif img_path == l22:
        bot.send_message(message.chat.id, " ")
    elif img_path == l23:
        bot.send_message(message.chat.id, " ")
    elif img_path == l24:
        bot.send_message(message.chat.id, " ")
    elif img_path == l25:
        bot.send_message(message.chat.id, " ")
    elif img_path == l26:
        bot.send_message(message.chat.id, " ")
    elif img_path == l27:
        bot.send_message(message.chat.id, " ")
    elif img_path == l28:
        bot.send_message(message.chat.id, " ")
    elif img_path == l29:
        bot.send_message(message.chat.id, " ")
    elif img_path == l30:
        bot.send_message(message.chat.id, " ")
    elif img_path == l31:
        bot.send_message(message.chat.id, " ")
    elif img_path == l32:
        bot.send_message(message.chat.id, " ")
    elif img_path == l33:
        bot.send_message(message.chat.id, " ")
    elif img_path == l34:
        bot.send_message(message.chat.id, " ")
    elif img_path == l35:
        bot.send_message(message.chat.id, " ")
    elif img_path == l36:
        bot.send_message(message.chat.id, " ")
    elif img_path == l37:
        bot.send_message(message.chat.id, " ")
    elif img_path == l38:
        bot.send_message(message.chat.id, " ")
    elif img_path == l39:
        bot.send_message(message.chat.id, " ")
    elif img_path == l40:
        bot.send_message(message.chat.id, " ")
    elif img_path == l41:
        bot.send_message(message.chat.id, " ")
    else:
        bot.send_message(message.chat.id, " ")'''

    bot.send_message(message.chat.id, "<b>Как интерпретировать карту?</b> \n<b>1. Доверяйте первым ощущениям.</b> Обратите внимание на эмоции и мысли, которые возникли сразу после того, как вы увидели карту. \n<b>2. Свяжите образ с запросом.</b> Подумайте, как изображение соотносится с вашим вопросом - ищите личные, а не «универсальные» смыслы.  \n<b>3. Опишите детали.</b> Что на карте бросается в глаза? Персонажи, цвета, обстановка, направление движения - каждая деталь может нести подсказку. \n<b>4. Задавайте вопросы себе.</b> Например: «Что это говорит обо мне?», «На что это похоже в моей жизни?», «Какой совет здесь скрыт?». \n<b>5. Фиксируйте ассоциации.</b> Запишите ключевые слова, фразы, воспоминания, которые всплывают при взгляде на карту. Подумайте о том, как они связаны с вашим вопросом.", parse_mode="html", reply_markup=keyboard)
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add(button_nazad)
#Обработчик кнопки НАЗАД
@bot.callback_query_handler(func=lambda call: call.data == 'nazad_data')
def nazad_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_save = telebot.types.InlineKeyboardButton(text="Расклады МАК🔮",
                                                     callback_data='save_data')
    button_change = telebot.types.InlineKeyboardButton(text="Тесты📄",
                                                       callback_data='change_data')
    #button_kurs = telebot.types.InlineKeyboardButton(text="Курс📚",
    #                                                 callback_data='kurs_data')
    button_rasskaz = telebot.types.InlineKeyboardButton(text="️Психотерапевтические рассказы⭐️",
                                                        callback_data='rasskaz_data')
    button_medi = telebot.types.InlineKeyboardButton(text="Отзывы❤️",
                                                    callback_data='medi_data')
    button_zapis = telebot.types.InlineKeyboardButton(text="️Записаться на консультацию✏️",
                                                      callback_data='zapis_data')
    keyboard.add(button_save, button_rasskaz,button_change, button_zapis, button_medi, row_width=1)
    img = 'https://sun9-32.userapi.com/s/v1/ig2/t2Fje7Ezewl5tg0GGaVjCVsJCXVv28lqa0vkZtErcyMAAEAMkOTXRCp4JaaUVvdA2sBCbvwCurfTrXKmJ3NNWv1g.jpg?quality=95&as=32x43,48x64,72x96,108x144,160x213,240x320,360x480,480x640,540x720,640x853,720x960,1080x1440,1280x1707,1440x1920,1920x2560&from=bu&cs=1920x0'
    bot.send_photo(message.chat.id, img, caption='Добро пожаловать в чат-бот психолога Ирины Елисеевой',
                   reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'change_data')
def change_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad)
    link1 = 'https://psytests.org/life/svsK.html'
    link2 = 'https://psytests.org/typo/tmig.html'
    link3 = 'https://psytests.org/trait/viais.html'
    link4 = 'https://psytests.org/work/ddoG.html'
    link5 = 'https://psytests.org/big5/ineoB.html'
    bot.send_message(message.chat.id, "Проходите тесты с удовольствием — они помогут вам лучше узнать себя и найти интересные идеи для развития! Но помните: результаты тестов носят ознакомительный характер и предназначены для самопознания и развлечения. Они не являются профессиональной психологической диагностикой. Для глубокой оценки личности лучше обратитесь к квалифицированному психологу.\n\n 1. Тест на определение ценностей: "+ link1 + "\n 2. Тест на преобладающий вид интеллекта: "+ link2 + "\n 3. Тест, определяющий достоинства личности: "+ link3 + "\n 4. Профориентационный тест: "+ link4 + "\n 5. Тест на измерение 5-ти основных черт личности: общительности, ответственности,доброты, эмоциональной устойчивости и открытости  новому: "+ link5,  reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'kurs_data')
def kurs_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad)
    link1 = 'https://psytests.org'
    bot.send_message(message.chat.id, "Вот ссылка на мой курс: \n "+ link1 + "\n Приятного обучения!")

@bot.callback_query_handler(func=lambda call: call.data == 'rasskaz_data')
def rasskaz_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_sbornik = telebot.types.InlineKeyboardButton(text="Сборник рассказов «Внутренний свет»",
                                                     callback_data='rassk_vse')
    button_rassk1 = telebot.types.InlineKeyboardButton(text="«Тревожность»",
                                                       callback_data='rassk_1')
    button_rassk2 = telebot.types.InlineKeyboardButton(text="«Душевные страдания»",
                                                     callback_data='rassk_2')
    button_rassk3 = telebot.types.InlineKeyboardButton(text="️«Ледяное сердце»",
                                                        callback_data='rassk_3')
    button_rassk4 = telebot.types.InlineKeyboardButton(text="«Ожидания»",
                                                     callback_data='rassk_4')
    button_rassk5 = telebot.types.InlineKeyboardButton(text="️«Триггер»",
                                                      callback_data='rassk_5')
    button_rassk6 = telebot.types.InlineKeyboardButton(text="️«Контакт с теневой стороной»",
                                                       callback_data='rassk_6')
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_sbornik, button_rassk1, button_rassk2, button_rassk3, button_rassk4, button_rassk5, button_rassk6, button_nazad, row_width=1)
    img = 'https://sun9-10.userapi.com/s/v1/ig2/7rYUCkDxUWT1PQo86Z7VOO-J15iysO1z56J4h4jR17FJm6bfznO37H2dEB9N9SLPPyH_IvV3n8HHXSyUBa3AgPJj.jpg?quality=95&as=32x41,48x62,72x93,108x139,160x206,240x309,360x463,480x617,540x694,640x823,720x926,896x1152&from=bu&cs=896x0'
    bot.send_photo(message.chat.id, img, caption='Вы находитесь в разделе психотерапевтических рассказов. Выберите подходящий вариант:',
                   reply_markup=keyboard)

#Ссылка на сборник рассказов
@bot.callback_query_handler(func=lambda call: call.data == 'rassk_vse')
def rasskvse_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad)
    rasskv = 'https://www.litres.ru/book/irina-germanovna-eli/vnutrenniy-svet-sbornik-psihoterapevticheskih-rasskaz-72497620/'
    bot.send_message(message.chat.id, "Сборник рассказов «Внутренний свет» доступен бесплатно на Литрес по ссылке: \n "+ rasskv,
                   reply_markup=keyboard)

#Ссылка на рассказ ТРЕВОЖНОСТЬ
@bot.callback_query_handler(func=lambda call: call.data == 'rassk_1')
def rassk1_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad, row_width=1)
    rassk1 = 'https://www.b17.ru/blog/596320/'
    bot.send_message(message.chat.id, "Психотерапевтический рассказ «Тревожность»: \n "+ rassk1,
                   reply_markup=keyboard)

#Ссылка на рассказ ДУШЕВНЫЕ СТРАДАНИЯ
@bot.callback_query_handler(func=lambda call: call.data == 'rassk_2')
def rassk1_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad, row_width=1)
    rassk2 = 'https://www.b17.ru/blog/585496/'
    bot.send_message(message.chat.id, "Психотерапевтический рассказ «Душевные страдания»: \n "+ rassk2,
                   reply_markup=keyboard)

#Ссылка на рассказ ЛЕДЯНОЕ СЕРДЦЕ
@bot.callback_query_handler(func=lambda call: call.data == 'rassk_3')
def rassk1_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad, row_width=1)
    rassk3 = 'https://www.b17.ru/blog/583725/'
    bot.send_message(message.chat.id, "Психотерапевтический рассказ «Ледяное сердце»: \n "+ rassk3,
                   reply_markup=keyboard)

#Ссылка на рассказ ОЖИДАНИЯ
@bot.callback_query_handler(func=lambda call: call.data == 'rassk_4')
def rassk1_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad, row_width=1)
    rassk4 = 'https://www.b17.ru/article/672811/'
    bot.send_message(message.chat.id, "Психотерапевтический рассказ «Ожидания»: \n "+ rassk4,
                   reply_markup=keyboard)

#Ссылка на рассказ ТРИГГЕР
@bot.callback_query_handler(func=lambda call: call.data == 'rassk_5')
def rassk1_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad, row_width=1)
    rassk5 = 'https://www.b17.ru/blog/506497/'
    bot.send_message(message.chat.id, "Психотерапевтический рассказ «Триггер»: \n "+ rassk5,
                   reply_markup=keyboard)

#Ссылка на рассказ КОНТАКТ С ТЕНЕВОЙ СТОРОНОЙ
@bot.callback_query_handler(func=lambda call: call.data == 'rassk_6')
def rassk1_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad, row_width=1)
    rassk6 = 'https://www.b17.ru/article/593286/'
    bot.send_message(message.chat.id, "Психотерапевтический рассказ «Контакт с теневой стороной»: \n "+ rassk6,
                   reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'zapis_data')
def kurs_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad)
    ss1 = 't.me/irina_psyy'
    bot.send_message(message.chat.id, "Чтобы записаться на консультацию, напишите, пожалуйста, мне в личные сообщения: \n "+ ss1,
                   reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data == 'medi_data')
def kurs_btn(call):
    message = call.message
    chat_id = message.chat.id
    keyboard = telebot.types.InlineKeyboardMarkup()
    button_nazad = telebot.types.InlineKeyboardButton(text="Назад",
                                                      callback_data='nazad_data')
    keyboard.add(button_nazad)
    audio1 = 'https://vk.ru/album-221761246_296697148'
    bot.send_message(message.chat.id, "Отзывы можно просмотреть по ссылке: \n "+ audio1,
                   reply_markup=keyboard)



if __name__ == '__main__':
    print('Бот запущен!')
    bot.infinity_polling()
