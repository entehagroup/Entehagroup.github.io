#!/usr/bin/env python3
"""Builds the service pages of the Enteha Group site.

Persian pages go to the site root (custom-machines.html, automation.html,
parts-manufacturing.html); English pages go to en/. Every page is plain HTML
with its text, FAQ and JSON-LD written in, so search engines and AI crawlers
that do not run JavaScript still read all of it.

Edit the text in PAGES / COMMON below, then run from the repository root:
    python3 tools/build_services.py
"""
import json
import os

SITE = 'https://entehagroup.github.io/'
UPDATED = {'iso': '2026-10-31', 'fa': '۹ آبان ۱۴۰۵', 'en': '31 October 2026'}
PHONE = '+989962233898'
PHONE_TXT = {'fa': '۰۹۹۶۲۲۳۳۸۹۸', 'en': '+98 996 223 3898'}
EMAIL = 'Nasiri2752@Gmail.com'
INSTAGRAM = 'https://www.instagram.com/enteha.eng/'
FORM = 'https://formspree.io/f/mrevzvga'
ORG_ID = SITE + '#org'
BRAND = {'fa': 'گروه فنی مهندسی انتها', 'en': 'Enteha Group'}

ORDER = ['custom-machines', 'automation', 'parts-manufacturing']


def url(slug, lang):
    return SITE + (slug + '.html' if lang == 'fa' else 'en/' + slug + '.html')


# Text shared by all three pages ------------------------------------------------
COMMON = {
    'fa': {
        'home': 'خانه', 'services': 'خدمات', 'contact': 'تماس', 'switch': 'English',
        'glance': 'در یک نگاه', 'process': 'مراحل کار', 'work': 'نمونه‌کارهای ما',
        'industries': 'صنایعی که برایشان کار کرده‌ایم', 'why': 'چرا انتها؟',
        'team': 'چه کسانی کار را انجام می‌دهند؟', 'faq': 'پرسش‌های متداول',
        'related': 'خدمات دیگر انتها', 'updated': 'آخرین به‌روزرسانی:',
        'quote_btn': 'درخواست برآورد قیمت رایگان', 'call_btn': 'تماس تلفنی',
        'cta_h': 'برآورد قیمت رایگان بگیرید',
        'cta_p': 'شرح کار، نقشه یا حتی عکس نمونه را بفرستید. کارشناسان ما پس از بررسی فنی و مشورت با مشاوران، معمولاً ظرف یک تا دو هفته برآورد قیمت را اعلام می‌کنند.',
        'name': 'نام شما', 'email': 'ایمیل شما', 'msg': 'شرح پروژه…', 'send': 'ارسال درخواست',
        'sending': 'در حال ارسال…', 'ok': 'درخواست شما رسید؛ به‌زودی با شما تماس می‌گیریم.',
        'err': 'ارسال نشد. لطفاً دوباره امتحان کنید یا تماس بگیرید.', 'net': 'خطای شبکه. لطفاً تماس بگیرید.',
        'other': 'راه‌های ارتباطی دیگر:', 'rights': 'همه‌ی حقوق محفوظ است.',
        'why_list': [
            '<strong>یک مسئول از طراحی تا مونتاژ.</strong> بیشتر دردسرهای برون‌سپاری از آنجا شروع می‌شود که طراحی، ساخت و مونتاژ دست چند نفر مختلف است و هیچ‌کس کل دستگاه را نمی‌بیند. در انتها کسی که طراحی می‌کند تا آخر کار بالای سر ساخت و مونتاژ می‌ماند.',
            '<strong>هسته‌ی مهندسی و شبکه‌ی همکاران.</strong> سه مهندس مکانیک دانش‌آموخته‌ی دانشگاه‌های صنعتی شریف، علم و صنعت، خواجه نصیر و تربیت مدرس، همراه با کارگاه‌های صنعتی و مهندسان متخصص تحلیل، کنترل کیفی و مشاوره.',
            '<strong>کارنامه‌ی قابل‌بررسی.</strong> ساخت ۸۰ ربات سورتر برای شرکت ملی پست، نخستین دستگاه تست پروتز زانوی ساخت ایران، برگزیده‌ی جایزه‌ی البرز و دو بار جشنواره‌ی جوان خوارزمی، و مقاله در مجله‌های Scientific Reports و International Journal of Mechanical Sciences.',
            '<strong>کنترل کیفیت پیش از تحویل.</strong> بازرسی ابعادی و جوش و تست عملکرد را خودمان پیش از تحویل انجام می‌دهیم.',
        ],
        'industry_list': ['تجهیزات پزشکی و دندان‌پزشکی', 'پست و لجستیک', 'ساخت افزایشی (پرینت سه‌بعدی)', 'دانشگاه‌ها و مراکز تحقیقاتی', 'رباتیک خدماتی'],
        'team_list': [
            ('حسن نصیری خونساری', 'مدیر فنی و طراحی', 'کارشناسی ارشد طراحی کاربردی، دانشگاه صنعتی شریف؛ کارشناسی مکانیک، دانشگاه علم و صنعت ایران', 'https://www.linkedin.com/in/hassan-nasiri-khonsari-44bb49198/', 'av-hassan.webp'),
            ('علیرضا پیرحاجی', 'سرپرست ساخت و کنترل کیفیت', 'کارشناسی ارشد ساخت و تولید، دانشگاه تربیت مدرس؛ کارشناسی مکانیک، دانشگاه صنعتی شریف', 'https://www.linkedin.com/in/alireza-pirhaji-9a0787139/', 'av-alireza.webp'),
            ('سید مصطفی بنی‌هاشمی', 'سرپرست پروژه و تحقیق و توسعه', 'کارشناسی ارشد طراحی کاربردی (دینامیک، کنترل و رباتیک)، دانشگاه صنعتی شریف؛ کارشناسی مکانیک، دانشگاه خواجه نصیر', 'https://www.linkedin.com/in/mostafa-banihashemi/', 'av-mostafa.webp'),
        ],
    },
    'en': {
        'home': 'Home', 'services': 'Services', 'contact': 'Contact', 'switch': 'فارسی',
        'glance': 'At a glance', 'process': 'How we work', 'work': 'Our work',
        'industries': 'Industries we have worked for', 'why': 'Why Enteha?',
        'team': 'Who does the work?', 'faq': 'Frequently asked questions',
        'related': 'Other Enteha services', 'updated': 'Last updated:',
        'quote_btn': 'Request a free quote', 'call_btn': 'Call us',
        'cta_h': 'Get a free quote',
        'cta_p': 'Send us a description, a drawing or even a photo of a sample. After a technical review and consultation with our advisers, we usually send the quote within one to two weeks.',
        'name': 'Your name', 'email': 'Your email', 'msg': 'Describe your project…', 'send': 'Send request',
        'sending': 'Sending…', 'ok': 'Thank you — we have your request and will be in touch soon.',
        'err': 'Could not send. Please try again or call us.', 'net': 'Network error. Please call us.',
        'other': 'Other ways to reach us:', 'rights': 'All rights reserved.',
        'why_list': [
            '<strong>One owner from design to assembly.</strong> Most outsourcing trouble starts when design, fabrication and assembly are in different hands and nobody sees the whole machine. At Enteha, the engineer who designs it stays with fabrication and assembly to the end.',
            '<strong>A core engineering team plus a partner network.</strong> Three mechanical engineers from Sharif University of Technology, IUST, K. N. Toosi and Tarbiat Modares University, working with industrial workshops and specialist engineers in analysis, quality control and consulting.',
            '<strong>A track record you can check.</strong> 80 postal sorting robots built for Iran Post, the first knee-prosthesis test rig made in Iran, the Alborz Elite Prize and two Khwarizmi Youth Festival awards, and papers in Scientific Reports and the International Journal of Mechanical Sciences.',
            '<strong>Quality control before delivery.</strong> We carry out dimensional and weld inspection and functional testing ourselves before anything ships.',
        ],
        'industry_list': ['Medical and dental devices', 'Postal and logistics', 'Additive manufacturing (3D printing)', 'Universities and research centres', 'Service robotics'],
        'team_list': [
            ('Hassan Nasiri Khonsari', 'Technical & Design Director', 'MSc Applied Design, Sharif University of Technology; BSc Mechanical Engineering, IUST', 'https://www.linkedin.com/in/hassan-nasiri-khonsari-44bb49198/', 'av-hassan.webp'),
            ('Alireza Pirhaji', 'Manufacturing & Quality Lead', 'MSc Manufacturing Engineering, Tarbiat Modares University; BSc Mechanical Engineering, Sharif University of Technology', 'https://www.linkedin.com/in/alireza-pirhaji-9a0787139/', 'av-alireza.webp'),
            ('Seyed Mostafa Banihashemi', 'Project & R&D Lead', 'MSc Applied Design (Dynamics, Control & Robotics), Sharif University of Technology; BSc Mechanical Engineering, K. N. Toosi University', 'https://www.linkedin.com/in/mostafa-banihashemi/', 'av-mostafa.webp'),
        ],
    },
}

# FAQ answers that hold for every service -----------------------------------
FAQ_QUOTE = {
    'fa': ('برآورد قیمت رایگان است؟ چقدر طول می‌کشد؟',
           'بله، برآورد قیمت رایگان است. معمولاً یک تا دو هفته طول می‌کشد، چون کارشناسان ما پیش از اعلام قیمت، کار را از نظر فنی بررسی می‌کنند و با مشاوران گروه مشورت می‌کنند تا قیمت و زمان اعلام‌شده واقعی باشد.'),
    'en': ('Is the quote free? How long does it take?',
           'Yes, quotes are free. A quote usually takes one to two weeks, because our engineers review the job technically and consult the group\'s advisers before giving a price, so that the price and schedule we quote are realistic.'),
}
FAQ_AREA = {
    'fa': ('فقط در تهران و اصفهان کار می‌کنید؟',
           'خیر. دفتر و کارگاه‌های همکار ما در تهران و اصفهان است، ولی برای کارفرمایان سراسر ایران کار می‌کنیم.'),
    'en': ('Do you only work in Tehran and Isfahan?',
           'No. Our office and partner workshops are in Tehran and Isfahan, but we work for clients across Iran.'),
}
FAQ_FILES = {
    'fa': ('برای شروع چه اطلاعاتی لازم است؟ چه فرمت‌هایی از نقشه را می‌پذیرید؟',
           'هر چیزی که دارید کافی است: نقشه‌ی دوبعدی یا مدل سه‌بعدی در هر فرمتی (مثل STEP، DWG، DXF، SolidWorks یا PDF)، عکس، طرح دستی، یا فقط شرح کار. اگر نقشه ندارید و نمونه‌ی فیزیکی دارید، با مهندسی معکوس نقشه را از روی نمونه تهیه می‌کنیم.'),
    'en': ('What do you need to get started? Which drawing formats do you accept?',
           'Whatever you have is enough: 2D drawings or 3D models in any format (such as STEP, DWG, DXF, SolidWorks or PDF), photos, a hand sketch, or just a description of the job. If you have a physical sample but no drawings, we reverse-engineer the drawings from the sample.'),
}
FAQ_SUPPORT = {
    'fa': ('بعد از تحویل چه پشتیبانی‌ای دارید؟',
           'ایرادهای دستگاه‌هایی را که خودمان طراحی کرده و ساخته‌ایم تا دو ماه پس از تحویل رفع می‌کنیم (جدا از درخواست‌های تازه‌ی کارفرما). ضمانت طولانی‌تر، تعمیر و ارتقا را هم هر طور که کارفرما بخواهد در قرارداد می‌گنجانیم. اگر طرح از کارفرما بوده و کار ما فقط پیمانکاری ساخت بوده، رفع ایرادِ ناشی از طرح را انجام می‌دهیم ولی هزینه‌ی آن جداگانه محاسبه می‌شود.'),
    'en': ('What support do you give after delivery?',
           'For machines we designed and built ourselves, we fix any faults for two months after delivery (separate from new requests from the client). A longer warranty, repairs and upgrades can be written into the contract however the client wants. If the design came from the client and we only did the fabrication, we still fix faults caused by the design, but that work is charged separately.'),
}

# The three service pages ------------------------------------------------------
PAGES = {
 'custom-machines': {
  'img': 'p-sorter-3-m.webp',
  'fa': {
   'title': 'طراحی و ساخت دستگاه خاص‌منظوره و ربات صنعتی سفارشی | گروه فنی مهندسی انتها',
   'desc': 'طراحی و ساخت دستگاه خاص‌منظوره، تجهیزات آزمون و ربات صنعتی سفارشی، از نیازسنجی تا راه‌اندازی. تهران و اصفهان، برای کارفرمایان سراسر ایران. سفارش تک‌دستگاه و برآورد قیمت رایگان.',
   'nav': 'دستگاه و ربات سفارشی',
   'h1': 'طراحی و ساخت دستگاه خاص‌منظوره و ربات صنعتی سفارشی',
   'lead': [
    'گروه فنی مهندسی انتها دستگاه‌ها، ربات‌ها و تجهیزات آزمون صنعتی را برای فرآیند مشخص هر کارفرما از صفر طراحی می‌کند و می‌سازد؛ از نیازسنجی و طراحی مفهومی تا طراحی تفصیلی، تحلیل مهندسی، ساخت، مونتاژ، کنترل کیفیت و راه‌اندازی. هر جا دستگاه آماده‌ای در بازار نیست، یا دستگاه موجود با خط تولید شما جور نیست، ماشینی می‌سازیم که دقیقاً همان کار را انجام دهد.',
    'دفتر و کارگاه‌های همکار ما در تهران و اصفهان است و برای کارفرمایان سراسر ایران کار می‌کنیم. سفارش تک‌دستگاه هم می‌پذیریم و برآورد قیمت رایگان است.',
   ],
   'facts': [
    ('چه می‌سازیم', 'دستگاه خاص‌منظوره، تجهیزات آزمون، ربات صنعتی و خدماتی و متحرک، دستگاه CNC و پرینتر سه‌بعدی صنعتی'),
    ('دامنه‌ی کار', 'نیازسنجی، طراحی، تحلیل مهندسی، ساخت، مونتاژ، کنترل کیفیت، راه‌اندازی'),
    ('ابعاد کارهای قبلی', 'دستگاه‌هایی از ۱۰ تا ۲۵۰ کیلوگرم و سازه‌هایی تا حدود ۱ تا ۲ تن'),
    ('زمان معمول', 'دستگاه خاص‌منظوره‌ی ساده: ۱ تا ۲ ماه طراحی و ۱ تا ۲ ماه ساخت'),
    ('تعداد سفارش', 'از یک دستگاه تا تولید سری'),
    ('برآورد قیمت', 'رایگان، معمولاً ظرف ۱ تا ۲ هفته'),
    ('پشتیبانی', 'رفع ایراد تا ۲ ماه پس از تحویل؛ ضمانت و ارتقا طبق قرارداد'),
    ('محل', 'تهران و اصفهان؛ برای سراسر ایران'),
   ],
   'what_h': 'چه دستگاه‌هایی طراحی و ساخت می‌کنیم؟',
   'what': [
    ('دستگاه‌های خاص‌منظوره (SPM)', 'ماشینی که فقط برای یک مرحله از فرآیند شما ساخته می‌شود، مثل دستگاه‌های تغذیه، جابه‌جایی، تفکیک، برش یا مونتاژ، وقتی دستگاه آماده‌ای برای آن در بازار نیست.'),
    ('تجهیزات آزمون و تست', 'دستگاه‌های آزمون مکانیکی برای آزمایشگاه‌ها و کنترل کیفیت، مطابق استانداردهایی مثل ASTM؛ از جمله دستگاه تست پروتز زانو در شش درجه‌ی آزادی.'),
    ('ربات‌های صنعتی، خدماتی و متحرک', 'ربات‌های سورتر و تفکیک بار، ربات‌های حمل و سرو، و ربات‌های کابلی؛ از طراحی مکانیزم و شاسی تا سیستم حرکت و کنترل.'),
    ('رباتیک پزشکی و توانبخشی', 'طراحی، ساخت و کنترل سیستم‌های رباتیک برای پژوهش و توانبخشی، همراه با دانشگاه‌ها و مراکز تحقیقاتی.'),
    ('دستگاه CNC و پرینتر سه‌بعدی صنعتی', 'طراحی سازه، انتخاب درایو و موتور، الکترونیک، فرم‌ور و راه‌اندازی کنترل؛ از پرینتر FDM با حجم کاری ۵۰۰×۵۰۰×۴۰۰ میلی‌متر تا CNC با میز حدود ۱۰۰×۱۰۰ سانتی‌متر.'),
    ('طراحی مکانیزم و تحلیل مهندسی (FEA)', 'بررسی استحکام، تغییرشکل و رفتار سازه و مکانیزم با تحلیل اجزای محدود، پیش از آنکه هزینه‌ی ساخت پرداخت شود.'),
    ('مهندسی معکوس و بازطراحی', 'تهیه‌ی نقشه از روی نمونه‌ی موجود و بازطراحی دستگاه یا قطعه‌ای که نقشه ندارد یا باید بهتر شود.'),
   ],
   'steps': [
    ('گفت‌وگو و نیازسنجی', 'شرح کار، نقشه، عکس یا نمونه را می‌فرستید و ظرفیت، دقت و محدودیت‌های فرآیند را با هم مشخص می‌کنیم.'),
    ('برآورد قیمت رایگان', 'پس از بررسی فنی و مشورت با مشاوران، معمولاً ظرف ۱ تا ۲ هفته قیمت و زمان‌بندی را اعلام می‌کنیم.'),
    ('طراحی و تحلیل', 'طراحی مفهومی و تفصیلی، تحلیل مهندسی و انتخاب قطعات، با تأیید شما در هر مرحله.'),
    ('ساخت و مونتاژ', 'ساخت در کارگاه‌های همکار و مونتاژ زیر نظر همان مهندسی که طراحی کرده است.'),
    ('کنترل کیفیت و آزمون', 'بازرسی ابعادی و تست عملکرد دستگاه پیش از تحویل.'),
    ('تحویل، راه‌اندازی و پشتیبانی', 'تحویل و راه‌اندازی دستگاه، و رفع ایراد تا ۲ ماه پس از تحویل.'),
   ],
   'projects': [
    ('p-sorter-3-m.webp', 'ربات‌های سورتر پستی (۱۳۹۹ تا ۱۴۰۴)', 'ربات‌های خودگردان تفکیک مرسولات برای شرکت ملی پست. ساخت و مونتاژ نسل‌های اول و دوم: ۵۰ دستگاه برای تهران و ۳۰ دستگاه برای کرمانشاه. طراحی نسل سوم (مکانیزم تخلیه‌ی بار، توزین، استراکچر و سیستم حرکت) در تیراژ ۲۰۰ دستگاه به تولید رسید. مقام دوم بیست‌وششمین جشنواره‌ی جوان خوارزمی.'),
    ('p-knee-m.webp', 'دستگاه تست تقید و پایداری پروتز زانو (۱۴۰۰)', 'آزمون پروتز کامل زانو در شش درجه‌ی آزادی مطابق استاندارد ASTM F1223؛ نخستین نمونه‌ی ساخت ایران، در حالی که معادل‌های تجاری را شرکت‌هایی مثل EndoLab و AMTI می‌سازند. طراحی مکانیکی، اتوماسیون، PLC و HMI. برگزیده‌ی جایزه‌ی البرز و جشنواره‌ی جوان خوارزمی.'),
    ('p-printer-3-m.webp', 'پرینترهای سه‌بعدی FDM صنعتی (۱۳۹۹ تا ۱۴۰۲)', 'پنج دستگاه که از صفر طراحی و ساخته شدند، تا ماشینی با حجم کاری ۵۰۰×۵۰۰×۴۰۰ میلی‌متر با بال‌اسکرو و ریل خطی صنعتی روی همه‌ی محورها؛ سازه، الکترونیک و فرم‌ور مستقل.'),
    ('p-cnc-m.webp', 'CNC صنعتی دوکاره (۱۴۰۲)', 'CNC برای برش چوب و فلزات سبک با میز حدود ۱۰۰×۱۰۰ سانتی‌متر که با تعویض هد به پرینتر سه‌بعدی تبدیل می‌شود؛ برای کارگاه‌های کوچک و متوسط.'),
    ('p-waiter-m.webp', 'ربات‌های گارسون (۱۴۰۰)', 'ناوگانی هفت‌تایی از ربات‌های حمل و سرو غذا؛ شاسی و سیستم حرکت برای کار پایدار روی کف ناهموار رستوران.'),
    ('p-dmd-m.webp', 'سامانه‌ی تغذیه‌ی پودر DMD (۱۳۹۸)', 'تغذیه‌کننده‌ی پودر برای رسوب مستقیم فلز با لیزر، با کنترل نرخ تغذیه در بازه‌ی ۱ تا ۱۰۰ گرم بر دقیقه.'),
   ],
   'faq': [
    ('هزینه‌ی طراحی و ساخت دستگاه خاص‌منظوره چقدر است؟', 'به پیچیدگی، ابعاد، دقت و تعداد دستگاه بستگی دارد، پس قیمت ثابتی ندارد. شرح کار را بفرستید تا برآورد قیمت رایگان را معمولاً ظرف یک تا دو هفته دریافت کنید.'),
    ('ساخت یک دستگاه چقدر طول می‌کشد؟', 'بسته به پروژه، از یک تا دو هفته تا حدود یک سال. برای یک دستگاه خاص‌منظوره‌ی ساده، طراحی معمولاً ۱ تا ۲ ماه و ساخت هم ۱ تا ۲ ماه طول می‌کشد.'),
    ('سفارش تک‌دستگاه هم می‌پذیرید؟', 'بله. از یک دستگاه تا تولید سری را می‌پذیریم؛ تعداد مناسب برای تولید سری به حجم پروژه بستگی دارد.'),
    ('دستگاه‌هایی با چه ابعاد و وزنی ساخته‌اید؟', 'دستگاه‌هایی از حدود ۱۰ تا ۲۵۰ کیلوگرم و سازه‌هایی تا حدود ۱ تا ۲ تن. جنس هر بخش را بر اساس کاربرد همان بخش انتخاب می‌کنیم، از فولاد و استیل ۳۱۶ تا آلومینیوم، پلاستیک‌های مهندسی و کامپوزیت.'),
    ('مهندسی معکوس هم انجام می‌دهید؟', 'بله. از روی دستگاه یا قطعه‌ی موجود نقشه تهیه می‌کنیم و در صورت نیاز آن را بازطراحی و بهینه می‌کنیم.'),
    FAQ_QUOTE['fa'], FAQ_FILES['fa'], FAQ_SUPPORT['fa'], FAQ_AREA['fa'],
   ],
  },
  'en': {
   'title': 'Custom Special-Purpose Machines & Industrial Robots — Design and Build | Enteha Group',
   'desc': 'Design and fabrication of special-purpose machines, test rigs and custom industrial robots, from requirements to commissioning. Based in Tehran and Isfahan, serving clients across Iran. One-off machines welcome; free quotes.',
   'nav': 'Custom machines & robots',
   'h1': 'Custom special-purpose machines and industrial robots',
   'lead': [
    'Enteha Group designs and builds industrial machines, robots and test equipment from scratch for each client\'s specific process — from requirements and concept design through detailed design, engineering analysis, fabrication, assembly, quality control and commissioning. Where no off-the-shelf machine exists, or the available ones do not fit your line, we build one that does exactly that job.',
    'Our office and partner workshops are in Tehran and Isfahan, and we work for clients across Iran. We take one-off orders, and quotes are free.',
   ],
   'facts': [
    ('What we build', 'Special-purpose machines, test rigs, industrial, service and mobile robots, CNC machines and industrial 3D printers'),
    ('Scope', 'Requirements, design, engineering analysis, fabrication, assembly, quality control, commissioning'),
    ('Size of past work', 'Machines from 10 to 250 kg and structures of about 1–2 tonnes'),
    ('Typical timeline', 'Simple special-purpose machine: 1–2 months design and 1–2 months fabrication'),
    ('Order size', 'From a single machine to series production'),
    ('Quote', 'Free, usually within 1–2 weeks'),
    ('Support', 'Faults fixed for 2 months after delivery; warranty and upgrades by contract'),
    ('Location', 'Tehran and Isfahan; serving all of Iran'),
   ],
   'what_h': 'What machines do we design and build?',
   'what': [
    ('Special-purpose machines (SPM)', 'A machine built for one step of your process — feeding, handling, sorting, cutting or assembly — when there is no ready-made machine for it on the market.'),
    ('Test rigs and test equipment', 'Mechanical test machines for laboratories and quality control, built to standards such as ASTM — including a six-degree-of-freedom knee prosthesis test rig.'),
    ('Industrial, service and mobile robots', 'Sorting robots, delivery and serving robots, and cable-driven robots — from mechanism and chassis design to drive and control systems.'),
    ('Medical and rehabilitation robotics', 'Design, fabrication and control of robotic systems for research and rehabilitation, together with universities and research centres.'),
    ('CNC machines and industrial 3D printers', 'Structure design, drive and motor selection, electronics, firmware and control set-up — from an FDM printer with a 500 × 500 × 400 mm build volume to a CNC with a table of about 100 × 100 cm.'),
    ('Mechanism design and engineering analysis (FEA)', 'Checking the strength, deflection and behaviour of structures and mechanisms with finite element analysis before money is spent on fabrication.'),
    ('Reverse engineering and redesign', 'Drawings made from an existing sample, and redesign of a machine or part that has no drawings or needs to be improved.'),
   ],
   'steps': [
    ('Discussion and requirements', 'You send a description, drawings, photos or a sample, and together we pin down capacity, accuracy and process constraints.'),
    ('Free quote', 'After a technical review and consultation with our advisers, we usually send the price and schedule within 1–2 weeks.'),
    ('Design and analysis', 'Concept and detailed design, engineering analysis and component selection, with your approval at each stage.'),
    ('Fabrication and assembly', 'Fabrication in our partner workshops and assembly supervised by the same engineer who designed it.'),
    ('Quality control and testing', 'Dimensional inspection and functional testing before delivery.'),
    ('Delivery, commissioning and support', 'Delivery and commissioning, and faults fixed for 2 months after delivery.'),
   ],
   'projects': [
    ('p-sorter-3-m.webp', 'Postal sorting robots (2020–2025)', 'Autonomous parcel-sorting robots for Iran Post. We built and assembled generations 1 and 2: 50 units for Tehran and 30 for Kermanshah. Our generation 3 design (unloading mechanism, weighing, structure and drive system) went into production in a run of 200 units. Second place at the 26th Khwarizmi Youth Festival.'),
    ('p-knee-m.webp', 'Knee prosthesis constraint & stability test rig (2021)', 'Tests total knee prostheses in six degrees of freedom to ASTM F1223 — the first rig of its kind made in Iran, where commercial equivalents come from companies such as EndoLab and AMTI. Mechanical design, automation, PLC and HMI. Recognised by the Alborz Elite Prize and the Khwarizmi Youth Festival.'),
    ('p-printer-3-m.webp', 'Industrial FDM 3D printers (2020–2023)', 'Five machines designed and built from scratch, up to a 500 × 500 × 400 mm build volume with industrial ball screws and linear rails on every axis; our own structure, electronics and firmware.'),
    ('p-cnc-m.webp', 'Dual-purpose industrial CNC (2023)', 'A CNC for cutting wood and light metals with a table of about 100 × 100 cm that becomes a 3D printer by swapping the head; built for small and medium workshops.'),
    ('p-waiter-m.webp', 'Waiter robots (2021)', 'A fleet of seven food delivery and serving robots, with a chassis and drive system designed to stay stable on uneven restaurant floors.'),
    ('p-dmd-m.webp', 'DMD powder feeder (2019)', 'A powder feeder for laser direct metal deposition, controlling the feed rate between 1 and 100 g/min.'),
   ],
   'faq': [
    ('How much does a special-purpose machine cost?', 'It depends on complexity, size, accuracy and quantity, so there is no fixed price. Send us a description and you will usually receive a free quote within one to two weeks.'),
    ('How long does it take to build a machine?', 'Depending on the project, anything from one or two weeks to about a year. For a simple special-purpose machine, design usually takes 1–2 months and fabrication another 1–2 months.'),
    ('Do you take orders for a single machine?', 'Yes. We take everything from a single machine to series production; the right quantity for a series depends on the project.'),
    ('What sizes and weights have you built?', 'Machines from about 10 to 250 kg and structures of about 1–2 tonnes. We choose the material of each part for its application — from steel and 316 stainless to aluminium, engineering plastics and composites.'),
    ('Do you do reverse engineering?', 'Yes. We produce drawings from an existing machine or part and, where needed, redesign and improve it.'),
    FAQ_QUOTE['en'], FAQ_FILES['en'], FAQ_SUPPORT['en'], FAQ_AREA['en'],
   ],
  },
 },
 'automation': {
  'img': 'p-cnc-panel-open-m.webp',
  'fa': {
   'title': 'اتوماسیون خط تولید، برنامه‌نویسی PLC و ساخت تابلو کنترل | گروه فنی مهندسی انتها',
   'desc': 'خودکارسازی مراحل دستی و نیمه‌خودکار خط تولید: طراحی کنترل، برنامه‌نویسی PLC دلتا و زیمنس، HMI، کنترل حرکت با سروو و استپر، توزین و تابلو برق. تهران و اصفهان، برای سراسر ایران.',
   'nav': 'اتوماسیون خط تولید',
   'h1': 'اتوماسیون خط تولید و طراحی سیستم کنترل',
   'lead': [
    'گروه فنی مهندسی انتها مراحل دستی و نیمه‌خودکار خط تولید را خودکار می‌کند: طراحی سیستم کنترل، برنامه‌نویسی PLC (دلتا و زیمنس)، طراحی HMI، کنترل حرکت با درایوهای سروو و استپر، سنسور و سامانه‌ی توزین و اندازه‌گیری، ساخت تابلو برق و کنترل، و یکپارچه‌سازی با تجهیزات موجود شما. چون طراحی مکانیکی و ساخت را هم خودمان انجام می‌دهیم، بخش مکانیکی و کنترلی اتوماسیون را یک تیم و به‌صورت هماهنگ طراحی می‌کند.',
    'دفتر و کارگاه‌های همکار ما در تهران و اصفهان است و برای کارفرمایان سراسر ایران کار می‌کنیم. برآورد قیمت رایگان است.',
   ],
   'facts': [
    ('چه انجام می‌دهیم', 'طراحی کنترل، PLC و HMI، کنترل حرکت، توزین و اندازه‌گیری، تابلو برق، طراحی خط و ایستگاه مونتاژ'),
    ('برندهای PLC', 'دلتا (Delta) و زیمنس (Siemens)'),
    ('کنترل حرکت', 'درایوهای سروو و استپر'),
    ('تجهیزات موجود', 'یکپارچه‌سازی با دستگاه‌ها و خط فعلی شما'),
    ('زمان معمول', 'از ۱ تا ۲ هفته تا چند ماه، بسته به پروژه'),
    ('برآورد قیمت', 'رایگان، معمولاً ظرف ۱ تا ۲ هفته'),
    ('پشتیبانی', 'رفع ایراد تا ۲ ماه پس از تحویل؛ ضمانت و ارتقا طبق قرارداد'),
    ('محل', 'تهران و اصفهان؛ برای سراسر ایران'),
   ],
   'what_h': 'در اتوماسیون چه کارهایی انجام می‌دهیم؟',
   'what': [
    ('طراحی سیستم کنترل و معماری اتوماسیون', 'تعیین ترتیب کار، سنسورها، عملگرها و منطق کنترل برای اینکه یک مرحله یا کل خط بدون دخالت دستی کار کند.'),
    ('برنامه‌نویسی PLC (دلتا و زیمنس) و طراحی HMI', 'نوشتن برنامه‌ی PLC و طراحی صفحه‌ی اپراتور (HMI) برای فرمان، تنظیم و نمایش وضعیت دستگاه.'),
    ('کنترل حرکت با سروو و استپر', 'انتخاب و راه‌اندازی موتور و درایو برای حرکت‌های دقیق و تکرارپذیر در دستگاه‌ها و خطوط.'),
    ('سنسور، سامانه‌ی توزین و اندازه‌گیری', 'افزودن اندازه‌گیری و توزین به فرآیند برای کنترل کیفیت و تفکیک خودکار؛ مثل سامانه‌ی توزین ربات‌های سورتر پستی.'),
    ('تابلوهای برق و کنترل', 'طراحی و ساخت تابلو برق و فرمان دستگاه‌ها.'),
    ('طراحی خط تولید و ایستگاه‌های مونتاژ', 'طراحی جانمایی و ایستگاه‌های کاری برای افزایش ظرفیت و کاهش کار دستی.'),
    ('یکپارچه‌سازی با تجهیزات موجود', 'اتصال دستگاه‌های جدید به خط و تجهیزات فعلی، به‌جای تعویض کل خط.'),
   ],
   'steps': [
    ('بررسی و نیازسنجی', 'بررسی مرحله‌ای که باید خودکار شود، ظرفیت، دقت و تجهیزات موجود.'),
    ('برآورد قیمت رایگان', 'پس از بررسی فنی و مشورت با مشاوران، معمولاً ظرف ۱ تا ۲ هفته.'),
    ('طراحی کنترل و مکانیک', 'معماری کنترل، انتخاب PLC، درایو و سنسورها، و طراحی بخش‌های مکانیکی لازم.'),
    ('ساخت تابلو و برنامه‌نویسی', 'ساخت تابلو برق و کنترل، برنامه‌نویسی PLC و طراحی HMI.'),
    ('نصب و راه‌اندازی', 'نصب روی خط، یکپارچه‌سازی با تجهیزات موجود و تست.'),
    ('پشتیبانی', 'رفع ایراد تا ۲ ماه پس از تحویل؛ ضمانت و ارتقا طبق قرارداد.'),
   ],
   'projects': [
    ('p-knee-m.webp', 'دستگاه تست تقید و پایداری پروتز زانو (۱۴۰۰)', 'معماری اتوماسیون، برنامه‌نویسی PLC و توسعه‌ی HMI برای دستگاهی که پروتز زانو را در شش درجه‌ی آزادی مطابق ASTM F1223 آزمون می‌کند.'),
    ('p-sorter-3-m.webp', 'ربات‌های سورتر پستی (۱۳۹۹ تا ۱۴۰۴)', 'سامانه‌ی توزین، مکانیزم تخلیه و سیستم حرکت ربات‌های تفکیک مرسولات شرکت ملی پست؛ نسل سوم در تیراژ ۲۰۰ دستگاه تولید شد.'),
    ('p-cnc-panel-open-m.webp', 'تابلو برق CNC صنعتی دوکاره (۱۴۰۲)', 'انتخاب درایوها و موتورها، ساخت تابلو برق و راه‌اندازی کنترل با G-Code برای CNC با میز حدود ۱۰۰×۱۰۰ سانتی‌متر.'),
    ('p-dmd-m.webp', 'سامانه‌ی تغذیه‌ی پودر DMD (۱۳۹۸)', 'پیاده‌سازی کامل الکترونیک، کنترل و منطق دستگاه، با کنترل نرخ تغذیه‌ی پودر در بازه‌ی ۱ تا ۱۰۰ گرم بر دقیقه.'),
   ],
   'faq': [
    ('با چه برندهایی از PLC کار می‌کنید؟', 'با PLCهای دلتا (Delta) و زیمنس (Siemens). برنامه‌نویسی PLC و طراحی HMI را خودمان انجام می‌دهیم.'),
    ('می‌توانید دستگاه‌های فعلی ما را هم خودکار کنید؟', 'بله. یکپارچه‌سازی با تجهیزات موجود بخشی از کار ماست؛ لازم نیست کل خط عوض شود.'),
    ('تابلو برق و کنترل هم می‌سازید؟', 'بله. طراحی و ساخت تابلوهای برق و کنترل دستگاه‌ها را انجام می‌دهیم.'),
    ('اتوماسیون یک مرحله از خط چقدر طول می‌کشد؟', 'به اندازه و پیچیدگی کار بستگی دارد؛ از یک تا دو هفته برای کارهای کوچک تا چند ماه برای پروژه‌های بزرگ‌تر. زمان دقیق را همراه برآورد قیمت اعلام می‌کنیم.'),
    ('بخش مکانیکی اتوماسیون را هم انجام می‌دهید؟', 'بله. طراحی مکانیکی، ساخت و مونتاژ را هم خودمان انجام می‌دهیم، پس مکانیک و کنترل را یک تیم هماهنگ طراحی می‌کند.'),
    FAQ_QUOTE['fa'], FAQ_FILES['fa'], FAQ_SUPPORT['fa'], FAQ_AREA['fa'],
   ],
  },
  'en': {
   'title': 'Production Line Automation, PLC Programming & Control Cabinets | Enteha Group',
   'desc': 'Automating manual and semi-automatic production steps: control design, Delta and Siemens PLC programming, HMI, servo and stepper motion control, weighing and control cabinets. Tehran and Isfahan, serving all of Iran.',
   'nav': 'Production line automation',
   'h1': 'Production line automation and control system design',
   'lead': [
    'Enteha Group automates the manual and semi-automatic steps of production lines: control system design, PLC programming (Delta and Siemens), HMI design, servo and stepper motion control, sensors and weighing and measurement systems, electrical and control cabinets, and integration with your existing equipment. Because we also do the mechanical design and fabrication, one team designs the mechanical and control sides of the automation together.',
    'Our office and partner workshops are in Tehran and Isfahan, and we work for clients across Iran. Quotes are free.',
   ],
   'facts': [
    ('What we do', 'Control design, PLC and HMI, motion control, weighing and measurement, control cabinets, line and assembly station design'),
    ('PLC brands', 'Delta and Siemens'),
    ('Motion control', 'Servo and stepper drives'),
    ('Existing equipment', 'Integration with your current machines and line'),
    ('Typical timeline', 'From 1–2 weeks to several months, depending on the project'),
    ('Quote', 'Free, usually within 1–2 weeks'),
    ('Support', 'Faults fixed for 2 months after delivery; warranty and upgrades by contract'),
    ('Location', 'Tehran and Isfahan; serving all of Iran'),
   ],
   'what_h': 'What do we do in automation?',
   'what': [
    ('Control system design and automation architecture', 'Defining the sequence, sensors, actuators and control logic so that one step or a whole line runs without manual work.'),
    ('PLC programming (Delta, Siemens) and HMI design', 'Writing the PLC program and designing the operator screen (HMI) to command, adjust and monitor the machine.'),
    ('Motion control with servo and stepper drives', 'Selecting and commissioning motors and drives for precise, repeatable motion in machines and lines.'),
    ('Sensors, weighing and measurement systems', 'Adding measurement and weighing to the process for quality control and automatic sorting — such as the weighing system of the postal sorting robots.'),
    ('Electrical and control cabinets', 'Design and build of machine power and control cabinets.'),
    ('Production line and assembly station design', 'Layout and workstation design to raise capacity and reduce manual work.'),
    ('Integration with existing equipment', 'Connecting new machines to your current line and equipment instead of replacing the whole line.'),
   ],
   'steps': [
    ('Review and requirements', 'Reviewing the step to automate, capacity, accuracy and existing equipment.'),
    ('Free quote', 'After a technical review and consultation with our advisers, usually within 1–2 weeks.'),
    ('Control and mechanical design', 'Control architecture, choice of PLC, drives and sensors, and design of the mechanical parts needed.'),
    ('Cabinet build and programming', 'Building the control cabinet, PLC programming and HMI design.'),
    ('Installation and commissioning', 'Installation on the line, integration with existing equipment and testing.'),
    ('Support', 'Faults fixed for 2 months after delivery; warranty and upgrades by contract.'),
   ],
   'projects': [
    ('p-knee-m.webp', 'Knee prosthesis constraint & stability test rig (2021)', 'Automation architecture, PLC programming and HMI development for a rig that tests knee prostheses in six degrees of freedom to ASTM F1223.'),
    ('p-sorter-3-m.webp', 'Postal sorting robots (2020–2025)', 'Weighing system, unloading mechanism and drive system of Iran Post\'s parcel-sorting robots; generation 3 went into production in a run of 200 units.'),
    ('p-cnc-panel-open-m.webp', 'Control cabinet of a dual-purpose industrial CNC (2023)', 'Drive and motor selection, control cabinet build and G-code control set-up for a CNC with a table of about 100 × 100 cm.'),
    ('p-dmd-m.webp', 'DMD powder feeder (2019)', 'Complete electronics, control and machine logic, controlling the powder feed rate between 1 and 100 g/min.'),
   ],
   'faq': [
    ('Which PLC brands do you work with?', 'Delta and Siemens PLCs. We do the PLC programming and HMI design ourselves.'),
    ('Can you automate the machines we already have?', 'Yes. Integration with existing equipment is part of what we do; there is no need to replace the whole line.'),
    ('Do you build electrical and control cabinets?', 'Yes. We design and build machine power and control cabinets.'),
    ('How long does it take to automate one step of a line?', 'It depends on the size and complexity of the job — from one or two weeks for small jobs to several months for larger projects. We give the exact schedule with the quote.'),
    ('Do you also handle the mechanical side?', 'Yes. We also do the mechanical design, fabrication and assembly, so one team designs the mechanics and the controls together.'),
    FAQ_QUOTE['en'], FAQ_FILES['en'], FAQ_SUPPORT['en'], FAQ_AREA['en'],
   ],
  },
 },
 'parts-manufacturing': {
  'img': 'p-platform-m.webp',
  'fa': {
   'title': 'ساخت قطعات صنعتی طبق نقشه در تهران و اصفهان؛ ماشین‌کاری CNC، برش لیزر و سازه‌ی جوشی | انتها',
   'desc': 'ساخت قطعه و مجموعه‌ی صنعتی طبق نقشه، تک‌نمونه یا تیراژی: ماشین‌کاری CNC، برش لیزر، خم و نورد، سازه‌ی جوشی فولاد و استیل ۳۱۶، مخزن، قالب تزریق و بازرسی ابعادی. برای سراسر ایران.',
   'nav': 'ساخت قطعات صنعتی',
   'h1': 'ساخت قطعات صنعتی طبق نقشه، تک‌نمونه و تیراژی',
   'lead': [
    'گروه فنی مهندسی انتها قطعه‌ها و مجموعه‌های صنعتی را طبق نقشه‌ی شما، به‌صورت تک‌نمونه یا تیراژی، با کارگاه‌های همکار در تهران و اصفهان می‌سازد و پیش از تحویل خودش کنترل کیفیت می‌کند: ماشین‌کاری CNC، برش لیزر، خم‌کاری و نورد، سازه‌های جوشی فولادی و استیل ۳۱۶، محفظه و مخزن تحت فشار، قالب تزریق پلاستیک، و بازرسی ابعادی و جوش با GD&amp;T.',
    'چون خودمان طراح و سازنده‌ی دستگاه هستیم، قطعه را فقط از روی نقشه نمی‌سازیم؛ به جفت‌شدن قطعه‌ها در مونتاژ هم فکر می‌کنیم تا روز مونتاژ غافلگیر نشوید. برای کارفرمایان سراسر ایران کار می‌کنیم و برآورد قیمت رایگان است.',
   ],
   'facts': [
    ('فرآیندها', 'ماشین‌کاری CNC، برش لیزر، خم‌کاری، نورد، جوشکاری، قالب‌سازی، چاپ سه‌بعدی'),
    ('مواد', 'فولاد، استیل ۳۱۶ و هر ماده‌ای که کاربرد قطعه لازم دارد'),
    ('ابعاد کارهای قبلی', 'از قطعه‌های کوچک تا سازه‌هایی حدود ۱ تا ۲ تن'),
    ('تعداد سفارش', 'تک‌نمونه تا تیراژی'),
    ('نقشه', 'همه‌ی فرمت‌ها؛ مهندسی معکوس از روی نمونه'),
    ('کنترل کیفیت', 'بازرسی ابعادی و جوش، GD&amp;T، پیش از تحویل'),
    ('برآورد قیمت', 'رایگان، معمولاً ظرف ۱ تا ۲ هفته'),
    ('محل', 'تهران و اصفهان؛ برای سراسر ایران'),
   ],
   'what_h': 'چه قطعه‌ها و مجموعه‌هایی می‌سازیم؟',
   'what': [
    ('ماشین‌کاری CNC', 'تراش و فرز CNC قطعه‌های دقیق طبق نقشه و تلرانس‌های شما.'),
    ('برش لیزر، خم‌کاری و نورد ورق', 'ساخت قطعه‌های ورقی، بدنه و پوشش دستگاه‌ها.'),
    ('سازه‌های جوشی فولادی و استیل ۳۱۶', 'شاسی، استراکچر، سکو و سازه‌های بزرگ، تا حدود ۱ تا ۲ تن؛ همراه با نصب در محل در صورت نیاز.'),
    ('محفظه و مخزن تحت فشار', 'ساخت محفظه‌ها و مخازن صنعتی.'),
    ('قالب تزریق پلاستیک', 'طراحی و ماشین‌کاری قالب تزریق پلاستیک.'),
    ('چاپ سه‌بعدی قطعه و نمونه', 'نمونه‌ی اولیه، ماکت و قطعه با چاپ سه‌بعدی FDM و رزینی (DLP).'),
    ('بازرسی ابعادی و جوش (GD&amp;T)', 'کنترل ابعاد، تلرانس‌های هندسی و کیفیت جوش پیش از تحویل.'),
    ('مهندسی معکوس', 'تهیه‌ی نقشه از روی قطعه‌ی موجود، وقتی نقشه در دست نیست.'),
   ],
   'steps': [
    ('ارسال نقشه یا نمونه', 'نقشه در هر فرمتی، عکس یا نمونه‌ی فیزیکی، همراه با تعداد مورد نیاز.'),
    ('برآورد قیمت رایگان', 'بررسی نقشه، فرآیند ساخت و جنس مناسب؛ معمولاً ظرف ۱ تا ۲ هفته.'),
    ('بازبینی نقشه برای ساخت و مونتاژ', 'پیش از ساخت، نقشه را از نظر قابلیت ساخت و جفت‌شدن قطعه‌ها بررسی می‌کنیم.'),
    ('ساخت', 'ساخت در کارگاه‌های همکار تهران و اصفهان زیر نظر سرپرست ساخت گروه.'),
    ('کنترل کیفیت', 'بازرسی ابعادی و جوش پیش از تحویل.'),
    ('تحویل', 'تحویل قطعه یا مجموعه‌ی مونتاژشده، و نصب در محل در صورت نیاز.'),
   ],
   'projects': [
    ('p-platform-m.webp', 'پلتفرم متحرک ریلی روی استخر (۱۴۰۳)', 'سکو و اتاقک متحرک ریلی روی استخر آزمون کیفیت تصفیه‌ی آب؛ طراحی سازه، ساخت و نصب در محل.'),
    ('p-mold-m.webp', 'قالب تزریق پلاستیک (۱۳۹۹)', 'طراحی و ماشین‌کاری قالب تزریق پلاستیک.'),
    ('p-sorter-1-m.webp', 'تولید سری ربات‌های سورتر پستی', 'ساخت و مونتاژ ۸۰ ربات برای شرکت ملی پست (۵۰ دستگاه برای تهران و ۳۰ دستگاه برای کرمانشاه).'),
    ('p-dental-m.webp', 'الاینر ارتودنسی و لمینت دندان (۱۴۰۳)', 'امکان‌سنجی و تولید الاینر ارتودنسی و لمینت متحرک دندان با چاپ سه‌بعدی رزینی (DLP).'),
    ('p-maquette-m.webp', 'ماکت برش‌خورده‌ی موتور جت', 'ماکت آموزشی و نمایشی موتور جت، ساخته‌شده با چاپ سه‌بعدی.'),
   ],
   'faq': [
    ('سفارش تکی هم می‌پذیرید؟', 'بله. تک‌نمونه و تیراژی هر دو را می‌پذیریم؛ تعداد مناسب برای تولید تیراژی به حجم کار بستگی دارد.'),
    ('با چه موادی کار می‌کنید؟', 'جنس هر قطعه را بر اساس کاربرد همان قطعه انتخاب می‌کنیم: از فولاد و استیل ضدزنگ ۳۱۶ تا آلومینیوم، پلاستیک‌های مهندسی و کامپوزیت. اگر جنس در نقشه مشخص است، طبق نقشه می‌سازیم.'),
    ('قطعه‌ها و سازه‌های بزرگ هم می‌سازید؟', 'بله. سازه‌هایی تا حدود ۱ تا ۲ تن ساخته‌ایم و در صورت نیاز نصب در محل را هم انجام می‌دهیم.'),
    ('کیفیت قطعه‌ها را چطور کنترل می‌کنید؟', 'پیش از تحویل، بازرسی ابعادی و جوش را خودمان انجام می‌دهیم و تلرانس‌های هندسی (GD&amp;T) را کنترل می‌کنیم.'),
    ('اگر نقشه نداشته باشم چه؟', 'اگر قطعه‌ی نمونه دارید، با مهندسی معکوس از روی آن نقشه تهیه می‌کنیم. اگر فقط ایده یا شرح کار دارید، طراحی را هم خودمان انجام می‌دهیم.'),
    FAQ_QUOTE['fa'], FAQ_FILES['fa'], FAQ_SUPPORT['fa'], FAQ_AREA['fa'],
   ],
  },
  'en': {
   'title': 'Industrial Parts Manufacturing to Drawing in Tehran & Isfahan — CNC, Laser Cutting, Welded Structures | Enteha',
   'desc': 'Industrial parts and assemblies made to your drawings, one-off or in series: CNC machining, laser cutting, bending and rolling, steel and 316 stainless welded structures, vessels, injection moulds and dimensional inspection. Serving all of Iran.',
   'nav': 'Industrial parts manufacturing',
   'h1': 'Industrial parts made to your drawings — one-off or in series',
   'lead': [
    'Enteha Group makes industrial parts and assemblies to your drawings, one-off or in series, with partner workshops in Tehran and Isfahan, and carries out its own quality control before delivery: CNC machining, laser cutting, bending and rolling, welded structures in steel and 316 stainless, pressure vessels and enclosures, plastic injection moulds, and dimensional and weld inspection with GD&amp;T.',
    'Because we design and build machines ourselves, we do not just follow the drawing — we also think about how the parts fit together at assembly, so there are no surprises on assembly day. We work for clients across Iran, and quotes are free.',
   ],
   'facts': [
    ('Processes', 'CNC machining, laser cutting, bending, rolling, welding, mould making, 3D printing'),
    ('Materials', 'Steel, 316 stainless and whatever material the part\'s application calls for'),
    ('Size of past work', 'From small parts to structures of about 1–2 tonnes'),
    ('Order size', 'One-off to series'),
    ('Drawings', 'Any format; reverse engineering from a sample'),
    ('Quality control', 'Dimensional and weld inspection, GD&amp;T, before delivery'),
    ('Quote', 'Free, usually within 1–2 weeks'),
    ('Location', 'Tehran and Isfahan; serving all of Iran'),
   ],
   'what_h': 'What parts and assemblies do we make?',
   'what': [
    ('CNC machining', 'CNC turning and milling of precision parts to your drawings and tolerances.'),
    ('Laser cutting, bending and rolling', 'Sheet-metal parts, machine frames, housings and covers.'),
    ('Welded structures in steel and 316 stainless', 'Chassis, frames, platforms and large structures of up to about 1–2 tonnes, with on-site installation where needed.'),
    ('Pressure vessels and enclosures', 'Industrial enclosures and vessels.'),
    ('Plastic injection moulds', 'Design and machining of plastic injection moulds.'),
    ('3D-printed parts and prototypes', 'Prototypes, models and parts by FDM and resin (DLP) 3D printing.'),
    ('Dimensional and weld inspection (GD&amp;T)', 'Checking dimensions, geometric tolerances and weld quality before delivery.'),
    ('Reverse engineering', 'Drawings made from an existing part when no drawings are available.'),
   ],
   'steps': [
    ('Send drawings or a sample', 'Drawings in any format, photos or a physical sample, plus the quantity you need.'),
    ('Free quote', 'Review of the drawings, fabrication process and suitable material; usually within 1–2 weeks.'),
    ('Drawing review for fabrication and assembly', 'Before fabrication, we check the drawings for manufacturability and for how the parts fit together.'),
    ('Fabrication', 'Fabrication in partner workshops in Tehran and Isfahan, supervised by the group\'s manufacturing lead.'),
    ('Quality control', 'Dimensional and weld inspection before delivery.'),
    ('Delivery', 'Delivery of the parts or the assembled unit, with on-site installation where needed.'),
   ],
   'projects': [
    ('p-platform-m.webp', 'Rail-guided platform over a test pool (2024)', 'A rail-guided moving platform and cabin over a pool used for water treatment quality testing; structural design, fabrication and on-site installation.'),
    ('p-mold-m.webp', 'Plastic injection mould (2020)', 'Design and machining of a plastic injection mould.'),
    ('p-sorter-1-m.webp', 'Series production of postal sorting robots', 'Fabrication and assembly of 80 robots for Iran Post (50 units for Tehran and 30 for Kermanshah).'),
    ('p-dental-m.webp', 'Dental aligners & veneers (2024)', 'Feasibility study and production of orthodontic aligners and removable veneers by resin (DLP) 3D printing.'),
    ('p-maquette-m.webp', 'Jet engine cutaway model', 'A jet engine cutaway model for display and training, made by 3D printing.'),
   ],
   'faq': [
    ('Do you take one-off orders?', 'Yes. We take both one-off and series orders; the right quantity for series production depends on the job.'),
    ('Which materials do you work with?', 'We choose the material of each part for its application — from steel and 316 stainless to aluminium, engineering plastics and composites. If the drawing specifies the material, we follow the drawing.'),
    ('Do you make large parts and structures?', 'Yes. We have built structures of about 1–2 tonnes and can install them on site where needed.'),
    ('How do you control quality?', 'Before delivery we carry out our own dimensional and weld inspection and check geometric tolerances (GD&amp;T).'),
    ('What if I have no drawings?', 'If you have a sample part, we reverse-engineer drawings from it. If you only have an idea or a description, we can do the design as well.'),
    FAQ_QUOTE['en'], FAQ_FILES['en'], FAQ_SUPPORT['en'], FAQ_AREA['en'],
   ],
  },
 },
}

ICON_PHONE = '<svg viewBox="0 0 24 24" width="17" height="17" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8.1 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>'
ICON_GLOBE = '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg>'


def strip(s):
    """Plain text for JSON-LD (drops tags, decodes the one entity used)."""
    import re
    return re.sub(r'<[^>]+>', '', s).replace('&amp;', '&')


def jsonld(slug, lang, P):
    page_url = url(slug, lang)
    C = COMMON[lang]
    other = 'en' if lang == 'fa' else 'fa'
    home = SITE + ('?lang=' + lang)
    graph = [
        {'@type': 'Organization', '@id': ORG_ID, 'name': BRAND['en'],
         'alternateName': [BRAND['fa'], 'Enteha', 'انتها'], 'url': SITE, 'logo': SITE + 'logo.png',
         'email': EMAIL, 'telephone': PHONE, 'sameAs': [INSTAGRAM]},
        {'@type': 'WebPage', '@id': page_url + '#page', 'url': page_url, 'name': P['title'],
         'description': P['desc'], 'inLanguage': lang, 'isPartOf': {'@type': 'WebSite', 'url': SITE, 'name': BRAND[lang]},
         'about': {'@id': page_url + '#service'}, 'primaryImageOfPage': SITE + PAGES[slug]['img'],
         'dateModified': UPDATED['iso'], 'breadcrumb': {'@id': page_url + '#bc'},
         'translationOfWork' if lang == 'en' else 'workTranslation': {'@id': url(slug, other) + '#page'}},
        {'@type': 'BreadcrumbList', '@id': page_url + '#bc', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': C['home'], 'item': home},
            {'@type': 'ListItem', 'position': 2, 'name': C['services'], 'item': home + '#services'},
            {'@type': 'ListItem', 'position': 3, 'name': P['nav'], 'item': page_url}]},
        {'@type': 'Service', '@id': page_url + '#service', 'name': P['h1'], 'serviceType': P['nav'],
         'description': ' '.join(strip(x) for x in P['lead']), 'url': page_url, 'provider': {'@id': ORG_ID},
         'areaServed': {'@type': 'Country', 'name': 'Iran'},
         'availableChannel': {'@type': 'ServiceChannel', 'servicePhone': PHONE, 'serviceUrl': page_url + '#quote'},
         'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': strip(P['what_h']), 'itemListElement': [
             {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': strip(n), 'description': strip(d)}} for n, d in P['what']]}},
        {'@type': 'FAQPage', '@id': page_url + '#faq', 'inLanguage': lang, 'mainEntity': [
            {'@type': 'Question', 'name': strip(q), 'acceptedAnswer': {'@type': 'Answer', 'text': strip(a)}} for q, a in P['faq']]},
    ]
    return json.dumps({'@context': 'https://schema.org', '@graph': graph}, ensure_ascii=False)


def render(slug, lang):
    P = PAGES[slug][lang]
    C = COMMON[lang]
    other = 'en' if lang == 'fa' else 'fa'
    root = '' if lang == 'fa' else '../'
    rtl = lang == 'fa'
    home = root + 'index.html?lang=' + lang
    here = url(slug, lang)
    alt_href = (('en/' + slug + '.html') if lang == 'fa' else ('../' + slug + '.html'))

    def svc_href(s):
        return s + '.html'

    menu = ''.join('<a href="%s"%s>%s</a>' % (svc_href(s), ' aria-current="page" class="on"' if s == slug else '', PAGES[s][lang]['nav']) for s in ORDER)
    facts = ''.join('<div><dt>%s</dt><dd>%s</dd></div>' % f for f in P['facts'])
    what = ''.join('<li><h3>%s</h3><p>%s</p></li>' % w for w in P['what'])
    steps = ''.join('<li><h3>%s</h3><p>%s</p></li>' % s for s in P['steps'])
    projects = ''.join(
        '<article class="pj"><img src="%s%s" alt="%s" loading="lazy" width="640" height="480"><div><h3>%s</h3><p>%s</p></div></article>'
        % (root, img, strip(t), t, d) for img, t, d in P['projects'])
    inds = ''.join('<li>%s</li>' % i for i in C['industry_list'])
    why = ''.join('<li>%s</li>' % w for w in C['why_list'])
    team = ''.join(
        '<li><img src="%s%s" alt="%s" width="56" height="56" loading="lazy"><div><a href="%s" target="_blank" rel="noopener">%s</a><span>%s</span><small>%s</small></div></li>'
        % (root, av, n, li, n, r, e) for n, r, e, li, av in C['team_list'])
    faq = ''.join('<div class="qa"><h3>%s</h3><p>%s</p></div>' % qa for qa in P['faq'])
    related = ''.join('<a href="%s">%s <span aria-hidden="true">%s</span></a>' % (svc_href(s), PAGES[s][lang]['nav'], '←' if rtl else '→') for s in ORDER if s != slug)
    font = 'Vazirmatn'

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{'rtl' if rtl else 'ltr'}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{P['title']}</title>
<meta name="description" content="{P['desc']}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{here}">
<link rel="alternate" hreflang="{lang}" href="{here}">
<link rel="alternate" hreflang="{other}" href="{url(slug, other)}">
<link rel="alternate" hreflang="x-default" href="{url(slug, 'fa')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND[lang]}">
<meta property="og:title" content="{P['title']}">
<meta property="og:description" content="{P['desc']}">
<meta property="og:url" content="{here}">
<meta property="og:locale" content="{'fa_IR' if rtl else 'en_US'}">
<meta property="og:image" content="{SITE}cover.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#16191D">
<link rel="icon" type="image/png" href="{root}favicon.png">
<link rel="icon" href="{root}favicon.ico" sizes="any">
<link rel="apple-touch-icon" href="{root}apple-touch-icon.png">
<script type="application/ld+json">{jsonld(slug, lang, P)}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={font}:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{root}services.css">
</head>
<body>
<nav><div class="wrap">
  <a href="{home}" class="brand"><img src="{root}logo-96.webp" width="34" height="34" alt="">{BRAND[lang]}</a>
  <div class="menu">{menu}<a href="#quote" class="nav-cta">{C['contact']}</a></div>
  <div class="tools">
    <a class="lang" href="{alt_href}" hreflang="{other}" lang="{other}" data-lang="{other}">{ICON_GLOBE}{C['switch']}</a>
    <a href="tel:{PHONE}" class="nav-phone" aria-label="{C['call_btn']}">{ICON_PHONE}</a>
  </div>
</div></nav>
<header class="hero"><div class="wrap">
  <ol class="bc"><li><a href="{home}">{C['home']}</a></li><li><a href="{home}#services">{C['services']}</a></li><li aria-current="page">{P['nav']}</li></ol>
  <h1>{P['h1']}</h1>
  {''.join('<p class="lead">%s</p>' % x for x in P['lead'])}
  <div class="btns"><a class="btn btn-gold" href="#quote">{C['quote_btn']}</a><a class="btn btn-ghost" href="tel:{PHONE}">{ICON_PHONE}<span class="ltr">{PHONE_TXT[lang]}</span></a></div>
</div></header>
<main>
<section class="block"><div class="wrap">
  <h2>{C['glance']}</h2>
  <dl class="facts">{facts}</dl>
</div></section>
<section class="block alt"><div class="wrap">
  <h2>{P['what_h']}</h2>
  <ul class="what">{what}</ul>
</div></section>
<section class="block"><div class="wrap">
  <h2>{C['process']}</h2>
  <ol class="steps">{steps}</ol>
</div></section>
<section class="block alt"><div class="wrap">
  <h2>{C['work']}</h2>
  <div class="pjs">{projects}</div>
  <p class="more"><a href="{home}#projects">{'همه‌ی نمونه‌کارها' if rtl else 'All projects'} <span aria-hidden="true">{'←' if rtl else '→'}</span></a></p>
</div></section>
<section class="block"><div class="wrap two">
  <div><h2>{C['why']}</h2><ul class="why">{why}</ul></div>
  <div><h2>{C['industries']}</h2><ul class="inds">{inds}</ul>
  <h2 class="mt">{C['team']}</h2><ul class="team">{team}</ul></div>
</div></section>
<section class="block alt" id="faq"><div class="wrap">
  <h2>{C['faq']}</h2>
  <div class="faq">{faq}</div>
</div></section>
<section class="block quote" id="quote"><div class="wrap">
  <h2>{C['cta_h']}</h2>
  <p>{C['cta_p']}</p>
  <form class="cform" id="contactForm" action="{FORM}" method="POST">
    <input type="hidden" name="_subject" value="Enteha Group website — {PAGES[slug]['en']['nav']}">
    <input type="hidden" name="source" value="{here}">
    <div class="cf-row"><input type="text" name="name" placeholder="{C['name']}" aria-label="{C['name']}" required><input type="email" name="email" placeholder="{C['email']}" aria-label="{C['email']}" required></div>
    <textarea name="message" rows="4" placeholder="{C['msg']}" aria-label="{C['msg']}" required></textarea>
    <button type="submit" class="cf-btn">{C['send']}</button>
    <div class="cf-status" id="cfStatus" aria-live="polite"></div>
  </form>
  <p class="c-other">{C['other']}</p>
  <div class="c-links"><a href="tel:{PHONE}"><span>{PHONE_TXT[lang]}</span></a><a href="mailto:{EMAIL}"><span>{EMAIL}</span></a><a href="{INSTAGRAM}" target="_blank" rel="noopener"><span>@enteha.eng</span></a></div>
</div></section>
<section class="block"><div class="wrap">
  <h2>{C['related']}</h2>
  <div class="related">{related}</div>
  <p class="upd">{C['updated']} <time datetime="{UPDATED['iso']}">{UPDATED[lang]}</time></p>
</div></section>
</main>
<footer>© <span id="yr">{'۱۴۰۵' if rtl else '2026'}</span> {BRAND[lang]} — {C['rights']}</footer>
<script>
(function(){{
  var M = {json.dumps({k: C[k] for k in ('sending', 'ok', 'err', 'net')}, ensure_ascii=False)};
  document.querySelector('a.lang').addEventListener('click', function(){{ try{{ localStorage.setItem('enteha-lang', this.dataset.lang); }}catch(e){{}} }});
  var f = document.getElementById('contactForm');
  f.addEventListener('submit', function(e){{
    e.preventDefault();
    var st = document.getElementById('cfStatus'), b = f.querySelector('.cf-btn'), old = b.textContent;
    st.textContent = ''; st.className = 'cf-status'; b.disabled = true; b.textContent = M.sending;
    fetch(f.action, {{method:'POST', body:new FormData(f), headers:{{'Accept':'application/json'}}}})
      .then(function(r){{ if(r.ok){{ f.reset(); st.textContent = M.ok; st.className = 'cf-status ok'; }} else {{ st.textContent = M.err; st.className = 'cf-status err'; }} }})
      .catch(function(){{ st.textContent = M.net; st.className = 'cf-status err'; }})
      .then(function(){{ b.disabled = false; b.textContent = old; }});
  }});
}})();
</script>
</body>
</html>
'''


def main():
    os.makedirs('en', exist_ok=True)
    for slug in ORDER:
        for lang in ('fa', 'en'):
            path = (slug + '.html') if lang == 'fa' else os.path.join('en', slug + '.html')
            with open(path, 'w', encoding='utf-8') as fh:
                fh.write(render(slug, lang))
            print('wrote', path)


if __name__ == '__main__':
    main()
