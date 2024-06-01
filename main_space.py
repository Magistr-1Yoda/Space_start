import telebot
from telebot import *
import database_space


def keyboards_create(ListNameBTN, NumberColumns=2):
    keyboards = types.ReplyKeyboardMarkup(
    row_width=NumberColumns, resize_keyboard=True)
    btn_names = [types.KeyboardButton(text=x) for x in ListNameBTN]
    keyboards.add(*btn_names)
    return keyboards

def keyboards_create_posters(list_posters, NumberColumns=3):
    keyboards = types.ReplyKeyboardMarkup(
    row_width=NumberColumns, resize_keyboard=True)
    btn_names = [types.KeyboardButton(text=x) for x in list_posters]
    keyboards.add(*btn_names)
    return keyboards


bot = telebot.TeleBot('TOKEN BOT')


spacefacts = ['Солнце в 300 000 раз больше, чем наша планета Земля', 'Солнце полностью проворачивается вокруг своей оси за 25-35 дней', 'Земля, Марс, Меркурий и Венера также называются «внутренними планетами», так как расположены ближе всего к Солнцу',
'Солнце теряет до 1 000 000 тонн своей массы каждую секунду из-за солнечного ветра', 'Меркурий и Венера уникальны тем, что у них отсутствуют какие-либо спутники', 'На Меркурии нет атмосферы, а значит ветра или какой-либо другой погоды',
'Вeнeрa являeтся eдинствeннoй плaнeтoй, кoтoрaя врaщaeтся в прoтивoпoлoжнyю стoрoнy oтнoситeльнo дрyгих плaнeт Сoлнeчнoй систeмы', 'Ио, спутник Юпитера - самое вулканическое место в солнечной системе',
'С тoчки зрeния Тeoрии oтнoситeльнoсти, пoмимo чёрных дыр, дoлжны сyщeствoвaть и бeлыe дыры, хoтя мы eщё нe oбнaрyжили ни oднoй (сyщeствoвaниe чёрных дыр тaкжe пoдвeргaeтся сoмнeнию)',
'Учениые считают, что создать кротовую нору из "Интерстеллара" возможно', 'Аккреционный диск у черной дыры на самом деле синего цвета', 'Планета, у которой больше всего спутников, это Юпитер с 67 спутниками',
'Так как Сатурн обладает низкой плотностью, то если вы его положите в воду, то он поплывёт!', 'Энцeлaд — этo oдин из сaмых мaлeньких спyтникoв Сaтyрнa. Этoт спyтник oтрaжaeт дo 90% сoлнeчнoгo свeтa, чтo прeвoсхoдит дaжe прoцeнт oтрaжeния свeтa oт снeгa!',
'Уран имеет уникальный наклон, из-за которого одна ночь на нём длится, только представьте, 21 год!', 'Плутон (по англ. Pluto) назван в честь римского бога, а не в честь собаки из Диснея, как полагают некоторые',
'Сейчас в Солнечной системе насчитывается 5 карликовых планет: Церера, Плутон, Хаумеа, Эрида и Макемаке', 'Сoвeтский и рoссийский кoсмoнaвт Сeргeй Кoнстaнтинoвич Крикaлёв являeтся рeкoрдсмeнoм пo врeмeни нaхoждeния в кoсмoсe. Eгo рeкoрд дoстигaeт 803 днeй, 9 чaсoв и 39 минyт, чтo эквивaлeнтнo 2.2 лeт!',
'Тoлькo 24 чeлoвeкa видeли нaшy плaнeтy из кoсмoсa. Нo блaгoдaря прoeктy Google Earth, oстaльныe люди бoлee 500 миллиoнoв рaз скaчaли вид Зeмли из кoсмoсa',
'Световой год — это дистанция, которую свет проходит за один год. Это расстояние равно 95 триллионам километров!', 'Если уменьшить Солнце до размеров бактерии, то галактика Млечный Путь будет размер с США',
'В северной части неба вы можете увидеть две галактики — это галактика Андромеды (М31) и галактика Треугольника (М33)', 'Прямо сейчас к нам приближается галактика Андромеда',
'Сaмaя дaлёкaя гaлaктикa, кoтoрyю нaм yдaлoсь oбнaрyжить, нaзывaeтся GRB 090423, кoтoрaя нaхoдится нa рaсстoянии 13.6 миллиaрдoв свeтoвых лeт! Этo oзнaчaeт, чтo свeт,исхoдящий oт нeё, нaчaл свoё пyтeшeствиe всeгo лишь спyстя 600 000 лeт пoслe oбрaзoвaния Всeлeннoй!',
'В кoсмoсe нaсчитывaeтся пoрядкa 2**1023 звёзд. Гoвoря пo-рyсски, этo числo рaвнo 200 000 000 000 000 000 000 000 000 000!', 'Звёзды типа «красный карлик» имеют самую маленькую массу и могут непрерывно сгорать в течение 10 триллионов лет',
'День на Плутоне длится 6 дней и 9 часов', 'В 1895 году Константин Циолковский, один из первых российских ученых-ракетчиков, первым предложил концепцию космических лифтов, типа космической транспортной системы', 'Если звезда пройдет слишком близко к черной дыре, она может быть разорвана на части',
'Галактика Whirlpool (M51) была первым небесным объектом, идентифицированным как спиральный', 'Галактика Млечный Путь имеет ширину 105 700 световых лет', 'Следы, оставленные на Луне, не исчезнут, пока нет ветра',
'Если на Земле вы весите 60кг, то на Марсе вы будете весить 28кг!', 'Закат на Марсе синего цвета', 'Земля-единственная планета, не названная в честь Бога', 'На самом деле никто не знает почему Землю назвали именно так',
'В космосе звезд больше, чем песчинок в мире', 'Всего в 4 световых годах от нас есть планета, на которой может быть жизнь', 'Только 5% Вселенной видно с Земли', 'В любой момент на Земле происходит не менее 2000 гроз', 'Мы знаем больше о Марсе и нашей Луне, чем о наших океанах',
'Mariner 10 был первым космическим кораблем, который посетил Меркурий в 1974 году', 'Астронавты могут вырасти примерно на два дюйма (5 см) в высоту, когда находятся в космосе', 'Пояс Койпера-это область Солнечной системы за орбитой Нептуна',
'Экзопланеты-это планеты, которые вращаются вокруг других звезд', 'Центр Млечного Пути пахнет ромом и на вкус как малина', 'Наша Луна удаляется от Земли со скоростью 4 см в год!', 'МКС видна более чем 90% населения Земли', 
'Слово “астронавт” означает “звездный моряк” в своем происхождении', 'Красное пятно Юпитера уменьшается', 'Юпитер "защищает" Землю от астероидов, притягивая своей гравитацией большинство астероидов', 'День на Меркурии эквивалентен 58 земным дням',
'Шариковые ручки не работают в космосе, поэтому космонавтам выдают карандаши', 'Уже в 240 году до нашей эры китайцы начали документировать появление кометы Галлея', 'Существует планета, полностью состоящая из алмазов', 'Масса Солнца составляет 99.86% от массы всей Солнечной системы, оставшиеся 0.14% приходятся на планеты и астероиды',
'Большинство тяжелых элементов, содержащихся в вашем организме (таких как кальций, железо и углерод), являются побочными продуктами взрыва группы сверхновых звезд, положившего начало формированию Солнечной системы', 'Официальная научная теория гласит, что человек сможет выжить в открытом космосе без скафандра в течение 90 секунд, если немедленно выдохнет весь воздух из легких',
'Главный претендент на звание обитаемой планеты внесолнечной системы, «Супер-Земля» GJ 667Cc, находится на расстоянии всего 22 световых лет от Земли. Однако путешествие до нее займет у нас 13 878 738 000 лет', '«Космическая юла» под названием нейтронная звезда – это самый быстро крутящийся объект во Вселенной, который делает вокруг своей оси до 500 оборотов в секунду. Помимо этого эти космические тела настолько плотные, что одна столовая ложка составляющего их вещества будет весить ~10 млрд. тонн',
'1 плутонианский год длится 248 земных лет. Это означает, что в то время как Плутон делает всего один полный оборот вокруг Солнца, Земля успевает сделать 248', 'Магнитное поле Юпитера настолько мощное, что ежедневно обогащает магнитное поле нашей планеты миллиардами Ватт', 
'Нашей Солнечной системе требуется 230 миллионов лет, чтобы сделать оборот вокруг Млечного Пути', 'Больше чем на 90% вселенная состоит из темной материи', 'На Юпитере и Сатурне идет алмазный дождь',
'Одна из лун Сатурна имеет форму пельменя, потому что она поглощает некоторые из колец Сатурна', 'Самый большой астероид в Солнечной системе имеет диаметр 525 километров', 'На Земле деревьев больше, чем звезд в Млечном Пути',
'Следы лунной посадки, вероятно, все еще будут видны через миллионы лет']

def welcome_message(message):
    id = message.chat.id
    score = db.check_profile(id)
    db.delete_correct(id)
    if score[1] == 0:
        bot.send_message(message.from_user.id,f'○★~Привет из космоса для всех любителей необъятной вселенной!!! Жаждите новой информации? Хотите проверить свой уровень знаний? Тогда, не будем томить : "поехали!"~★○', reply_markup=keyboards_create([ "📚Викторина!" , '👀 Факт о космосе!', '🚀 Цитаты космонавтов' , '🌌 Космические постеры', '🔥 Мультисериал', '🔮Будущее или 🌏Реальность']))
        db.visit(id)
        bot.register_next_step_handler(message, check_choice)
    else:
        bot.send_message(message.from_user.id,f'Вы вернулись в главное меню, здесь вы можете посмотреть другие разделы🔎', reply_markup=keyboards_create([ "📚Викторина!" , '👀 Факт о космосе!', '🚀 Цитаты космонавтов' , '🌌 Космические постеры', '🔥 Мультисериал', '🔮Будущее или 🌏Реальность']))
        bot.register_next_step_handler(message, check_choice)

@bot.message_handler(commands=['start'])
def start(message):
    nic =  message.from_user.username
    id = message.chat.id
    new = db.check_human(id)
    if new is not None:
        welcome_message(message)
    elif new is None:
        list_names_surnames = []
        list_names_surnames.append(nic)
        bot.send_message(message.from_user.id, "Вы начали регестрацию💭 \nВведите своё имя:")
        bot.register_next_step_handler(message, names, list_names_surnames)

def check_choice(message):
    choice = message.text
    if choice == "📚Викторина!":
        viktorina1(message)
    elif choice == '👀 Факт о космосе!':
        fact(message)
    elif choice == '🌌 Космические постеры':
        choice_posters(message, choice)
    elif choice == '🚀 Цитаты космонавтов':
        choice_quote(message, choice)
    elif choice == '🔥 Мультисериал':
        choice_series(message, choice)
    elif choice == '🔮Будущее или 🌏Реальность':
        predict1(message)




def names(message, list_names_surnames):
    names = message.text.strip()
    list_names_surnames.append(names)
    bot.send_message(message.from_user.id, "Введите свою фамилию:")
    bot.register_next_step_handler(message, surnames, list_names_surnames)

def surnames(message, list_names_surnames):
    surnames = message.text.strip()
    list_names_surnames.append(surnames)
    db.new_human(message.chat.id, list_names_surnames)
    welcome_message(message)


def viktorina1(message):
    msg = bot.send_message(message.chat.id, "В викторине будет 9 вопросов, время не ограничено, вы готовы?🏁✨", reply_markup=keyboards_create(['Главное меню🔙', 'Начать▶']))
    bot.register_next_step_handler(msg, viktorina2)
def viktorina2(message):
    list_nub = [1,2,3,4,5,6,7,8,9]
    if message.text == 'Начать▶':
        if message.text:
            send_question(message, list_nub)
    elif message.text == 'Главное меню🔙':
        welcome_message(message)

def send_question(message, list_nub):
    if len(list_nub) != 0:
        random_number = random.choice(list_nub)
        if random_number in list_nub:
            id = message.chat.id
            data = db.start_viktorina(id, random_number)
            question = data[1]

            keyboards = types.ReplyKeyboardMarkup(resize_keyboard=True)
            buttons = [types.KeyboardButton(str(i)) for i in range(1, 4)]
            keyboards.add(*buttons)

            bot.send_message(
                id,
                f'{question[1]}\n1. {question[2]}\n2. {question[3]}\n3. {question[4]}'
                ,reply_markup=keyboards
            )
        
            bot.register_next_step_handler(message, check_answer, id, data, list_nub, random_number)
    elif len(list_nub) == 0:
        id = message.chat.id
        score = db.check_profile(id)
        correct_otvet = f'{score[2]*10} баллов'
        bot.send_message(message.chat.id,f'Вопросы кончились☹️\nЗа эту попытку вы получили: {correct_otvet}\nВаше общее количество баллов: {score[0]}')
        welcome_message(message)
        db.delete_correct(id)
        

def check_answer(message, id, data, list_nub, random_number ):
    try:
        answer = int(message.text)
        current_question = data[0]

        correct_option = current_question[id]['otvet']
        if answer == correct_option:
            number = "score=score+10"
            bot.send_message(id, 'Верно, вы получили 10 баллов за этот вопрос!🥳')
            list_nub.remove(random_number)
            db.score(id, number)
            send_question(message, list_nub)
        else:
            bot.send_message(id, 'Неверно🔥')
            list_nub.remove(random_number)
            send_question(message, list_nub)

            
    except ValueError:
        bot.send_message(id, 'Пожалуйста, введите номер ответа')
        send_question(message, list_nub)


def fact(message):
    for i in range(1):
        bot.send_message(message.from_user.id, random.choice(spacefacts), reply_markup=keyboards_create([ "📚Викторина!" , '👀 Факт о космосе!', '🚀 Цитаты космонавтов' , '🌌 Космические постеры', '🔥 Мультисериал', '🔮Будущее или 🌏Реальность']))
        bot.register_next_step_handler(message, check_choice )

def choice_posters(message, choice):
    list_posters_back = ['1 Постер','2 Постер','3 Постер','4 Постер','5 Постер','6 Постер', 'Главное меню🔙']
    bot.send_message(message.from_user.id, '⬇ Выберите интересующий вас постер', reply_markup=keyboards_create_posters(list_posters_back))
    bot.register_next_step_handler(message, check_poster, list_posters_back, choice)
def check_poster(message, list_posters_back, choice):
    variant = message.text
    list_posters = ['1 Постер','2 Постер','3 Постер','4 Постер','5 Постер','6 Постер']
    if variant in list_posters:
        link = db.start_section(choice, variant)
        bot.send_message(message.from_user.id, f'Ваш раздел: {link[0]}\n \n👍🏻 Отличный выбор\n \n📲 Посмотреть постер можно по ссылки🌐 или снизу по фотографии👇🏻 {link[1]}', reply_markup=keyboards_create_posters(list_posters_back))
        bot.register_next_step_handler(message, check_poster, list_posters_back, choice)
    else:
        welcome_message(message)



def choice_quote(message, choice):
    list_quote_back = ['🔙 Главное меню','🔎 Цитата Юрия Гагарина','🔎 Цитата Глушко Валентина','🔎 Цитата Джанибекова Владимира','🔎 Цитата Королёва Сергея','🔎 Цитата Криколёва Сергея',
        '🔎 Цитата Леонова Алексея','🔎 Цитата Севастьянова Виталия','🔎 Цитата Терешковой Валентины','🔎 Цитата Титова Германа','🔎 Цитата Уточкина Сергея','🔎 Цитата Фёдорова Николая',
        '🔎 Цитата Цилковского Константина','🔎 Цитата Челомия Владимира','🔎 Цитата Чертока Бориса','🔎 Цитата Юрчихина Фёдора',]
    bot.send_message(message.from_user.id, '⬇ Выберите интересующего вас цитату космонавта', reply_markup=keyboards_create(list_quote_back))
    bot.register_next_step_handler(message, check_quote, list_quote_back, choice)

def check_quote(message, list_quote_back, choice):
    variant = message.text
    list_quote = ['🔎 Цитата Юрия Гагарина','🔎 Цитата Глушко Валентина','🔎 Цитата Джанибекова Владимира','🔎 Цитата Королёва Сергея','🔎 Цитата Криколёва Сергея','🔎 Цитата Леонова Алексея',
        '🔎 Цитата Севастьянова Виталия','🔎 Цитата Терешковой Валентины','🔎 Цитата Титова Германа','🔎 Цитата Уточкина Сергея','🔎 Цитата Фёдорова Николая','🔎 Цитата Цилковского Константина',
        '🔎 Цитата Челомия Владимира','🔎 Цитата Чертока Бориса','🔎 Цитата Юрчихина Фёдора',]
    if variant in list_quote:
        link = db.start_section(choice, variant)
        bot.send_message(message.from_user.id, f'Вы выбрали {link[0]}\n \n👍🏻 Отличный выбор\n \n📲 Прочитать цитату и посмотреть на этого космонавта можно по смылки🌐 или снизу по фотографии👇🏻 {link[1]}', reply_markup=keyboards_create(list_quote_back))
        bot.register_next_step_handler(message, check_quote, list_quote_back, choice)
    else:
        welcome_message(message)

def choice_series(message, choice):
    list_series_back = ['🔙 Главное меню','1 серия🎬🍿','2 серия🎬🍿','3 серия🎬🍿','4 серия🎬🍿']
    bot.send_message(message.from_user.id, '⬇ Выберите серию которую вы желаете посмотреть', reply_markup=keyboards_create_posters(list_series_back))
    bot.register_next_step_handler(message, check_series, list_series_back, choice)

def check_series(message, list_series_back, choice):
    variant = message.text
    list_series = ['1 серия🎬🍿','2 серия🎬🍿','3 серия🎬🍿','4 серия🎬🍿']
    if variant in list_series:
        link = db.start_section(choice, variant)
        bot.send_message(message.from_user.id, f'Вы выбрали {link[0]}\n \n👍🏻 Отличный выбор\n \n📲 Посмотреть эту серию можно по ссылке🌐👇🏻\n{link[1]}', reply_markup=keyboards_create(list_series_back))
        bot.register_next_step_handler(message, check_series, list_series_back, choice)
    else:
        welcome_message(message)


def predict1(message):
    msg = bot.send_message(message.chat.id, "Игра '🔮Будущее или 🌏Реальность'. \nСмысл в том, чтобы угадать, действительно ли событие уже случилось, или ещё нет. Это не всегда будет просто, но тем интереснее🤔💭. За каждый правильный ответ вы будете получать 5 Баллов.\nГотовы проверить свою интуицию?🏁✨", 
    reply_markup=keyboards_create(['Главное меню🔙', 'Начать▶']))
    bot.register_next_step_handler(msg, predict2)


def predict2(message):
    list_nub = [1,2,3,4,5,6,7,8,9]
    if message.text == 'Начать▶':
        if message.text:
            choice_predict(message, list_nub)
    elif message.text == 'Главное меню🔙':
        welcome_message(message)

def choice_predict(message, list_nub):
    if len(list_nub) != 0:
        random_number = random.choice(list_nub)
        if random_number in list_nub:
            list_variant = ['Будущее 🔮📝', 'Реальность 🌏✨']
            id = message.chat.id
            data = db.start_predict(random_number)
            bot.send_message(message.from_user.id, data[1], reply_markup=keyboards_create(list_variant))
            bot.register_next_step_handler(message, check_predict, id, data, list_nub, random_number) 
    elif len(list_nub) == 0:
        id = message.chat.id
        score = db.check_profile(id)
        correct_otvet = f'{score[2]*5} баллов'
        bot.send_message(message.chat.id,f'Игра окончена\nЗа эту попытку вы получили: {correct_otvet}\nВаше общее количество баллов: {score[0]}')
        welcome_message(message)
        db.delete_correct(id)

def check_predict(message, id, data, list_nub, random_number):
    try:
        user_otvet = str(message.text)
        text_otvet = data[2]
        otvet = data[3]

        if user_otvet == otvet:
            number = "score=score+5"
            bot.send_message(id, f'Верно, вы получили 5 баллов🥳\n💡Объяснение: {text_otvet}' )
            list_nub.remove(random_number)
            db.score(id, number)
            choice_predict(message, list_nub)
        else:
            bot.send_message(id, f'Неверно🔥 \n💡Объяснение: {text_otvet}')
            list_nub.remove(random_number)
            choice_predict(message, list_nub)
            
    except ValueError:
        bot.send_message(id, 'Такого варианта ответа нету')
        choice_predict(message, list_nub)
if __name__ == '__main__':
    db = database_space.Database()
    bot.infinity_polling()