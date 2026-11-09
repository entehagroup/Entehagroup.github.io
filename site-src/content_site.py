# -*- coding: utf-8 -*-
"""همه‌ی متن‌های سایت انتها (فارسی و انگلیسی کنار هم).
بعد از هر تغییر، از ریشه‌ی ریپازیتوری بسازید:  python3 site-src/build_site.py
راهنمای کامل در site-src/README.md است.
"""

# ---------------------------------------------------------------- تنظیمات
BASE = "https://entehagroup.ir"          # آدرس سایت، بدون / در آخر
GA_ID = ""                               # شناسه‌ی گوگل آنالیتیکس (مثل G-XXXXXXX)؛ خالی = بدون آنالیتیکس
FORMSPREE = "https://formspree.io/f/mrevzvga"
PHONE = "+989962233898"
PHONE_TXT = {"fa": "۰۹۹۶۲۲۳۳۸۹۸", "en": "+98 996 223 3898"}
EMAIL = "Nasiri2752@Gmail.com"
INSTAGRAM = "https://www.instagram.com/enteha.eng/"
INSTAGRAM_HANDLE = "@enteha.eng"
RESUME = {"en": "enteha-resume-en-v1.4.pdf", "fa": "enteha-resume-fa-v1.4.pdf"}

NAME = {"fa": "گروه فنی مهندسی انتها", "en": "Enteha Group"}
ALT_NAMES = ["Enteha Group", "Enteha", "Enteha Engineering Group", "گروه فنی مهندسی انتها", "گروه انتها", "انتها"]
# جمله‌ی تمایز: فقط در داده‌ی ساخت‌یافته و llms.txt می‌آید، نه در متن قابل‌دیدن
DISAMBIG = {
    "en": "Enteha Group (گروه فنی مهندسی انتها) is a mechanical engineering design-and-build group based in Tehran and Isfahan, Iran; it is not related to other businesses that use the word “Enteha” (انتها, “end”) in their names.",
    "fa": "گروه فنی مهندسی انتها یک گروه طراحی و ساخت مهندسی مکانیک در تهران و اصفهان است و با کسب‌وکارهای دیگری که واژه‌ی «انتها» در نامشان است ارتباطی ندارد.",
}

# ---------------------------------------------------------------- متن‌های کوتاه رابط
UI = {
 "fa": {
  "nav": [("services", "خدمات"), ("projects", "نمونه‌کارها"), ("about", "درباره و تیم")],
  "contact": "تماس", "lang_label": "English", "call": "تماس تلفنی", "home": "خانه",
  "year": "سال", "view": "مشاهده ›", "photos": "تصویر", "who": "انجام‌دهنده",
  "examples": "نمونه‌ها:", "details": "جزئیات و پرسش‌های متداول ←", "quote": "درخواست برآورد قیمت ←",
  "all_projects": "همه‌ی نمونه‌کارها ←", "all_services": "همه‌ی خدمات ←", "more_about": "درباره‌ی گروه و تیم ←",
  "all_honors": "همه‌ی افتخارات ←",
  "key_facts": "در یک نگاه", "team_role": "انجام‌دهنده", "field": "حوزه", "service": "خدمت مرتبط",
  "awards": "افتخارات این پروژه", "similar": "پروژه‌ی مشابهی دارید؟",
  "similar_p": "شرح کار، نقشه یا عکس را بفرستید؛ برآورد قیمت رایگان است و معمولاً ظرف یک تا دو هفته آماده می‌شود.",
  "start": "درخواست برآورد قیمت", "prev": "پروژه‌ی قبلی", "next": "پروژه‌ی بعدی",
  "resume_en": "رزومه‌ی انگلیسی (<bdi>PDF</bdi>)", "resume_fa": "رزومه‌ی فارسی (<bdi>PDF</bdi>)",
  "rights": "همه‌ی حقوق محفوظ است.", "play": "پخش: ", "updated": "آخرین به‌روزرسانی:",
  "why": "چرا انتها؟", "industries": "صنایعی که برایشان کار کرده‌ایم", "team_h": "چه کسانی کار را انجام می‌دهند؟",
  "related": "خدمات دیگر انتها", "process": "مراحل کار", "work": "نمونه‌کارهای مرتبط", "faq": "پرسش‌های متداول",
  "glance": "در یک نگاه", "logo_alt": "لوگوی گروه فنی مهندسی انتها", "cover_alt": "نمونه‌ای از ماشین‌ها و ربات‌هایی که گروه انتها طراحی و ساخته است",
  "photo": "تصویر ", "close": "بستن", "prev_img": "قبلی", "next_img": "بعدی", "linkedin": "لینکدین",
  "view_paper": "مشاهده‌ی مقاله ↗", "published": "سال انتشار", "our_role": "نقش ما",
 },
 "en": {
  "nav": [("services", "Services"), ("projects", "Projects"), ("about", "About & team")],
  "contact": "Contact", "lang_label": "فارسی", "call": "Call", "home": "Home",
  "year": "Year", "view": "View ›", "photos": "photos", "who": "Done by",
  "examples": "Examples:", "details": "Details & FAQ →", "quote": "Request a quote →",
  "all_projects": "All projects →", "all_services": "All services →", "more_about": "About the group and team →",
  "all_honors": "All honors →",
  "key_facts": "At a glance", "team_role": "Done by", "field": "Field", "service": "Related service",
  "awards": "Recognition", "similar": "Have a similar project?",
  "similar_p": "Send a description, drawings or photos. Quotes are free and usually ready within one to two weeks.",
  "start": "Request a quote", "prev": "Previous project", "next": "Next project",
  "resume_en": "Resume · English (PDF)", "resume_fa": "Resume · Persian (PDF)",
  "rights": "All rights reserved.", "play": "Play: ", "updated": "Last updated:",
  "why": "Why Enteha?", "industries": "Industries we have worked for", "team_h": "Who does the work?",
  "related": "Other Enteha services", "process": "How we work", "work": "Related projects", "faq": "Frequently asked questions",
  "glance": "At a glance", "logo_alt": "Enteha Group logo", "cover_alt": "Machines and robots designed and built by Enteha Group",
  "photo": "Photo ", "close": "Close", "prev_img": "Previous", "next_img": "Next", "linkedin": "LinkedIn",
  "view_paper": "View paper ↗", "published": "Published", "our_role": "Our role",
 },
}

CONTACT = {
 "fa": {"h": "تماس", "p": "برای پروژه‌های طراحی، ساخت یا اتوماسیون، فرم زیر را پر کنید یا مستقیم با ما تماس بگیرید. برآورد قیمت رایگان است و معمولاً ظرف یک تا دو هفته آماده می‌شود.",
        "name": "نام شما", "email": "ایمیل شما", "msg": "شرح پروژه…", "send": "ارسال پیام", "other": "راه‌های ارتباطی دیگر:",
        "sending": "در حال ارسال…", "ok": "پیام شما ارسال شد. به‌زودی پاسخ می‌دهیم.",
        "err": "ارسال انجام نشد. لطفاً دوباره تلاش کنید یا از ایمیل استفاده کنید.", "net": "ارسال انجام نشد. اتصال اینترنت را بررسی کنید."},
 "en": {"h": "Contact", "p": "For design, fabrication or automation projects, use the form below or reach us directly. Quotes are free and usually ready within one to two weeks.",
        "name": "Your name", "email": "Your email", "msg": "Describe your project…", "send": "Send message", "other": "Other ways to reach us:",
        "sending": "Sending…", "ok": "Your message has been sent. We'll get back to you soon.",
        "err": "Sending failed. Please try again or use email.", "net": "Sending failed. Please check your connection."},
}

# ---------------------------------------------------------------- صفحه‌ی اصلی
HOME = {
 "fa": {
  "title": "گروه فنی مهندسی انتها — طراحی و ساخت دستگاه، ربات صنعتی و اتوماسیون در تهران و اصفهان",
  "desc": "گروه فنی مهندسی انتها دستگاه‌های خاص‌منظوره و ربات‌های صنعتی سفارشی را طراحی می‌کند و می‌سازد، خط تولید را خودکار می‌کند و قطعه‌ی صنعتی طبق نقشه می‌سازد. تهران و اصفهان، برای سراسر ایران.",
  "cta1": "خدمات ما", "cta2": "نمونه‌کارها",
  "about_kk": "معرفی", "about_h": "درباره‌ی گروه",
  "numbers": "در کارنامه‌ی اعضای گروه: ساخت ۸۰ ربات سورتر برای شرکت ملی پست و طراحی نسل سومی که در تیراژ ۲۰۰ دستگاه به تولید رسید، نخستین دستگاه تست پروتز زانو از این نوع در ایران، پنج پرینتر سه‌بعدی صنعتی، و جوایزی از جمله جایزه‌ی البرز نخبگانی و دو بار مقام دوم جشنواره‌ی جوان خوارزمی.",
  "svc_kk": "حوزه‌های کاری", "svc_h": "خدمات ما", "svc_p": "سه حوزه‌ی کاری؛ هر کدام با نمونه‌کار واقعی و صفحه‌ای با جزئیات و پرسش‌های متداول.",
  "proj_kk": "نمونه‌کارها", "proj_h": "پروژه‌های منتخب", "proj_p": "روی هر پروژه کلیک کنید تا تصویرها و جزئیات آن را ببینید. عکس‌های کوچک، انجام‌دهنده‌ی کار را نشان می‌دهند.",
  "clip_kk": "کلیپ‌ها", "clip_h": "ویدیوها",
  "team_kk": "اعضای تیم", "team_h": "هسته‌ی اصلی تیم", "team_p": "هر پروژه را عضوی از هسته‌ی اصلی هدایت می‌کند که در حوزه‌ی تخصص اوست و کارگاه‌ها و مهندسان متخصص همکار در ساخت، تحلیل و کنترل کیفی به کار می‌پیوندند.",
  "hon_kk": "دستاوردها", "hon_h": "افتخارات و جوایز", "hon_p": "جوایز ملی برای دستگاه‌ها، ربات‌ها و پژوهش‌های اعضای گروه.",
 },
 "en": {
  "title": "Enteha Group — Custom Machines, Industrial Robots & Automation in Tehran and Isfahan",
  "desc": "Enteha Group designs and builds special-purpose machines and custom industrial robots, automates production lines, and manufactures industrial parts to drawing. Tehran and Isfahan, serving clients across Iran.",
  "cta1": "Our services", "cta2": "Projects",
  "about_kk": "Who we are", "about_h": "About the group",
  "numbers": "Our members' track record includes 80 postal sorting robots built for Iran Post and a third-generation design produced as a 200-unit series, the first knee-prosthesis test rig of its kind in Iran, five industrial 3D printers, and awards including the Alborz Elite Prize and two second places at the Khwarizmi Youth Festival.",
  "svc_kk": "Services", "svc_h": "What we do", "svc_p": "Three service lines, each with real projects and a page of details and FAQs.",
  "proj_kk": "Portfolio", "proj_h": "Selected projects", "proj_p": "Click a project to see its photos and details. The small portraits show who did it.",
  "clip_kk": "Clips", "clip_h": "Videos",
  "team_kk": "Team", "team_h": "The core team", "team_p": "Each project is led by the core member whose field it falls in; partner workshops and specialist engineers join for fabrication, analysis and quality control.",
  "hon_kk": "Achievements", "hon_h": "Honors & awards", "hon_p": "National awards for the machines, robots and research of our team.",
 },
}

# ---------------------------------------------------------------- صفحه‌ی خدمات (نمای کلی)
SERVICES_PAGE = {
 "fa": {"title": "خدمات گروه فنی مهندسی انتها: ساخت دستگاه و ربات سفارشی، اتوماسیون، ساخت قطعه",
        "desc": "سه حوزه‌ی کاری انتها: طراحی و ساخت دستگاه خاص‌منظوره و ربات صنعتی، اتوماسیون خط تولید و ساخت قطعات صنعتی طبق نقشه. روند همکاری و پرسش‌های متداول.",
        "kk": "خدمات", "h1": "خدمات گروه فنی مهندسی انتها",
        "lead": "از ایده تا دستگاهی که روی خط تولید کار می‌کند: طراحی، تحلیل، ساخت، مونتاژ، کنترل کیفیت و راه‌اندازی، با یک تیم و یک مسئول از ابتدا تا انتها.",
        "svc_h": "سه حوزه‌ی کاری", "steps_h": "روند همکاری", "faq_h": "پرسش‌های متداول"},
 "en": {"title": "Enteha Group services: custom machines and robots, automation, parts manufacturing",
        "desc": "Enteha's three service lines: special-purpose machines and industrial robots, production line automation, and industrial parts made to drawing. How we work and FAQs.",
        "kk": "Services", "h1": "What Enteha Group does",
        "lead": "From an idea to a machine running on your line: design, analysis, fabrication, assembly, quality control and commissioning — one team, and one owner from start to finish.",
        "svc_h": "Three service lines", "steps_h": "How we work together", "faq_h": "Frequently asked questions"},
}

STEPS = {
 "fa": [("نیازسنجی", "شرح کار، نقشه در هر فرمتی، عکس یا نمونه را می‌فرستید و ظرفیت، دقت و محدودیت‌ها را با هم مشخص می‌کنیم."),
        ("برآورد قیمت رایگان", "پس از بررسی فنی و مشورت با مشاوران گروه، معمولاً ظرف یک تا دو هفته قیمت و زمان‌بندی را اعلام می‌کنیم."),
        ("طراحی و تحلیل", "طراحی مفهومی و تفصیلی و تحلیل مهندسی، با تأیید شما در هر مرحله."),
        ("ساخت، مونتاژ و کنترل کیفیت", "ساخت در کارگاه‌های همکار تهران و اصفهان، زیر نظر همان مهندسی که طراحی کرده، و بازرسی پیش از تحویل."),
        ("تحویل و پشتیبانی", "تحویل و راه‌اندازی، و رفع ایراد تا دو ماه پس از تحویل؛ ضمانت و ارتقا طبق قرارداد.")],
 "en": [("Requirements", "You send a description, drawings in any format, photos or a sample, and together we pin down capacity, accuracy and constraints."),
        ("Free quote", "After a technical review and consultation with our advisers, we usually send the price and schedule within one to two weeks."),
        ("Design and analysis", "Concept and detailed design and engineering analysis, with your approval at each stage."),
        ("Fabrication, assembly and QC", "Fabrication in partner workshops in Tehran and Isfahan, supervised by the engineer who designed it, and inspection before delivery."),
        ("Delivery and support", "Delivery and commissioning, and faults fixed for two months after delivery; warranty and upgrades by contract.")],
}

FAQ = {
 "fa": [
  ("گروه فنی مهندسی انتها چیست؟", "گروهی از مهندسان مکانیک در تهران و اصفهان که دستگاه‌ها و ربات‌های صنعتی سفارشی طراحی می‌کند و می‌سازد، خط تولید را خودکار می‌کند و قطعه‌ی صنعتی طبق نقشه می‌سازد. هسته‌ی گروه سه مهندس دانش‌آموخته‌ی دانشگاه‌های صنعتی شریف، علم و صنعت، خواجه نصیر و تربیت مدرس است که با شبکه‌ای از کارگاه‌ها و متخصصان همکار کار می‌کنند."),
  ("چه کارهایی انجام می‌دهید؟", "سه حوزه‌ی کاری داریم: طراحی و ساخت دستگاه خاص‌منظوره، تجهیزات آزمون و ربات صنعتی؛ اتوماسیون خط تولید (<bdi>PLC</bdi> دلتا و زیمنس، <bdi>HMI</bdi>، کنترل حرکت و تابلو برق)؛ و ساخت قطعات و سازه‌های صنعتی طبق نقشه با کنترل کیفیت پیش از تحویل."),
  ("چه کسانی پشت انتها هستند؟", "حسن نصیری خونساری (مدیر فنی و طراحی)، علیرضا پیرحاجی (سرپرست ساخت و کنترل کیفیت) و سید مصطفی بنی‌هاشمی (سرپرست پروژه و تحقیق و توسعه)."),
  ("کجا هستید و برای کدام شهرها کار می‌کنید؟", "دفتر و کارگاه‌های همکار ما در تهران و اصفهان است، ولی برای کارفرمایان سراسر ایران کار می‌کنیم."),
  ("هزینه و زمان کار چقدر است؟", "قیمت به پیچیدگی، ابعاد، دقت و تعداد بستگی دارد. برآورد قیمت رایگان است و معمولاً یک تا دو هفته طول می‌کشد. زمان اجرا از یک تا دو هفته تا حدود یک سال است؛ برای یک دستگاه خاص‌منظوره‌ی ساده، طراحی ۱ تا ۲ ماه و ساخت هم ۱ تا ۲ ماه."),
  ("سفارش تکی هم می‌پذیرید؟", "بله. از یک دستگاه یا یک قطعه تا تولید سری را می‌پذیریم؛ تعداد مناسب برای تولید سری به حجم کار بستگی دارد."),
  ("چطور شروع کنیم؟", "شرح کار را با فرم همین صفحه، تلفن، ایمیل یا اینستاگرام بفرستید. نقشه در هر فرمتی، عکس یا طرح دستی کافی است؛ اگر فقط نمونه‌ی فیزیکی دارید، با مهندسی معکوس نقشه را تهیه می‌کنیم."),
  ("بعد از تحویل چه پشتیبانی‌ای دارید؟", "ایرادهای دستگاه‌هایی را که خودمان طراحی کرده و ساخته‌ایم تا دو ماه پس از تحویل رفع می‌کنیم. ضمانت طولانی‌تر، تعمیر و ارتقا را هر طور که کارفرما بخواهد در قرارداد می‌گنجانیم. اگر طرح از کارفرما بوده و کار ما فقط ساخت بوده، رفع ایراد ناشی از طرح با هزینه‌ی جداگانه انجام می‌شود."),
 ],
 "en": [
  ("What is Enteha Group?", "A group of mechanical engineers in Tehran and Isfahan that designs and builds custom industrial machines and robots, automates production lines and manufactures industrial parts to drawing. Its core is three engineers from Sharif University of Technology, IUST, K. N. Toosi and Tarbiat Modares University, working with a network of partner workshops and specialists."),
  ("What do you do?", "We have three service lines: design and build of special-purpose machines, test rigs and industrial robots; production line automation (Delta and Siemens PLC, HMI, motion control and control cabinets); and industrial parts and structures made to drawing, with quality control before delivery."),
  ("Who is behind Enteha?", "Hassan Nasiri Khonsari (Technical & Design Director), Alireza Pirhaji (Manufacturing & Quality Lead) and Seyed Mostafa Banihashemi (Project & R&D Lead)."),
  ("Where are you, and which cities do you work in?", "Our office and partner workshops are in Tehran and Isfahan, but we work for clients across Iran."),
  ("How much does it cost and how long does it take?", "The price depends on complexity, size, accuracy and quantity. Quotes are free and usually take one to two weeks. Projects take anything from one or two weeks to about a year; for a simple special-purpose machine, design takes 1–2 months and fabrication another 1–2 months."),
  ("Do you take one-off orders?", "Yes. We take everything from a single machine or part to series production; the right quantity for a series depends on the job."),
  ("How do we get started?", "Send us a description of the job using the form on this page, by phone, email or Instagram. Drawings in any format, photos or a hand sketch are enough; if you only have a physical sample, we reverse-engineer the drawings from it."),
  ("What support do you give after delivery?", "For machines we designed and built ourselves, we fix any faults for two months after delivery. A longer warranty, repairs and upgrades can be written into the contract however the client wants. If the design came from the client and we only did the fabrication, faults caused by the design are fixed for a separate fee."),
 ],
}

# ---------------------------------------------------------------- صفحه‌ی نمونه‌کارها و درباره
PROJECTS_PAGE = {
 "fa": {"title": "نمونه‌کارهای گروه فنی مهندسی انتها: ربات، دستگاه خاص‌منظوره، اتوماسیون و ساخت",
        "desc": "۱۳ پروژه‌ی طراحی و ساخت اعضای گروه انتها: ربات‌های سورتر پستی، دستگاه تست پروتز زانو، پرینترهای سه‌بعدی صنعتی، CNC، ربات‌های گارسون، سازه‌ی ریلی و قالب تزریق.",
        "kk": "نمونه‌کارها", "h1": "نمونه‌کارها",
        "lead": "پروژه‌هایی که اعضای گروه طراحی کرده و ساخته‌اند؛ هر کدام صفحه‌ای با تصویرها، جزئیات فنی و انجام‌دهنده‌ی کار دارد."},
 "en": {"title": "Enteha Group projects: robots, special-purpose machines, automation and fabrication",
        "desc": "13 design-and-build projects by Enteha's members: postal sorting robots, a knee prosthesis test rig, industrial 3D printers, a CNC, waiter robots, a rail-guided structure and an injection mould.",
        "kk": "Projects", "h1": "Projects",
        "lead": "Projects our members have designed and built; each has a page with photos, technical details and who did the work."},
}

ABOUT_PAGE = {
 "fa": {"title": "درباره‌ی گروه فنی مهندسی انتها: تیم، افتخارات، پژوهش و سوابق",
        "desc": "گروه فنی مهندسی انتها: سه مهندس مکانیک از دانشگاه‌های شریف، علم و صنعت، خواجه نصیر و تربیت مدرس با شبکه‌ای از کارگاه‌ها و متخصصان همکار در تهران و اصفهان. تیم، جوایز، مقالات، مهارت‌ها و سوابق.",
        "kk": "درباره", "h1": "درباره‌ی گروه فنی مهندسی انتها",
        "team_h": "هسته‌ی اصلی تیم", "hon_h": "افتخارات و جوایز", "pub_h": "مقالات علمی", "pub_p": "مقالات مجله و کنفرانسی اعضای گروه.",
        "skills_h": "مهارت‌ها و نرم‌افزارها", "exp_h": "تجربه‌ی حرفه‌ای"},
 "en": {"title": "About Enteha Group: team, honors, research and experience",
        "desc": "Enteha Group: three mechanical engineers from Sharif, IUST, K. N. Toosi and Tarbiat Modares universities, with partner workshops and specialists in Tehran and Isfahan. Team, awards, papers, skills and experience.",
        "kk": "About", "h1": "About Enteha Group",
        "team_h": "The core team", "hon_h": "Honors & awards", "pub_h": "Publications", "pub_p": "Journal and conference papers by the team.",
        "skills_h": "Skills & software", "exp_h": "Professional experience"},
}

# ---------------------------------------------------------------- کلیپ‌ها (ویدیو روی خود سایت)
CLIPS = [
 {"slug": "outsourcing", "video": "v-outsourcing.mp4", "poster": "v-outsourcing.jpg", "date": "2026-10-31", "duration": "PT1M",
  "fa": {"title": "برون‌سپاری بی‌دردسر", "year": "۱۴۰۵",
         "desc": "قطعه‌ها را تک‌تک تحویل گرفته‌اید و همه درست به نظر می‌رسند، ولی روز مونتاژ با هم جفت نمی‌شوند؛ چون طراحی، ساخت و مونتاژ دست چند نفر مختلف بوده و کسی کل دستگاه را نمی‌دیده. در انتها کسی که طراحی می‌کند تا آخر کار بالای سر ساخت و مونتاژ می‌ماند؛ از دستگاه خاص‌منظوره و اتوماسیون خط تولید تا قطعه‌ی تیراژی."},
  "en": {"title": "Hassle-free outsourcing", "year": "2026",
         "desc": "Every part arrives and each one looks right, yet on assembly day they don't fit together — because design, fabrication and assembly were in different hands and nobody saw the whole machine. At Enteha, the person who designs it stays with fabrication and assembly to the end: from special-purpose machines and production line automation to parts in series."}},
]

# بالای صفحه‌ی اصلی
HERO = {
 "headline": {
  "fa": "ربات‌های صنعتی، <b>ماشین‌آلات سفارشی</b> و اتوماسیون؛ طراحی و ساخت در یک تیم.",
  "en": "Industrial robots, <b>custom machinery</b> and automation — designed and built by one team.",
 },
 "lead": {
  "fa": "هسته‌ی اصلی ما را مهندسان مکانیک باتجربه از دانشگاه‌های صنعتی شریف، علم و صنعت، خواجه نصیر و تربیت مدرس تشکیل می‌دهند که در کنار شبکه‌ای از کارگاه‌های صنعتی و متخصصان همکار، پروژه را از طراحی مفهومی تا ساخت، کنترل کیفیت و راه‌اندازی پیش می‌برند.",
  "en": "Our core team of experienced mechanical engineers from Sharif, IUST, K. N. Toosi and Tarbiat Modares universities works with a network of partner workshops and specialists — taking each project from concept design through fabrication, quality control and commissioning.",
 },
 "eyebrow": {"fa": "طراحی مکانیک · ساخت · رباتیک", "en": "Mechanical design · Fabrication · Robotics"},
}

# معرفی گروه (صفحه‌ی اصلی و صفحه‌ی درباره)
ABOUT_PARAS = [
 {
  "fa": "گروه فنی مهندسی انتها دستگاه‌ها، ربات‌ها و تجهیزات صنعتی سفارشی طراحی می‌کند و می‌سازد. هسته‌ی اصلی گروه را سه مهندس مکانیک کاربلد تشکیل می‌دهند که با شبکه‌ی گسترده‌ای از همکاران، از کارگاه‌های صنعتی تا مهندسان متخصص در تحلیل، کنترل کیفی و مشاوره، کار می‌کنند. در هر پروژه، هر بخش از کار به خبره‌ترین افراد همان حوزه سپرده می‌شود؛ در کل زنجیره‌ی طراحی مفهومی و تفصیلی، تحلیل مهندسی، ساخت و مونتاژ، کنترل کیفیت و راه‌اندازی.",
  "en": "Enteha Group designs and builds custom industrial machines, robots and equipment. At its core are three experienced mechanical engineers, working with a wide network of collaborators — from industrial workshops to specialist engineers in analysis, quality control and consulting. On every project, each part of the work goes to the people best qualified for it, across the whole chain: concept and detailed design, engineering analysis, fabrication and assembly, quality control and commissioning.",
 },
 {
  "fa": "تخصص‌های ما مکمل یکدیگرند: طراحی ماشین و ربات، مکاترونیک و اتوماسیون؛ ساخت و تولید، کامپوزیت و کنترل کیفیت؛ و طراحی مکانیزم، کنترل و رباتیک پزشکی. مدرک‌های ما از چهار دانشگاه صنعتی برتر کشور است.",
  "en": "Our backgrounds complement each other: machine and robot design, mechatronics and automation; manufacturing, composites and quality control; and mechanism design, control and medical robotics. Between us we hold degrees from four of Iran's leading technical universities.",
 },
 {
  "fa": "کارهای ما در جایزه‌ی البرز نخبگانی، جشنواره‌ی جوان خوارزمی، جشنواره‌ی طراحی صنعتی ایران و پارک علم و فناوری شریف برگزیده شده و در مجله‌های <bdi>Scientific Reports</bdi> و <bdi>International Journal of Mechanical Sciences</bdi> منتشر شده است.",
  "en": "Our work has been recognised by the Alborz Elite Prize, the Khwarizmi Youth Festival, the Iran Industrial Design Festival and Sharif Science and Technology Park, and published in Scientific Reports and the International Journal of Mechanical Sciences.",
 },
]

# جدول کنار معرفی: [عنوان، مقدار]
ABOUT_FACTS = [
 {"fa": ["مستقر در", "تهران و اصفهان"], "en": ["Based in", "Tehran & Isfahan, Iran"]},
 {"fa": ["تیم", "هسته‌ی مهندسی و شبکه‌ی همکاران"], "en": ["Team", "Core engineers + partner network"]},
 {
  "fa": ["دانشگاه‌ها", "شریف · علم و صنعت · خواجه نصیر · تربیت مدرس"],
  "en": ["Universities", "Sharif · IUST · KNTU · TMU"],
 },
 {"fa": ["دامنه‌ی کار", "طراحی، ساخت، کنترل کیفیت، تحویل"], "en": ["Scope", "Design → build → QC → delivery"]},
 {"fa": ["وضعیت", "آماده‌ی پذیرش پروژه"], "en": ["Status", "Open to new projects"]},
]

# اعضای هسته‌ی تیم؛ کلیدها (h، a، m) در فیلد who پروژه‌ها، افتخارات و سوابق به کار می‌روند
PEOPLE = {
 "h": {
  "name": {"fa": "حسن نصیری خونساری", "en": "Hassan Nasiri Khonsari"},
  "role": {"fa": "مدیر فنی و طراحی", "en": "Technical & Design Director"},
  "edu": {
   "fa": "کارشناسی ارشد طراحی کاربردی، دانشگاه صنعتی شریف · کارشناسی مکانیک، دانشگاه علم و صنعت ایران",
   "en": "MSc Applied Design, Sharif University of Technology · BSc Mechanical Engineering, IUST",
  },
  "bio": {
   "fa": "طراحی مکانیکی ماشین‌ها و ربات‌های صنعتی و پیگیری ساخت، مونتاژ و راه‌اندازی آن‌ها. برگزیده‌ی شصت‌وچهارمین جایزه‌ی البرز و دو بار دارنده‌ی مقام دوم جشنواره‌ی جوان خوارزمی.",
   "en": "Mechanical design of industrial machines and robots, carried through fabrication, assembly and commissioning. Laureate of the 64th Alborz Elite Prize and twice second-place winner at the Khwarizmi Youth Festival.",
  },
  "linkedin": "https://www.linkedin.com/in/hassan-nasiri-khonsari-44bb49198/",
  "por": "por-hassan.webp",
  "av": "av-hassan.webp",
 },
 "a": {
  "name": {"fa": "علیرضا پیرحاجی", "en": "Alireza Pirhaji"},
  "role": {"fa": "سرپرست ساخت و کنترل کیفیت", "en": "Manufacturing & Quality Lead"},
  "edu": {
   "fa": "کارشناسی ارشد ساخت و تولید، دانشگاه تربیت مدرس · کارشناسی مکانیک، دانشگاه صنعتی شریف",
   "en": "MSc Manufacturing Engineering, Tarbiat Modares University · BSc Mechanical Engineering, Sharif University of Technology",
  },
  "bio": {
   "fa": "ساخت قطعات و سازه‌های صنعتی، کامپوزیت و چاپ سه‌بعدی. سرپرستی تولید ربات‌های سورتر پستی را بر عهده داشته و اکنون پیمانکاری ساخت، کنترل کیفی و مونتاژ مجموعه‌های صنعتی را انجام می‌دهد.",
   "en": "Fabrication of industrial parts and structures, composites and 3D printing. Led production of the postal sorting robots and now runs contract fabrication, quality control and assembly of industrial part sets.",
  },
  "linkedin": "https://www.linkedin.com/in/alireza-pirhaji-9a0787139/",
  "por": "por-alireza.webp",
  "av": "av-alireza.webp",
 },
 "m": {
  "name": {"fa": "سید مصطفی بنی‌هاشمی", "en": "Seyed Mostafa Banihashemi"},
  "role": {"fa": "سرپرست پروژه و تحقیق و توسعه", "en": "Project & R&D Lead"},
  "edu": {
   "fa": "کارشناسی ارشد طراحی کاربردی (دینامیک، کنترل و رباتیک)، دانشگاه صنعتی شریف · کارشناسی مکانیک، دانشگاه خواجه نصیر",
   "en": "MSc Applied Design (Dynamics, Control & Robotics), Sharif University of Technology · BSc Mechanical Engineering, K. N. Toosi University",
  },
  "bio": {
   "fa": "طراحی مکانیزم، کنترل و رباتیک پزشکی. برآورد و قیمت‌گذاری، تأمین متریال و پیگیری ساخت پروژه‌های گروه با اوست. پژوهشگر برتر دانشکده‌ی مهندسی مکانیک شریف در سال ۱۴۰۴.",
   "en": "Mechanism design, control and medical robotics. Handles estimating, procurement and fabrication follow-up for the group's projects. Named top researcher of Sharif's mechanical engineering faculty in 2025.",
  },
  "linkedin": "https://www.linkedin.com/in/mostafa-banihashemi/",
  "por": "por-mostafa.webp",
  "av": "av-mostafa.webp",
 },
}

# سه خدمت: کارت صفحه‌ی اصلی (card_h، card_p، card_list)، نمونه‌ها (examples: slug پروژه‌ها)
# و صفحه‌ی اختصاصی هر خدمت (title، desc، h1، lead، facts، what، steps، projects، faq).
# projects: [slug پروژه، عکس، عنوان، توضیح مخصوص همین خدمت]
SERVICES = [
 {
  "slug": "custom-machines",
  "img": "p-sorter-3-m.webp",
  "examples": ["postal-sorting-robots", "knee-prosthesis-test-rig", "dual-purpose-cnc", "industrial-3d-printers"],
  "fa": {
   "card_h": "طراحی و ساخت دستگاه‌ها و ربات‌های صنعتی سفارشی",
   "card_p": "دستگاهی که برای فرآیند شما ساخته می‌شود؛ از نیازسنجی و طراحی مفهومی تا ساخت، مونتاژ و راه‌اندازی.",
   "card_list": [
    "دستگاه‌های خاص‌منظوره و تجهیزات آزمون",
    "ربات‌های صنعتی، خدماتی و متحرک",
    "طراحی مکانیزم و تحلیل مهندسی (<bdi>FEA</bdi>)",
    "دستگاه <bdi>CNC</bdi> و پرینتر سه‌بعدی صنعتی",
   ],
   "title": "طراحی و ساخت دستگاه خاص‌منظوره و ربات صنعتی سفارشی | گروه فنی مهندسی انتها",
   "desc": "طراحی و ساخت دستگاه خاص‌منظوره، تجهیزات آزمون و ربات صنعتی سفارشی، از نیازسنجی تا راه‌اندازی. تهران و اصفهان، برای کارفرمایان سراسر ایران. سفارش تک‌دستگاه و برآورد قیمت رایگان.",
   "nav": "دستگاه و ربات سفارشی",
   "h1": "طراحی و ساخت دستگاه خاص‌منظوره و ربات صنعتی سفارشی",
   "lead": [
    "گروه فنی مهندسی انتها دستگاه‌ها، ربات‌ها و تجهیزات آزمون صنعتی را برای فرآیند مشخص هر کارفرما از صفر طراحی می‌کند و می‌سازد؛ از نیازسنجی و طراحی مفهومی تا طراحی تفصیلی، تحلیل مهندسی، ساخت، مونتاژ، کنترل کیفیت و راه‌اندازی. هر جا دستگاه آماده‌ای در بازار نیست، یا دستگاه موجود با خط تولید شما جور نیست، ماشینی می‌سازیم که دقیقاً همان کار را انجام دهد.",
    "دفتر و کارگاه‌های همکار ما در تهران و اصفهان است و برای کارفرمایان سراسر ایران کار می‌کنیم. سفارش تک‌دستگاه هم می‌پذیریم و برآورد قیمت رایگان است.",
   ],
   "facts": [
    [
     "چه می‌سازیم",
     "دستگاه خاص‌منظوره، تجهیزات آزمون، ربات صنعتی و خدماتی و متحرک، دستگاه CNC و پرینتر سه‌بعدی صنعتی",
    ],
    ["دامنه‌ی کار", "نیازسنجی، طراحی، تحلیل مهندسی، ساخت، مونتاژ، کنترل کیفیت، راه‌اندازی"],
    ["ابعاد کارهای قبلی", "دستگاه‌هایی از ۱۰ تا ۲۵۰ کیلوگرم و سازه‌هایی تا حدود ۱ تا ۲ تن"],
    ["زمان معمول", "دستگاه خاص‌منظوره‌ی ساده: ۱ تا ۲ ماه طراحی و ۱ تا ۲ ماه ساخت"],
    ["تعداد سفارش", "از یک دستگاه تا تولید سری"],
    ["برآورد قیمت", "رایگان، معمولاً ظرف ۱ تا ۲ هفته"],
    ["پشتیبانی", "رفع ایراد تا ۲ ماه پس از تحویل؛ ضمانت و ارتقا طبق قرارداد"],
    ["محل", "تهران و اصفهان؛ برای سراسر ایران"],
   ],
   "what_h": "چه دستگاه‌هایی طراحی و ساخت می‌کنیم؟",
   "what": [
    [
     "دستگاه‌های خاص‌منظوره (SPM)",
     "ماشینی که فقط برای یک مرحله از فرآیند شما ساخته می‌شود، مثل دستگاه‌های تغذیه، جابه‌جایی، تفکیک، برش یا مونتاژ، وقتی دستگاه آماده‌ای برای آن در بازار نیست.",
    ],
    [
     "تجهیزات آزمون و تست",
     "دستگاه‌های آزمون مکانیکی برای آزمایشگاه‌ها و کنترل کیفیت، مطابق استانداردهایی مثل ASTM؛ از جمله دستگاه تست پروتز زانو در شش درجه‌ی آزادی.",
    ],
    [
     "ربات‌های صنعتی، خدماتی و متحرک",
     "ربات‌های سورتر و تفکیک بار، ربات‌های حمل و سرو، و ربات‌های کابلی؛ از طراحی مکانیزم و شاسی تا سیستم حرکت و کنترل.",
    ],
    [
     "رباتیک پزشکی و توانبخشی",
     "طراحی، ساخت و کنترل سیستم‌های رباتیک برای پژوهش و توانبخشی، همراه با دانشگاه‌ها و مراکز تحقیقاتی.",
    ],
    [
     "دستگاه CNC و پرینتر سه‌بعدی صنعتی",
     "طراحی سازه، انتخاب درایو و موتور، الکترونیک، فرم‌ور و راه‌اندازی کنترل؛ از پرینتر FDM با حجم کاری ۵۰۰×۵۰۰×۴۰۰ میلی‌متر تا CNC با میز حدود ۱۰۰×۱۰۰ سانتی‌متر.",
    ],
    [
     "طراحی مکانیزم و تحلیل مهندسی (FEA)",
     "بررسی استحکام، تغییرشکل و رفتار سازه و مکانیزم با تحلیل اجزای محدود، پیش از آنکه هزینه‌ی ساخت پرداخت شود.",
    ],
    [
     "مهندسی معکوس و بازطراحی",
     "تهیه‌ی نقشه از روی نمونه‌ی موجود و بازطراحی دستگاه یا قطعه‌ای که نقشه ندارد یا باید بهتر شود.",
    ],
   ],
   "steps": [
    [
     "گفت‌وگو و نیازسنجی",
     "شرح کار، نقشه، عکس یا نمونه را می‌فرستید و ظرفیت، دقت و محدودیت‌های فرآیند را با هم مشخص می‌کنیم.",
    ],
    [
     "برآورد قیمت رایگان",
     "پس از بررسی فنی و مشورت با مشاوران، معمولاً ظرف ۱ تا ۲ هفته قیمت و زمان‌بندی را اعلام می‌کنیم.",
    ],
    ["طراحی و تحلیل", "طراحی مفهومی و تفصیلی، تحلیل مهندسی و انتخاب قطعات، با تأیید شما در هر مرحله."],
    ["ساخت و مونتاژ", "ساخت در کارگاه‌های همکار و مونتاژ زیر نظر همان مهندسی که طراحی کرده است."],
    ["کنترل کیفیت و آزمون", "بازرسی ابعادی و تست عملکرد دستگاه پیش از تحویل."],
    ["تحویل، راه‌اندازی و پشتیبانی", "تحویل و راه‌اندازی دستگاه، و رفع ایراد تا ۲ ماه پس از تحویل."],
   ],
   "projects": [
    [
     "postal-sorting-robots",
     "p-sorter-3-m.webp",
     "ربات‌های سورتر پستی (۱۳۹۹ تا ۱۴۰۴)",
     "ربات‌های خودگردان تفکیک مرسولات برای شرکت ملی پست. ساخت و مونتاژ نسل‌های اول و دوم: ۵۰ دستگاه برای تهران و ۳۰ دستگاه برای کرمانشاه. طراحی نسل سوم (مکانیزم تخلیه‌ی بار، توزین، استراکچر و سیستم حرکت) در تیراژ ۲۰۰ دستگاه به تولید رسید. مقام دوم بیست‌وششمین جشنواره‌ی جوان خوارزمی.",
    ],
    [
     "knee-prosthesis-test-rig",
     "p-knee-m.webp",
     "دستگاه تست تقید و پایداری پروتز زانو (۱۴۰۰)",
     "آزمون پروتز کامل زانو در شش درجه‌ی آزادی مطابق استاندارد ASTM F1223؛ نخستین نمونه از این نوع در ایران، در حالی که معادل‌های تجاری را شرکت‌هایی مثل EndoLab و AMTI می‌سازند. طراحی مکانیکی، اتوماسیون، PLC و HMI. برگزیده‌ی جایزه‌ی البرز و جشنواره‌ی جوان خوارزمی.",
    ],
    [
     "industrial-3d-printers",
     "p-printer-3-m.webp",
     "پرینترهای سه‌بعدی FDM صنعتی (۱۳۹۹ تا ۱۴۰۲)",
     "پنج دستگاه که از صفر طراحی و ساخته شدند، تا ماشینی با حجم کاری ۵۰۰×۵۰۰×۴۰۰ میلی‌متر با بال‌اسکرو و ریل خطی صنعتی روی همه‌ی محورها؛ سازه، الکترونیک و فرم‌ور مستقل.",
    ],
    [
     "dual-purpose-cnc",
     "p-cnc-m.webp",
     "CNC صنعتی دوکاره (۱۴۰۲)",
     "CNC برای برش چوب و فلزات سبک با میز حدود ۱۰۰×۱۰۰ سانتی‌متر که با تعویض هد به پرینتر سه‌بعدی تبدیل می‌شود؛ برای کارگاه‌های کوچک و متوسط.",
    ],
    [
     "waiter-robots",
     "p-waiter-m.webp",
     "ربات‌های گارسون (۱۴۰۰)",
     "ناوگانی هفت‌تایی از ربات‌های حمل و سرو غذا؛ شاسی و سیستم حرکت برای کار پایدار روی کف ناهموار رستوران.",
    ],
    [
     "dmd-powder-feeder",
     "p-dmd-m.webp",
     "سامانه‌ی تغذیه‌ی پودر DMD (۱۳۹۸)",
     "تغذیه‌کننده‌ی پودر برای لایه‌نشانی مستقیم فلز با لیزر، با کنترل نرخ تغذیه در بازه‌ی ۱ تا ۱۰۰ گرم بر دقیقه.",
    ],
   ],
   "faq": [
    [
     "هزینه‌ی طراحی و ساخت دستگاه خاص‌منظوره چقدر است؟",
     "به پیچیدگی، ابعاد، دقت و تعداد دستگاه بستگی دارد، پس قیمت ثابتی ندارد. شرح کار را بفرستید تا برآورد قیمت رایگان را معمولاً ظرف یک تا دو هفته دریافت کنید.",
    ],
    [
     "ساخت یک دستگاه چقدر طول می‌کشد؟",
     "بسته به پروژه، از یک تا دو هفته تا حدود یک سال. برای یک دستگاه خاص‌منظوره‌ی ساده، طراحی معمولاً ۱ تا ۲ ماه و ساخت هم ۱ تا ۲ ماه طول می‌کشد.",
    ],
    [
     "سفارش تک‌دستگاه هم می‌پذیرید؟",
     "بله. از یک دستگاه تا تولید سری را می‌پذیریم؛ تعداد مناسب برای تولید سری به حجم پروژه بستگی دارد.",
    ],
    [
     "دستگاه‌هایی با چه ابعاد و وزنی ساخته‌اید؟",
     "دستگاه‌هایی از حدود ۱۰ تا ۲۵۰ کیلوگرم و سازه‌هایی تا حدود ۱ تا ۲ تن. جنس هر بخش را بر اساس کاربرد همان بخش انتخاب می‌کنیم، از فولاد و استیل ۳۱۶ تا آلومینیوم، پلاستیک‌های مهندسی و کامپوزیت.",
    ],
    [
     "مهندسی معکوس هم انجام می‌دهید؟",
     "بله. از روی دستگاه یا قطعه‌ی موجود نقشه تهیه می‌کنیم و در صورت نیاز آن را بازطراحی و بهینه می‌کنیم.",
    ],
    [
     "برآورد قیمت رایگان است؟ چقدر طول می‌کشد؟",
     "بله، برآورد قیمت رایگان است. معمولاً یک تا دو هفته طول می‌کشد، چون کارشناسان ما پیش از اعلام قیمت، کار را از نظر فنی بررسی می‌کنند و با مشاوران گروه مشورت می‌کنند تا قیمت و زمان اعلام‌شده واقعی باشد.",
    ],
    [
     "برای شروع چه اطلاعاتی لازم است؟ چه فرمت‌هایی از نقشه را می‌پذیرید؟",
     "هر چیزی که دارید کافی است: نقشه‌ی دوبعدی یا مدل سه‌بعدی در هر فرمتی (مثل STEP، DWG، DXF، SolidWorks یا PDF)، عکس، طرح دستی، یا فقط شرح کار. اگر نقشه ندارید و نمونه‌ی فیزیکی دارید، با مهندسی معکوس نقشه را از روی نمونه تهیه می‌کنیم.",
    ],
    [
     "بعد از تحویل چه پشتیبانی‌ای دارید؟",
     "ایرادهای دستگاه‌هایی را که خودمان طراحی کرده و ساخته‌ایم تا دو ماه پس از تحویل رفع می‌کنیم (جدا از درخواست‌های تازه‌ی کارفرما). ضمانت طولانی‌تر، تعمیر و ارتقا را هم هر طور که کارفرما بخواهد در قرارداد می‌گنجانیم. اگر طرح از کارفرما بوده و کار ما فقط پیمانکاری ساخت بوده، رفع ایرادِ ناشی از طرح را انجام می‌دهیم ولی هزینه‌ی آن جداگانه محاسبه می‌شود.",
    ],
    [
     "فقط در تهران و اصفهان کار می‌کنید؟",
     "خیر. دفتر و کارگاه‌های همکار ما در تهران و اصفهان است، ولی برای کارفرمایان سراسر ایران کار می‌کنیم.",
    ],
   ],
  },
  "en": {
   "card_h": "Custom industrial machines & robots",
   "card_p": "A machine built for your process — from requirements and concept design to fabrication, assembly and commissioning.",
   "card_list": [
    "Special-purpose machines and test rigs",
    "Industrial, service and mobile robots",
    "Mechanism design and engineering analysis (FEA)",
    "CNC machines and industrial 3D printers",
   ],
   "title": "Custom Special-Purpose Machines & Industrial Robots — Design and Build | Enteha Group",
   "desc": "Design and fabrication of special-purpose machines, test rigs and custom industrial robots, from requirements to commissioning. Based in Tehran and Isfahan, serving clients across Iran. One-off machines welcome; free quotes.",
   "nav": "Custom machines & robots",
   "h1": "Custom special-purpose machines and industrial robots",
   "lead": [
    "Enteha Group designs and builds industrial machines, robots and test equipment from scratch for each client's specific process — from requirements and concept design through detailed design, engineering analysis, fabrication, assembly, quality control and commissioning. Where no off-the-shelf machine exists, or the available ones do not fit your line, we build one that does exactly that job.",
    "Our office and partner workshops are in Tehran and Isfahan, and we work for clients across Iran. We take one-off orders, and quotes are free.",
   ],
   "facts": [
    [
     "What we build",
     "Special-purpose machines, test rigs, industrial, service and mobile robots, CNC machines and industrial 3D printers",
    ],
    ["Scope", "Requirements, design, engineering analysis, fabrication, assembly, quality control, commissioning"],
    ["Size of past work", "Machines from 10 to 250 kg and structures of about 1–2 tonnes"],
    ["Typical timeline", "Simple special-purpose machine: 1–2 months design and 1–2 months fabrication"],
    ["Order size", "From a single machine to series production"],
    ["Quote", "Free, usually within 1–2 weeks"],
    ["Support", "Faults fixed for 2 months after delivery; warranty and upgrades by contract"],
    ["Location", "Tehran and Isfahan; serving all of Iran"],
   ],
   "what_h": "What machines do we design and build?",
   "what": [
    [
     "Special-purpose machines (SPM)",
     "A machine built for one step of your process — feeding, handling, sorting, cutting or assembly — when there is no ready-made machine for it on the market.",
    ],
    [
     "Test rigs and test equipment",
     "Mechanical test machines for laboratories and quality control, built to standards such as ASTM — including a six-degree-of-freedom knee prosthesis test rig.",
    ],
    [
     "Industrial, service and mobile robots",
     "Sorting robots, delivery and serving robots, and cable-driven robots — from mechanism and chassis design to drive and control systems.",
    ],
    [
     "Medical and rehabilitation robotics",
     "Design, fabrication and control of robotic systems for research and rehabilitation, together with universities and research centres.",
    ],
    [
     "CNC machines and industrial 3D printers",
     "Structure design, drive and motor selection, electronics, firmware and control set-up — from an FDM printer with a 500 × 500 × 400 mm build volume to a CNC with a table of about 100 × 100 cm.",
    ],
    [
     "Mechanism design and engineering analysis (FEA)",
     "Checking the strength, deflection and behaviour of structures and mechanisms with finite element analysis before money is spent on fabrication.",
    ],
    [
     "Reverse engineering and redesign",
     "Drawings made from an existing sample, and redesign of a machine or part that has no drawings or needs to be improved.",
    ],
   ],
   "steps": [
    [
     "Discussion and requirements",
     "You send a description, drawings, photos or a sample, and together we pin down capacity, accuracy and process constraints.",
    ],
    [
     "Free quote",
     "After a technical review and consultation with our advisers, we usually send the price and schedule within 1–2 weeks.",
    ],
    [
     "Design and analysis",
     "Concept and detailed design, engineering analysis and component selection, with your approval at each stage.",
    ],
    [
     "Fabrication and assembly",
     "Fabrication in our partner workshops and assembly supervised by the same engineer who designed it.",
    ],
    ["Quality control and testing", "Dimensional inspection and functional testing before delivery."],
    [
     "Delivery, commissioning and support",
     "Delivery and commissioning, and faults fixed for 2 months after delivery.",
    ],
   ],
   "projects": [
    [
     "postal-sorting-robots",
     "p-sorter-3-m.webp",
     "Postal sorting robots (2020–2025)",
     "Autonomous parcel-sorting robots for Iran Post. We built and assembled generations 1 and 2: 50 units for Tehran and 30 for Kermanshah. Our generation 3 design (unloading mechanism, weighing, structure and drive system) went into production in a run of 200 units. Second place at the 26th Khwarizmi Youth Festival.",
    ],
    [
     "knee-prosthesis-test-rig",
     "p-knee-m.webp",
     "Knee prosthesis constraint & stability test rig (2021)",
     "Tests total knee prostheses in six degrees of freedom to ASTM F1223 — the first rig of its kind made in Iran, where commercial equivalents come from companies such as EndoLab and AMTI. Mechanical design, automation, PLC and HMI. Recognised by the Alborz Elite Prize and the Khwarizmi Youth Festival.",
    ],
    [
     "industrial-3d-printers",
     "p-printer-3-m.webp",
     "Industrial FDM 3D printers (2020–2023)",
     "Five machines designed and built from scratch, up to a 500 × 500 × 400 mm build volume with industrial ball screws and linear rails on every axis; our own structure, electronics and firmware.",
    ],
    [
     "dual-purpose-cnc",
     "p-cnc-m.webp",
     "Dual-purpose industrial CNC (2023)",
     "A CNC for cutting wood and light metals with a table of about 100 × 100 cm that becomes a 3D printer by swapping the head; built for small and medium workshops.",
    ],
    [
     "waiter-robots",
     "p-waiter-m.webp",
     "Waiter robots (2021)",
     "A fleet of seven food delivery and serving robots, with a chassis and drive system designed to stay stable on uneven restaurant floors.",
    ],
    [
     "dmd-powder-feeder",
     "p-dmd-m.webp",
     "DMD powder feeder (2019)",
     "A powder feeder for laser direct metal deposition, controlling the feed rate between 1 and 100 g/min.",
    ],
   ],
   "faq": [
    [
     "How much does a special-purpose machine cost?",
     "It depends on complexity, size, accuracy and quantity, so there is no fixed price. Send us a description and you will usually receive a free quote within one to two weeks.",
    ],
    [
     "How long does it take to build a machine?",
     "Depending on the project, anything from one or two weeks to about a year. For a simple special-purpose machine, design usually takes 1–2 months and fabrication another 1–2 months.",
    ],
    [
     "Do you take orders for a single machine?",
     "Yes. We take everything from a single machine to series production; the right quantity for a series depends on the project.",
    ],
    [
     "What sizes and weights have you built?",
     "Machines from about 10 to 250 kg and structures of about 1–2 tonnes. We choose the material of each part for its application — from steel and 316 stainless to aluminium, engineering plastics and composites.",
    ],
    [
     "Do you do reverse engineering?",
     "Yes. We produce drawings from an existing machine or part and, where needed, redesign and improve it.",
    ],
    [
     "Is the quote free? How long does it take?",
     "Yes, quotes are free. A quote usually takes one to two weeks, because our engineers review the job technically and consult the group's advisers before giving a price, so that the price and schedule we quote are realistic.",
    ],
    [
     "What do you need to get started? Which drawing formats do you accept?",
     "Whatever you have is enough: 2D drawings or 3D models in any format (such as STEP, DWG, DXF, SolidWorks or PDF), photos, a hand sketch, or just a description of the job. If you have a physical sample but no drawings, we reverse-engineer the drawings from the sample.",
    ],
    [
     "What support do you give after delivery?",
     "For machines we designed and built ourselves, we fix any faults for two months after delivery (separate from new requests from the client). A longer warranty, repairs and upgrades can be written into the contract however the client wants. If the design came from the client and we only did the fabrication, we still fix faults caused by the design, but that work is charged separately.",
    ],
    [
     "Do you only work in Tehran and Isfahan?",
     "No. Our office and partner workshops are in Tehran and Isfahan, but we work for clients across Iran.",
    ],
   ],
  },
 },
 {
  "slug": "automation",
  "img": "p-cnc-panel-open-m.webp",
  "examples": ["knee-prosthesis-test-rig", "postal-sorting-robots", "dual-purpose-cnc"],
  "fa": {
   "card_h": "اتوماسیون خط تولید",
   "card_p": "خودکارسازی مراحل دستی و نیمه‌خودکار خط تولید: طراحی کنترل، برنامه‌نویسی <bdi>PLC</bdi>، طراحی <bdi>HMI</bdi> و یکپارچه‌سازی با تجهیزات موجود.",
   "card_list": [
    "برنامه‌نویسی <bdi>PLC</bdi> (دلتا، زیمنس) و <bdi>HMI</bdi>",
    "کنترل حرکت با درایوهای سروو و استپر",
    "سنسور، سامانه‌ی توزین و اندازه‌گیری",
    "تابلوهای برق و کنترل",
    "طراحی خط تولید و ایستگاه‌های مونتاژ",
   ],
   "title": "اتوماسیون خط تولید، برنامه‌نویسی PLC و ساخت تابلو کنترل | گروه فنی مهندسی انتها",
   "desc": "خودکارسازی مراحل دستی و نیمه‌خودکار خط تولید: طراحی کنترل، برنامه‌نویسی PLC دلتا و زیمنس، HMI، کنترل حرکت با سروو و استپر، توزین و تابلو برق. تهران و اصفهان، برای سراسر ایران.",
   "nav": "اتوماسیون خط تولید",
   "h1": "اتوماسیون خط تولید و طراحی سیستم کنترل",
   "lead": [
    "گروه فنی مهندسی انتها مراحل دستی و نیمه‌خودکار خط تولید را خودکار می‌کند: طراحی سیستم کنترل، برنامه‌نویسی PLC (دلتا و زیمنس)، طراحی HMI، کنترل حرکت با درایوهای سروو و استپر، سنسور و سامانه‌ی توزین و اندازه‌گیری، ساخت تابلو برق و کنترل، و یکپارچه‌سازی با تجهیزات موجود شما. چون طراحی مکانیکی و ساخت را هم خودمان انجام می‌دهیم، بخش مکانیکی و کنترلی اتوماسیون را یک تیم و به‌صورت هماهنگ طراحی می‌کند.",
    "دفتر و کارگاه‌های همکار ما در تهران و اصفهان است و برای کارفرمایان سراسر ایران کار می‌کنیم. برآورد قیمت رایگان است.",
   ],
   "facts": [
    [
     "چه انجام می‌دهیم",
     "طراحی کنترل، PLC و HMI، کنترل حرکت، توزین و اندازه‌گیری، تابلو برق، طراحی خط و ایستگاه مونتاژ",
    ],
    ["برندهای PLC", "دلتا (Delta) و زیمنس (Siemens)"],
    ["کنترل حرکت", "درایوهای سروو و استپر"],
    ["تجهیزات موجود", "یکپارچه‌سازی با دستگاه‌ها و خط فعلی شما"],
    ["زمان معمول", "از ۱ تا ۲ هفته تا چند ماه، بسته به پروژه"],
    ["برآورد قیمت", "رایگان، معمولاً ظرف ۱ تا ۲ هفته"],
    ["پشتیبانی", "رفع ایراد تا ۲ ماه پس از تحویل؛ ضمانت و ارتقا طبق قرارداد"],
    ["محل", "تهران و اصفهان؛ برای سراسر ایران"],
   ],
   "what_h": "در اتوماسیون چه کارهایی انجام می‌دهیم؟",
   "what": [
    [
     "طراحی سیستم کنترل و معماری اتوماسیون",
     "تعیین ترتیب کار، سنسورها، عملگرها و منطق کنترل برای اینکه یک مرحله یا کل خط بدون دخالت دستی کار کند.",
    ],
    [
     "برنامه‌نویسی PLC (دلتا و زیمنس) و طراحی HMI",
     "نوشتن برنامه‌ی PLC و طراحی صفحه‌ی اپراتور (HMI) برای فرمان، تنظیم و نمایش وضعیت دستگاه.",
    ],
    [
     "کنترل حرکت با سروو و استپر",
     "انتخاب و راه‌اندازی موتور و درایو برای حرکت‌های دقیق و تکرارپذیر در دستگاه‌ها و خطوط.",
    ],
    [
     "سنسور، سامانه‌ی توزین و اندازه‌گیری",
     "افزودن اندازه‌گیری و توزین به فرآیند برای کنترل کیفیت و تفکیک خودکار؛ مثل سامانه‌ی توزین ربات‌های سورتر پستی.",
    ],
    ["تابلوهای برق و کنترل", "طراحی و ساخت تابلو برق و فرمان دستگاه‌ها."],
    ["طراحی خط تولید و ایستگاه‌های مونتاژ", "طراحی جانمایی و ایستگاه‌های کاری برای افزایش ظرفیت و کاهش کار دستی."],
    ["یکپارچه‌سازی با تجهیزات موجود", "اتصال دستگاه‌های جدید به خط و تجهیزات فعلی، به‌جای تعویض کل خط."],
   ],
   "steps": [
    ["بررسی و نیازسنجی", "بررسی مرحله‌ای که باید خودکار شود، ظرفیت، دقت و تجهیزات موجود."],
    ["برآورد قیمت رایگان", "پس از بررسی فنی و مشورت با مشاوران، معمولاً ظرف ۱ تا ۲ هفته."],
    ["طراحی کنترل و مکانیک", "معماری کنترل، انتخاب PLC، درایو و سنسورها، و طراحی بخش‌های مکانیکی لازم."],
    ["ساخت تابلو و برنامه‌نویسی", "ساخت تابلو برق و کنترل، برنامه‌نویسی PLC و طراحی HMI."],
    ["نصب و راه‌اندازی", "نصب روی خط، یکپارچه‌سازی با تجهیزات موجود و تست."],
    ["پشتیبانی", "رفع ایراد تا ۲ ماه پس از تحویل؛ ضمانت و ارتقا طبق قرارداد."],
   ],
   "projects": [
    [
     "knee-prosthesis-test-rig",
     "p-knee-m.webp",
     "دستگاه تست تقید و پایداری پروتز زانو (۱۴۰۰)",
     "معماری اتوماسیون، برنامه‌نویسی PLC و توسعه‌ی HMI برای دستگاهی که پروتز زانو را در شش درجه‌ی آزادی مطابق ASTM F1223 آزمون می‌کند.",
    ],
    [
     "postal-sorting-robots",
     "p-sorter-3-m.webp",
     "ربات‌های سورتر پستی (۱۳۹۹ تا ۱۴۰۴)",
     "سامانه‌ی توزین، مکانیزم تخلیه و سیستم حرکت ربات‌های تفکیک مرسولات شرکت ملی پست؛ نسل سوم در تیراژ ۲۰۰ دستگاه تولید شد.",
    ],
    [
     "dual-purpose-cnc",
     "p-cnc-panel-open-m.webp",
     "تابلو برق CNC صنعتی دوکاره (۱۴۰۲)",
     "انتخاب درایوها و موتورها، ساخت تابلو برق و راه‌اندازی کنترل با G-Code برای CNC با میز حدود ۱۰۰×۱۰۰ سانتی‌متر.",
    ],
    [
     "dmd-powder-feeder",
     "p-dmd-m.webp",
     "سامانه‌ی تغذیه‌ی پودر DMD (۱۳۹۸)",
     "پیاده‌سازی کامل الکترونیک، کنترل و منطق دستگاه، با کنترل نرخ تغذیه‌ی پودر در بازه‌ی ۱ تا ۱۰۰ گرم بر دقیقه.",
    ],
   ],
   "faq": [
    [
     "با چه برندهایی از PLC کار می‌کنید؟",
     "با PLCهای دلتا (Delta) و زیمنس (Siemens). برنامه‌نویسی PLC و طراحی HMI را خودمان انجام می‌دهیم.",
    ],
    [
     "می‌توانید دستگاه‌های فعلی ما را هم خودکار کنید؟",
     "بله. یکپارچه‌سازی با تجهیزات موجود بخشی از کار ماست؛ لازم نیست کل خط عوض شود.",
    ],
    ["تابلو برق و کنترل هم می‌سازید؟", "بله. طراحی و ساخت تابلوهای برق و کنترل دستگاه‌ها را انجام می‌دهیم."],
    [
     "اتوماسیون یک مرحله از خط چقدر طول می‌کشد؟",
     "به اندازه و پیچیدگی کار بستگی دارد؛ از یک تا دو هفته برای کارهای کوچک تا چند ماه برای پروژه‌های بزرگ‌تر. زمان دقیق را همراه برآورد قیمت اعلام می‌کنیم.",
    ],
    [
     "بخش مکانیکی اتوماسیون را هم انجام می‌دهید؟",
     "بله. طراحی مکانیکی، ساخت و مونتاژ را هم خودمان انجام می‌دهیم، پس مکانیک و کنترل را یک تیم هماهنگ طراحی می‌کند.",
    ],
    [
     "برآورد قیمت رایگان است؟ چقدر طول می‌کشد؟",
     "بله، برآورد قیمت رایگان است. معمولاً یک تا دو هفته طول می‌کشد، چون کارشناسان ما پیش از اعلام قیمت، کار را از نظر فنی بررسی می‌کنند و با مشاوران گروه مشورت می‌کنند تا قیمت و زمان اعلام‌شده واقعی باشد.",
    ],
    [
     "برای شروع چه اطلاعاتی لازم است؟ چه فرمت‌هایی از نقشه را می‌پذیرید؟",
     "هر چیزی که دارید کافی است: نقشه‌ی دوبعدی یا مدل سه‌بعدی در هر فرمتی (مثل STEP، DWG، DXF، SolidWorks یا PDF)، عکس، طرح دستی، یا فقط شرح کار. اگر نقشه ندارید و نمونه‌ی فیزیکی دارید، با مهندسی معکوس نقشه را از روی نمونه تهیه می‌کنیم.",
    ],
    [
     "بعد از تحویل چه پشتیبانی‌ای دارید؟",
     "ایرادهای دستگاه‌هایی را که خودمان طراحی کرده و ساخته‌ایم تا دو ماه پس از تحویل رفع می‌کنیم (جدا از درخواست‌های تازه‌ی کارفرما). ضمانت طولانی‌تر، تعمیر و ارتقا را هم هر طور که کارفرما بخواهد در قرارداد می‌گنجانیم. اگر طرح از کارفرما بوده و کار ما فقط پیمانکاری ساخت بوده، رفع ایرادِ ناشی از طرح را انجام می‌دهیم ولی هزینه‌ی آن جداگانه محاسبه می‌شود.",
    ],
    [
     "فقط در تهران و اصفهان کار می‌کنید؟",
     "خیر. دفتر و کارگاه‌های همکار ما در تهران و اصفهان است، ولی برای کارفرمایان سراسر ایران کار می‌کنیم.",
    ],
   ],
  },
  "en": {
   "card_h": "Production line automation",
   "card_p": "Automating the manual and semi-automatic steps of your line: control design, PLC programming, HMI and integration with existing equipment.",
   "card_list": [
    "PLC programming (Delta, Siemens) and HMI",
    "Motion control with servo and stepper drives",
    "Sensors, weighing and measurement systems",
    "Electrical and control cabinets",
    "Production line and assembly station design",
   ],
   "title": "Production Line Automation, PLC Programming & Control Cabinets | Enteha Group",
   "desc": "Automating manual and semi-automatic production steps: control design, Delta and Siemens PLC programming, HMI, servo and stepper motion control, weighing and control cabinets. Tehran and Isfahan, serving all of Iran.",
   "nav": "Production line automation",
   "h1": "Production line automation and control system design",
   "lead": [
    "Enteha Group automates the manual and semi-automatic steps of production lines: control system design, PLC programming (Delta and Siemens), HMI design, servo and stepper motion control, sensors and weighing and measurement systems, electrical and control cabinets, and integration with your existing equipment. Because we also do the mechanical design and fabrication, one team designs the mechanical and control sides of the automation together.",
    "Our office and partner workshops are in Tehran and Isfahan, and we work for clients across Iran. Quotes are free.",
   ],
   "facts": [
    [
     "What we do",
     "Control design, PLC and HMI, motion control, weighing and measurement, control cabinets, line and assembly station design",
    ],
    ["PLC brands", "Delta and Siemens"],
    ["Motion control", "Servo and stepper drives"],
    ["Existing equipment", "Integration with your current machines and line"],
    ["Typical timeline", "From 1–2 weeks to several months, depending on the project"],
    ["Quote", "Free, usually within 1–2 weeks"],
    ["Support", "Faults fixed for 2 months after delivery; warranty and upgrades by contract"],
    ["Location", "Tehran and Isfahan; serving all of Iran"],
   ],
   "what_h": "What do we do in automation?",
   "what": [
    [
     "Control system design and automation architecture",
     "Defining the sequence, sensors, actuators and control logic so that one step or a whole line runs without manual work.",
    ],
    [
     "PLC programming (Delta, Siemens) and HMI design",
     "Writing the PLC program and designing the operator screen (HMI) to command, adjust and monitor the machine.",
    ],
    [
     "Motion control with servo and stepper drives",
     "Selecting and commissioning motors and drives for precise, repeatable motion in machines and lines.",
    ],
    [
     "Sensors, weighing and measurement systems",
     "Adding measurement and weighing to the process for quality control and automatic sorting — such as the weighing system of the postal sorting robots.",
    ],
    ["Electrical and control cabinets", "Design and build of machine power and control cabinets."],
    [
     "Production line and assembly station design",
     "Layout and workstation design to raise capacity and reduce manual work.",
    ],
    [
     "Integration with existing equipment",
     "Connecting new machines to your current line and equipment instead of replacing the whole line.",
    ],
   ],
   "steps": [
    ["Review and requirements", "Reviewing the step to automate, capacity, accuracy and existing equipment."],
    ["Free quote", "After a technical review and consultation with our advisers, usually within 1–2 weeks."],
    [
     "Control and mechanical design",
     "Control architecture, choice of PLC, drives and sensors, and design of the mechanical parts needed.",
    ],
    ["Cabinet build and programming", "Building the control cabinet, PLC programming and HMI design."],
    [
     "Installation and commissioning",
     "Installation on the line, integration with existing equipment and testing.",
    ],
    ["Support", "Faults fixed for 2 months after delivery; warranty and upgrades by contract."],
   ],
   "projects": [
    [
     "knee-prosthesis-test-rig",
     "p-knee-m.webp",
     "Knee prosthesis constraint & stability test rig (2021)",
     "Automation architecture, PLC programming and HMI development for a rig that tests knee prostheses in six degrees of freedom to ASTM F1223.",
    ],
    [
     "postal-sorting-robots",
     "p-sorter-3-m.webp",
     "Postal sorting robots (2020–2025)",
     "Weighing system, unloading mechanism and drive system of Iran Post's parcel-sorting robots; generation 3 went into production in a run of 200 units.",
    ],
    [
     "dual-purpose-cnc",
     "p-cnc-panel-open-m.webp",
     "Control cabinet of a dual-purpose industrial CNC (2023)",
     "Drive and motor selection, control cabinet build and G-code control set-up for a CNC with a table of about 100 × 100 cm.",
    ],
    [
     "dmd-powder-feeder",
     "p-dmd-m.webp",
     "DMD powder feeder (2019)",
     "Complete electronics, control and machine logic, controlling the powder feed rate between 1 and 100 g/min.",
    ],
   ],
   "faq": [
    [
     "Which PLC brands do you work with?",
     "Delta and Siemens PLCs. We do the PLC programming and HMI design ourselves.",
    ],
    [
     "Can you automate the machines we already have?",
     "Yes. Integration with existing equipment is part of what we do; there is no need to replace the whole line.",
    ],
    [
     "Do you build electrical and control cabinets?",
     "Yes. We design and build machine power and control cabinets.",
    ],
    [
     "How long does it take to automate one step of a line?",
     "It depends on the size and complexity of the job — from one or two weeks for small jobs to several months for larger projects. We give the exact schedule with the quote.",
    ],
    [
     "Do you also handle the mechanical side?",
     "Yes. We also do the mechanical design, fabrication and assembly, so one team designs the mechanics and the controls together.",
    ],
    [
     "Is the quote free? How long does it take?",
     "Yes, quotes are free. A quote usually takes one to two weeks, because our engineers review the job technically and consult the group's advisers before giving a price, so that the price and schedule we quote are realistic.",
    ],
    [
     "What do you need to get started? Which drawing formats do you accept?",
     "Whatever you have is enough: 2D drawings or 3D models in any format (such as STEP, DWG, DXF, SolidWorks or PDF), photos, a hand sketch, or just a description of the job. If you have a physical sample but no drawings, we reverse-engineer the drawings from the sample.",
    ],
    [
     "What support do you give after delivery?",
     "For machines we designed and built ourselves, we fix any faults for two months after delivery (separate from new requests from the client). A longer warranty, repairs and upgrades can be written into the contract however the client wants. If the design came from the client and we only did the fabrication, we still fix faults caused by the design, but that work is charged separately.",
    ],
    [
     "Do you only work in Tehran and Isfahan?",
     "No. Our office and partner workshops are in Tehran and Isfahan, but we work for clients across Iran.",
    ],
   ],
  },
 },
 {
  "slug": "parts-manufacturing",
  "img": "p-platform-m.webp",
  "examples": ["rail-guided-test-platform", "injection-mould"],
  "fa": {
   "card_h": "ساخت قطعات صنعتی در تهران و اصفهان",
   "card_p": "ساخت قطعه و مجموعه طبق نقشه‌ی شما، تک‌نمونه یا سری، با کنترل کیفیت خودمان پیش از تحویل.",
   "card_list": [
    "ماشین‌کاری <bdi>CNC</bdi>، برش لیزر، خم‌کاری و نورد",
    "سازه‌های جوشی فولادی و استیل ۳۱۶",
    "محفظه و مخزن تحت فشار",
    "قالب تزریق پلاستیک",
    "بازرسی ابعادی و جوش، <bdi>GD&amp;T</bdi>",
   ],
   "title": "ساخت قطعات صنعتی طبق نقشه در تهران و اصفهان؛ ماشین‌کاری CNC، برش لیزر و سازه‌ی جوشی | انتها",
   "desc": "ساخت قطعه و مجموعه‌ی صنعتی طبق نقشه، تک‌نمونه یا تیراژی: ماشین‌کاری CNC، برش لیزر، خم و نورد، سازه‌ی جوشی فولاد و استیل ۳۱۶، مخزن، قالب تزریق و بازرسی ابعادی. برای سراسر ایران.",
   "nav": "ساخت قطعات صنعتی",
   "h1": "ساخت قطعات صنعتی طبق نقشه، تک‌نمونه و تیراژی",
   "lead": [
    "گروه فنی مهندسی انتها قطعه‌ها و مجموعه‌های صنعتی را طبق نقشه‌ی شما، به‌صورت تک‌نمونه یا تیراژی، با کارگاه‌های همکار در تهران و اصفهان می‌سازد و پیش از تحویل خودش کنترل کیفیت می‌کند: ماشین‌کاری CNC، برش لیزر، خم‌کاری و نورد، سازه‌های جوشی فولادی و استیل ۳۱۶، محفظه و مخزن تحت فشار، قالب تزریق پلاستیک، و بازرسی ابعادی و جوش با GD&amp;T.",
    "چون خودمان طراح و سازنده‌ی دستگاه هستیم، قطعه را فقط از روی نقشه نمی‌سازیم؛ به جفت‌شدن قطعه‌ها در مونتاژ هم فکر می‌کنیم تا روز مونتاژ غافلگیر نشوید. برای کارفرمایان سراسر ایران کار می‌کنیم و برآورد قیمت رایگان است.",
   ],
   "facts": [
    ["فرآیندها", "ماشین‌کاری CNC، برش لیزر، خم‌کاری، نورد، جوشکاری، قالب‌سازی، چاپ سه‌بعدی"],
    ["مواد", "فولاد، استیل ۳۱۶ و هر ماده‌ای که کاربرد قطعه لازم دارد"],
    ["ابعاد کارهای قبلی", "از قطعه‌های کوچک تا سازه‌هایی حدود ۱ تا ۲ تن"],
    ["تعداد سفارش", "تک‌نمونه تا تیراژی"],
    ["نقشه", "همه‌ی فرمت‌ها؛ مهندسی معکوس از روی نمونه"],
    ["کنترل کیفیت", "بازرسی ابعادی و جوش، GD&amp;T، پیش از تحویل"],
    ["برآورد قیمت", "رایگان، معمولاً ظرف ۱ تا ۲ هفته"],
    ["محل", "تهران و اصفهان؛ برای سراسر ایران"],
   ],
   "what_h": "چه قطعه‌ها و مجموعه‌هایی می‌سازیم؟",
   "what": [
    ["ماشین‌کاری CNC", "تراش و فرز CNC قطعه‌های دقیق طبق نقشه و تلرانس‌های شما."],
    ["برش لیزر، خم‌کاری و نورد ورق", "ساخت قطعه‌های ورقی، بدنه و پوشش دستگاه‌ها."],
    [
     "سازه‌های جوشی فولادی و استیل ۳۱۶",
     "شاسی، استراکچر، سکو و سازه‌های بزرگ، تا حدود ۱ تا ۲ تن؛ همراه با نصب در محل در صورت نیاز.",
    ],
    ["محفظه و مخزن تحت فشار", "ساخت محفظه‌ها و مخازن صنعتی."],
    ["قالب تزریق پلاستیک", "طراحی و ماشین‌کاری قالب تزریق پلاستیک."],
    ["چاپ سه‌بعدی قطعه و نمونه", "نمونه‌ی اولیه، ماکت و قطعه با چاپ سه‌بعدی FDM و رزینی (DLP)."],
    ["بازرسی ابعادی و جوش (GD&amp;T)", "کنترل ابعاد، تلرانس‌های هندسی و کیفیت جوش پیش از تحویل."],
    ["مهندسی معکوس", "تهیه‌ی نقشه از روی قطعه‌ی موجود، وقتی نقشه در دست نیست."],
   ],
   "steps": [
    ["ارسال نقشه یا نمونه", "نقشه در هر فرمتی، عکس یا نمونه‌ی فیزیکی، همراه با تعداد مورد نیاز."],
    ["برآورد قیمت رایگان", "بررسی نقشه، فرآیند ساخت و جنس مناسب؛ معمولاً ظرف ۱ تا ۲ هفته."],
    [
     "بازبینی نقشه برای ساخت و مونتاژ",
     "پیش از ساخت، نقشه را از نظر قابلیت ساخت و جفت‌شدن قطعه‌ها بررسی می‌کنیم.",
    ],
    ["ساخت", "ساخت در کارگاه‌های همکار تهران و اصفهان زیر نظر سرپرست ساخت گروه."],
    ["کنترل کیفیت", "بازرسی ابعادی و جوش پیش از تحویل."],
    ["تحویل", "تحویل قطعه یا مجموعه‌ی مونتاژشده، و نصب در محل در صورت نیاز."],
   ],
   "projects": [
    [
     "rail-guided-test-platform",
     "p-platform-m.webp",
     "پلتفرم متحرک ریلی روی استخر (۱۴۰۳)",
     "سکو و اتاقک متحرک ریلی روی استخر آزمون کیفیت تصفیه‌ی آب؛ طراحی سازه، ساخت و نصب در محل.",
    ],
    ["injection-mould", "p-mold-m.webp", "قالب تزریق پلاستیک (۱۳۹۹)", "طراحی و ماشین‌کاری قالب تزریق پلاستیک."],
    [
     "postal-sorting-robots",
     "p-sorter-1-m.webp",
     "تولید سری ربات‌های سورتر پستی",
     "ساخت و مونتاژ ۸۰ ربات برای شرکت ملی پست (۵۰ دستگاه برای تهران و ۳۰ دستگاه برای کرمانشاه).",
    ],
    [
     "dental-aligners",
     "p-dental-m.webp",
     "الاینر ارتودنسی و لمینت دندان (۱۴۰۳)",
     "امکان‌سنجی و تولید الاینر ارتودنسی و لمینت متحرک دندان با چاپ سه‌بعدی رزینی (DLP).",
    ],
    [
     "jet-engine-model",
     "p-maquette-m.webp",
     "ماکت برش‌خورده‌ی موتور جت",
     "ماکت آموزشی و نمایشی موتور جت، ساخته‌شده با چاپ سه‌بعدی.",
    ],
   ],
   "faq": [
    [
     "سفارش تکی هم می‌پذیرید؟",
     "بله. تک‌نمونه و تیراژی هر دو را می‌پذیریم؛ تعداد مناسب برای تولید تیراژی به حجم کار بستگی دارد.",
    ],
    [
     "با چه موادی کار می‌کنید؟",
     "جنس هر قطعه را بر اساس کاربرد همان قطعه انتخاب می‌کنیم: از فولاد و استیل ضدزنگ ۳۱۶ تا آلومینیوم، پلاستیک‌های مهندسی و کامپوزیت. اگر جنس در نقشه مشخص است، طبق نقشه می‌سازیم.",
    ],
    [
     "قطعه‌ها و سازه‌های بزرگ هم می‌سازید؟",
     "بله. سازه‌هایی تا حدود ۱ تا ۲ تن ساخته‌ایم و در صورت نیاز نصب در محل را هم انجام می‌دهیم.",
    ],
    [
     "کیفیت قطعه‌ها را چطور کنترل می‌کنید؟",
     "پیش از تحویل، بازرسی ابعادی و جوش را خودمان انجام می‌دهیم و تلرانس‌های هندسی (GD&amp;T) را کنترل می‌کنیم.",
    ],
    [
     "اگر نقشه نداشته باشم چه؟",
     "اگر قطعه‌ی نمونه دارید، با مهندسی معکوس از روی آن نقشه تهیه می‌کنیم. اگر فقط ایده یا شرح کار دارید، طراحی را هم خودمان انجام می‌دهیم.",
    ],
    [
     "برآورد قیمت رایگان است؟ چقدر طول می‌کشد؟",
     "بله، برآورد قیمت رایگان است. معمولاً یک تا دو هفته طول می‌کشد، چون کارشناسان ما پیش از اعلام قیمت، کار را از نظر فنی بررسی می‌کنند و با مشاوران گروه مشورت می‌کنند تا قیمت و زمان اعلام‌شده واقعی باشد.",
    ],
    [
     "برای شروع چه اطلاعاتی لازم است؟ چه فرمت‌هایی از نقشه را می‌پذیرید؟",
     "هر چیزی که دارید کافی است: نقشه‌ی دوبعدی یا مدل سه‌بعدی در هر فرمتی (مثل STEP، DWG، DXF، SolidWorks یا PDF)، عکس، طرح دستی، یا فقط شرح کار. اگر نقشه ندارید و نمونه‌ی فیزیکی دارید، با مهندسی معکوس نقشه را از روی نمونه تهیه می‌کنیم.",
    ],
    [
     "بعد از تحویل چه پشتیبانی‌ای دارید؟",
     "ایرادهای دستگاه‌هایی را که خودمان طراحی کرده و ساخته‌ایم تا دو ماه پس از تحویل رفع می‌کنیم (جدا از درخواست‌های تازه‌ی کارفرما). ضمانت طولانی‌تر، تعمیر و ارتقا را هم هر طور که کارفرما بخواهد در قرارداد می‌گنجانیم. اگر طرح از کارفرما بوده و کار ما فقط پیمانکاری ساخت بوده، رفع ایرادِ ناشی از طرح را انجام می‌دهیم ولی هزینه‌ی آن جداگانه محاسبه می‌شود.",
    ],
    [
     "فقط در تهران و اصفهان کار می‌کنید؟",
     "خیر. دفتر و کارگاه‌های همکار ما در تهران و اصفهان است، ولی برای کارفرمایان سراسر ایران کار می‌کنیم.",
    ],
   ],
  },
  "en": {
   "card_h": "Industrial parts manufacturing — Tehran & Isfahan",
   "card_p": "Parts and assemblies made to your drawings, one-off or in series, with our own quality control before delivery.",
   "card_list": [
    "CNC machining, laser cutting, bending and rolling",
    "Welded structures in steel and 316 stainless",
    "Pressure vessels and enclosures",
    "Plastic injection moulds",
    "Dimensional and weld inspection, GD&amp;T",
   ],
   "title": "Industrial Parts Manufacturing to Drawing in Tehran & Isfahan — CNC, Laser Cutting, Welded Structures | Enteha",
   "desc": "Industrial parts and assemblies made to your drawings, one-off or in series: CNC machining, laser cutting, bending and rolling, steel and 316 stainless welded structures, vessels, injection moulds and dimensional inspection. Serving all of Iran.",
   "nav": "Industrial parts manufacturing",
   "h1": "Industrial parts made to your drawings — one-off or in series",
   "lead": [
    "Enteha Group makes industrial parts and assemblies to your drawings, one-off or in series, with partner workshops in Tehran and Isfahan, and carries out its own quality control before delivery: CNC machining, laser cutting, bending and rolling, welded structures in steel and 316 stainless, pressure vessels and enclosures, plastic injection moulds, and dimensional and weld inspection with GD&amp;T.",
    "Because we design and build machines ourselves, we do not just follow the drawing — we also think about how the parts fit together at assembly, so there are no surprises on assembly day. We work for clients across Iran, and quotes are free.",
   ],
   "facts": [
    ["Processes", "CNC machining, laser cutting, bending, rolling, welding, mould making, 3D printing"],
    ["Materials", "Steel, 316 stainless and whatever material the part's application calls for"],
    ["Size of past work", "From small parts to structures of about 1–2 tonnes"],
    ["Order size", "One-off to series"],
    ["Drawings", "Any format; reverse engineering from a sample"],
    ["Quality control", "Dimensional and weld inspection, GD&amp;T, before delivery"],
    ["Quote", "Free, usually within 1–2 weeks"],
    ["Location", "Tehran and Isfahan; serving all of Iran"],
   ],
   "what_h": "What parts and assemblies do we make?",
   "what": [
    ["CNC machining", "CNC turning and milling of precision parts to your drawings and tolerances."],
    ["Laser cutting, bending and rolling", "Sheet-metal parts, machine frames, housings and covers."],
    [
     "Welded structures in steel and 316 stainless",
     "Chassis, frames, platforms and large structures of up to about 1–2 tonnes, with on-site installation where needed.",
    ],
    ["Pressure vessels and enclosures", "Industrial enclosures and vessels."],
    ["Plastic injection moulds", "Design and machining of plastic injection moulds."],
    ["3D-printed parts and prototypes", "Prototypes, models and parts by FDM and resin (DLP) 3D printing."],
    [
     "Dimensional and weld inspection (GD&amp;T)",
     "Checking dimensions, geometric tolerances and weld quality before delivery.",
    ],
    ["Reverse engineering", "Drawings made from an existing part when no drawings are available."],
   ],
   "steps": [
    [
     "Send drawings or a sample",
     "Drawings in any format, photos or a physical sample, plus the quantity you need.",
    ],
    ["Free quote", "Review of the drawings, fabrication process and suitable material; usually within 1–2 weeks."],
    [
     "Drawing review for fabrication and assembly",
     "Before fabrication, we check the drawings for manufacturability and for how the parts fit together.",
    ],
    [
     "Fabrication",
     "Fabrication in partner workshops in Tehran and Isfahan, supervised by the group's manufacturing lead.",
    ],
    ["Quality control", "Dimensional and weld inspection before delivery."],
    ["Delivery", "Delivery of the parts or the assembled unit, with on-site installation where needed."],
   ],
   "projects": [
    [
     "rail-guided-test-platform",
     "p-platform-m.webp",
     "Rail-guided platform over a test pool (2024)",
     "A rail-guided moving platform and cabin over a pool used for water treatment quality testing; structural design, fabrication and on-site installation.",
    ],
    [
     "injection-mould",
     "p-mold-m.webp",
     "Plastic injection mould (2020)",
     "Design and machining of a plastic injection mould.",
    ],
    [
     "postal-sorting-robots",
     "p-sorter-1-m.webp",
     "Series production of postal sorting robots",
     "Fabrication and assembly of 80 robots for Iran Post (50 units for Tehran and 30 for Kermanshah).",
    ],
    [
     "dental-aligners",
     "p-dental-m.webp",
     "Dental aligners & veneers (2024)",
     "Feasibility study and production of orthodontic aligners and removable veneers by resin (DLP) 3D printing.",
    ],
    [
     "jet-engine-model",
     "p-maquette-m.webp",
     "Jet engine cutaway model",
     "A jet engine cutaway model for display and training, made by 3D printing.",
    ],
   ],
   "faq": [
    [
     "Do you take one-off orders?",
     "Yes. We take both one-off and series orders; the right quantity for series production depends on the job.",
    ],
    [
     "Which materials do you work with?",
     "We choose the material of each part for its application — from steel and 316 stainless to aluminium, engineering plastics and composites. If the drawing specifies the material, we follow the drawing.",
    ],
    [
     "Do you make large parts and structures?",
     "Yes. We have built structures of about 1–2 tonnes and can install them on site where needed.",
    ],
    [
     "How do you control quality?",
     "Before delivery we carry out our own dimensional and weld inspection and check geometric tolerances (GD&amp;T).",
    ],
    [
     "What if I have no drawings?",
     "If you have a sample part, we reverse-engineer drawings from it. If you only have an idea or a description, we can do the design as well.",
    ],
    [
     "Is the quote free? How long does it take?",
     "Yes, quotes are free. A quote usually takes one to two weeks, because our engineers review the job technically and consult the group's advisers before giving a price, so that the price and schedule we quote are realistic.",
    ],
    [
     "What do you need to get started? Which drawing formats do you accept?",
     "Whatever you have is enough: 2D drawings or 3D models in any format (such as STEP, DWG, DXF, SolidWorks or PDF), photos, a hand sketch, or just a description of the job. If you have a physical sample but no drawings, we reverse-engineer the drawings from the sample.",
    ],
    [
     "What support do you give after delivery?",
     "For machines we designed and built ourselves, we fix any faults for two months after delivery (separate from new requests from the client). A longer warranty, repairs and upgrades can be written into the contract however the client wants. If the design came from the client and we only did the fabrication, we still fix faults caused by the design, but that work is charged separately.",
    ],
    [
     "Do you only work in Tehran and Isfahan?",
     "No. Our office and partner workshops are in Tehran and Isfahan, but we work for clients across Iran.",
    ],
   ],
  },
 },
]

# «چرا انتها؟»، صنایع و فهرست تیم در صفحه‌های خدمات
WHY = {
 "fa": {
  "home": "خانه",
  "services": "خدمات",
  "contact": "تماس",
  "switch": "English",
  "glance": "در یک نگاه",
  "process": "مراحل کار",
  "work": "نمونه‌کارهای ما",
  "industries": "صنایعی که برایشان کار کرده‌ایم",
  "why": "چرا انتها؟",
  "team": "چه کسانی کار را انجام می‌دهند؟",
  "faq": "پرسش‌های متداول",
  "related": "خدمات دیگر انتها",
  "updated": "آخرین به‌روزرسانی:",
  "quote_btn": "درخواست برآورد قیمت رایگان",
  "call_btn": "تماس تلفنی",
  "cta_h": "برآورد قیمت رایگان بگیرید",
  "cta_p": "شرح کار، نقشه یا حتی عکس نمونه را بفرستید. کارشناسان ما پس از بررسی فنی و مشورت با مشاوران، معمولاً ظرف یک تا دو هفته برآورد قیمت را اعلام می‌کنند.",
  "name": "نام شما",
  "email": "ایمیل شما",
  "msg": "شرح پروژه…",
  "send": "ارسال درخواست",
  "sending": "در حال ارسال…",
  "ok": "درخواست شما رسید؛ به‌زودی با شما تماس می‌گیریم.",
  "err": "ارسال نشد. لطفاً دوباره امتحان کنید یا تماس بگیرید.",
  "net": "خطای شبکه. لطفاً تماس بگیرید.",
  "other": "راه‌های ارتباطی دیگر:",
  "rights": "همه‌ی حقوق محفوظ است.",
  "why_list": [
   "<strong>یک مسئول از طراحی تا مونتاژ.</strong> بیشتر دردسرهای برون‌سپاری از آنجا شروع می‌شود که طراحی، ساخت و مونتاژ دست چند نفر مختلف است و هیچ‌کس کل دستگاه را نمی‌بیند. در انتها کسی که طراحی می‌کند تا آخر کار بالای سر ساخت و مونتاژ می‌ماند.",
   "<strong>هسته‌ی مهندسی و شبکه‌ی همکاران.</strong> سه مهندس مکانیک دانش‌آموخته‌ی دانشگاه‌های صنعتی شریف، علم و صنعت، خواجه نصیر و تربیت مدرس، همراه با کارگاه‌های صنعتی و مهندسان متخصص تحلیل، کنترل کیفی و مشاوره.",
   "<strong>کارنامه‌ی قابل‌بررسی.</strong> ساخت ۸۰ ربات سورتر برای شرکت ملی پست، نخستین دستگاه تست پروتز زانو از این نوع در ایران، برگزیده‌ی جایزه‌ی البرز و دو بار جشنواره‌ی جوان خوارزمی، و مقاله در مجله‌های Scientific Reports و International Journal of Mechanical Sciences.",
   "<strong>کنترل کیفیت پیش از تحویل.</strong> بازرسی ابعادی و جوش و تست عملکرد را خودمان پیش از تحویل انجام می‌دهیم.",
  ],
  "industry_list": [
   "تجهیزات پزشکی و دندان‌پزشکی",
   "پست و لجستیک",
   "ساخت افزایشی (پرینت سه‌بعدی)",
   "دانشگاه‌ها و مراکز تحقیقاتی",
   "رباتیک خدماتی",
  ],
  "team_list": [
   [
    "حسن نصیری خونساری",
    "مدیر فنی و طراحی",
    "کارشناسی ارشد طراحی کاربردی، دانشگاه صنعتی شریف؛ کارشناسی مکانیک، دانشگاه علم و صنعت ایران",
    "https://www.linkedin.com/in/hassan-nasiri-khonsari-44bb49198/",
    "av-hassan.webp",
   ],
   [
    "علیرضا پیرحاجی",
    "سرپرست ساخت و کنترل کیفیت",
    "کارشناسی ارشد ساخت و تولید، دانشگاه تربیت مدرس؛ کارشناسی مکانیک، دانشگاه صنعتی شریف",
    "https://www.linkedin.com/in/alireza-pirhaji-9a0787139/",
    "av-alireza.webp",
   ],
   [
    "سید مصطفی بنی‌هاشمی",
    "سرپرست پروژه و تحقیق و توسعه",
    "کارشناسی ارشد طراحی کاربردی (دینامیک، کنترل و رباتیک)، دانشگاه صنعتی شریف؛ کارشناسی مکانیک، دانشگاه خواجه نصیر",
    "https://www.linkedin.com/in/mostafa-banihashemi/",
    "av-mostafa.webp",
   ],
  ],
 },
 "en": {
  "home": "Home",
  "services": "Services",
  "contact": "Contact",
  "switch": "فارسی",
  "glance": "At a glance",
  "process": "How we work",
  "work": "Our work",
  "industries": "Industries we have worked for",
  "why": "Why Enteha?",
  "team": "Who does the work?",
  "faq": "Frequently asked questions",
  "related": "Other Enteha services",
  "updated": "Last updated:",
  "quote_btn": "Request a free quote",
  "call_btn": "Call us",
  "cta_h": "Get a free quote",
  "cta_p": "Send us a description, a drawing or even a photo of a sample. After a technical review and consultation with our advisers, we usually send the quote within one to two weeks.",
  "name": "Your name",
  "email": "Your email",
  "msg": "Describe your project…",
  "send": "Send request",
  "sending": "Sending…",
  "ok": "Thank you — we have your request and will be in touch soon.",
  "err": "Could not send. Please try again or call us.",
  "net": "Network error. Please call us.",
  "other": "Other ways to reach us:",
  "rights": "All rights reserved.",
  "why_list": [
   "<strong>One owner from design to assembly.</strong> Most outsourcing trouble starts when design, fabrication and assembly are in different hands and nobody sees the whole machine. At Enteha, the engineer who designs it stays with fabrication and assembly to the end.",
   "<strong>A core engineering team plus a partner network.</strong> Three mechanical engineers from Sharif University of Technology, IUST, K. N. Toosi and Tarbiat Modares University, working with industrial workshops and specialist engineers in analysis, quality control and consulting.",
   "<strong>A track record you can check.</strong> 80 postal sorting robots built for Iran Post, the first knee-prosthesis test rig of its kind in Iran, the Alborz Elite Prize and two Khwarizmi Youth Festival awards, and papers in Scientific Reports and the International Journal of Mechanical Sciences.",
   "<strong>Quality control before delivery.</strong> We carry out dimensional and weld inspection and functional testing ourselves before anything ships.",
  ],
  "industry_list": [
   "Medical and dental devices",
   "Postal and logistics",
   "Additive manufacturing (3D printing)",
   "Universities and research centres",
   "Service robotics",
  ],
  "team_list": [
   [
    "Hassan Nasiri Khonsari",
    "Technical & Design Director",
    "MSc Applied Design, Sharif University of Technology; BSc Mechanical Engineering, IUST",
    "https://www.linkedin.com/in/hassan-nasiri-khonsari-44bb49198/",
    "av-hassan.webp",
   ],
   [
    "Alireza Pirhaji",
    "Manufacturing & Quality Lead",
    "MSc Manufacturing Engineering, Tarbiat Modares University; BSc Mechanical Engineering, Sharif University of Technology",
    "https://www.linkedin.com/in/alireza-pirhaji-9a0787139/",
    "av-alireza.webp",
   ],
   [
    "Seyed Mostafa Banihashemi",
    "Project & R&D Lead",
    "MSc Applied Design (Dynamics, Control & Robotics), Sharif University of Technology; BSc Mechanical Engineering, K. N. Toosi University",
    "https://www.linkedin.com/in/mostafa-banihashemi/",
    "av-mostafa.webp",
   ],
  ],
 },
}

# نمونه‌کارها، به همان ترتیبی که نمایش داده می‌شوند. هر پروژه یک صفحه دارد: /projects/<slug>.html
# slug را بعد از انتشار عوض نکنید (آدرس صفحه و شناسه‌ی آمار است).
# imgs: [فایل، عرض، ارتفاع، زیرنویس فارسی، زیرنویس انگلیسی]؛ هر عکس یک نسخه‌ی کوچک -t.webp هم لازم دارد.
# service: خدمت مرتبط (slug یکی از SERVICES). short: یک جمله برای کارت و پیش‌نمایش.
PROJECTS = [
 {
  "slug": "postal-sorting-robots",
  "date": "2020",
  "service": "custom-machines",
  "who": ["h", "a"],
  "year": {"fa": "۱۳۹۹ تا ۱۴۰۴", "en": "2020–2025"},
  "imgs": [
   ["p-sorter-1.webp", 1344, 896, "نسل اول", "Generation 1"],
   ["p-sorter-2.webp", 1288, 924, "نسل دوم", "Generation 2"],
   ["p-sorter-3.webp", 1288, 952, "نسل سوم", "Generation 3"],
  ],
  "fa": {
   "title": "ربات‌های سورتر پستی",
   "short": "ساخت ۸۰ ربات خودگردان تفکیک مرسولات برای شرکت ملی پست؛ طراحی نسل سوم در تیراژ ۲۰۰ دستگاه به تولید رسید.",
   "desc": [
    "ربات‌های سورتر خودگردان برای تفکیک مرسولات در شرکت ملی پست. ساخت و مونتاژ نسل‌های اول و دوم را انجام دادیم: ۵۰ دستگاه برای مرکز توزیع تهران و ۳۰ دستگاه برای کرمانشاه، در مجموع ۸۰ ربات.",
    "طراحی نسل سوم، شامل مکانیزم تخلیه‌ی بار، سامانه‌ی توزین، استراکچر و سیستم حرکت، کار حسن نصیری خونساری است که در تیراژ ۲۰۰ دستگاه به تولید رسید. این پروژه مقام دوم بیست‌وششمین جشنواره‌ی جوان خوارزمی را گرفت.",
   ],
   "tags": ["ساخت ربات", "تولید سری", "طراحی مکانیک"],
  },
  "en": {
   "title": "Postal sorting robots",
   "short": "80 autonomous parcel-sorting robots built for Iran Post; the third-generation design went into production as a 200-unit series.",
   "desc": [
    "Autonomous sorting robots for parcel sorting at Iran Post. We built and assembled the first and second generations: 50 robots for the Tehran distribution centre and 30 for Kermanshah, 80 in total.",
    "The third generation was designed by Hassan Nasiri Khonsari — unloading mechanism, weighing system, frame and drive — and went into production at a volume of 200 units. The project won second place at the 26th Khwarizmi Youth Festival.",
   ],
   "tags": ["Robot fabrication", "Series production", "Mechanical design"],
  },
 },
 {
  "slug": "knee-prosthesis-test-rig",
  "date": "2021",
  "service": "custom-machines",
  "who": ["h"],
  "year": {"fa": "۱۴۰۰", "en": "2021"},
  "imgs": [["p-knee.webp", 952, 1288, "", ""]],
  "fa": {
   "title": "دستگاه تست تقید و پایداری پروتز زانو",
   "short": "دستگاه آزمون پروتز کامل زانو در شش درجه‌ی آزادی مطابق <bdi>ASTM F1223</bdi>؛ نخستین نمونه از این نوع در ایران.",
   "desc": [
    "دستگاهی برای آزمون تقید و پایداری پروتز کامل زانو در شش درجه‌ی آزادی، مطابق استاندارد <bdi>ASTM F1223</bdi>؛ پایان‌نامه‌ی کارشناسی ارشد در دانشگاه صنعتی شریف، زیر نظر دکتر محمد دورعلی و با مشاوره‌ی دکتر فرهمند. طراحی مکانیکی، معماری اتوماسیون، برنامه‌نویسی <bdi>PLC</bdi> و توسعه‌ی <bdi>HMI</bdi> همه در همین پروژه انجام شد. دستگاه تحویل شده و در کارهای پژوهشی استفاده می‌شود.",
    "پیش از این، نمونه‌ی مشابهی در ایران وجود نداشت و معادل‌های تجاری آن را شرکت‌هایی مثل <bdi>EndoLab</bdi> آلمان و <bdi>AMTI</bdi> آمریکا می‌سازند. این پروژه عنوان برترین پایان‌نامه‌ی فناورانه‌ی دانشکده، مقام دوم بیست‌وچهارمین جشنواره‌ی جوان خوارزمی و برگزیدگی در شصت‌وچهارمین جایزه‌ی البرز را به دست آورد. بعدها همین دستگاه برای مطالعه‌ی اصطکاک میان استخوان و ایمپلنت بازپیکربندی شد که حاصلش مقاله‌ای در <bdi>Scientific Reports</bdi> است.",
   ],
   "tags": ["تجهیزات پزشکی", "اتوماسیون", "<bdi>ASTM F1223</bdi>"],
  },
  "en": {
   "title": "Knee prosthesis constraint & stability test rig",
   "short": "A six-degree-of-freedom test rig for total knee prostheses to ASTM F1223 — the first of its kind in Iran.",
   "desc": [
    "A six-degree-of-freedom rig for constraint and stability testing of total knee prostheses to ASTM F1223, built as an MSc thesis at Sharif University of Technology under Dr Mohammad Durali, advised by Dr Farzam Farahmand. Mechanical design, automation architecture, PLC programming and HMI development were all done in-house. The rig has been delivered and is in research use.",
    "No comparable machine existed in Iran; commercial equivalents come from companies such as EndoLab (Germany) and AMTI (USA). The project was named the faculty's best technological thesis, took second place at the 24th Khwarizmi Youth Festival, and was selected at the 64th Alborz Elite Prize. The rig was later reconfigured to study bone–implant friction, leading to a paper in Scientific Reports.",
   ],
   "tags": ["Medical devices", "Automation", "ASTM F1223"],
  },
 },
 {
  "slug": "dmd-powder-feeder",
  "date": "2019",
  "service": "automation",
  "who": ["h"],
  "year": {"fa": "۱۳۹۸", "en": "2019"},
  "imgs": [["p-dmd.webp", 1288, 952, "", ""]],
  "fa": {
   "title": "سامانه‌ی تغذیه‌ی پودر DMD",
   "short": "تغذیه‌کننده‌ی پودر برای لایه‌نشانی مستقیم فلز با لیزر، با کنترل نرخ تغذیه از ۱ تا ۱۰۰ گرم بر دقیقه.",
   "desc": [
    "تغذیه‌کننده‌ی پودر برای فرآیند لایه‌نشانی مستقیم فلز با لیزر (<bdi>DMD</bdi>). طراحی تفصیلی، ساخت و پیاده‌سازی کامل الکترونیک، کنترل و منطق دستگاه در همین پروژه انجام شد؛ نرخ تغذیه در بازه‌ی ۱ تا ۱۰۰ گرم بر دقیقه کنترل می‌شود.",
    "این پروژه پایان‌نامه‌ی کارشناسی در دانشگاه علم و صنعت ایران بود، زیر نظر دکتر سید علی نیکنام.",
   ],
   "tags": ["ساخت افزایشی فلز", "کنترل", "الکترونیک"],
  },
  "en": {
   "title": "DMD powder feeder",
   "short": "A powder feeder for laser direct metal deposition, controlling the feed rate between 1 and 100 g/min.",
   "desc": [
    "A powder feeder for laser direct metal deposition (DMD). Detailed design, fabrication, and the complete electronics, control and machine logic were developed in-house; the feed rate is controlled between 1 and 100 g/min.",
    "This was a BSc thesis at Iran University of Science and Technology, supervised by Dr Seyed Ali Niknam.",
   ],
   "tags": ["Metal additive manufacturing", "Control", "Electronics"],
  },
 },
 {
  "slug": "industrial-3d-printers",
  "date": "2020",
  "service": "custom-machines",
  "who": ["h"],
  "year": {"fa": "۱۳۹۹ تا ۱۴۰۲", "en": "2020–2023"},
  "imgs": [
   ["p-printer-1.webp", 1288, 952, "نسل اول — ۳۰×۳۰×۴۰ سانتی‌متر", "Generation 1 — 30 × 30 × 40 cm"],
   ["p-printer-2.webp", 756, 1008, "نسل دوم — ۳۰×۳۰×۴۰ سانتی‌متر", "Generation 2 — 30 × 30 × 40 cm"],
   ["p-printer-3.webp", 980, 1232, "نسل سوم — ۵۰×۵۰×۴۰ سانتی‌متر", "Generation 3 — 50 × 50 × 40 cm"],
  ],
  "fa": {
   "title": "پرینترهای سه‌بعدی FDM صنعتی",
   "short": "پنج پرینتر <bdi>FDM</bdi> که از صفر طراحی و ساخته شدند، تا ماشینی صنعتی با حجم کاری ۵۰۰×۵۰۰×۴۰۰ میلی‌متر.",
   "desc": [
    "پنج دستگاه که از صفر طراحی و ساخته شدند و نسل‌به‌نسل بازمهندسی شدند: از یک دستگاه ۲۰۰×۲۰۰×۱۵۰ میلی‌متری تا ماشینی صنعتی با حجم کاری ۵۰۰×۵۰۰×۴۰۰ میلی‌متر که روی همه‌ی محورها بال‌اسکرو و ریل خطی صنعتی دارد.",
    "سازه، مکانیزم، انتخاب موتورها، الکترونیک، فرم‌ور و بهینه‌سازی اسلایسر همه مستقل انجام شد.",
   ],
   "tags": ["پرینت سه‌بعدی", "طراحی مکانیزم", "الکترونیک و فرم‌ور"],
  },
  "en": {
   "title": "Industrial FDM 3D printers",
   "short": "Five FDM printers designed and built from scratch, up to an industrial machine with a 500 × 500 × 400 mm build volume.",
   "desc": [
    "Five machines designed and built from scratch and re-engineered generation by generation: from a 200 × 200 × 150 mm printer to an industrial machine with a 500 × 500 × 400 mm build volume, ball screws and industrial linear rails on every axis.",
    "Frame, mechanism, motor selection, electronics, firmware and slicer tuning were all done independently.",
   ],
   "tags": ["3D printing", "Mechanism design", "Electronics & firmware"],
  },
 },
 {
  "slug": "rail-guided-test-platform",
  "date": "2024",
  "service": "parts-manufacturing",
  "who": ["h", "a", "m"],
  "year": {"fa": "۱۴۰۳", "en": "2024"},
  "imgs": [["p-platform.webp", 586, 780, "", ""]],
  "fa": {
   "title": "پلتفرم متحرک ریلی روی استخر",
   "short": "سکو و اتاقک متحرک ریلی روی استخر آزمون تصفیه‌ی آب: طراحی سازه، ساخت و نصب در محل.",
   "desc": [
    "سکو و اتاقک متحرک ریلی روی استخری که برای آزمون کیفیت تصفیه‌ی آب استفاده می‌شود. سازه، ساخت و نصب در محل را تیم انجام داد.",
   ],
   "tags": ["سازه‌ی جوشی", "ساخت", "نصب"],
  },
  "en": {
   "title": "Rail-guided platform over a test pool",
   "short": "A rail-guided platform and cabin over a water-treatment test pool: structural design, fabrication and on-site installation.",
   "desc": [
    "A rail-guided mobile platform and cabin built over a pool used for water-treatment quality testing. The team handled the structure, fabrication and on-site installation.",
   ],
   "tags": ["Welded structure", "Fabrication", "Installation"],
  },
 },
 {
  "slug": "cable-rehabilitation-robot",
  "date": "2022",
  "service": "custom-machines",
  "who": ["m"],
  "year": {"fa": "۱۴۰۱ تا ۱۴۰۴", "en": "2022–2025"},
  "imgs": [["p-rehab.webp", 780, 585, "", ""]],
  "fa": {
   "title": "ربات کابلی توانبخشی",
   "short": "ربات کابلی برای اصلاح ناراستایی وضعیتی در کودکان دچار فلج مغزی؛ طراحی، ساخت و کنترل.",
   "desc": [
    "طراحی، ساخت و کنترل یک سیستم رباتیک کابلی برای اصلاح ناراستایی وضعیتی در کودکان دچار فلج مغزی. پایان‌نامه‌ی کارشناسی ارشد در دانشگاه صنعتی شریف، زیر نظر دکتر فرزام فرهمند و دکتر محمد دورعلی.",
   ],
   "tags": ["رباتیک پزشکی", "ربات کابلی", "کنترل"],
  },
  "en": {
   "title": "Cable-driven rehabilitation robot",
   "short": "A cable-driven robot to improve postural alignment in children with cerebral palsy: design, fabrication and control.",
   "desc": [
    "A cable-driven robotic system to improve postural alignment in children with cerebral palsy — design, fabrication and control. MSc thesis at Sharif University of Technology, supervised by Dr Farzam Farahmand and Dr Mohammad Durali.",
   ],
   "tags": ["Medical robotics", "Cable-driven robot", "Control"],
  },
 },
 {
  "slug": "waiter-robots",
  "date": "2021",
  "service": "custom-machines",
  "who": ["h"],
  "year": {"fa": "۱۴۰۰", "en": "2021"},
  "imgs": [["p-waiter.webp", 896, 1344, "", ""]],
  "fa": {
   "title": "ربات‌های گارسون",
   "short": "ناوگانی هفت‌تایی از ربات‌های حمل و سرو غذا که روی کف ناهموار رستوران هم پایدار کار می‌کنند.",
   "desc": [
    "طراحی، ساخت و مونتاژ مکانیکی ناوگانی هفت‌تایی از ربات‌های گارسون برای حمل و سرو غذا در رستوران.",
    "تمرکز اصلی روی شاسی و سیستم حرکت بود تا ربات‌ها روی کف ناهموار رستوران هم پایدار و قابل اعتماد کار کنند؛ بدنه هم با در نظر گرفتن ایمنی و ظاهر مناسب محیط پذیرایی طراحی شد.",
   ],
   "tags": ["رباتیک خدماتی", "طراحی بدنه"],
  },
  "en": {
   "title": "Waiter robots",
   "short": "A fleet of seven food delivery and serving robots that stay stable on uneven restaurant floors.",
   "desc": [
    "Design, fabrication and mechanical assembly of a fleet of seven waiter robots for carrying and serving food in a restaurant.",
    "The main focus was the chassis and drive, so the robots stay stable and reliable on uneven restaurant floors; the body was designed with safety and a look suited to a dining room in mind.",
   ],
   "tags": ["Service robotics", "Body design"],
  },
 },
 {
  "slug": "dual-purpose-cnc",
  "date": "2023",
  "service": "custom-machines",
  "who": ["h"],
  "year": {"fa": "۱۴۰۲", "en": "2023"},
  "imgs": [
   ["p-cnc.webp", 1372, 896, "دستگاه", "Machine"],
   ["p-cnc-panel.webp", 1148, 1064, "تابلو برق", "Electrical cabinet"],
   ["p-cnc-panel-open.webp", 952, 1288, "داخل تابلو برق", "Inside the cabinet"],
  ],
  "fa": {
   "title": "CNC صنعتی دوکاره",
   "short": "<bdi>CNC</bdi> ماژولار با میز حدود ۱۰۰×۱۰۰ سانتی‌متر برای چوب و فلزات سبک که با تعویض هد، پرینتر سه‌بعدی می‌شود.",
   "desc": [
    "یک دستگاه <bdi>CNC</bdi> صنعتی برای برش چوب و فلزات سبک با میز کاری بزرگ (حدود ۱۰۰×۱۰۰ سانتی‌متر) که به‌صورت ماژولار طراحی شده است؛ یعنی با تعویض ساده‌ی هد، می‌تواند به یک پرینتر سه‌بعدی قدرتمند تبدیل شود.",
    "طراحی سازه، انتخاب درایوها و موتورها و راه‌اندازی سیستم کنترل با <bdi>G-Code</bdi> بخشی از این کار بود. هدف، ساخت یک ماشین چندکاره و مقرون‌به‌صرفه برای کارگاه‌های کوچک و متوسط بود.",
   ],
   "tags": ["<bdi>CNC</bdi>", "<bdi>CAM</bdi>", "طراحی سازه"],
  },
  "en": {
   "title": "Dual-purpose industrial CNC",
   "short": "A modular CNC with a bed of about 100 × 100 cm for wood and light metals that becomes a 3D printer with a head swap.",
   "desc": [
    "An industrial CNC for cutting wood and light metals with a large bed (about 100 × 100 cm), designed as a modular machine: swapping the head turns it into a capable 3D printer.",
    "Structural design, selection of drives and motors, and setting up the G-code control system were part of the work. The goal was an affordable multi-purpose machine for small and medium workshops.",
   ],
   "tags": ["CNC", "CAM", "Structural design"],
  },
 },
 {
  "slug": "dental-aligners",
  "date": "2024",
  "service": "parts-manufacturing",
  "who": ["a"],
  "year": {"fa": "۱۴۰۳", "en": "2024"},
  "imgs": [["p-dental.webp", 780, 439, "", ""]],
  "fa": {
   "title": "الاینر ارتودنسی و لمینت دندان",
   "short": "تولید الاینر ارتودنسی و لمینت متحرک دندان با چاپ سه‌بعدی رزینی (<bdi>DLP</bdi>).",
   "desc": ["امکان‌سنجی و تولید الاینر ارتودنسی و لمینت متحرک دندان به روش چاپ سه‌بعدی رزینی (<bdi>DLP</bdi>)."],
   "tags": ["چاپ سه‌بعدی رزینی", "تجهیزات دندانی"],
  },
  "en": {
   "title": "Dental aligners & veneers",
   "short": "Orthodontic aligners and removable dental veneers produced by resin (DLP) 3D printing.",
   "desc": [
    "Feasibility study and production of orthodontic aligners and removable dental veneers by resin (DLP) 3D printing.",
   ],
   "tags": ["Resin 3D printing", "Dental devices"],
  },
 },
 {
  "slug": "conveyor-3d-printer",
  "date": "",
  "service": "custom-machines",
  "who": ["a"],
  "year": {"fa": "", "en": ""},
  "imgs": [["p-conveyor.webp", 586, 780, "", ""]],
  "fa": {
   "title": "پرینتر سه‌بعدی نوار نقاله‌ای (FDM)",
   "short": "پرینتر <bdi>FDM</bdi> با بستر نوار نقاله‌ای برای چاپ پیوسته‌ی قطعات بلند و تولید دسته‌ای.",
   "desc": ["پرینتر <bdi>FDM</bdi> با بستر نوار نقاله‌ای برای چاپ پیوسته‌ی قطعات بلند و تولید دسته‌ای."],
   "tags": ["پرینت سه‌بعدی", "چاپ پیوسته"],
  },
  "en": {
   "title": "Conveyor-belt FDM 3D printer",
   "short": "An FDM printer with a conveyor-belt bed for continuous printing of long parts and batches.",
   "desc": ["An FDM printer with a conveyor-belt bed for continuous printing of long parts and batches."],
   "tags": ["3D printing", "Continuous printing"],
  },
 },
 {
  "slug": "injection-mould",
  "date": "2020",
  "service": "parts-manufacturing",
  "who": ["a"],
  "year": {"fa": "۱۳۹۹", "en": "2020"},
  "imgs": [["p-mold.webp", 735, 820, "", ""]],
  "fa": {
   "title": "قالب تزریق پلاستیک",
   "short": "طراحی و ماشین‌کاری قالب تزریق پلاستیک.",
   "desc": ["طراحی و ماشین‌کاری قالب تزریق پلاستیک."],
   "tags": ["طراحی قالب", "ماشین‌کاری"],
  },
  "en": {
   "title": "Plastic injection mould",
   "short": "Design and machining of a plastic injection mould.",
   "desc": ["Design and machining of a plastic injection mould."],
   "tags": ["Mould design", "Machining"],
  },
 },
 {
  "slug": "jet-engine-model",
  "date": "",
  "service": "parts-manufacturing",
  "who": ["a"],
  "year": {"fa": "", "en": ""},
  "imgs": [["p-maquette.webp", 780, 586, "", ""]],
  "fa": {
   "title": "ماکت برش‌خورده‌ی موتور جت",
   "short": "ماکت برش‌خورده‌ی موتور جت برای نمایش و آموزش، ساخته‌شده با چاپ سه‌بعدی.",
   "desc": ["ماکت برش‌خورده‌ی موتور جت برای نمایش و آموزش، ساخته‌شده با چاپ سه‌بعدی."],
   "tags": ["ماکت‌سازی", "پرینت سه‌بعدی"],
  },
  "en": {
   "title": "Jet engine cutaway model",
   "short": "A 3D-printed cutaway model of a jet engine for display and teaching.",
   "desc": ["A 3D-printed cutaway model of a jet engine for display and teaching."],
   "tags": ["Model making", "3D printing"],
  },
 },
 {
  "slug": "cable-drawing-robot",
  "date": "2020",
  "service": "custom-machines",
  "who": ["h"],
  "year": {"fa": "۱۳۹۹", "en": "2020"},
  "imgs": [["p-painter.webp", 896, 1344, "", ""]],
  "fa": {
   "title": "ربات نقاش کابلی",
   "short": "ربات نقاش کابلی که هر عکس را به نقاشی سیاه‌قلم تبدیل می‌کند و روی بوم می‌کشد.",
   "desc": [
    "یک ربات نقاش بر پایه‌ی مکانیزم ربات‌های کابلی که قلم را با کنترل طول کابل‌ها در صفحه حرکت می‌دهد. این ربات می‌تواند هر عکس را به یک نقاشی سیاه‌قلم تبدیل کند و روی بوم بکشد (در تصویر، نقشه‌ی ایران را رسم کرده است).",
    "بخش جذاب پروژه، الگوریتم تبدیل تصویر به مسیر قلم و هماهنگی دقیق حرکت کابل‌ها برای رسیدن قلم به نقطه‌ی دلخواه بود.",
   ],
   "tags": ["ربات کابلی", "پردازش تصویر", "کنترل"],
  },
  "en": {
   "title": "Cable-driven drawing robot",
   "short": "A cable-driven drawing robot that turns any photo into a line drawing and draws it on canvas.",
   "desc": [
    "A drawing robot based on a cable-driven mechanism that moves a pen across the canvas by controlling cable lengths. It turns any photo into a line drawing and draws it on the canvas (shown here drawing a map of Iran).",
    "The interesting part was the algorithm that converts an image into a pen path, and the precise coordination of the cables to bring the pen to any point.",
   ],
   "tags": ["Cable robot", "Image processing", "Control"],
  },
 },
]

# افتخارات: top=True یعنی در صفحه‌ی اصلی هم نمایش داده شود. [عنوان، توضیح]
HONORS = [
 {
  "icon": "medal",
  "top": True,
  "who": ["h"],
  "fa": [
   "برگزیده‌ی شصت‌وچهارمین جایزه‌ی البرز نخبگانی",
   "یکی از ۱۲ برگزیده‌ی بخش فناوران و مخترعان، برای دستگاه تست تقید و پایداری پروتز زانو؛ همراه با تقدیر دانشگاه صنعتی شریف و اهدای مدال نقره — ۱۴۰۵.",
  ],
  "en": [
   "Laureate, 64th Alborz Elite Prize",
   "One of 12 laureates in the Technologists & Inventors category, for the knee prosthesis constraint and stability test rig; with a commendation from Sharif University of Technology and a silver medal — 2026.",
  ],
 },
 {
  "icon": "trophy",
  "top": True,
  "who": ["h", "a"],
  "fa": ["مقام دوم بیست‌وششمین جشنواره‌ی جوان خوارزمی", "برای ربات‌های سورتر پستی — ۱۴۰۳."],
  "en": ["2nd place, 26th Khwarizmi Youth Festival", "For the postal sorting robots — 2024."],
 },
 {
  "icon": "trophy",
  "top": True,
  "who": ["h"],
  "fa": [
   "مقام دوم بیست‌وچهارمین جشنواره‌ی جوان خوارزمی",
   "برای دستگاه تست پروتز زانو، همراه با گواهی یونسکو و تقدیر رئیس‌جمهور — ۱۴۰۱.",
  ],
  "en": [
   "2nd place, 24th Khwarizmi Youth Festival",
   "For the knee prosthesis test rig, with a UNESCO certificate and a presidential commendation — 2022.",
  ],
 },
 {
  "icon": "trophy",
  "top": False,
  "who": ["h", "a"],
  "fa": ["طرح برتر چهارمین جشنواره‌ی طراحی صنعتی ایران", "برای ربات‌های هوشمند پستی — ۱۴۰۳."],
  "en": ["Best design, 4th Iran Industrial Design Festival", "For the postal sorting robots — 2024."],
 },
 {
  "icon": "star",
  "top": False,
  "who": ["h", "a"],
  "fa": ["استارتاپ برتر پارک علم و فناوری شریف", "برای تیم ربات‌های هوشمند پستی — ۱۴۰۳."],
  "en": ["Top startup, Sharif Science & Technology Park", "For the postal sorting robots team — 2024."],
 },
 {
  "icon": "star",
  "top": False,
  "who": ["m"],
  "fa": ["پژوهشگر و فناور برتر دانشکده‌ی مکانیک شریف", "مقطع کارشناسی ارشد، هفته‌ی پژوهش — ۱۴۰۴."],
  "en": [
   "Top researcher & technologist, Sharif",
   "MSc level, Faculty of Mechanical Engineering, Research Week — 2025.",
  ],
 },
]

# مقاله‌ی اصلی
PUB_MAIN = {
 "title": "Frictional behavior between bone and additively manufactured Ti6Al4V implants is affected by bone density and surface texture under varying loads",
 "journal": "Scientific Reports",
 "publisher": "Nature Portfolio",
 "year": "2025",
 "doi": "https://doi.org/10.1038/s41598-025-25586-0",
 "who": ["h"],
 "authors": "Ali Abedi, Farzam Farahmand, Mohammadjavad Salmanimehrjardi &amp; <b>Hasan Nasiri Khonsari</b>",
 "badge": "Scientific Reports — Nature · <b>Q1</b>",
 "fa": {
  "summary": "بررسی رفتار اصطکاکی میان استخوان و ایمپلنت‌های تیتانیومی (<bdi>Ti6Al4V</bdi>) ساخته‌شده با روش ذوب لیزری انتخابی (<bdi>SLM</bdi>). در این پژوهش، ضریب اصطکاک برای ترکیب‌های مختلف چگالی استخوان، بافت سطح ایمپلنت و میزان بار اندازه‌گیری شد؛ نتایجی که به طراحی ایمپلنت‌های ارتوپدی سفارشی و متناسب با ویژگی‌های استخوانی هر بیمار کمک می‌کند.",
  "role": "نقش ما در این پژوهش: توسعه و ساخت دستگاه آزمون اصطکاک.",
 },
 "en": {
  "summary": "A study of friction between bone and titanium (Ti6Al4V) implants made by selective laser melting (SLM). The friction coefficient was measured for different combinations of bone density, implant surface texture and load — results that support the design of custom orthopaedic implants matched to each patient's bone.",
  "role": "Our role: development and fabrication of the friction test apparatus.",
 },
}

# مقاله‌های دیگر
PUBS = [
 {
  "who": ["a"],
  "title": "Large deformation of shape-memory polymer-based lattice metamaterials",
  "venue": "International Journal of Mechanical Sciences (Elsevier) · <a href=\"https://doi.org/10.1016/j.ijmecsci.2022.107593\" target=\"_blank\" rel=\"noopener\">DOI ↗</a>",
 },
 {
  "who": ["m"],
  "title": "Prediction of Lower Limb Gait Trajectories in Patients with Cerebral Palsy Using Deep Learning Models",
  "venue": "ICRoM 2025 — Best Paper",
 },
 {
  "who": ["m"],
  "title": "Application of Deep Learning Models in Classification of Sagittal Gait Patterns Based on Rodda's Classification System in Patients with Cerebral Palsy",
  "venue": "ICBME 2024",
 },
 {
  "who": ["a"],
  "title": "Simulation and Fabrication of Auxetic Polymer Tube and Shape Memory Behavior",
  "venue": "9th International Conference on Manufacturing Engineering, Tehran · <a href=\"https://civilica.com/doc/2014920\" target=\"_blank\" rel=\"noopener\">Link ↗</a>",
 },
 {
  "who": ["m"],
  "title": "Design and Control of a Cable-Driven Parallel Robot for Postural Alignment Improvement in Cerebral Palsy",
  "venue": "Manuscript in preparation",
 },
]

# مهارت‌ها: [عنوان دسته، [برچسب‌ها]]
SKILLS = [
 {
  "fa": [
   "طراحی و تحلیل",
   [
    "SolidWorks",
    "CATIA",
    "Inventor",
    "ANSYS",
    "Abaqus",
    "طراحی مکانیزم",
    "تحلیل اجزای محدود (<bdi>FEA</bdi>)",
    "تحلیل ارتعاشی",
   ],
  ],
  "en": [
   "Design & analysis",
   ["SolidWorks", "CATIA", "Inventor", "ANSYS", "Abaqus", "Mechanism design", "FEA", "Vibration analysis"],
  ],
 },
 {
  "fa": [
   "ساخت و تولید",
   [
    "ماشین‌کاری <bdi>CNC</bdi>",
    "SolidCAM",
    "Mastercam",
    "PowerMill",
    "GD&amp;T",
    "سازه‌های جوشی",
    "فورج سرد",
    "کامپوزیت",
   ],
  ],
  "en": [
   "Manufacturing",
   [
    "CNC machining",
    "SolidCAM",
    "Mastercam",
    "PowerMill",
    "GD&amp;T",
    "Welded structures",
    "Cold forging",
    "Composites",
   ],
  ],
 },
 {
  "fa": [
   "اتوماسیون و کنترل",
   [
    "<bdi>PLC</bdi> دلتا",
    "Siemens TIA Portal",
    "HMI",
    "LabVIEW",
    "MATLAB / Simulink",
    "ADAMS",
    "کنترل <bdi>PID</bdi> و مود لغزشی",
    "کنترل حرکت",
   ],
  ],
  "en": [
   "Automation & control",
   [
    "Delta PLC",
    "Siemens TIA Portal",
    "HMI",
    "LabVIEW",
    "MATLAB / Simulink",
    "ADAMS",
    "PID & sliding-mode control",
    "Motion control",
   ],
  ],
 },
 {
  "fa": [
   "الکترونیک و نمونه‌سازی",
   ["ARM / STM32", "AVR / Arduino", "Altium", "Proteus", "پرینت سه‌بعدی <bdi>FDM</bdi> و <bdi>DLP</bdi>"],
  ],
  "en": ["Electronics & prototyping", ["ARM / STM32", "AVR / Arduino", "Altium", "Proteus", "FDM & DLP 3D printing"]],
 },
 {
  "fa": [
   "رباتیک و هوش مصنوعی",
   [
    "ربات صنعتی و خدماتی",
    "ربات کابلی",
    "اسکلت بیرونی",
    "یادگیری عمیق (<bdi>CNN</bdi>، <bdi>LSTM</bdi>، <bdi>Transformer</bdi>)",
   ],
  ],
  "en": [
   "Robotics & AI",
   [
    "Industrial & service robots",
    "Cable-driven robots",
    "Exoskeletons",
    "Deep learning (CNN, LSTM, Transformer)",
   ],
  ],
 },
]

# سوابق کاری: [زمان، عنوان، محل، توضیح]؛ team=True یعنی کار خود گروه
EXPERIENCE = [
 {
  "who": ["h", "a", "m"],
  "team": True,
  "fa": [
   "۱۴۰۴ تا اکنون",
   "پیمانکاری طراحی و ساخت — گروه فنی مهندسی انتها",
   "تهران و اصفهان",
   "ساخت قطعات، مجموعه‌ها و سازه‌های صنعتی: برآورد و قیمت‌گذاری، تأمین متریال، مدیریت فرآیندهای ماشین‌کاری، برش لیزر، خم‌کاری، نورد و جوشکاری، کنترل کیفیت و مونتاژ.",
  ],
  "en": [
   "2025 – present",
   "Design & fabrication contracting — Enteha Group",
   "Tehran & Isfahan",
   "Industrial parts, assemblies and structures: estimating and pricing, material procurement, managing machining, laser cutting, bending, rolling and welding, quality control and assembly.",
  ],
 },
 {
  "who": ["h"],
  "team": False,
  "fa": [
   "۱۴۰۴ تا اکنون",
   "مهندس ارشد مکانیک",
   "تهران",
   "طراحی قطعه و مجموعه، بازرسی ابعادی و جوش، و مدیریت کارگاه‌های ماشین‌کاری و ساخت بیرونی؛ تا امروز بیش از ۸٬۰۰۰ قطعه‌ی صنعتی تحویل شده است.",
  ],
  "en": [
   "2025 – present",
   "Senior Mechanical Engineer",
   "Tehran",
   "Part and assembly design, dimensional and weld inspection, and management of machining and external fabrication shops; more than 8,000 industrial parts delivered so far.",
  ],
 },
 {
  "who": ["a"],
  "team": False,
  "fa": [
   "آذر ۱۴۰۴ تا اکنون",
   "مهندس مکانیک تولید (خوداشتغال)",
   "اصفهان",
   "پیمانکاری، ساخت، کنترل کیفی و مونتاژ مجموعه‌قطعات صنعتی و مدیریت تیم مهندسی.",
  ],
  "en": [
   "2025 – present",
   "Production Mechanical Engineer (self-employed)",
   "Isfahan",
   "Contract fabrication, quality control and assembly of industrial part sets; leading an engineering team.",
  ],
 },
 {
  "who": ["m"],
  "team": False,
  "fa": [
   "۱۴۰۴",
   "مهندس تحقیق و توسعه‌ی رباتیک",
   "تهران",
   "ربات اسکلت بیرونی پایین‌تنه: طراحی مفهومی، انتخاب عملگر، طراحی سازه و مکانیزم و طراحی مکانیکی جزئی.",
  ],
  "en": [
   "2025",
   "R&D Robotics Engineer",
   "Tehran",
   "Lower-limb exoskeleton: concept design, actuator selection, structure and mechanism, detailed mechanical design.",
  ],
 },
 {
  "who": ["m"],
  "team": False,
  "fa": [
   "۱۴۰۳ تا ۱۴۰۴",
   "داور ثبت اختراع در حوزه‌ی مکانیک — دانشگاه صنعتی شریف",
   "تهران",
   "بررسی و داوری تقاضانامه‌های ثبت اختراع در حوزه‌ی مهندسی مکانیک.",
  ],
  "en": [
   "2024 – 2025",
   "Patent Examiner, Mechanical Engineering — Sharif University of Technology",
   "Tehran",
   "Reviewing and evaluating patent applications in mechanical engineering.",
  ],
 },
 {
  "who": ["h"],
  "team": False,
  "fa": [
   "۱۴۰۲",
   "مدرس — دانشگاه تهران، پردیس بین‌المللی کیش",
   "کیش",
   "تدریس دروس «روش‌های تولید» و «فیزیک ۲» در نیم‌سال دوم ۱۴۰۲-۱۴۰۳.",
  ],
  "en": [
   "2024",
   "Lecturer — University of Tehran, Kish International Campus",
   "Kish",
   "Taught Manufacturing Processes and Physics 2 in the second semester of 2023–24.",
  ],
 },
 {
  "who": ["m"],
  "team": False,
  "fa": [
   "۱۴۰۲ تا ۱۴۰۴",
   "مدرس و دستیار آموزشی — دانشگاه صنعتی شریف",
   "تهران",
   "تدریس آزمایشگاه‌های دینامیک ماشین و اندازه‌گیری و کنترل؛ دستیار آموزشی دروس کنترل غیرخطی، رباتیک پزشکی، بیومکانیک اسکلتی‌عضلانی و دینامیک پیشرفته.",
  ],
  "en": [
   "2023 – 2025",
   "Lecturer & Teaching Assistant — Sharif University of Technology",
   "Tehran",
   "Taught the Dynamics of Machinery and Measurement & Control laboratories; TA for Nonlinear Control, Medical Robotics, Musculoskeletal Biomechanics and Advanced Dynamics.",
  ],
 },
 {
  "who": ["m"],
  "team": False,
  "fa": [
   "۱۴۰۱ تا اکنون",
   "دستیار پژوهشی — آزمایشگاه رباتیک پزشکی، دانشگاه صنعتی شریف",
   "تهران",
   "پژوهش در رباتیک پزشکی و توانبخشی، زیر نظر دکتر فرزام فرهمند و دکتر سعید بهزادی‌پور.",
  ],
  "en": [
   "2022 – present",
   "Research Assistant — Medical Robotics Lab, Sharif University of Technology",
   "Tehran",
   "Research in medical and rehabilitation robotics, supervised by Dr Farzam Farahmand and Dr Saeed Behzadipour.",
  ],
 },
 {
  "who": ["a"],
  "team": False,
  "fa": [
   "۱۴۰۱ تا ۱۴۰۳",
   "سرپرست تولید — ربات‌های سورتر پستی",
   "تهران",
   "ساخت و مدیریت تولید ربات‌های هوشمند تفکیک مرسولات پست ایران؛ طراحی خط تولید مطابق استانداردهای تولید صنعتی؛ بهینه‌سازی هزینه و فرآیند.",
  ],
  "en": [
   "2022 – 2024",
   "Production Supervisor — Postal Sorting Robots",
   "Tehran",
   "Fabrication and production management of smart parcel-sorting robots for Iran Post; production line design to industrial standards; cost and process optimisation.",
  ],
 },
 {
  "who": ["m"],
  "team": False,
  "fa": [
   "۱۴۰۱",
   "کارآموز مهندسی مکانیک — چاپ سه‌بعدی ساختمان",
   "تهران",
   "طراحی مفهومی، امکان‌سنجی و تحلیل دینامیکی مکانیزم ربات چاپ ساختمان با نرم‌افزار <bdi>ADAMS</bdi>.",
  ],
  "en": [
   "2022",
   "Mechanical Engineering Intern — construction 3D printing",
   "Tehran",
   "Concept design, feasibility study and dynamic analysis of a construction-printing robot in ADAMS.",
  ],
 },
 {
  "who": ["h"],
  "team": False,
  "fa": [
   "۱۴۰۰ تا ۱۴۰۳",
   "مدیر طراحی محصول (پاره‌وقت)",
   "تهران",
   "طراحی مکانیک و الکترونیک ربات متحرک با چرخ‌های همه‌جهته.",
  ],
  "en": [
   "2021 – 2024",
   "Product Design Manager (part-time)",
   "Tehran",
   "Mechanical and electronic design of an omnidirectional mobile robot.",
  ],
 },
 {
  "who": ["h"],
  "team": False,
  "fa": [
   "۱۳۹۹ تا ۱۴۰۴",
   "مدیر واحد مهندسی مکانیک — رباتیک صنعتی",
   "تهران",
   "توسعه‌ی مکانیکی ربات‌های صنعتی؛ مدیریت ساخت ۵۰ ربات سورتر برای مرکز توزیع مرسولات تهران و ۳۰ ربات برای کرمانشاه، هماهنگی کارگاه‌ها و سرپرستی تیم مونتاژ و یکپارچه‌سازی.",
  ],
  "en": [
   "2020 – 2025",
   "Head of Mechanical Engineering — Industrial Robotics",
   "Tehran",
   "Mechanical development of industrial robots; managed the build of 50 sorting robots for Iran Post's Tehran distribution centre and 30 for Kermanshah, coordinating workshops and supervising the assembly and integration team.",
  ],
 },
 {
  "who": ["h", "a"],
  "team": False,
  "fa": [
   "۱۳۹۸",
   "کارآموز پروژه — اتوماسیون تئاتر شهر",
   "تهران",
   "اتوماسیون و تجهیز ماشین‌آلات سالن اصلی تئاتر شهر تهران.",
  ],
  "en": [
   "2019",
   "Project Intern — Tehran City Theatre automation",
   "Tehran",
   "Automation and stage machinery for the main hall of Tehran City Theatre.",
  ],
 },
 {
  "who": ["a"],
  "team": False,
  "fa": [
   "۱۳۹۶ تا ۱۳۹۷",
   "کارشناس فنی و تحقیق و توسعه — شکل‌دهی فلز",
   "اصفهان",
   "طراحی و مونتاژ قطعات ماشین‌آلات، رزوه‌زنی و فورج سرد، اندازه‌گیری و کنترل کیفیت، <bdi>GD&amp;T</bdi>.",
  ],
  "en": [
   "2017 – 2018",
   "Technical & R&D Specialist — metal forming",
   "Isfahan",
   "Design and assembly of machine parts, thread rolling and cold forging, measurement and quality control, GD&amp;T.",
  ],
 },
]

# آیکون کارت‌های سه خدمت (SVG)
SVC_ICONS = [
 "<svg viewBox=\"0 0 24 24\" width=\"26\" height=\"26\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><circle cx=\"12\" cy=\"12\" r=\"3\"/><path d=\"M12 2v3M12 19v3M4.2 4.2l2.1 2.1M17.7 17.7l2.1 2.1M2 12h3M19 12h3M4.2 19.8l2.1-2.1M17.7 6.3l2.1-2.1\"/></svg>",
 "<svg viewBox=\"0 0 24 24\" width=\"26\" height=\"26\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><rect x=\"5\" y=\"7\" width=\"14\" height=\"11\" rx=\"3\"/><path d=\"M12 7V4M9 12h.01M15 12h.01M9 15h6\"/><circle cx=\"12\" cy=\"3.5\" r=\"1\"/></svg>",
 "<svg viewBox=\"0 0 24 24\" width=\"26\" height=\"26\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"1.8\" stroke-linecap=\"round\" stroke-linejoin=\"round\" aria-hidden=\"true\"><path d=\"M4 20h16M6 20V9h12v11M9 9V5h6v4\"/><path d=\"M6 14h12\"/></svg>",
]
