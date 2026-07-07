# -*- coding: utf-8 -*-
"""
Генератор сайта bau — ремонт квартир под ключ, г. Астана.
Версия 2: без Tailwind CDN. Весь CSS зашит в страницу с @media-запросами,
поэтому адаптивность работает всегда, даже офлайн. Self-contained.
Запуск:  python3 build.py
"""
import urllib.parse

PHONE_HUMAN = "+7 747 647 8605"
PHONE_TEL   = "+77476478605"
WA_NUMBER   = "77476478605"
SITE        = "bau"
DOMAIN      = "https://bau.kz/"            # placeholder — заменить на реальный домен
CITY        = "Астана"
ANUKEN_WA   = "77074534518"

WA_TEXT = urllib.parse.quote(
    "Здравствуйте! Пишу с сайта bau, хочу получить консультацию по ремонту квартиры под ключ."
)
def wa(text=None):
    t = WA_TEXT if text is None else urllib.parse.quote(text)
    return f"https://wa.me/{WA_NUMBER}?text={t}"

SERVICES = [
    ("remont-pod-klyuch", "Ремонт под ключ", "Ремонт квартир под ключ",
     "Полный цикл ремонта от демонтажа до чистовой отделки и уборки. Вы получаете готовую квартиру и один договор с фиксированной сметой.",
     ["Демонтаж и вывоз строительного мусора","Электромонтажные и сантехнические работы",
      "Штукатурка стен и стяжка пола под маяк","Натяжные потолки и конструкции из ГКЛ",
      "Укладка плитки, керамогранита и ламината","Обои или покраска, установка дверей и плинтусов",
      "Финишная уборка и сдача под заселение"],
     ["«Ремонт под ключ» — это одна бригада, одна смета и один ответственный за результат. Мы берём на себя весь процесс: замер, проект, закупку материалов, черновые и чистовые работы, а вы въезжаете в готовую квартиру.",
      "Каждый этап фиксируется в смете, стоимость не меняется в процессе без вашего согласия. Скрытые работы — электрику, разводку воды, гидроизоляцию — фотографируем до того, как их закроют отделкой.",
      "Работаем по квартирам в новостройках и на вторичном рынке Астаны. Подбираем решение под бюджет: от аккуратного бюджетного ремонта до дизайнерского уровня."]),

    ("chernovoy-remont", "Черновой ремонт", "Черновой ремонт квартиры",
     "Подготовка квартиры под чистовую отделку: коммуникации, стены, полы и потолки выведены в ноль под финиш.",
     ["Демонтаж старых покрытий и перегородок","Разводка электрики и слаботочки","Разводка водоснабжения и канализации",
      "Штукатурка стен под маяк","Стяжка или наливной пол под маяк","Гидроизоляция мокрых зон"],
     ["Черновой ремонт — фундамент всего последующего результата. Кривые стены и полы, ошибки в разводке коммуникаций потом невозможно спрятать за обоями, поэтому этот этап мы делаем особенно тщательно.",
      "Стены выводим под маяк с проверкой правилом, стяжку заливаем в уровень по всей квартире, электрику и сантехнику разводим по согласованному плану розеток и точек воды.",
      "После чернового этапа квартира полностью готова к чистовой отделке — без переделок и сюрпризов."]),

    ("chistovoy-remont", "Чистовой ремонт", "Чистовая отделка квартиры",
     "Финишная отделка, после которой квартира готова к заселению: стены, потолки, полы, двери и декор.",
     ["Шпаклёвка и шкурка стен под лампу LOSSEW","Обои или покраска стен","Натяжные потолки и потолки из ГКЛ",
      "Укладка ламината и плитки","Установка межкомнатных дверей","Монтаж плинтусов и декоративных элементов"],
     ["Чистовая отделка — это то, что вы видите каждый день. Здесь важна аккуратность в мелочах: ровные швы, стыки без зазоров, углы плитки, запиленные под 45 градусов.",
      "Стены перед покраской и оклейкой шпаклюем и шкурим под лампу LOSSEW — боковой свет выявляет любые неровности, которые обычная лампа не покажет.",
      "Результат принимаем вместе с вами при дневном и искусственном освещении, устраняем замечания до подписания акта."]),

    ("dizaynerskiy-remont", "Дизайнерский ремонт", "Дизайнерский ремонт квартиры",
     "Ремонт по авторскому дизайн-проекту: сложные потолки, свет, декоративные покрытия и индивидуальные решения.",
     ["Реализация по готовому дизайн-проекту","Многоуровневые потолки и скрытая подсветка","Декоративная штукатурка и покраска",
      "Сложная укладка плитки и керамогранита","Монтаж декоративных элементов и молдингов","Подбор и установка света под сценарии"],
     ["Дизайнерский ремонт — это точная реализация проекта дизайнера с сохранением всех деталей: раскладки плитки, световых сценариев, фактур и стыков материалов.",
      "Мы читаем чертежи и развёртки, соблюдаем размеры до сантиметра и согласовываем узлы, где разные материалы встречаются друг с другом.",
      "Если проекта пока нет — подскажем проверенных дизайнеров или предложим готовые решения под ваш вкус и бюджет."]),

    ("remont-sanuzla", "Ремонт санузла", "Ремонт ванной и санузла",
     "Ремонт ванной и туалета под ключ: гидроизоляция, разводка, плитка и сантехника. Мокрые зоны — наша ответственность.",
     ["Демонтаж и вывоз мусора","Гидроизоляция мокрых зон","Разводка воды и канализации","Укладка керамогранита на стену и пол",
      "Запил углов плитки под 45 градусов","Установка сантехники и полотенцесушителя"],
     ["Санузел — самая ответственная зона в квартире. Ошибка в гидроизоляции или уклоне слива обернётся протечкой к соседям, поэтому эти работы мы делаем по технологии и проверяем.",
      "Плитку и керамогранит укладываем с ровными швами, наружные углы запиливаем под 45 градусов — без пластиковых уголков, аккуратно и дорого на вид.",
      "Подключаем и проверяем всю сантехнику, сдаём санузел готовым к использованию."]),

    ("remont-kuhni", "Ремонт кухни", "Ремонт кухни под ключ",
     "Ремонт кухни с учётом будущего гарнитура: розетки, вода, фартук и подключение техники — всё по месту.",
     ["Разводка розеток под технику и гарнитур","Вывод воды и канализации под мойку","Выравнивание стен и пола",
      "Укладка плитки-фартука","Подключение вытяжки и техники","Финишная отделка и плинтус"],
     ["Кухня требует продуманной подготовки: розетки под технику, вывод воды, вентиляция под вытяжку должны совпасть с будущим гарнитуром до сантиметра.",
      "Мы работаем с вашим проектом кухни или замерами от кухонной компании, чтобы фартук, розетки и коммуникации встали ровно там, где нужно.",
      "После укладки фартука и отделки подключаем технику и сдаём кухню готовой к монтажу гарнитура."]),

    ("elektromontazh", "Электромонтажные работы", "Электромонтаж в квартире",
     "Полная замена и разводка электрики: щиток, кабель, розетки и освещение под ваш план расстановки.",
     ["Сборка и монтаж электрощита","Штробление и прокладка кабеля","Увеличение количества розеток и точек света",
      "Установка розеток, выключателей, автоматов","Монтаж подсветки и групп освещения","Проверка и запуск линий"],
     ["Электрика — это безопасность квартиры на годы вперёд. Мы разводим линии с запасом по нагрузке, ставим отдельные автоматы на мощные группы и собираем щит аккуратно и понятно.",
      "Расположение розеток и выключателей согласовываем по плану мебели — чтобы не тянуть удлинители после ремонта. Увеличиваем количество точек освещения там, где это нужно.",
      "Все линии проверяем под нагрузкой и подписываем схему щита, чтобы вы всегда знали, что за что отвечает."]),

    ("santehnika", "Сантехнические работы", "Сантехнические работы",
     "Разводка воды и канализации, установка приборов и защита от протечек в мокрых зонах.",
     ["Разводка водоснабжения","Монтаж канализации с уклоном","Гидроизоляция мокрых зон","Установка смесителей и приборов",
      "Шумоизоляция стока и канализационных труб","Опрессовка и проверка на протечки"],
     ["Скрытая разводка воды и канализации закрывается стяжкой и плиткой, поэтому переделать её потом дорого. Мы монтируем трубы по технологии, с проверкой давлением до закрытия.",
      "Канализацию выводим с правильным уклоном, стояки и стоки шумоизолируем, чтобы не слышать соседей сверху.",
      "Устанавливаем и подключаем сантехприборы, проверяем каждое соединение на протечку перед сдачей."]),

    ("shtukaturka", "Штукатурка и стяжка", "Штукатурка стен и стяжка пола",
     "Выравнивание стен под маяк и заливка пола в уровень — основа ровной чистовой отделки.",
     ["Установка маяков","Штукатурка стен под правило","Заливка наливного пола под маяк","Стяжка пола в уровень",
      "Проверка геометрии углов","Подготовка под плитку, ламинат и обои"],
     ["Ровные стены и пол — это то, на чём держится вся чистовая отделка. Мы штукатурим стены по маякам с контролем правилом и выводим углы в 90 градусов.",
      "Пол заливаем наливной смесью или стяжкой в единый уровень по всей квартире, чтобы ламинат и плитка легли без перепадов.",
      "Основание проверяем на ровность перед следующим этапом — так финишные материалы ложатся идеально."]),

    ("natyazhnye-potolki", "Натяжные потолки", "Натяжные потолки",
     "Матовые, сатиновые и тканевые потолки с точным монтажом света и обходом коммуникаций.",
     ["Замер и раскрой полотна","Монтаж багета и профиля","Установка матовых или сатиновых полотен","Обвод точек света и люстр",
      "Скрытая подсветка и парящие потолки","Обход труб и коммуникаций"],
     ["Натяжной потолок скрывает неровности плиты и коммуникации, а монтируется за один день без пыли. Мы точно размечаем точки света и вырезаем отверстия по месту.",
      "Предлагаем матовые, сатиновые и тканевые полотна, а также сложные решения — многоуровневые и парящие потолки со скрытой подсветкой.",
      "Работаем аккуратно на финишном этапе, когда стены уже готовы, чтобы не повредить отделку."]),

    ("ukladka-plitki", "Укладка плитки", "Укладка плитки и керамогранита",
     "Плитка и керамогранит на пол и стены с ровными швами и запилом углов под 45 градусов.",
     ["Подготовка и грунтовка основания","Раскладка плитки по проекту","Укладка керамогранита на стену и пол",
      "Запил углов плитки под 45 градусов","Затирка швов в тон","Монтаж декоративных вставок"],
     ["Плитка проверяет мастера на аккуратность: ровные швы, совпадение рисунка и чистые углы отличают хорошую работу от посредственной.",
      "Наружные углы запиливаем под 45 градусов вместо пластиковых уголков — это выглядит аккуратно и дорого. Раскладку согласовываем заранее, чтобы подрезка ушла в незаметные места.",
      "Работаем с крупноформатным керамогранитом, мозаикой и декором, затирку подбираем в тон плитке."]),

    ("malyarnye-raboty", "Малярные работы", "Малярные и отделочные работы",
     "Шпаклёвка, покраска и оклейка стен с подготовкой под лампу LOSSEW для идеально ровной поверхности.",
     ["Грунтовка и шпаклёвка стен","Шкурка под лампу LOSSEW","Покраска стен и потолков","Оклейка обоями",
      "Покраска и монтаж декоративных элементов","Финишная защита поверхностей"],
     ["Под покраску и светлые обои важна идеально ровная стена — любая волна или бугорок будут видны при боковом свете. Поэтому мы шпаклюем и шкурим поверхность под лампу LOSSEW.",
      "Краску наносим в несколько слоёв с промежуточной шлифовкой, обои клеим со стыковкой рисунка и без пузырей.",
      "Декоративные элементы — молдинги, плинтусы, карнизы — красим и монтируем аккуратно, в один тон с отделкой."]),
]
SVC_NAME = dict((s[0], s[1]) for s in SERVICES)
NAV_MAIN = ["remont-pod-klyuch","chernovoy-remont","chistovoy-remont","remont-sanuzla","remont-kuhni","elektromontazh"]

PACKAGE = [
    "Электромонтажные работы","Сантехнические работы","Заливка наливного пола под маяк","Штукатурка стен под маяк",
    "Натяжные потолки","Увеличение количества точек освещения и розеток","Обои или покраска стен",
    "Конструкция потолка из ГКЛ","Укладка ламината","Установка плинтуса","Гидроизоляция мокрых зон",
    "Укладка керамогранита на стену и на пол с/у","Монтаж декоративных элементов","Запил углов плитки под 45 градусов",
    "Установка межкомнатных дверей","Перепланировка квартиры","Шпаклёвка и шкурка стен под лампу LOSSEW",
    "Шумоизоляция стока и канализационных труб",
]

WHY_ITEMS = [
    ('<path d="M12 3l7 3v5c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/>',"Договор и фиксированная смета","Стоимость и объём работ фиксируем в договоре до начала. В процессе ремонта цена не растёт без вашего согласия."),
    ('<path d="M3 20h18M5 20V9l5 3V9l5 3V9l4 2v9"/>',"Своя бригада мастеров","Работают штатные электрики, сантехники и отделочники со стажем. Без субподрядов и случайных людей на объекте."),
    ('<rect x="5" y="3" width="14" height="18"/><path d="M8 7h8M8 11h3M13 11h3M8 15h3M13 15h3"/>',"Прозрачные этапы","Каждый этап принимаете вы. Скрытые работы — электрику и сантехнику — фотографируем до закрытия отделкой."),
    ('<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>',"Материалы по себестоимости","Закупаем материалы по оптовым ценам и показываем чеки. Не зарабатываем на скрытых наценках."),
    ('<path d="M4 4h16v16H4z"/><path d="M8 8h8M8 12h8M8 16h5"/>',"Работаем по графику","Составляем план-график с датами по этапам и придерживаемся сроков. Вы всегда знаете, что делается сейчас."),
    ('<circle cx="12" cy="8" r="3.2"/><path d="M5 20a7 7 0 0114 0"/>',"Чистота и порядок","Выносим мусор, защищаем чистовые поверхности, убираем за собой. Сдаём квартиру готовой к заселению."),
]

CSS = """
:root{--navy:#214357;--ink2:#1B3A4B;--sub:#566670;--accent:#CFA384;--accenth:#BE9070;--soft:#F8F0EB;--cream:#F5EDE3;--line:#E7DED3}
*,*::before,*::after{box-sizing:border-box}*{margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Manrope',sans-serif;color:var(--navy);background:#fff;line-height:1.5;-webkit-font-smoothing:antialiased}
img{max-width:100%;height:auto;display:block}
a{color:inherit;text-decoration:none}
ul{list-style:none}
.wrap{max-width:1200px;margin:0 auto;padding:0 20px}
.up{text-transform:uppercase;letter-spacing:.045em}
.accent{color:var(--accent)}
.center{text-align:center}
.s-navy{background:var(--navy)}.s-soft{background:var(--soft)}.s-white{background:#fff}
.sec{padding:64px 0}
@media(min-width:768px){.sec{padding:80px 0}}
.h1{color:#fff;font-weight:800;font-size:30px;line-height:1.12;text-transform:uppercase;letter-spacing:.045em}
@media(min-width:768px){.h1{font-size:48px;margin-top:40px}}
.h2{font-weight:800;text-transform:uppercase;letter-spacing:.045em;font-size:24px;line-height:1.15;color:var(--navy)}
@media(min-width:768px){.h2{font-size:32px}}
.h2-lg{font-size:24px}
@media(min-width:768px){.h2-lg{font-size:40px}}
.h2-white{color:#fff}
.lead{color:rgba(255,255,255,.8);font-size:16px;line-height:1.6;max-width:640px}
@media(min-width:768px){.lead{font-size:18px}}
.sub{color:var(--sub)}
.btn,.btn-o{display:inline-flex;align-items:center;justify-content:center;gap:8px;font-weight:700;border-radius:0;cursor:pointer;text-align:center;transition:all .2s;font-size:15px;font-family:inherit}
.btn{background:var(--accent);color:#fff;padding:15px 30px;border:0}
.btn:hover{background:var(--accenth)}
.btn-o{border:1px solid var(--navy);color:var(--navy);padding:14px 29px;background:transparent}
.btn-o:hover{background:var(--navy);color:#fff}
.btn-w{border-color:#fff;color:#fff}
.btn-w:hover{background:#fff;color:var(--navy)}
.btn-full{width:100%}
.header{position:sticky;top:0;z-index:50;background:var(--navy);border-bottom:1px solid rgba(255,255,255,.1)}
.header-in{display:flex;align-items:center;justify-content:space-between;height:60px}
@media(min-width:768px){.header-in{height:72px}}
.logo{height:40px;width:auto;display:block;border:0}
@media(min-width:768px){.logo{height:44px}}
.nav{display:none;align-items:center;gap:20px}
.nav-a{font-weight:600;font-size:13.5px;letter-spacing:.02em;color:#fff;transition:color .2s;white-space:nowrap}
.nav-a:hover{color:var(--accent)}
.header-cta{display:none;align-items:center;gap:16px;padding-left:20px;border-left:1px solid rgba(255,255,255,.15)}
.header-phone{font-weight:600;font-size:13.5px;color:#fff;white-space:nowrap}
.header-phone:hover{color:var(--accent)}
.btn-head{background:var(--accent);color:#fff;padding:10px 20px;font-weight:700;font-size:14px;white-space:nowrap;transition:background .2s}
.btn-head:hover{background:var(--accenth)}
.burger{background:none;border:0;padding:8px;margin-right:-8px;cursor:pointer;line-height:0}
@media(min-width:1024px){.nav{display:flex}.header-cta{display:flex}.burger{display:none}}
.overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:50;display:none}
.overlay.open{display:block}
.menu{position:fixed;top:0;right:0;height:100%;width:86%;max-width:360px;background:var(--navy);z-index:51;transform:translateX(100%);transition:transform .25s ease;overflow-y:auto;box-shadow:0 0 40px rgba(0,0,0,.4)}
.menu.open{transform:translateX(0)}
.menu-head{display:flex;align-items:center;justify-content:space-between;height:60px;padding:0 20px;border-bottom:1px solid rgba(255,255,255,.1)}
.menu-nav{padding:0 20px 24px}
.mlink{display:block;padding:12px 0;border-bottom:1px solid rgba(255,255,255,.1);font-size:16px;font-weight:600;color:#fff}
.menu-foot{margin-top:20px;display:flex;flex-direction:column;gap:12px}
.menu-phone{display:block;font-size:18px;font-weight:700;color:#fff}
.close{background:none;border:0;padding:8px;margin-right:-8px;cursor:pointer;line-height:0}
@media(min-width:1024px){.menu,.overlay{display:none!important}}
.hero-img{display:none;position:relative;background:var(--ink2);border:1px solid rgba(255,255,255,.08);aspect-ratio:21/8;overflow:hidden}
@media(min-width:768px){.hero-img{display:block}}
.hero-img img{width:100%;height:100%;object-fit:cover}
.hero-top{padding:32px 0 48px}
@media(min-width:768px){.hero-top{padding:40px 0 64px}}
.hero-row{margin-top:24px;display:flex;flex-direction:column;gap:20px}
@media(min-width:768px){.hero-row{flex-direction:row;align-items:center;gap:32px}}
.hero-btn{width:100%}
@media(min-width:768px){.hero-btn{width:auto}}
.grid-features{display:grid;gap:24px;margin-top:40px;grid-template-columns:1fr}
@media(min-width:640px){.grid-features{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1024px){.grid-features{grid-template-columns:repeat(4,1fr)}}
.feat{display:flex;align-items:center;gap:12px}
.feat-ic{flex-shrink:0;width:44px;height:44px;border-radius:999px;border:1px solid rgba(255,255,255,.4);display:flex;align-items:center;justify-content:center;color:#fff}
.feat-t{color:#fff;font-weight:700;font-size:14px;line-height:1.2}
.feat-s{color:rgba(255,255,255,.6);font-size:14px}
.quiz-box{max-width:768px;margin:0 auto;background:var(--navy);padding:24px}
@media(min-width:768px){.quiz-box{padding:40px}}
.qbar-track{height:4px;background:rgba(255,255,255,.15);margin-bottom:24px}
.qbar{height:4px;background:var(--accent);width:25%}
.qtitle{color:#fff;font-weight:700;text-transform:uppercase;letter-spacing:.045em;font-size:18px;margin-bottom:24px}
@media(min-width:768px){.qtitle{font-size:20px}}
.qopts{display:grid;grid-template-columns:1fr;gap:16px}
@media(min-width:768px){.qopts{grid-template-columns:repeat(2,1fr);gap:16px 32px}}
.qopt{display:flex;align-items:center;gap:12px;text-align:left;color:rgba(255,255,255,.9);padding:4px 0;background:none;border:0;cursor:pointer;font-family:inherit;font-size:15px;width:100%}
.qradio{flex-shrink:0;width:20px;height:20px;border-radius:999px;border:2px solid rgba(255,255,255,.4);display:flex;align-items:center;justify-content:center}
.qradio.sel{border-color:var(--accent)}
.qdot{width:10px;height:10px;border-radius:999px;background:var(--accent)}
.qopt.sel .qtext{color:#fff}
.qinputs{display:grid;grid-template-columns:1fr;gap:12px;margin-bottom:16px}
@media(min-width:768px){.qinputs{grid-template-columns:repeat(2,1fr)}}
.qinput{width:100%;padding:12px 16px;background:#fff;color:var(--navy);border:0;outline:none;border-radius:0;font-family:inherit;font-size:15px}
.qfoot{display:flex;align-items:center;justify-content:space-between;margin-top:32px}
.qback{text-transform:uppercase;letter-spacing:.045em;font-size:14px;font-weight:700;padding:12px 24px;background:rgba(255,255,255,.1);color:rgba(255,255,255,.7);border:0;cursor:pointer;transition:background .2s}
.qback:hover{background:rgba(255,255,255,.15)}
.hidden{display:none}
.grid-why{display:grid;gap:20px;grid-template-columns:1fr}
@media(min-width:768px){.grid-why{grid-template-columns:repeat(3,1fr);gap:24px}}
.why-card{background:var(--cream);padding:24px}
@media(min-width:768px){.why-card{padding:28px}}
.why-ic{width:48px;height:48px;border-radius:999px;background:var(--navy);display:flex;align-items:center;justify-content:center;color:#fff;margin-bottom:16px}
.why-t{font-weight:800;text-transform:uppercase;letter-spacing:.045em;color:var(--navy);font-size:14px;margin-bottom:8px;line-height:1.3}
.why-p{color:var(--sub);font-size:14px;line-height:1.6}
.actions{margin-top:48px;display:flex;flex-direction:column;align-items:center;gap:16px}
@media(min-width:640px){.actions{flex-direction:row;justify-content:center}}
.grid-package{display:grid;grid-template-columns:1fr;gap:2px 40px;max-width:900px;margin:0 auto}
@media(min-width:768px){.grid-package{grid-template-columns:repeat(2,1fr)}}
.pkg-item{display:flex;align-items:flex-start;gap:12px;padding:8px 0}
.pkg-dot{margin-top:4px;flex-shrink:0;width:14px;height:14px;background:var(--accent);transform:rotate(45deg)}
.pkg-t{color:rgba(255,255,255,.9);font-size:14px;font-weight:600;text-transform:uppercase;letter-spacing:.045em;line-height:1.3}
.svc-intro{color:var(--sub);margin-bottom:32px;max-width:640px}
.grid-services{display:grid;gap:20px;grid-template-columns:1fr}
@media(min-width:640px){.grid-services{grid-template-columns:repeat(2,1fr)}}
@media(min-width:1024px){.grid-services{grid-template-columns:repeat(3,1fr);gap:24px}}
.card{display:block;background:var(--cream);border:1px solid var(--line);transition:transform .2s,box-shadow .2s}
.card:hover{box-shadow:0 12px 34px rgba(33,67,87,.12);transform:translateY(-2px)}
.ph{position:relative;background:#EADFCF;overflow:hidden}
.ph .lbl{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;color:#A99A82;font-size:12px;text-align:center;padding:10px;line-height:1.4}
.ph img{position:relative;z-index:1;width:100%;height:100%;object-fit:cover}
.r43{aspect-ratio:4/3}
.card-body{padding:20px;display:flex;align-items:center;justify-content:space-between;gap:10px}
.card-t{font-weight:700;font-size:16px;line-height:1.2;text-transform:uppercase;letter-spacing:.045em;color:var(--navy)}
.pf-head{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:32px;gap:16px}
.pf-all{display:none;align-items:center;gap:6px;color:var(--navy);font-weight:600;font-size:13.5px;text-transform:uppercase;letter-spacing:.02em}
.pf-all:hover{color:var(--accent)}
@media(min-width:640px){.pf-all{display:inline-flex}}
.grid-portfolio{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
@media(min-width:768px){.grid-portfolio{grid-template-columns:repeat(3,1fr)}}
.pf-mob{margin-top:32px}
@media(min-width:640px){.pf-mob{display:none}}
.grid-gallery{display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
@media(min-width:768px){.grid-gallery{grid-template-columns:repeat(4,1fr)}}
.cta-band{display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:24px;text-align:center;padding:48px 0}
@media(min-width:768px){.cta-band{flex-direction:row;text-align:left;padding:56px 0}}
.cta-h{color:#fff;font-size:24px;font-weight:800;text-transform:uppercase;letter-spacing:.045em}
@media(min-width:768px){.cta-h{font-size:30px}}
.cta-p{color:rgba(255,255,255,.7);margin-top:8px;font-size:16px}
.cta-actions{display:flex;flex-direction:column;align-items:center;gap:12px;flex-shrink:0}
@media(min-width:640px){.cta-actions{flex-direction:row}}
.cta-phone{color:#fff;font-size:20px;font-weight:700;white-space:nowrap}
.footer{background:var(--ink2);color:#fff}
.grid-footer{display:grid;grid-template-columns:1fr;gap:40px;padding:56px 0}
@media(min-width:768px){.grid-footer{grid-template-columns:repeat(4,1fr)}}
.foot-t{color:#fff;font-weight:700;margin-bottom:16px;font-size:14px;text-transform:uppercase;letter-spacing:.045em}
.foot-list li{margin-bottom:10px}
.foot-link{color:rgba(255,255,255,.65);font-size:14px;transition:color .2s}
.foot-link:hover{color:#fff}
.foot-p{color:rgba(255,255,255,.55);font-size:14px;line-height:1.6}
.foot-phone{display:block;color:#fff;font-size:18px;font-weight:700;margin-bottom:8px}
.foot-bottom{border-top:1px solid rgba(255,255,255,.1)}
.foot-bottom-in{display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:12px;padding:20px 0;color:rgba(255,255,255,.45);font-size:12px;text-align:center}
@media(min-width:640px){.foot-bottom-in{flex-direction:row;text-align:left}}
.foot-bottom-in a:hover{color:rgba(255,255,255,.8)}
.fab-wrap{position:fixed;z-index:40;right:16px;bottom:16px;display:flex;flex-direction:column;gap:8px}
.fab{width:46px;height:46px;display:flex;align-items:center;justify-content:center;background:var(--navy);color:#fff;box-shadow:0 6px 18px rgba(0,0,0,.22);border:0;cursor:pointer;transition:background .2s,opacity .25s}
.fab:hover{background:var(--accent)}
.crumb{color:rgba(255,255,255,.5);font-size:12px;text-transform:uppercase;letter-spacing:.045em;margin-bottom:20px}
.crumb a:hover{color:#fff}
.inner-hero{padding:24px 0 48px}
@media(min-width:768px){.inner-hero{padding:32px 0 56px}}
.split{display:grid;grid-template-columns:1fr;gap:32px;align-items:center}
@media(min-width:768px){.split{grid-template-columns:repeat(2,1fr);gap:40px}}
.svc-hero-img{position:relative;background:var(--ink2);border:1px solid rgba(255,255,255,.08);aspect-ratio:4/3;overflow:hidden}
.svc-h1{color:#fff;font-weight:800;text-transform:uppercase;letter-spacing:.045em;font-size:30px;line-height:1.15}
@media(min-width:768px){.svc-h1{font-size:36px}}
.svc-lead{color:rgba(255,255,255,.8);font-size:16px;line-height:1.6;margin-top:20px}
@media(min-width:768px){.svc-lead{font-size:18px}}
.svc-btns{margin-top:28px;display:flex;flex-direction:column;gap:12px}
@media(min-width:640px){.svc-btns{flex-direction:row}}
.about-grid{display:grid;grid-template-columns:1fr;gap:40px}
@media(min-width:768px){.about-grid{grid-template-columns:repeat(2,1fr);gap:56px}}
.prose p{color:var(--sub);font-size:16px;line-height:1.6;margin-bottom:16px}
.incl-box{background:var(--soft);padding:24px}
@media(min-width:768px){.incl-box{padding:32px}}
.incl-h{color:var(--navy);font-weight:800;text-transform:uppercase;letter-spacing:.045em;font-size:20px;margin-bottom:16px}
@media(min-width:768px){.incl-h{font-size:24px}}
.incl-item{display:flex;align-items:flex-start;gap:12px;padding:10px 0}
.incl-dot{margin-top:4px;flex-shrink:0;width:14px;height:14px;background:var(--accent);transform:rotate(45deg)}
.incl-t{color:var(--navy);font-size:15px;line-height:1.3}
.contact-field{margin-bottom:24px}
.contact-label{color:var(--sub);text-transform:uppercase;letter-spacing:.045em;font-size:12px;margin-bottom:4px}
.contact-val{color:var(--navy);font-size:18px;font-weight:700}
.contact-phone{color:var(--navy);font-size:28px;font-weight:800}
@media(min-width:768px){.contact-phone{font-size:32px}}
.contact-box{background:var(--soft);padding:32px}
@media(min-width:768px){.contact-box{padding:40px}}
.max3{max-width:768px}
.mb-2{margin-bottom:8px}.mb-4{margin-bottom:16px}.mb-6{margin-bottom:24px}.mb-8{margin-bottom:32px}
.mt-4{margin-top:16px}
"""

def head(title, desc, canon):
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'AW-XXXXXXXXXX');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="images/hero-main.webp">
<meta property="og:url" content="{canon}">
<link rel="icon" type="image/png" href="images/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
"""

LOGO = f'<img src="images/logo.png" alt="{SITE} — ремонт квартир под ключ в Астане" class="logo">'

def header():
    nav = "".join(f'<a href="{s}.html" class="nav-a">{SVC_NAME[s]}</a>' for s in NAV_MAIN)
    nav += '<a href="portfolio.html" class="nav-a">Портфолио</a><a href="contacts.html" class="nav-a">Контакты</a>'
    menu = "".join(f'<a href="{s[0]}.html" class="mlink">{s[1]}</a>' for s in SERVICES)
    menu += '<a href="portfolio.html" class="mlink">Портфолио</a><a href="about.html" class="mlink">О компании</a><a href="contacts.html" class="mlink">Контакты</a>'
    return f'''
<header class="header">
  <div class="wrap header-in">
    <a href="index.html" style="display:flex;align-items:center;flex-shrink:0">{LOGO}</a>
    <nav class="nav">{nav}</nav>
    <div class="header-cta">
      <a href="tel:{PHONE_TEL}" class="header-phone">{PHONE_HUMAN}</a>
      <a href="{wa()}" target="_blank" rel="noopener" class="btn-head">Оставить заявку</a>
    </div>
    <button id="burger" class="burger" aria-label="Меню">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
  </div>
</header>
<div id="overlay" class="overlay"></div>
<aside id="menu" class="menu">
  <div class="menu-head">{LOGO}
    <button id="close" class="close" aria-label="Закрыть">
      <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>
    </button>
  </div>
  <nav class="menu-nav">{menu}
    <div class="menu-foot">
      <a href="tel:{PHONE_TEL}" class="menu-phone">{PHONE_HUMAN}</a>
      <a href="{wa()}" target="_blank" rel="noopener" class="btn btn-full">Написать в WhatsApp</a>
    </div>
  </nav>
</aside>
'''

def cta_band():
    return f'''
<section class="s-navy">
  <div class="wrap cta-band">
    <div>
      <h2 class="cta-h">Нужен расчёт стоимости ремонта?</h2>
      <p class="cta-p">Выезжаем на замер, готовим смету и план работ. Перезвоним в течение рабочего дня.</p>
    </div>
    <div class="cta-actions">
      <a href="tel:{PHONE_TEL}" class="cta-phone">{PHONE_HUMAN}</a>
      <a href="{wa()}" target="_blank" rel="noopener" class="btn">Написать в WhatsApp</a>
    </div>
  </div>
</section>
'''

def footer():
    c1 = "".join(f'<li><a href="{s[0]}.html" class="foot-link">{s[1]}</a></li>' for s in SERVICES[:6])
    c2 = "".join(f'<li><a href="{s[0]}.html" class="foot-link">{s[1]}</a></li>' for s in SERVICES[6:])
    c2 += '<li><a href="portfolio.html" class="foot-link">Портфолио</a></li><li><a href="about.html" class="foot-link">О компании</a></li>'
    return f'''
<footer class="footer">
  <div class="wrap grid-footer">
    <div>
      <div class="mb-4">{LOGO}</div>
      <p class="foot-p">Ремонт квартир под ключ в Астане: замер, проект, черновые и чистовые работы, сдача под заселение.</p>
    </div>
    <div>
      <div class="foot-t">Услуги</div>
      <ul class="foot-list">{c1}</ul>
    </div>
    <div>
      <div class="foot-t">&nbsp;</div>
      <ul class="foot-list">{c2}</ul>
    </div>
    <div>
      <div class="foot-t">Контакты</div>
      <a href="tel:{PHONE_TEL}" class="foot-phone">{PHONE_HUMAN}</a>
      <p class="foot-p mb-4">Астана, Казахстан</p>
      <a href="{wa()}" target="_blank" rel="noopener" class="btn" style="padding:10px 20px;font-size:14px">WhatsApp</a>
    </div>
  </div>
  <div class="foot-bottom">
    <div class="wrap foot-bottom-in">
      <span>© 2026 BAU.KZ — все права защищены</span>
      <a href="https://wa.me/{ANUKEN_WA}" target="_blank" rel="noopener">Разработка сайта — студия Anuken</a>
    </div>
  </div>
</footer>
'''

FAB = '''
<div class="fab-wrap">
  <button id="goback" class="fab" aria-label="Назад">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>
  </button>
  <button id="gotop" class="fab" aria-label="Наверх" style="opacity:0;pointer-events:none">
    <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 15l-6-6-6 6"/></svg>
  </button>
</div>
'''

JS_BASE = '''
<script>
(function(){
  var b=document.getElementById('burger'),m=document.getElementById('menu'),
      o=document.getElementById('overlay'),c=document.getElementById('close');
  function open(){m.classList.add('open');o.classList.add('open');document.body.style.overflow='hidden';}
  function close(){m.classList.remove('open');o.classList.remove('open');document.body.style.overflow='';}
  if(b)b.addEventListener('click',open); if(c)c.addEventListener('click',close); if(o)o.addEventListener('click',close);
  var gb=document.getElementById('goback'),gt=document.getElementById('gotop');
  if(gb)gb.addEventListener('click',function(){ if(history.length>1)history.back(); else location.href='index.html'; });
  if(gt)gt.addEventListener('click',function(){ window.scrollTo({top:0,behavior:'smooth'}); });
  function tg(){ if(!gt)return; if(window.scrollY>300){gt.style.opacity='1';gt.style.pointerEvents='auto';}else{gt.style.opacity='0';gt.style.pointerEvents='none';} }
  window.addEventListener('scroll',tg,{passive:true}); tg();
})();
</script>
'''

QUIZ_JS = '''
<script>
(function(){
  var Q=[["Какой ремонт интересует?", ["Косметический", "Капитальный", "Ремонт под ключ", "Дизайнерский", "Пока не знаю"]], ["Площадь квартиры?", ["До 40 м\\u00b2", "40\\u201360 м\\u00b2", "60\\u201390 м\\u00b2", "Более 90 м\\u00b2", "Не знаю точно"]], ["Состояние квартиры?", ["Новостройка (черновая)", "Вторичное жильё", "После застройщика", "Требует демонтажа"]], ["Когда планируете начать?", ["Срочно", "В течение 1\\u20132 недель", "В этом месяце", "Просто узнаю цену"]]];
  var step=0, answers=[];
  var box=document.getElementById('qbox'), contact=document.getElementById('qcontact'),
      title=document.getElementById('qtitle'), opts=document.getElementById('qopts'),
      bar=document.getElementById('qbar'), back=document.getElementById('qback'), next=document.getElementById('qnext');
  var total=Q.length+1;
  function render(){
    bar.style.width=((step+1)/total*100)+'%';
    if(step<Q.length){
      box.classList.remove('hidden'); contact.classList.add('hidden');
      title.textContent=Q[step][0];
      opts.innerHTML='';
      Q[step][1].forEach(function(o){
        var sel=answers[step]===o;
        var el=document.createElement('button');
        el.type='button';
        el.className='qopt'+(sel?' sel':'');
        el.innerHTML='<span class="qradio'+(sel?' sel':'')+'">'+(sel?'<span class="qdot"></span>':'')+'</span><span class="qtext">'+o+'</span>';
        el.onclick=function(){answers[step]=o; render();};
        opts.appendChild(el);
      });
      next.textContent = step===Q.length-1 ? 'Далее \\u2192' : 'Следующий вопрос \\u2192';
    } else {
      box.classList.add('hidden'); contact.classList.remove('hidden');
      next.textContent='Получить расчёт';
    }
    back.style.visibility = step===0 ? 'hidden':'visible';
  }
  next.onclick=function(){
    if(step<Q.length){
      if(!answers[step]){ return; }
      step++; render();
    } else {
      var n=document.getElementById('qname').value.trim(), p=document.getElementById('qphone').value.trim();
      var lines=Q.map(function(q,i){return q[0]+' '+(answers[i]||'\\u2014');}).join('%0A');
      var msg='Заявка с сайта bau (квиз):%0A'+lines+'%0AИмя: '+encodeURIComponent(n||'\\u2014')+'%0AТелефон: '+encodeURIComponent(p||'\\u2014');
      window.open('https://wa.me/WANUM?text='+msg,'_blank');
    }
  };
  back.onclick=function(){ if(step>0){step--; render();} };
  render();
})();
</script>
'''.replace("WANUM", WA_NUMBER)

def page(title, desc, canon, body, quiz=False):
    html = head(title, desc, canon) + header() + body + cta_band() + footer() + FAB + JS_BASE
    if quiz:
        html += QUIZ_JS
    return html + "\n</body>\n</html>"

def feat(icon, t1, t2):
    return f'<div class="feat"><span class="feat-ic">{icon}</span><div><div class="feat-t">{t1}</div><div class="feat-s">{t2}</div></div></div>'

IC_SHIELD = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l7 3v5c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg>'
IC_CLOCK  = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/></svg>'
IC_DOC    = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="4" width="14" height="16"/><path d="M9 8h6M9 12h6M9 16h3"/></svg>'
IC_HAND   = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="3.2"/><path d="M5 20a7 7 0 0114 0"/></svg>'
ARROW = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#CFA384" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" style="flex-shrink:0"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

HERO_FEATURES = feat(IC_HAND,"Ремонт под ключ","одна бригада")+feat(IC_CLOCK,"Смета и план","за 3 часа")+feat(IC_DOC,"Фиксированная цена","в договоре")+feat(IC_SHIELD,"Гарантия","на все работы")

def why_card(path, t, p):
    return f'<div class="why-card"><span class="why-ic"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{path}</svg></span><h3 class="why-t">{t}</h3><p class="why-p">{p}</p></div>'

def why_section():
    cards = "".join(why_card(*w) for w in WHY_ITEMS)
    return f'''
<section class="s-navy sec">
  <div class="wrap">
    <h2 class="h2 h2-lg h2-white center mb-8">Почему заказывают ремонт квартир <span class="accent">у нас</span></h2>
    <div class="grid-why">{cards}</div>
    <div class="actions">
      <a href="{wa()}" target="_blank" rel="noopener" class="btn up">Оставить заявку</a>
      <span style="color:rgba(255,255,255,.6);font-size:14px">Перезвоним в течение рабочего дня</span>
    </div>
  </div>
</section>'''

def package_section():
    items = "".join(f'<div class="pkg-item"><span class="pkg-dot"></span><span class="pkg-t">{w}</span></div>' for w in PACKAGE)
    return f'''
<section class="s-navy sec">
  <div class="wrap">
    <h2 class="h2 h2-lg h2-white center mb-2">Какие работы входят в пакет</h2>
    <p class="accent center mb-8" style="font-size:17px">Ремонт «под ключ» — всё включено в одну смету</p>
    <div class="grid-package">{items}</div>
    <div class="actions">
      <a href="remont-pod-klyuch.html" class="btn up">Подробнее о пакете</a>
      <a href="{wa()}" target="_blank" rel="noopener" class="btn-o btn-w up">Написать в WhatsApp</a>
    </div>
  </div>
</section>'''

def services_grid():
    cards = ""
    for slug, name, *_ in SERVICES:
        cards += f'''<a href="{slug}.html" class="card">
          <div class="ph r43"><span class="lbl">{slug}-1.webp</span><img src="images/{slug}-1.webp" alt="{name}" loading="lazy" onerror="this.remove()"></div>
          <div class="card-body"><h3 class="card-t">{name}</h3>{ARROW}</div></a>'''
    return f'''
<section class="s-soft sec">
  <div class="wrap">
    <h2 class="h2 mb-2">Наши услуги</h2>
    <p class="svc-intro">Полный спектр ремонтных работ для квартир в новостройках и вторичном жилье Астаны.</p>
    <div class="grid-services">{cards}</div>
  </div>
</section>'''

def portfolio_cells(n):
    return "".join(f'<div class="ph r43"><span class="lbl">portfolio-{i}.webp</span><img src="images/portfolio-{i}.webp" alt="Наш ремонт квартиры в Астане №{i}" loading="lazy" onerror="this.remove()"></div>' for i in range(1, n+1))

def build_index():
    hero = f'''
<section class="s-navy">
  <div class="wrap hero-top">
    <div class="hero-img"><span class="lbl">hero-main.webp</span><img src="images/hero-main.webp" alt="Ремонт квартир под ключ в Астане" onerror="this.remove()"></div>
    <h1 class="h1">Ремонт квартир под ключ<span class="accent"> в Астане</span></h1>
    <div class="hero-row">
      <a href="#quiz" class="btn up hero-btn">Рассчитать стоимость</a>
      <p class="lead">Черновые и чистовые работы, электрика, сантехника, плитка и отделка. От замера до сдачи под заселение <span class="accent">с гарантией</span> и <span class="accent">фиксированной сметой</span>.</p>
    </div>
    <div class="grid-features">{HERO_FEATURES}</div>
  </div>
</section>'''

    quiz = '''
<section id="quiz" class="s-soft sec">
  <div class="wrap">
    <h2 class="h2 h2-lg center">Ответьте на 4 вопроса и получите расчёт стоимости</h2>
    <p class="accent center mt-4 mb-8" style="font-size:17px">Узнайте стоимость и сроки ремонта за 1 минуту</p>
    <div class="quiz-box">
      <div class="qbar-track"><div id="qbar" class="qbar"></div></div>
      <div id="qbox">
        <h3 id="qtitle" class="qtitle"></h3>
        <div id="qopts" class="qopts"></div>
      </div>
      <div id="qcontact" class="hidden">
        <h3 class="qtitle" style="margin-bottom:8px">Куда отправить расчёт?</h3>
        <p style="color:rgba(255,255,255,.6);font-size:14px;margin-bottom:20px">Оставьте контакты — пришлём стоимость и сроки в WhatsApp.</p>
        <div class="qinputs">
          <input id="qname" type="text" placeholder="Ваше имя" class="qinput">
          <input id="qphone" type="tel" placeholder="Телефон" class="qinput">
        </div>
      </div>
      <div class="qfoot">
        <button id="qback" class="qback">← Назад</button>
        <button id="qnext" class="btn up">Следующий вопрос →</button>
      </div>
    </div>
  </div>
</section>'''

    portfolio = f'''
<section class="s-white sec">
  <div class="wrap">
    <div class="pf-head">
      <h2 class="h2">Наши работы</h2>
      <a href="portfolio.html" class="pf-all">Все работы {ARROW}</a>
    </div>
    <div class="grid-portfolio">{portfolio_cells(6)}</div>
    <div class="pf-mob"><a href="portfolio.html" class="btn-o btn-full up">Все работы</a></div>
  </div>
</section>'''

    body = hero + quiz + why_section() + package_section() + services_grid() + portfolio
    title = f"{SITE} — ремонт квартир под ключ в Астане | {PHONE_HUMAN}"
    desc  = f"Ремонт квартир под ключ в Астане: черновые и чистовые работы, электрика, сантехника, плитка, отделка. Договор, фиксированная смета, гарантия. Тел. {PHONE_HUMAN}"
    return page(title, desc, DOMAIN, body, quiz=True)

def build_service(s):
    slug, name, h1, lead, included, paras = s
    incl = "".join(f'<div class="incl-item"><span class="incl-dot"></span><span class="incl-t">{i}</span></div>' for i in included)
    gallery = "".join(f'<div class="ph r43"><span class="lbl">{slug}-{i}.webp</span><img src="images/{slug}-{i}.webp" alt="{name} в Астане — фото {i}" loading="lazy" onerror="this.remove()"></div>' for i in range(1,5))
    text = "".join(f'<p>{p}</p>' for p in paras)
    why3 = "".join(why_card(*w) for w in WHY_ITEMS[:3])
    body = f'''
<section class="s-navy">
  <div class="wrap inner-hero">
    <div class="crumb"><a href="index.html">Главная</a> / {name}</div>
    <div class="split">
      <div>
        <h1 class="svc-h1">{h1}<span class="accent"> в Астане</span></h1>
        <p class="svc-lead">{lead}</p>
        <div class="svc-btns">
          <a href="{wa()}" target="_blank" rel="noopener" class="btn up">Рассчитать стоимость</a>
          <a href="tel:{PHONE_TEL}" class="btn-o btn-w up">{PHONE_HUMAN}</a>
        </div>
      </div>
      <div class="svc-hero-img"><span class="lbl">{slug}-1.webp</span><img src="images/{slug}-1.webp" alt="{name} в Астане" onerror="this.remove()"></div>
    </div>
  </div>
</section>

<section class="s-white sec">
  <div class="wrap about-grid">
    <div><h2 class="h2 mb-6">Об услуге</h2><div class="prose">{text}</div></div>
    <div class="incl-box"><h2 class="incl-h">Что входит</h2>{incl}</div>
  </div>
</section>

<section class="s-soft sec">
  <div class="wrap">
    <h2 class="h2 mb-8">Примеры работ</h2>
    <div class="grid-gallery">{gallery}</div>
  </div>
</section>

<section class="s-navy sec">
  <div class="wrap">
    <h2 class="h2 h2-white center mb-8">Почему выбирают <span class="accent">нас</span></h2>
    <div class="grid-why">{why3}</div>
  </div>
</section>'''
    title = f"{h1} в Астане под ключ — {SITE} | {PHONE_HUMAN}"
    desc  = f"{h1} в Астане: {lead} Договор, фиксированная смета, гарантия. Тел. {PHONE_HUMAN}"
    return page(title, desc, DOMAIN + slug + ".html", body)

def build_portfolio():
    body = f'''
<section class="s-navy">
  <div class="wrap inner-hero">
    <div class="crumb"><a href="index.html">Главная</a> / Портфолио</div>
    <h1 class="svc-h1">Наши работы<span class="accent"> в Астане</span></h1>
    <p class="svc-lead" style="max-width:640px">Примеры завершённых квартир под ключ: черновые и чистовые работы, санузлы, кухни и отделка. Фото реальных объектов.</p>
  </div>
</section>
<section class="s-white sec">
  <div class="wrap"><div class="grid-portfolio">{portfolio_cells(6)}</div></div>
</section>'''
    title = f"Портфолио — ремонт квартир в Астане | {SITE}"
    desc  = f"Портфолио bau: фото завершённых ремонтов квартир под ключ в Астане. Черновые и чистовые работы, санузлы, кухни. Тел. {PHONE_HUMAN}"
    return page(title, desc, DOMAIN + "portfolio.html", body)

def build_about():
    why = "".join(why_card(*w) for w in WHY_ITEMS)
    body = f'''
<section class="s-navy">
  <div class="wrap inner-hero">
    <div class="crumb"><a href="index.html">Главная</a> / О компании</div>
    <h1 class="svc-h1">О компании <span class="accent">{SITE}</span></h1>
    <p class="svc-lead" style="max-width:760px">Мы делаем ремонт квартир под ключ в Астане: от новостроек с черновой отделкой до полного обновления вторичного жилья. Работаем своей бригадой, по договору и с фиксированной сметой.</p>
  </div>
</section>
<section class="s-white sec">
  <div class="wrap max3 prose">
    <p>Ремонт — это стресс, когда непонятно, кто отвечает за результат и не вырастет ли цена в процессе. Мы убираем эту неопределённость: один договор, одна смета, одна бригада и один ответственный за объект.</p>
    <p>До начала работ выезжаем на замер, составляем смету и план-график по этапам. Скрытые работы — электрику, сантехнику, гидроизоляцию — фотографируем до того, как их закроет отделка, чтобы вы видели, что спрятано в стенах.</p>
    <p>Материалы закупаем по себестоимости и показываем чеки. На все работы даём гарантию и остаёмся на связи после сдачи квартиры.</p>
  </div>
</section>
<section class="s-navy sec">
  <div class="wrap">
    <h2 class="h2 h2-white center mb-8">Как мы работаем</h2>
    <div class="grid-why">{why}</div>
  </div>
</section>'''
    title = f"О компании — ремонт квартир под ключ в Астане | {SITE}"
    desc  = f"О компании bau: ремонт квартир под ключ в Астане своей бригадой, по договору и фиксированной смете. Тел. {PHONE_HUMAN}"
    return page(title, desc, DOMAIN + "about.html", body)

def build_contacts():
    body = f'''
<section class="s-navy">
  <div class="wrap inner-hero">
    <div class="crumb"><a href="index.html">Главная</a> / Контакты</div>
    <h1 class="svc-h1">Контакты</h1>
    <p class="svc-lead" style="max-width:640px">Позвоните или напишите в WhatsApp — ответим на вопросы, рассчитаем стоимость и договоримся о замере.</p>
  </div>
</section>
<section class="s-white sec">
  <div class="wrap about-grid">
    <div>
      <div class="contact-field"><div class="contact-label">Телефон</div><a href="tel:{PHONE_TEL}" class="contact-phone">{PHONE_HUMAN}</a></div>
      <div class="contact-field"><div class="contact-label">Город</div><div class="contact-val">Астана, Казахстан</div></div>
      <div class="contact-field"><div class="contact-label">Режим работы</div><div class="contact-val">Ежедневно, 09:00 – 20:00</div></div>
      <div class="svc-btns">
        <a href="{wa()}" target="_blank" rel="noopener" class="btn up">Написать в WhatsApp</a>
        <a href="tel:{PHONE_TEL}" class="btn-o up">Позвонить</a>
      </div>
    </div>
    <div class="contact-box">
      <h2 class="incl-h">Оставьте заявку</h2>
      <p class="sub mb-6" style="font-size:14px;line-height:1.6">Нажмите кнопку — откроется WhatsApp с готовым сообщением. Опишите квартиру и задачу, мы рассчитаем стоимость и предложим дату замера.</p>
      <a href="{wa()}" target="_blank" rel="noopener" class="btn btn-full up">Открыть WhatsApp</a>
    </div>
  </div>
</section>'''
    title = f"Контакты — ремонт квартир под ключ в Астане | {SITE}"
    desc  = f"Контакты bau: ремонт квартир под ключ в Астане. Телефон {PHONE_HUMAN}, WhatsApp, ежедневно 09:00–20:00."
    return page(title, desc, DOMAIN + "contacts.html", body)

def w(name, html):
    with open(name, "w", encoding="utf-8") as f:
        f.write(html)
    print("  ", name)

if __name__ == "__main__":
    print("Генерация страниц:")
    w("index.html", build_index())
    for s in SERVICES:
        w(s[0] + ".html", build_service(s))
    w("portfolio.html", build_portfolio())
    w("about.html", build_about())
    w("contacts.html", build_contacts())
    print("Готово. Всего страниц:", 1 + len(SERVICES) + 3)
