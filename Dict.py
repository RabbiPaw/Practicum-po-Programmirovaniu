import telebot
import random
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def dictionary(message):
    diction = \
            ["Аваль - Вексельное поручительство, в отношении которого применяется вексельное право. Это поручительство "
             "означает гарантию полного или частичного платежа по тратте, если должник не выполнил в срок свои "
             "обязательства. Аваль дается на лицевой стороне векселя и выражается словами: «Считать за аваль» или "
             "всякой другой аналогичной фразой и подписывается авалистом. "
             "Аваль дается за любое ответственное по векселю лицо, "
             "поэтому авалист должен указать, за кого он дает поручительство. "
             "При отсутствии такого указания аваль считается выданным за векселедателя, т.е. не за должника, "
             "а за кредитора. Авалист и лицо, за которое он поручается, "
             "несут солидарную ответственность. Оплатив вексель, авалист приобретает право обратного требования к "
             "тому, за кого он выдал поручительство, а также к тем, кто обязан перед этим лицом.",
             "Аванс - Денежная сумма, выдаваемая в счет предстоящих платежей за материальные ценности, "
             "выполненные работы и оказанные услуги.",
             "Авизо - В банковской, коммерческой, бухгалтерской практике - извещение, посылаемое одним контрагентом "
             "другому, об изменениях в состоянии взаимных расчетов или о переводе денежных сумм, посылке товаров. "
             "Авизо,как документ, имеет юридический характер.",
             "Активы - Имущество предприятий, в состав которого входят основные средства, другие долгосрочные вложения "
             "(включая  активы), оборотные средства, финансовые активы.",
             "Акцепт - Согласие обязанного лица оплатить платежное требование и таким образом произвести "
             "предусмотренные контрактом расчеты с поставщиком продукции. Акцептная форма расчетов предполагает "
             "предъявление к оплате за поставляемую продукцию платежного требования, выписанного поставщиком товаров.",
             "Акциз - Косвенный налог, включаемый в цену товара и оплачиваемый покупателем. "
             "Законом РФ установлен порядок обложения акцизами реализуемых винно-водочных изделий, этилового спирта и "
             "пищевого сырья (кроме отпускаемого для выработки ликероводочных изделий и винодельческой продукции, "
             "пива, табачных изделий, шин, легковых автомобилей, грузовых автомобилей грузоподъемностью до 1,25 тонн, "
             "ювелирных изделий,бриллиантов, изделий из хрусталя, ковров и ковровых изделий, меховых изделий, "
             "а также одежды из натуральной кожи).",
             "Акции - Ценные бумаги, выпускаемые акционерными обществами и указывающие на долю владельца (держателя) "
             "в капитале данного общества, дающие право их владельцу на получение прибыли в виде дивиденда, а также, "
             "в зависимости от типа, способные давать право голоса на общем собрании акционеров (простая именная). "
             "Этот вид долевых ценных бумаг не выпускается государственными органами, "
             "они эмитируются только промышленными, торговыми и финансовыми корпорациями. "
             "Цена, по которой акция реализуется на рынке, называется курсом акции.",
             "Аудиторская деятельность - Деятельность независимого вневедомственного финансового контроля. "
             "Аудит (независимый финансовый контроль) осуществляют специализированные аудиторские фирмы и службы. "
             "Контрольные и консультационные услуги аудиторские фирмы оказывают всем предприятиям и "
             "организациям на платной основе. Аудиторские фирмы являются независимыми организациями, "
             "призванными способствовать повышению качества контроля, его объективности.",
             "Банки-корреспонденты - Банки, выполняющие на основе корреспондентского договора поручения друг друга по "
             "платежам и расчетам через специально открытые счета или через счета банков корреспондентов в "
             "третьем банке.",
             "Банковская гарантия - Письменное обязательство, даваемое банком или иным кредитным учреждением, "
             "или страховой организацией (гарант) по просьбе другого лица (принципал), "
             "уплатить кредитору принципала (бенефициару) в соответствии с условиями даваемого гарантом обязательства "
             "денежную сумму по представлении бенефициаром письменного требования о ее уплате. "
             "Банковская гарантия обеспечивает надлежащее исполнение принципалом его обязательства перед бенефициаром "
             "(основного обязательства). За выдачу банковской гарантии принципал уплачивает гаранту вознаграждение. "
             "Банковская гарантия вступает в силу со дня ее выдачи, если в гарантии не предусмотрено иное. "
             "Предусмотренное банковской гарантией обязательство гаранта перед бенефициаром не зависит в отношениях "
             "между ними от того основного обязательства, в обеспечение исполнения которого она выдана, "
             "даже если в гарантии содержится ссылка на это обязательство.",
             "Банковский перевод - Поручение одного лица (перевододателя) банку перевести определенную сумму в пользу "
             "другого лица (переводополучателя). Банк, принявший поручение на перевод, выполняет его через своего "
             "корреспондента.",
             "Банкротство - Неспособность должника удовлетворить требования кредиторов по оплате товаров "
             "(работ, услуг), включая неспособность обеспечить обязательные платежи в бюджет и во внебюджетные фонды.",
             "Бартерная сделка - Безвалютный, но оцененный и сбалансированный обмен товарами, "
             "оформляемый единым договором (контрактом).",
             "Безналичные расчеты - Расчеты между организациями, производимые путем перечисления банком суммы со счета "
             "организации должника на счет организации-кредитора по расчетным документам в безналичном порядке. "
             "Платежи могут производиться с согласия (акцепта) плательщика и по его поручению.",
             "Биржа товарная - Коммерческое предприятие, регулярно функционирующий рынок однородных товаров с "
             "определенными характеристиками.",
             "Биржа фондовая - Организованный и регулярно функционирующий рынок по купле-продаже ценных бумаг. "
             "Основными функциями фондовой биржи являются мобилизация временно свободных денежных средств через продажу"
             " ценных бумаг и установление рыночной стоимости ценных бумаг.",
             "Бюджет - Форма образования и расходования фонда денежных средств, предназначенных для финансового "
             "обеспечения задач и функций государства и местного самоуправления; экономическая категория, "
             "представленная денежными отношениями, возникающими у государства с юридическими и физическими лицами по "
             "поводу перераспределения национального дохода в связи с образованием и использованием бюджетного фонда "
             "страны, предназначенного на финансирование народного хозяйства, социально-культурных нужд, "
             "нужд обороны и государственного управления.",
             "Бюджет консолидированный - Свод бюджетов всех уровней бюджетной системы Российской Федерации на "
             "соответствующей территории.",
             "Бюджета дефицит - Превышение расходов бюджета над его доходами.",
             "Бюджета доходы - Денежные средства, поступающие в безвозмездном и безвозвратном порядке в соответствии "
             "с законодательством Российской Федерации в распоряжение органов государственной власти "
             "Российской Федерации, органов государственной власти субъектов Российской Федерации и "
             "органов местного самоуправления.",
             "Бюджета профицит - Превышение доходов бюджета над его расходами.",
             "Оферент - Лицо выступающее с офертой.",
             "Оферта - Формальное предложение определенному лицу заключить сделку с указанием всех необходимых для ее "
             "заключения условий.",
             "Полис - Документ страхового органа подтверждающий наличие заключенной сделки о страховании.",
             "Фьючерс, или фьючерсный контракт - Стандартный договор на поставку товара в будущем по цене, "
             "определенной сторонами при совершении сделки.",
             "Эмиссионное право - Совокупность юридических норм, регулирующих выпуск денег в обращение."]
    bot = telebot.TeleBot(os.getenv('TOKEN'))
    bot.send_message(message.chat.id, random.choice(diction))
