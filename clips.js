/* کلیپ‌های گروه فنی مهندسی انتها، برای بخش «کلیپ‌ها» در index.html.
   تا وقتی این فهرست خالی است، بخش «کلیپ‌ها» و لینک آن در منو نمایش داده نمی‌شوند.
   کارت‌ها به همان ترتیبی که اینجا نوشته شده‌اند نمایش داده می‌شوند.

   فیلدها:
   slug      شناسه‌ی ثابت انگلیسی، بدون فاصله (مثل "outsourcing")
   title_fa / title_en         عنوان
   year_fa / year_en           سال، مثل "۱۴۰۵" و "2026" (اختیاری)
   desc_fa / desc_en           توضیح کوتاه (اختیاری)

   video:   "v-<slug>.mp4"   فایل ویدیو کنار index.html؛ MP4 با کدک H.264، ترجیحاً زیر ۱۰ مگابایت
   poster:  "v-<slug>.jpg"   تصویر ثابت ۹۶۰×۵۴۰ (برای عمودی ۵۴۰×۹۶۰)، JPG حدود ۶۰ تا ۱۲۰ کیلوبایت
   d:       "2026-10-30"     تاریخ انتشار میلادی (اختیاری؛ برای گوگل)
   vertical: true            برای ویدیوی عمودی ۹:۱۶ (استوری و ریلز)
*/
window.CLIPS = [
 {
  "slug": "outsourcing",
  "title_fa": "برون‌سپاری بی‌دردسر",
  "title_en": "Hassle-free outsourcing",
  "year_fa": "۱۴۰۵",
  "year_en": "2026",
  "desc_fa": "قطعه‌ها را تک‌تک تحویل گرفته‌اید و همه درست به نظر می‌رسند، ولی روز مونتاژ با هم جفت نمی‌شوند؛ چون طراحی، ساخت و مونتاژ دست چند نفر مختلف بوده و کسی کل دستگاه را نمی‌دیده. در انتها کسی که طراحی می‌کند تا آخر کار بالای سر ساخت و مونتاژ می‌ماند؛ از دستگاه خاص‌منظوره و اتوماسیون خط تولید تا قطعه‌ی تیراژی.",
  "desc_en": "Every part arrives and each one looks right, yet on assembly day they don't fit together — because design, fabrication and assembly were in different hands and nobody saw the whole machine. At Enteha, the person who designs it stays with fabrication and assembly to the end: from special-purpose machines and production line automation to parts in series.",
  "video": "v-outsourcing.mp4",
  "poster": "v-outsourcing.jpg",
  "d": "2026-10-31",
  "vertical": true
 }
];
