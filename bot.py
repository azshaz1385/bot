while True:
	ennam = input("نام خانوادگی خود را وارد کنید: \n")
	break
import random

maxn = 542
n = random.randint(542, maxn)
print('Hello ' + ennam + ' sweetie-pie')
print('به آذرخش بات خوش امدید!!' )
guess = None
while guess != n:
    print('رمز را از سازنده ربات بگیرید')
    guess = int(input('رمز را به شماره وارد کنید :	\n'))
    if guess > n:
        print('درست نیست')
    if guess < n:
        print('این رمز خیلی کوتاه است اصلا ربطی ندارد.')
from requests import get
from re import findall
from rubika.client import Bot
from requests import post
import time
from PIL import Image
from json import loads
from gtts import gTTS
from mutagen.mp3 import MP3
import io
from random import choice

bot = Bot("AppName", auth="astouszvfqviwkbsdkmkugypfxwcmpeq")
target ="g0aeBD0df04b27b0cb91bf523bbf3d73"
bot.sendMessage(target, 'اپراتور آذرخش فعال شده🤖✅')
def hasAds(msg):
	links = ["http://","https://",".ir",".com",".org",".net",".me"]
	for i in links:
		if i in msg:
			return True
	

# static variable
answered, sleeped, retries = [], False, {}

alerts, blacklist = [] , []

def alert(guid,user,link=False):
	alerts.append(guid)
	coun = int(alerts.count(guid))

	haslink = ""
	if link : haslink = "گزاشتن لینک در گروه ممنوع میباشد .\n\n"

	if coun == 1:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (1/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")
	elif coun == 2:
		bot.sendMessage(target, "💢 اخطار [ @"+user+" ] \n"+haslink+" شما (2/3) اخطار دریافت کرده اید .\n\nپس از دریافت 3 اخطار از گروه حذف خواهید شد !\nجهت اطلاع از قوانین کلمه (قوانین) را ارسال کنید .")

	elif coun == 3:
		blacklist.append(guid)
		bot.sendMessage(target, "🚫 کاربر [ @"+user+" ] \n (3/3) اخطار دریافت کرد ، بنابراین اکنون اخراج میشود .")
		bot.banGroupMember(target, guid)

retries = {}
sleeped = False
 
plus= True

while True:
	try:
		admins = [i["member_guid"] for i in bot.getGroupAdmins(target)["data"]["in_chat_members"]]
		min_id = bot.getGroupInfo(target)["data"]["chat"]["last_message_id"]
		while True:
			try:
				messages = bot.getMessages(target,min_id)
				break
			except:
				continue
		
		open("id.db","w").write(str(messages[-1].get("message_id")))

		for msg in messages:
			if msg["type"]=="Text" and not msg.get("message_id") in answered:
				if not sleeped:
					if msg.get("text") == "/bot" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "The bot is now active", message_id=msg.get("message_id"))
						
					elif msg.get("text") == "خوبی":
							try:
								ans = ["چرا خوبم ممنون😋💛", "شما خوبی؟😄❤️","بله شما خوبی؟🤤🌹","سپاس شما خوبی؟🌺","مگه میشه شمارو بیینم خوب نباشم؟😃🐾"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err ranodm")
						
					elif msg.get("text") == "قلب":
							try:
								ans = ["❤️","🧡","💛","💚","💙","💜","🤎","🖤","🤍","♥️","💘","💝","💖","💗","💓","💞","💕","💟","❣️","💔"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err random")
								
					
									
					elif msg.get("text").startswith("فال"):
						
						try:
							args = msg['text'].split()[1]
							if '.ir' in args:
								response = get(f"https://api.codebazan.ir/webshot/?text=1000&domain={args}").content
							else:
								response = post("http://api.codebazan.ir/fal/index.php/pic").content
							with open("shot.jpg","wb") as shot: shot.write(response)
							bot.sendPhoto(target, "./shot.jpg", [720,40], caption="فال حافظ اماده شد آذرخش", message_id=msg["message_id"])
						except:
								bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("عکس دانستنی"):
						
						try:
							args = msg['text'].split()[1]
							if '.ir' in args:
								response = get(f"https://api.codebazan.ir/webshot/?text=1000&domain={args}").content
							else:
								response = post("http://api.codebazan.ir/danestani/pic").content
							with open("shot.jpg","wb") as shot: shot.write(response)
							bot.sendPhoto(target, "./shot.jpg", [720,40], caption="بدانید آذرخش", message_id=msg["message_id"])
						except:
								bot.sendMessage(target, "خطا در اجرای دستور", message_id=msg.get("message_id"))
								
					
								
					elif msg.get("text").startswith("شماره") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["phone"]["chat"]["object_guid"], "{phone}"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "شمارت ارسال شد.", message_id=msg.get("target=phone_id"))
						
					
								
					elif msg.get("text") == "ایموجی":
							try:
								ans = ["😀","😃","😁","😆","😅","😂","🤣","😭","😗","😙","😚","😘","🥰","😍","🥳","🤗","🙃","🙂","☺️","😊","😏","😌","😉","🤭","😶","😐","😑","😔","😋","😛","😝","😜","🤪","🤔","🤨","🧐","🙄","😒","😤","😠","😡","🤬","☹️","🙁","😟","🥺","😳","😬","🤐","🤫","😰","😨","😧","😦","😮","😯","😲","😱","🤯","😢","😥","😓","😞","😖","😣","😩","🤤","🥱","😴","😪","🤢","🤮","🤧","🤒","🤕","🥴","😵","🥵","🥶","😷","😇","🤠","🤑","😎","🤓","🤥"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err random")
								
					elif msg.get("text") == "گل":
							try:
								ans = ["💐","🌹","🌷","🌺","🌸","🏵️","🌻","🌼","💮"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err random")
						
					elif msg.get("text").startswith("بیو") or msg.get("text").startswith("bio") or msg.get("text").startswith("!bio"):
							try:
								response = get("https://api.codebazan.ir/bio").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err bio")
							
					elif msg.get("text").startswith("!شعر"):
							try:
								response = get("https://api.codebazan.ir/ghazalsaadi/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err sher")
								
					elif msg.get("text").startswith("!gold"):
							try:
								responser = get(f"http://api.codebazan.ir/arz/?type={msg.get('text').split()[1]}").json()
								bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
								bot.sendMessage(target, "نتیجه رو برات ارسال کردم😘", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "دستورت رو اشتباه وارد کردی", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("تعبیر خواب"):
							try:
								responser = get(f"https://api.codebazan.ir/tabir/?text={msg.get('text').split()[1]}").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err tabir khab")
							
					elif msg.get("text").startswith("دانش") or msg.get("text").startswith("danestani") or msg.get("text").startswith("!danestani"):
						try:
							response = get("https://api.codebazan.ir/danestani/").text
							bot.sendMessage(target, response,message_id=msg.get("message_id"))
						except:
							print("err danestani")
							
					elif msg.get("text").startswith("نسخه") or msg.get("text").startswith("/noskh") or msg.get("text").startswith("!noskh") or msg.get("text").startswith("\noskh"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "1⃣• نسخه 0.1.1 \n https://rubika.ir/MineShine_APK/BJJEAHGJDCJFGEG \n 2⃣• نسخه 0.2.0 \n https://rubika.ir/MineShine_APK/BJJEBFGJGDDIGEG \n 3⃣• نسخه 0.6.0 \n https://rubika.ir/MineShine_APK/BJJEDFHAGABGGEG \n 4⃣• نسخه 0.9.1 \n https://rubika.ir/MineShine_APK/BJJEDFHAGABGGEG \n 5⃣•نسخه 0.13.0 \n https://rubika.ir/MineShine_APK/BJJEEEHBADBIGEG \n 6⃣• نسخه 0.13.2  \n https://rubika.ir/MineShine_APK/BJJEEHHBBHDEGEG \n 7⃣• نسخه 1.2.7  \nhttps://rubika.ir/MineShine_APK/BJJIGJJGACBCGEG \n 8⃣• نسخه 1.8.0 \n https://rubika.ir/MineShine_APK/CAAJJJFBDBHHGEG \n 9⃣• نسخه 1.10.0 \n https://rubika.ir/MineShine_APK/CABEIHHIIHJGGEG \n 🔟• نسخه 1.11.4 \n https://rubika.ir/MineShine_APK/CABIGJJIECEIGEG \n 1⃣1⃣• نسخه 1.12.1 \n https://rubika.ir/MineShine_APK/CABIIIJJCHJIGEG \n 2⃣1⃣• نسخه 1.13.1 \n https://rubika.ir/MineShine_APK/CABJCFAAIBFBGEG \n 4⃣1⃣• نسخه 1.14.30 \n https://rubika.ir/MineShine_APK/CACCGEBHDEJFGEG \n5⃣1⃣• نسخه 1.16.40 \b https://rubika.ir/MineShine_APK/CACFGDDADFAJGEG \n 6⃣1⃣• نسخه 1.17.30 \n https://rubika.ir/MineShine_APK/CACJFDEJJDGIGEG \n 7⃣1⃣• نسخه 1.18.12\nhttps://rubika.ir/MineShine_APK/CBBHJDGAJFEHGEG").text
								bot.sendMessage(target, "دستور را درست وارد کنید ❌", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه برایت فرستادم 🌹", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("فارم") or msg.get("text").startswith("!farm") or msg.get("text").startswith("/farm") or msg.get("text").startswith("\farm"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "• فارم های پیشنهادی برای شما🧭🧡• \n آموزش ساخت فارم اندرمن \n https://rubika.ir/sun_crafter/BHBGIBAFADHGGGH \n • آموزش ساخت فارم کریپر بی‌نهایت🤯 \n https://rubika.ir/sun_crafter/BHADHADJBFDAGGH  \n • آموزش ساخت فارم ماهی🐠 \n https://rubika.ir/sun_crafter/BGGFIFECDHGCGGH \n • آموزش ساخت فارم امیرضا🐄، نیشکر و بامبو،\n بهترین فارم اکسپی در ماینکرفت و..... \n https://rubika.ir/CubicMine0/CAEIEJCEDHAHHEB \n • آموزش ساخت فارم طلا در ماینکرفت 🌟🔥 \n https://rubika.ir/CubicMine0/BIAIFCIFCGHIHEB \n • آموزش ساخت فارم ندرایت😱🔨 \n https://rubika.ir/CubicMine0/BIAICHIDFCGHHEB \n • آموزش ساخت فارم زامبی 🤤🧟‍♀️ \n https://rubika.ir/CubicMine0/BHIIIAIFBBCAHEB \n • آموزش ساخت فارم جادوگر🧙‍♀️ \n https://rubika.ir/iranmine/CEJGJHEHEJD \b آموزش ساخت فارم کدو🍮 \n /https://rubika.ir/CubicMine0/BHIFBHGIFDEGHEB\n لطفاً جوین ندید").text
								bot.sendMessage(target, "دستور را درست وارد کنید ❌", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه را برایت فرستادم 🌹", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("مپ") or msg.get("text").startswith("/map") or msg.get("text").startswith("!map") or msg.get("text").startswith("\map") :
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "• مپ های پیشنهادی برای شما🧭🌋 \n • مپ مزرعه و خانه ✨🏡 \n https://rubika.ir/CubicMine0/BHDCGBAFIGBDHEB \n • مپ اِگ وارز😍🥚\n https://rubika.ir/CubicMine0/BHABABEIFDEFHEB \n • مپ خانه شِرِک😂🦖\n https://rubika.ir/CubicMine0/BGGFBEFEDAFCHEB \n • مپ خونه رداِستونی⭕🏡 \n https://rubika.ir/CubicMine0/BFEFGDEBHCADHEB \n • مپ ساعت رداِستونی که کار میکنه🕰️✨ \n https://rubika.ir/CubicMine0/BDGBFIIFEFHCHEB \n • مپ اسکای لاکی بلاک😍🎈(پیشنهادی)  \n https://rubika.ir/CubicMine0/BBJIJHEFHEDCHEB \n • مپ شهر بازی در ماینکرفت🎡👾 \n https://rubika.ir/sun_crafter/BHBDABIFAABEGGH \n • مپ پارکور 🗿🧲 \n https://rubika.ir/sun_crafter/BHABABCGICIHGGH \n • مپ آمانگ آس🔮✨ \n https://rubika.ir/sun_crafter/BGHDGJIFDGEAGGH \n • مپ فیلمِ اسکویید گیم♟️🎫 \n https://rubika.ir/sun_crafter/BGDGJCJIJFBIGGH \n • مپ بمب اسکواد 💣 \n https://rubika.ir/sun_crafter/BEFBGEEJBCJCGGH \n • مپ برج تونی استارک👨‍🚀💞 \n https://rubika.ir/sun_crafter/BEAGIHIIEGJAGGH \n لطفا جوین ندیدن").text
								bot.sendMessage(target, "دستور را درست وارد کنید ❌", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه برایت فرستادم 🌹", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("/seed") or msg.get("text").startswith("!seed"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "🗻• بدون پستی بلندی با معدن رد استون  \n gimmeadamnvillage \n 🌊 • دریاچه بزرگ کم عمق \n 1509963643 \n 🏝 • جزیره با دو روستا \n -1060246543 \n 🏡 • روستای دو قلوی شنی \n trophiemoney \n 🧙🏻‍♂ • روستایی با کلبه ی جادوگر \n 77301621 \n 🍄 • روستای قارچی \n 1754 \n 🏞 • روستا و معبد روی آب  \n -114648 \n 💎 • روستا با معدن آهن و طلا و الماس فراوان \n -645243394 \n 🏔 • تکه زمین غول پیکر روی هوا \n retaw \n ❄️ • قندیل های یخی \n its a go \n 🏡 • بلند ترین روستا \n -1 \n 🗾 • صاف ترین زمین \n time \n 💧 • بزرگترین آبشار \n rainbowdash \n 💎 • معدنی پر از الماس \n booz \n 🏡 • روستای بسیار بزرگ \n Gigantic \n 🏘 • دو نوع روستا کنار هم \n poy \n 🏰 • دو معبد پر از تله کنار هم \n -2109943162 \n 🗺 • روستای استخر دار  \n -1320359977 \n 🍄 • روستای قارچی (توی بایوم قارچ) \n 175 \n 🎍• روستا در جزیره \n marabell \n 🏜 •  روستای قرمز \n 2773").text
								bot.sendMessage(target, "دستور را درست وارد کنید ❌", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه را برایت فرستادم 🌹", message_id=msg["message_id"])
					
								print("err answer hay")
								
					elif msg.get("text").startswith("/addon") or msg.get("text").startswith("!addon") or msg.get("text").startswith("ادان"):
							try:
								bot.sendMessage(msg.get("author_object_guid"),  "• ادان های پیشنهادی برای شما 🧭💙 \n - ادان حذف مِه های اطراف چانک 👇🏼💥 \n https://rubika.ir/CubicMine0/BJFBCEEBBBCCHEB \n - ادان حذف دایره بزرگ هنگام لمس صفحه✨ \n https://rubika.ir/CubicMine0/BJEHCBCBACDJHEB \n - ادان حالت محبوب هاردکور 💥📯 \n https://rubika.ir/CubicMine0/BJGBBFJGDBGHHEB \n - ادان شمشیر های جدید با قدرت های ماورایی⚔️🕸️ \n https://rubika.ir/CubicMine0/CBAGEFIHHFCEHEB \n - ادان جالبِ غول مِسی📯🗿 \n https://rubika.ir/CubicMine0/BHAAIJEHIDEDHEB \n - ادان موتور و اسبِ روح سوار 👹🔥 \n https://rubika.ir/CubicMine0/BHAEBAGEHDAHHEB \n - ادان جالب و کاربردی ایموجی برای ماینکرافت 😃🎈 \n https://rubika.ir/CubicMine0/BHBDAEBABAEIHEB \n - ادان جعبه ابزار 🧭🕸️ \n https://rubika.ir/CubicMine0/BHFIHFDIIIECHEB \n - ادان نور دهی مشعل و... با در دست گرفتن اون ها🥳💡 \n https://rubika.ir/CubicMine0/BIHHDBFEJIBBHEB \n لطفا جوین ندیدن").text
								bot.sendMessage(target, "دستور را درست وارد کنید ❌", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه را برایت فرستادم 🌹", message_id=msg["message_id"])
								
					elif msg.get("text") == "!game" or msg.get("text") == "/game" or msg.get("text") == "\game" and msg.get("author_object_guid") :
												bot.sendMessage(target, "برای دریافت بازی فقط بنویسید \n اکشن \n ورزشی \n پرتحرک \n پازل \n را وارد کنید", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "!minecraft" or msg.get("text") == "/minecraft"  and msg.get("author_object_guid") :
												bot.sendMessage(target, "به بخش ماینکرافت خوش آمدید  \n  برای دریافت سید های مختلف ماینکرافت !seed \n دانلود نسخه های مختلف ماینکرافت \noskh! n دانلود فیلم های آموزشی ساخت فارم های ماینکرافت \farm ! n و برای دانلود ادان های ماینکرافت !addon را استفاده کنید", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "ورزشی" and msg.get("author_object_guid") :
												bot.sendMessage(target, "🏀- بخش ورزشی  \n • فوتبال استار  \n ➖ https://b2n.ir/MC_rBOT2 \n • بسکتبال \n ➖ https://b2n.ir/MC_rBOT24 \n • پادشاه شوت کننده \n ➖ https://b2n.ir/MC_rBOT255 \n 🔴 راهنمایی: یکی از لینک ها را انتخاب کرده و کلیک کنید ؛ گزینه PLAY رو بزنید.", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "اکشن" and msg.get("author_object_guid") :
												bot.sendMessage(target, "🥊- بخش اکشن \n • نینجای جاذبه  \n ➖ https://b2n.ir/MC_rBOT3 \n • رانندگی کن یا بمیر \n ➖ https://b2n.ir/MC_rBOT9 \n • کونگ فو \n ➖ https://b2n.ir/MC_rBOT11 \n 🔴 راهنمایی: یکی از لینک ها را انتخاب کرده و کلیک کنید ؛ گزینه PLAY رو بزنید.", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "پر تحرک" and msg.get("author_object_guid") :
												bot.sendMessage(target, "💥- بخش پرتحرک \n • گربه دیوانه  \n ➖ https://b2n.ir/MC_rBOT4 \n • ماهی بادکنکی \n ➖ https://b2n.ir/MC_rBOT13 \n • دینگ دانگ \n ➖ https://b2n.ir/MC_rBOT12 \n 🔴 راهنمایی: یکی از لینک ها را انتخاب کرده و کلیک کنید ؛ گزینه PLAY رو بزنید.", message_id=msg.get("message_id"))
												
					elif msg.get("text") == "پازل" and msg.get("author_object_guid") :
												bot.sendMessage(target, "🏮-بخش پازل \n • پازل بلاکی \n ➖ https://b2n.ir/MC_rBOT5 \n • ساحل پاپ \n ➖ https://b2n.ir/MC_rBOT14 \n • جمع اعداد \n ➖ https://b2n.ir/MC_rBOT15 \n 🔴 راهنمایی: یکی از لینک ها را انتخاب کرده و کلیک کنید ؛ گزینه PLAY رو بزنید.", message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("الکی") or msg.get("text").startswith("alaki-masalan") or msg.get("text").startswith("!alaki-masalan"):
							try:
								response = get("https://api.codebazan.ir/jok/alaki-masalan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err alaki-masalan")
							
					
							
					elif msg.get("text").startswith("دانستنی") or msg.get("text").startswith("dastan") or msg.get("text").startswith("!dastan"):
							try:
								response = get("https://api.codebazan.ir/dastan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err dastan")
							
					
					elif msg.get("text") == "ویسکال" and msg.get("author_object_guid") in admins :
							try:
								bot.startVoiceChat(target,)
								bot.sendMessage(target, "ویسکال با موفقیت ایجاد شد✔️", message_id=msg.get("message_id"))
							except:
								print("err Voice Chat")
								
					elif msg.get("text").startswith("ذکر") or msg.get("text").startswith("zekr") or msg.get("text").startswith("!zekr"):
							try:
								response = get("http://api.codebazan.ir/zekr/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err zekr")
							
					elif msg.get("text").startswith("خاطره") or msg.get("text").startswith("khatere") or msg.get("text").startswith("!khatere"):
							try:
								response = get("http://api.codebazan.ir/jok/khatere").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err khatere")
							
					elif msg.get("text").startswith("پ ن پ") or msg.get("text").startswith("pa-na-pa") or msg.get("text").startswith("!pa-na-pa"):
							try:
								response = get("http://api.codebazan.ir/jok/pa-na-pa/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err pa-na-pa")
							
					
					
							
					
						
					elif msg.get("text").startswith("صکص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیری"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بیناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بی ناموص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بیناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("بی ناموس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کسکش"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کبص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیرم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادرتو"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادرت"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کون"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کوس"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کونی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("جنده"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("جند"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادر جنده"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("مادر جند"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("ممه"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("kir"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("https://"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام تبلیغاتی پاک شد", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایید"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگایدم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایدی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگاید"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نگایدیم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("گایدیم"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("کیر"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					
						
					elif msg.get("text").startswith("کص"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("لاشی"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("دیوث"):
						bot.deleteMessages(target, [str(msg.get("message_id"))])
						bot.sendMessage(target, "یک پیام مستهجن از گروه حذف شد.", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("غیر فعال ارام") and msg.get("author_object_guid") in admins:
							try:
								number = 0
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام غیرفعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))

						
					elif msg.get("text").startswith("ارام10") and msg.get("author_object_guid") in admins:
							try:
								number = 10
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام1") and msg.get("author_object_guid") in admins:
							try:
								number = 60
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام5") and msg.get("author_object_guid") in admins:
							try:
								number = 300
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))															
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام15") and msg.get("author_object_guid") in admins:
							try:
								number = 900
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام1s") and msg.get("author_object_guid") in admins:
							try:
								number = 1600
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("ارام30") and msg.get("author_object_guid") in admins:
							try:
								number = 30
								bot.setGroupTimer(target,number)

								bot.sendMessage(target, "✅ حالت آرام برای "+str(number)+"ثانیه فعال شد", message_id=msg.get("message_id"))

							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "!speak" or msg.get("text") == "speak" or msg.get("text") == "Speak" or msg.get("text") == "بگو":
							try:
								if msg.get('reply_to_message_id') != None:
									msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
									if msg_reply_info['text'] != None:
										text = msg_reply_info['text']
										speech = gTTS(text)
										changed_voice = io.BytesIO()
										speech.write_to_fp(changed_voice)
										b2 = changed_voice.getvalue()
										changed_voice.seek(0)
										audio = MP3(changed_voice)
										dur = audio.info.length
										dur = dur * 1000
										f = open('sound.ogg','wb')
										f.write(b2)
										f.close()
										bot.sendVoice(target , 'sound.ogg', dur,message_id=msg["message_id"])
										os.remove('sound.ogg')
										print('sended voice')
								else:
									bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
							except:
								print('server gtts bug')		
					
																			
				
					elif msg.get("text") == "سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.pin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر با موفقیت سنجاق شد!", message_id=msg.get("message_id"))
							except:
								print("err pin")
								
					
						 	 
						 	
					
								
					elif msg["text"].startswith("!number") or msg["text"].startswith("بشمار"):
							try:
								response = get(f"http://api.codebazan.ir/adad/?text={msg['text'].split()[1]}").json()
								bot.sendMessage(msg["author_object_guid"], "\n".join(list(response["result"].values())[:20])).text
								bot.sendMessage(target, "نتیجه بزودی برای شما ارسال خواهد شد...", message_id=msg["message_id"])
							except:
								print("err number")				
								
					elif msg.get("text").startswith("حدیث") or msg.get("text").startswith("hadis") or msg.get("text").startswith("!hadis"):
							try:
								response = get("http://api.codebazan.ir/hadis/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err hadis")
								
					elif msg.get("text").startswith("دیالوگ") or msg.get("text").startswith("dialog") or msg.get("text").startswith("!dialog"):
							try:
								response = get("http://api.codebazan.ir/dialog/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err dialog")
								
					
								
					if  msg.get("text").startswith('!info @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))
								
					elif msg.get("text").startswith("داستان") or msg.get("text").startswith("!dastan"):
							try:
								response = get("http://api.codebazan.ir/dastan/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err dastan")	
								
					elif msg.get("text") == "لینک":
							rules = open("dast.txt","r",encoding='utf-8').read()
							bot.send7Message(target, str(rules), message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("اپدیت لینک") and msg.get("author_object_guid") in admins:
							try:
								rules = open("dast.txt","w",encoding='utf-8').write(str(msg.get("text").strip("اپدیت لینک")))
								bot.sendMessage(target, "لینک باموفقیت اپدیت شد✔️", message_id=msg.get("message_id"))
								
							except:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید.", message_id=msg.get("message_id"))
								
				 
					elif msg.get("text").startswith("بازی") or msg.get("text").startswith("جرعت حقیقت") or msg.get("text").startswith("ج ح"):
							rules = open("jorat.txt","r",encoding='utf-8').read()
							bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("اپدیت بازی") and msg.get("author_object_guid") in admins:
							try:
								rules = open("jorat.txt","w",encoding='utf-8').write(str(msg.get("text").strip("اپدیت بازی")))
								bot.sendMessage(target, "بازی با موفقیت بروزرسانی شد.", message_id=msg.get("message_id"))
								
							except:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید.", message_id=msg.get("message_id"))			
								
					elif msg.get("text").startswith("اب وهوا") or msg.get("text").startswith("weather") or msg.get("text").startswith("!weather"):
							try:
								city = msg.get('text').split()[1]
								jd = loads(get('https://api.codebazan.ir/weather/?city=' + city).text)
								text = 'دما : \n'+jd['result']['دما'] + '\n سرعت باد:\n' + jd['result']['سرعت باد'] + '\n وضعیت هوا: \n' + jd['result']['وضعیت هوا'] + '\n\n بروز رسانی اطلاعات امروز: ' + jd['result']['به روز رسانی'] + '\n\nپیش بینی هوا فردا: \n  دما: ' + jd['فردا']['دما'] + '\n  وضعیت هوا : ' + jd['فردا']['وضعیت هوا']
								bot.sendMessage(target, text , message_id=msg["message_id"])
							except:
								print('code bz weather err')
								bot.sendMessage(target, 'متاسفانه سرور ارور داد' , message_id=msg["message_id"])	
								
					elif msg.get("text").startswith("مدیر کیه") or msg.get("text").startswith("مدیران") or msg.get("text").startswith("لیست مدیران"):
							rules = open("aa.txt","r",encoding='utf-8').read()
							bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							
					
								
					
							
					
								
					elif msg.get("text").startswith("کمک") or msg.get("text").startswith("/help") or msg.get("text").startswith("!help"):
							try:
								bot.sendMessage(msg.get("author_object_guid"), "دستورات زئوس دستورات زئوس بات✅🤖 \n ➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖ \nبرای کاربران گرارمی👌 \n1ـ 😁جوک \n2ـ😉فونت(فونت شاخ) \n3ـ😃دانستی \n4ـ💠 ماشین حساب (حساب) \n5ـ🔮 بیوگرافی \n6ـ📿ذکر  \n7ـ👨‍🎓سوال دانشی(دانشی) \n8ـ🤡 پ ن پ \n9ـ 😻 خاطره \n10ـ👻 الکی مثلا \n11ـ📃 ترجمه ( مترجم) \n12ـ💌 ارسال پیام به پیوی (پیام) \n13ـ👨‍👨‍👦‍👦 ادد ( افزودن کار بر با ایدی) \n14ـ📖 قوانین(قوانین گروه) \n15ـ⏰ تایم (ساعت) \n16ـ📆تاریخ \n17-🗣دادن ویس(بگو) \n18-📜ارسال حدیث \n19-✅دادن یک عدد وترجمه کردن ان عدد \n20-🗂داستان \n21-📙دیالوگ \n22-🔫لیست بازی ج \n23-⛈اب وهوا \n 24-📸شات از متن(شات) \n25-📹عکس جستجو (عکس جستجو)\n26-💡جستجو(جستجو) \n27-😎نام شاخ(نام شاخ) \n28-🗿یادگیر کلمات مثال \nwrt \nحرفه شما \nجواب ربات\n〰〰〰〰〰〰〰〰〰〰〰〰〰〰 \n توجه🤵( داشتی باشد اگه ادمین نت نداشته باشن قابلیت در دست رس نیست🤦‍♂) \n➰➰➰➰➰➰➰➰➰➰➰➰➰➰\n👮‍♂برای ادمین ها👩‍💻 \n1ـ🚫 اخطار(3)بشه ریم \n 2ـ❎گپ بسته (گپ سته میشه) \n3ـ✅گپ باز(گپ باز میشه) \n 4ـ❌ ریم (کار بر حذف میشه) \n5ـ📝 حذف(حذف پیام)باریپ رویه ان \n 6ـ💬 ارام (گروه 10ثانیه میره رو حالت ارام) \n7ـ🗯 غیر فعال ارام (غیر فعال کردن حالت ارام) \n8ـ☣روشن (روشن کردن آذرخش) \n9ـ📴 خاموش (خاموش کردن زئوس)\n10-🎙سنجاق پیام(سنجاق) \n ۱۱-🧠اموزش هوش مصنوعی اول کلمه(wet)رابزنید بعدمتن خودرا بگید بعد جواب زیر متن \n➿➿➿➿➿➿➿➿➿➿➿➿➿➿ \nتوجه😄(ربات داری قابلیت حذف فوش وحذف لینک میباشد پس لینک و فوش ندهید چت خوش😘❤️))").text
								bot.sendMessage(target, "نتیجه کامل به پیوی شما ارسال شد✔️", message_id=msg["message_id"])
							except:
								bot.sendMessage(target, "نتیجه کامل به پیوی شما ارسال شد✔️", message_id=msg["message_id"])
								
					elif msg.get("text").startswith("شات") or msg.get("text").startswith("!shot") or msg.get("text").startswith("shot"):
						if msg.get('reply_to_message_id') != None:
							msg_reply_info = bot.getMessagesInfo(target, [msg.get('reply_to_message_id')])[0]
							if msg_reply_info['text'] != None:
								text = msg_reply_info['text']
								res = get('https://api.otherapi.tk/carbon?type=create&code=' + text + '&theme=vscode')
								if res.status_code == 200 and res.content != b'':
									b2 = res.content
									print('get the image')
									f = open('image.jpg','wb')
									f.write(b2)
									f.close()
									p = Image.open('image.jpg')
									bot.sendPhoto(target, 'image.jpg', p.size,message_id=msg["message_id"])
								else:
									bot.sendMessage(target, 'ارتباط با سرور ناموفق',message_id=msg["message_id"])
							else:
								bot.sendMessage(target, 'پیام شما متن یا کپشن ندارد',message_id=msg["message_id"])
				
						else:
							bot.sendMessage(target, 'لطفا روی یک پیام ریپلای بزنید',message_id=msg["message_id"])
							
					elif msg.get("text").startswith("عکس جستجو") or msg.get("text").startswith("webshot") or msg.get("text").startswith("!webshot"):
						
						try:
							args = msg['text'].split()[1]
							if '.ir' in args:
								response = get(f"https://api.codebazan.ir/webshot/?text=1000&domain={args}").content
							else:
								response = get("https://http.cat/403").content
							with open("shot.jpg","wb") as shot: shot.write(response)
							bot.sendPhoto(target, "./shot.jpg", [720,720], caption="نمایی از صفحه موردنظر شما", message_id=msg["message_id"])
						except: bot.sendMessage(target, "متأسفانه نتیجه‌ای در بر نداشت ☹️", message_id=msg["message_id"])
					
					elif msg.get("text").startswith("جستجو") or msg.get("text").startswith("!search") or msg.get("text").startswith("search"):
							try:
								search = msg.get('text').split()[1]                             
								jd = loads(get('https://zarebin.ir/api/?q=' + search + '&page=1&limit=10').text)
								results = jd['results']['webs']
								text = ''
								for result in results:
									text += result['title'] + ':\n\n  ' + str(result['description']).replace('</em>', '').replace('<em>', '').replace('(Meta Search Engine)', '').replace('&quot;', '').replace(' — ', '').replace(' AP', '') + '\n\n'
									bot.sendMessage(target, 'نتایج کامل به پیوی شما ارسال شد', message_id=msg["message_id"])
									bot.sendMessage(msg['author_object_guid'], 'نتایج یافت شده برای (' + search + ') : \n\n'+text)
							except:
								print('zarebin search err')	
					
					elif msg.get("text") == "!del" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))
						
					elif msg.get("text").startswith("نام شاخ"):
							try:
								response = get("https://api.codebazan.ir/name/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err name")
						
					elif msg.get("text"):
						mop = open("data.txt","r",encoding="utf")
						ooo = mop.read().split("|/|")
						for i in ooo:
							ii = i.split("|=|")
							if msg.get("text") in ii[0]:
								bot.sendMessage(target, ii[1], message_id=msg["message_id"])
						mop.close()
					elif msg.get("text").startswith("wrt") and msg.get("author_object_guid") in admins :
							try:
								data = msg.get("text").split("\n")
								f = open("data.txt","a",encoding="utf")
								f.write(str(data[1] + "|=|" + data[2] + "|/|" + "\n" ))
								f.close()
								bot.sendMessage(target, "Was saved🤓", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "لطفا دستورات را درست وارد کنید ❌", message_id=msg.get("message_id"))
					
																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																			

					if msg.get("text") == "/بات" and msg.get("author_object_guid") in admins :
						bot.sendMessage(target, "ربات در حال اضر فعال است", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ادد") :
						bot.invite(target, [bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"]])
						bot.sendMessage(target, "کاربر به گپ اضافه شد ✅", message_id=msg.get("message_id"))

					

					elif msg.get("text").startswith("ماشین حساب") or msg.get("text").startswith("حساب") or msg.get("text").startswith("حساب کن"):
						msd = msg.get("text")
						if plus == True:
							try:
								call = [msd.split(" ")[1], msd.split(" ")[2], msd.split(" ")[3]]
								if call[1] == "+":
									am = float(call[0]) + float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
									plus = False
							
								elif call[1] == "-":
									am = float(call[0]) - float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "*":
									am = float(call[0]) * float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							
								elif call[1] == "/":
									am = float(call[0]) / float(call[2])
									bot.sendMessage(target, "حاصل :\n"+"".join(str(am)), message_id=msg.get("message_id"))
							except IndexError:
								bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌" ,message_id=msg.get("message_id"))
						plus= True
					elif msg.get("text").startswith("دعوت ") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "https://rubika.ir/joing/CBBAGJFB0NYDVKGTZRDVMRSPHQKSLFRM\nسلام کاربر گرامی شما به گروه ما دعوت شدید❤️☘\nراستی قوانین گپ را رعایت کن✅\nفحش=ریمو❌\nناسزاگویی=ریمو❌\nشاخ=ریمو❌\nاسپم=ریمو❌\nکد هنگی=ریمو❌\nممنون میشیم وارد گروهمون شوید❤️\nعشــــــــــــــــــــــــــــــــــــــقی❤️💐"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "‌‌د‌عوت نامه شما با موفقیت ارسال گشت.", message_id=msg.get("message_id"))
					elif msg.get("text").startswith("پیام ") :
						bot.sendMessage(bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["object_guid"], "شما یک پیام ناشناس دارید:\n"+" ".join(msg.get("text").split(" ")[2:]))
						bot.sendMessage(target, "پیام ارسال شد ✅", message_id=msg.get("message_id"))
					

																				
					

					elif msg.get("text") == "خاموش" and msg.get("author_object_guid") in admins :
						sleeped = True
						bot.sendMessage(target, "ربات خاموش شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("پینگ"):
							try:
								responser = get(f"https://api.codebazan.ir/ping/?url={msg.get('text').split()[1]}").text
								bot.sendMessage(target, responser,message_id=msg["message_id"])
							except:
								print("err ping")
							
					
						
					elif msg.get("text").startswith("بورس"):
							try:
								response = get("https://api.codebazan.ir/bours/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err bours")
							
					elif msg.get("text").startswith("اخبار"):
							try:
								response = get("https://api.codebazan.ir/khabar/?kind=iran").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err khabar")
					
					elif msg.get("text").startswith("غزل"):
							try:
								response = get("https://api.codebazan.ir/ghazalsaadi/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err ghazalsaadi")
							
					elif msg.get("text").startswith("اخطار") and msg.get("author_object_guid") in admins:
							try:
								user = msg.get("text").split(" ")[1][1:]
								guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
								if not guid in admins :
									alert(guid,user)
									
								else :
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
									
							except IndexError:
								guid = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
								user = bot.getUserInfo(guid)["data"]["user"]["username"]
								if not guid in admins:
									alert(guid,user)
								else:
									bot.sendMessage(target, "❌ کاربر ادمین میباشد", message_id=msg.get("message_id"))
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg.get("text") == "قوانین":
							rules = open("rules.txt","r",encoding='utf-8').read()
							bot.sendMessage(target, str(rules), message_id=msg.get("message_id"))
							
					elif msg.get("text").startswith("اپدیت قوانین") and msg.get("author_object_guid") in admins:
							try:
								rules = open("rules.txt","w",encoding='utf-8').write(str(msg.get("text").strip("اپدیت قوانین")))
								bot.sendMessage(target, "✅  قوانین بروزرسانی شد", message_id=msg.get("message_id"))
								# rules.close()
							except:
								bot.sendMessage(target, "❌ لطفا دستور را به درستی وارد کنید", message_id=msg.get("message_id"))
								
					elif msg["text"].startswith("امتیاز") or msg["text"].startswith("/star"):
								try:
									user = msg["text"].replace("امتیاز ","").replace("/star ","")[1:]
									guid = bot.getInfoByUsername(user)["data"]["chat"]["abs_object"]["object_guid"]
									star(guid,user)
									
								except:
									try:
										guid = bot.getMessagesInfo(target, [msg["reply_to_message_id"]])[0]["author_object_guid"]
										user = bot.getUserInfo(guid)["data"]["user"]["username"]
										star(guid,user)
									except:
										bot.sendMessage(target, "❌ خطا در اجرای دستور", msg["message_id"])
								
					elif msg.get("text") == "برداشتن سنجاق" and msg.get("author_object_guid") in admins :
							try:
								bot.unpin(target, msg["reply_to_message_id"])
								bot.sendMessage(target, "پیام مورد نظر از سنجاق برداشته شد!", message_id=msg.get("message_id"))
							except:
								print("err unpin")
								
					
								
					if  msg.get("text").startswith('!user @'):
						try:
							user_info = bot.getInfoByUsername( msg.get("text")[7:])
							if user_info['data']['exist'] == True:
								if user_info['data']['type'] == 'User':
									bot.sendMessage(target, 'Name User:\n ' + user_info['data']['user']['first_name'] + ' ' + user_info['data']['user']['last_name'] + '\n\nBio User:\n ' + user_info['data']['user']['bio'] + '\n\nGuid:\n ' + user_info['data']['user']['user_guid'] ,  msg.get('message_id'))
									print('sended response')
								else:
									bot.sendMessage(target, 'کانال است ❌' ,  msg.get('message_id'))
									print('sended response')
							else:
								bot.sendMessage(target, "کاربری وجود ندارد ❌" ,  msg.get('message_id'))
								print('sended response')
						except:
							print('server bug6')
							bot.sendMessage(target, "خطا در اجرای دستور مجددا سعی کنید ❌" ,message_id=msg.get("message_id"))		
					
					elif msg.get("text").startswith("ترجمه"):
						
						try:
							responser = get(f"https://api.codebazan.ir/translate/?type=json&from=en&to=fa&text={msg.get('text').split()[1:]}").json()
							al = [responser["result"]]
							bot.sendMessage(msg.get("author_object_guid"), "پاسخ به ترجمه:\n"+"".join(al)).text
							bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
						except:
							bot.sendMessage(target, "لطفا دستور را به طور صحیح وارد کنید ❌", message_id=msg["message_id"])
							
					
					elif msg.get("text").startswith("فونت"):
							#print("\n".join(list(response["result"].values())))
							try:
								response = get(f"https://api.codebazan.ir/font/?text={msg.get('text').split()[1]}").json()
								bot.sendMessage(msg.get("author_object_guid"), "\n".join(list(response["result"].values())[:110])).text
								bot.sendMessage(target, "نتیجه به پیوی شما ارسال شد ✅", message_id=msg["message_id"])
							except:
								print("err font")
							
					
					      
					elif msg.get("text") == "ربات":
							try:
								user = bot.getUserInfo(msg["author_object_guid"])["data"]["user"]["first_name"]
								ans = ["جــونـم " +user+ " خــوشـگلم ☺❤","بـفـرما " +user+ " عـشـقـم 🍫😁","جــون دلـم " +user+ " نــفس 😍🌹","جــون دلـم " +user+ " نــفس 🙊🔗","بـفـرما " +user+ " مهــربـونم 😢💝","امـر کـن " +user+ " قـشـنگم 🌷😋","جــونـم عشـــقم " +user+ " مهــربـونم 😝❤","بـفـرما " +user+ " عـزیـزم 😍🌹","جــونـم عشـــقم " +user+ " نـفــسم 🙊🔗","جــون ربـات " +user+ " خــوشـگلم 😍🌹","امـر کـن " +user+ " خــوشـگلم 😍❤","جــون دلـم " +user+ " نــفس ☺❤","جــون ربـات " +user+ " عـزیـزم 🙈🌹","جــونـم " +user+ " نــفس 🌷😋"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err random")
								
					
							
					elif msg.get("text") == "آذرخش":
					      user = bot.getUserInfo(msg["author_object_guid"])["data"]["user"]["first_name"]
					      text = f"جـــونــم {user} عــزیـزم🙂🌹"
					      bot.sendMessage(target, text, message_id=msg.get("message_id"))
																																																																																																									 																																																																	
					elif msg.get("text").startswith("جوک"):
							try:
								response = get("https://api.codebazan.ir/jok/").text
								bot.sendMessage(target, response,message_id=msg.get("message_id"))
							except:
								print("err jok")
							
					elif msg.get("text") == "سلام":
							try:
								user = bot.getUserInfo(msg["author_object_guid"])["data"]["user"]["first_name"]
								ans = ["هـــای " +user+ " عـــزیـزم🗿❤️","ســلام " +user+ " مــهربــونم🙊✨","ســـلام " +user+ " خــوبی😄؟","هـــای  " +user+ " نــپــصم😎🍿"]
								bot.sendMessage(target, choice(ans), message_id=msg.get("message_id"))
							except:
								print("err random")

					elif msg.get("text") == "تایم":
						bot.sendMessage(target, f"Time : {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}", message_id=msg.get("message_id"))

					elif msg.get("text") == "تاریخ":
						bot.sendMessage(target, f"Date: {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday}", message_id=msg.get("message_id"))

					elif msg.get("text") == "حذف" and msg.get("author_object_guid") in admins :
						bot.deleteMessages(target, [msg.get("reply_to_message_id")])
						bot.sendMessage(target, "پیام پاک شد ✅", message_id=msg.get("message_id"))

					
					elif msg.get("text") == "گپ بسته" and msg.get("author_object_guid") in admins :
						print(bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","AddMember"]).text)
						bot.sendMessage(target, "گپ بسته شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text") == "گپ باز" and msg.get("author_object_guid") in admins :
						bot.setMembersAccess(target, ["ViewMembers","ViewAdmins","SendMessages","AddMember"])
						bot.sendMessage(target, "گپ باز شد ✅", message_id=msg.get("message_id"))

					elif msg.get("text").startswith("ریم") and msg.get("author_object_guid") in admins :
						try:
							guid = bot.getInfoByUsername(msg.get("text").split(" ")[1][1:])["data"]["chat"]["abs_object"]["object_guid"]
							user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
							if not guid in admins :
								bot.banGroupMember(target, guid)
								bot.sendMessage(target, f"✅ کاربر حذف شد", message_id=msg.get("message_id"))
							else :
								bot.sendMessage(target, f"❎ کاربر حذف نشد", message_id=msg.get("message_id"))
								
						except IndexError:
							a = bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"]
							if a in admins:
								bot.sendMessage(target, f"کاربر حذف نشد ❌", message_id=msg.get("message_id"))
							else:
								bot.banGroupMember(target, bot.getMessagesInfo(target, [msg.get("reply_to_message_id")])[0]["author_object_guid"])
								bot.sendMessage(target, f"کاربر حذف شد ✅", message_id=msg.get("message_id"))

				else:
					if msg.get("text") == "روشن" and msg.get("author_object_guid") in admins :
						sleeped = False
						bot.sendMessage(target, "ربات فعال شد ✅", message_id=msg.get("message_id"))

			elif msg["type"]=="Event" and not msg.get("message_id") in answered and not sleeped:
				name = bot.getGroupInfo(target)["data"]["group"]["group_title"]
				data = msg['event_data']
				if data["type"]=="RemoveGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"کاربر به نام {user} و در زمان ({time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec})ازگروه حذف شد به دلیل رعایت نکردن قوانین", message_id=msg["message_id"])
				
				elif data["type"]=="AddedGroupMembers":
					user = bot.getUserInfo(data['peer_objects'][0]['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"کاربر {user} در زمان  {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec} و به تاریخ  {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday} به گروه  {name}عضو شد\nلطفا قوانین رو رعایت کن ✅                                               برای اطلاعات بیشتر از کلمه(قوانین)استفاده کنید😊برای اطلاعات بیشتر دستورات ربات ازکلمه ایه /help", message_id=msg["message_id"])
				
				
				elif data["type"]=="LeaveGroup":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"کاربر{user} در زمان ««{time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec}»»گروه ترک کرد", message_id=msg["message_id"])
					
				elif data["type"]=="JoinedGroupByLink":
					user = bot.getUserInfo(data['performer_object']['object_guid'])["data"]["user"]["first_name"]
					bot.sendMessage(target, f"کاربر {user} در زمان  {time.localtime().tm_hour} : {time.localtime().tm_min} : {time.localtime().tm_sec} و به تاریخ  {time.localtime().tm_year} / {time.localtime().tm_mon} / {time.localtime().tm_mday} به گروه  {name}عضو شد\nلطفا قوانین رو رعایت کن ✅                                               برای اطلاعات بیشتر از کلمه(قوانین)استفاده کنید😊برای اطلاعات بیشتر دستورات ربات ازکلمه ایه /help", message_id=msg["message_id"])

			answered.append(msg.get("message_id"))

	except KeyboardInterrupt:
		exit()

	except Exception as e:
		if type(e) in list(retries.keys()):
			if retries[type(e)] < 3:
				retries[type(e)] += 1
				continue
			else:
				retries.pop(type(e))
		else:
			retries[type(e)] = 1
			continue

