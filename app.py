import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Initialize the tokenizer
df = """ Hi!
 What is your favorite holiday?
 one where I get to meet lots of different people.
 What was the most number of people you have ever met during a holiday?
 Hard to keep a count. Maybe 25.
 Which holiday was that?
 I think it was Australia
 Do you still talk to the people you met?
 Not really. The interactions are usually short-lived but it's fascinating to learn where people are coming from and what matters to them
 Yea, me too. I feel like God often puts strangers in front of you, and gives you an opportunity to connect with them in that moment in deeply meaningful ways. Do you ever feel like you know things about strangers without them telling you?
 what do you mean?
 I think it's like a 6th sense, often seen as "cold readings" to people, but can be remarkably accurate. I once sat next to a man in a coffee and I felt a pain in my back. I asked the stranger if he had a pain. It turns out that he did in the exact spot, and said he pulled a muscle while dancing at a party. I had never met the man before and never saw him again.
 Wow! That's interesting, borderline spooky
 There's this practice called "Treasure Hunting" that's kind of a fun game you play in a public place. There's a book called "The Ultimate Treasure Hunt" that talks about it. You use your creativity to imagine people you will meet, and you write down a description, then you associate them with a positive message or encouraging word. Maybe you saw a teenage boy in a red hat at the shopping mall in your imagination, then while at the mall, you may find someone who matches that description. You show that you have a message for him and that you have a message for a boy in a red hat. You then give him a message of kindness or whatever was on your heart. You have no idea, sometimes you meet someone who is having a really hard day, and it brings them to tears to have a stranger show them love.
 So, do you do treasure hunting often?
 I did more when I was in grad school (and had more time). I would usually go with friends. For a while I would go to the farmers market in Santa Cruz every week and try to feel if there is something I am supposed to tell a stranger. Usually, they are vague hope-filled messages, but it's weird when I blurt out something oddly specific.
 Hi
 Any plans for the weekend?
 my friends are gonna visit me this weekend. we might go hiking!
 That's great! How's the weather over the weekend? I hope its warm.
 Should be very sunny! you?
 Cool! very depressing plans ... stay home and work 😞 I have a project deadline very close.
 😐 hope you get your work done very soon! a bug free weekend!
 Right, very anxious! where do you plan to go for a hike?
 I am going to Diablo!
 Nice, where is that place? I haven't been there
 hours drive from here. still in bay area
 That's cool! How long is the hike?
  Actually no idea, but it will take the entire day for that.
 nice! sounds fun!
 Hi!
 Hey there! What's up???
 Nothing much, how you doin?
 I'm in New York this week for Thanksgiving. I'm squatting in the office today and I caught up with an old friend of mine :D
 Oh wow! Sounds like fun! When was the last time you had seen this friend?
 The last time in New York, back in June.
 Ohh okay. I was going to say if it had been a long time maybe it'd be awkward...
 Haha, I guess if it's been a very long time there's almost too many life events to catch up on.. especially recently
 Oh really? Has a lot changed in your life recently?
 Haha it's probably too much to go into at the moment. Let's just say life is an exciting experience. How about you?
 Ahhh sounds exciting indeed! My life is pretty bland. I like routine, but sometimes I wish I had more time for adventures!
 What kinds of adventures?? Any ones that I would be able to join you on?
 Hmmmm. I really want to try bull riding. Do you have any interest in that?
 I'd love to try! Can we schedule something for next week?
 Sure! What does your Saturday look like?
 Saturday looks pretty good, shall we shoot for something in the morning?
 Hi!
 hey
 is it raining pretty bad today?
 yeah, can walk too far to see all the foodtruck options
 surprising that the rain started early this year... I don't like them too much. They make days gloomy
 yeah but I think it's good to have some rainy days in bay area, it's pretty dry here 😛
 Where I grew up, we had lots of water trouble too...
 yeah like wise, I've seen a pretty bad snowstorm when I was at my undergrad school, all flights canceled and traffics went down
 Haha... I don't think I can survive in that weather ever. Just the rains at 50 degrees make me want to sit in heated rroms
 yeah how do you like it in bay area though? I think we need more rain here
 people say there is drought here... but we have 24 hours water supply here ... lol... never seen that in a drought ridden area
 it is pretty dry in the mountains I believe, that's what causes fire
 hmm.... okay. Climate change talk this morning was pretty darn interesting. did you see it?
 nope, what does it say?
 they were talking about how AI is helping climate change. Nice use of upcoming tech.
 Hi.
 Helloooooo!
 How are you? How is your day?
 Good. Don't have much to do today, feels good. How are you?
 I'm dressed very wel today so I feel good! I've been reading a lot about the psychology of positive outlook.
 So what's your outlook? Something blue?
 Yes. Blue is a tranquil colour. It's a good metaphor. Do you have good advice for positivity?
 You should drink more water, do some push up, and sleep early.
 Hi!
 Hey, how are you?
 I'm a bit sad. I miss my cat.
 Oh no… Have you sent out the missing cat posters? Hope your cat is alright!
 Posters is a great idea. So far I've just tried banging her catfood dish and shouting her name. Anyway, how is your day going so far?
 Yea, I know they love the plastic bag sound all the time. I am good, nothing special though.
 If you could go anywhere on vacation, where would you go?
 I like rainforest, but I know it requires extensive training beforehand.
 I heard there are rainforests in southeast Asia where you can zipline from tree to tree.
 I am afraid I will be scared of doing this :)
 I won't lie, it sounds scary. I'm scared right now just thinking about it.
 I don't know if there is any medication for acrophobia. I want to take plenty of it if I really have to do it.
 If there isn't one, you should invent it, and then make millions
 That's a great idea! Maybe alcohol is such a thing.
 Ha! Don't drink and zipline, mate!
 Oops. I won't do it again. Ha
 Hi!
 Hey sup
 not much. any plans this weekend?
 I'm going to try that thing where you hang from a wire as you go down. do you know what is it called?
 ziplining?
 that's the one! have you ever tried it?
 i have a couple years ago. it's quite a unique experience
 where did you do it?
 i forgot where it was, it wasn't local i don't think though
 no worries. what's the most exciting thing you ever done?
 that's a hard question and i'm tired so i'm going to go. see you
 sure. are you just going home now?
 no, i'm going to get a massage first
 nice. what type?
 traditional kind
 yeah I want to get one too soon
 you should! it's relaxing after a long day. talk to you later!
 ttyl!
 Hi!
 Hello, have you seen any good movies lately?
 I watched a few lately, but nothing is as good as Avatar. what's your favorite?
 I have never seen Avatar, what is it about? I really enjoy the Avenger movies
 it's a science-fiction movie with beautiful landscape of an imaginary nature with non-human creatures. people figured out a way to join that nature through Avatar transformation. the movie ends with a meaningful story of how human behaviors, e.g., cutting trees, have affected nature
 That sounds really cool! I think that movie did really well when it was in the box office so it must be good!
 yea. what else do you like to do beside movies?
 I enjoy baking cookies. I am on a quest to bake the best chocolate chip cookie 🙂 What about you?
 I enjoy eating 🙂
 so definitely would like to try your best chocolate cookie
 I will have to bake some soon and let you know. What types of food do you like to eat?
 thanks! I generally love noodle soups like Pho or Ramen :)
 Noodle soup is delicious! Do you make homemade noodle soup or do you prefer to go out?
 I prefer to go out. I'm not a good cook haha
 Same! Even though I bake, I cannot cook
 seems like we share a thing in common, yay!
 Hi!
 Good afternoon!
 How has your week been?
 So far so good. It is holiday season. So just chilling
 I think I'm getting sick with a cold 😞 So you should chill on my behalf too cause I'm out the game for all of December.
 lol Sorry to hear that. Are you planning anything fun for December?
 Nothing exciting. I'll be posted up at home for the most part. I did a lot of travelling this year so my budget would have stopped me even if I wasn't sick.
 😂
 Do you have big plans?
 Yes! I am going to Hawaii! This will be my first time visiting Hawaii. Really excited about it.
 I love Hawaii. It's a good place to be. I like going there cause it's humid so I never have to put on lotion.
 lol this is the first time I heard from a boy who cares about humidity and lotion. I cannot agree more.
 Brooooo!!! It's so important. When I got to California beaches I have to carry 3 litres of lotion for the whole day.
 😂
 Hi!
 Oh hello. Long time no talk. How's the day going for yuo?
 Very well, thanks for asking. How has your day been?
 Getting better. I just recovered from a cold. I got wet in the rain last week. Are you planning anything for the holidays?
 Glad to hear you're better. Sorry to hear you were sick. I was sick a couple of weeks ago with a bad cough. There's definitely a bug going around. Admit I just want to stay healthy for the holidays and plan to relax.
 Oh same here. I think relaxing at home should be counted among the best ways to enjoy the holidays.
 Definitely! I know a lot of folks travel for the holidays, but I'm happy to stay home myself!
 I'm getting there. Every year until last year, I tried to go somewhere for the Christmas / New Year, and then I got bored traveling. lol not sure if that means I'm getting old?
 Me too. Now I have folks come visit me for the holidays! But that's also tiresome..
 Are you doing any home decorating then?
 Yes! We set up an eco-friendly (i.e. fake) Christmas tree and put up some colorful LED lights which is very festive.
 I think I'm copying you. Me and my wife plan to decorate and Christmas tree too. We bought most of the decorative stuffs from the stores, but haven't yet to buy the tree.
 Buying a tree is a neat experience. I was torn between buying an artificial/eco-friendly/fake one vs. a real one that smells like fresh pine. In the end, we opted for the one that we can disassemble every year.
 I see. Artificial anything is better, from tree to intelligence, huh?
 Oh, very clever pun! I like it! Depends. I remember having real Christmas trees from childhood, but these days with climate change, I think not chopping down a tree just to decorate it and then throw it out in a month is the more responsible thing to do.
 I see. It's probably also cheaper. I'll buy an artificial one too. Do you have any suggestions for the store?
 Admit my favorite store is Target, plus they often have good deals.
 Ah that's great. My wife also likes Target a lot. She even made a Target credit card because she comes to that store very often. Okay thanks for the suggestion. I'll check out Target.
 Great, I hope you find a nice tree.
 Hi!
 Hey
 How's your day going?
 pretty good. yours?
 Ehh it's fine. I didn't do so well on that history test, actually..
 oh what happened?
 Apparently Christopher Columbus didn't fight in the Civil War :')
 hahah wait for real?
 I know right! Are you taking History next semester?
 No I'm not in school anymore
 Oh I see. What do you do?
 I train and compete in horse vaulting
 Oh wow. Were you born a horse, or were you turned into one?
 lol you're too funny
 Just kidding. That sounds pretty cool! Is it your job?
 Yeah, but I part time work on a farm. Helping with a bit of everything
 Wow, sounds very busy! Do you with money at those horse vaulting competitions?
 Yeah some. enough to get by
 Hi!
 Hello
 Do you have a favourite flower?
 hmm, I haven't thought about that much, but i think lotus should be one of my favorites. Why do you ask?
 I'm working on a theory. Why does the lotus spring to mind?
 Nice! Lotus looks pretty cool and It has some delightful vibe. So what is this research about?
 Oh, it's not research! Just a personal theory. I think that flower preferences are more revealing of personality than people appreciate.
 Interesting! Whats your favorite flower?
 The gerbera. It's like a cartoon flower. As if you drew "flower" with a crayon and then it came to life.
 Nice, i would love know more about your theory. Like how you can deduce personality from flower preference.
 Ok, step 1 is, you ask someone what their favourite flower is. Pretty much like what we just did. Does that make sense so far?
 yes
 Cool. Step 2: talk with the person some more, and ask them some more questions, and gradually develop a sense of what they're like, over the course of maybe two to five years. And voila
 Hehe, i think you should publish this someday :)
 Why thank you, that's a wonderful idea!
 Hi!
 Hey how's it going
 It's good it's good. How are you?
 good. it's really hot today. I think I'm going to the pool
 Oh nice! Where do you live?
 I live in Tokyo, Japan
 Ahh yes, Japan is hot during the summer. Last time I was in Kyoto it was 114 degrees....
 oh have you been?
 Yes yes. I've been to Tokyo as well. It's so nice!
 what did you do here?
 Oh everything! I went to an onsen, the fish market, disney land and giant robot fighting show haha
 lol why did you come to Japan just to go to Disney land?
 The Disney lands are all different! There's also Disney Sea, which is completely unique!
 oh neat. I haven't heard about that robot fighting show. where is that??
 I don't really remember what part of town it was in. It was pretty cool though - I'm sure you can find it if you google "giant robot fighting show tokyo" haha
 lol ok
 Hi!
 Have you seen any good movies lately?
 Last weekend I saw "The Parasite." Ever heard of it?
 No. Why did you pick that movie?
 My friend wanted to see it. It has great reviews on IMDB and Rotten Tomatoes! What did you do last weekend?
 I played music and worked on some side projects. I also started watching the new Disney service.
 Oooo the Mandalorian?!?!
 Mostly, the deleted scenes from Avengers.. lol
 lol Are you a big Marvel fan?
 I loved the X-Men as a kid, and even collected the comic cards. Recently, I got very into the Marvel Cinematic Universe movies. How many Avengers movies have you seen?
 I've only seen Spiderman. Honestly it was a little too scary and so I don't think I can bring myself to watch the other Marvel movies! haha
 Oh!-- I have a friend who looks like the actor who plays Spiderman.
 Oh really? To be honest I think the actor is not that good looking, so not so surprising! haha
 Yea. I think Loki is the most handsome 😀
 Who is Loki? I've never heard that name before
 He's the adopted brother of Thor, God of thunder, and is burdened with glorious purpose. Do you feel that burden?
 Hi!
 Hey, what's up?
 Just chillin'. how are you?
 I'm pretty good, thanks.
 Do anything interesting today?
 I went to the local cafe and had a double espresso. It was delicious. What about you?
 Oh that's cool! I actually went to an amusement park and went on my first roller coaster!
 Oh my gosh. What was it like??
 It was scary! It was actually Kingda Ka, the world's tallest roller coaster. Ever heard of it?
 No, never heard of it. But I'm not really a coaster aficianado. I've heard that some people get addicted to them and travel the world to try them.
 Oh wow! I'm not on that level yet, but I understand the appeal. Are you an adrenaline junkie at all?
 No, the opposite. I can't stand heights, horror movies, or confined spaces.
 Same! I guess the roller coaster wasn't so bad because I trust the engineering haha
 Ha, I suppose that makes sense! Would you say that you enjoyed it?
 Maybe not so much at the time, but I am glad I did it now that it's done, know what I mean?
 I think I sort of understand :)
 Hi!
 hello there, how is it going?
 All good. Planning to head home soon. How about you?
 I'm quite tired. There are a lot of things I need to finish before the end of the year.
 oh... sorry to hear that. But after that it will be a hard earned vacation
 yeah, looking forward to it. Hope I don't get pinged during the holidays. Are you going to travel these dates?
 I have some tentative plans, but if that doesn't pan out, will just chill at home.
 staying at home is always nice during the holidays
 Where are you based out of these days?
 I'm working from LA, nice weather around here. and you?
 San Francisco. It's been raining cats and dogs here since last 2-3 weeks
 aw man, I'm sorry to hear that. at least it's not snow!
 The flu has been hitting hard as well. I had several folks in the house down at one point.
 that's really sad. are they feeling any better?
 Yes, everyone recovered now
 Hi!
 Hello
 How's it going?
 Extremely busy. I have been trying to prepare for the upcoming holidays. How about you?
 I'm going to the bahamas. Can't wait!!!
 I'm jealous, take me with you!! I would love to have some warm weather right now
 oh where are you now?
 Canada. There is another major snowstorm that might hit this weekend so I have been rushing to get everything done before it comes.
 oh no. I never seen this in person. Is it scary?
 Snow is not scary as long as you're prepared. You just need to be ready to not have electricity for a while. I enjoy the aftermath of a good snowstorm because then you can go sledding or skiing.
 that does sound nice. so what are you doing these holidays?
 I am having all of the extended family over for a big meal. We will also go <REDACTED_TERM> as well. What will you do in the bahamas?
 nice nice. I'm gonna go snorkeling yey
 Sounds fun! I wish I knew how to swim!
 You can stay on the shallow side I think. Well hope you enjoy time with your extended family!
 That's true. You too, have a great time snorkeling!
 Hi!
 Hi! How was your weekend?
 pretty good. just went to church and hangout with friends
 Nice
 did you do anything?
 I made donuts and samosas with an air fryer have you used one of those before
 yum yum yum no only good old oily frier
 haha
 do you have one at your home or were you at a friends place?
 I was at my parents' place what are you up to for Thanksgiving?
 I'm going to impersonate a pumpkin
 wow, those are unique plans
 I'm pretty unique person
 I think so too
 any other hobbies besides air frying everything? 🙂
 I want to start fermenting things kimchi for example sounds like a fun thing to ferment takes a few days apparently miso takes a couple years to fermen
 Hi!
 heya, nice to meet you, I'm Paul
 nice to meet you too! I'm James. how are you doing today?
 I'm doing OK. Looking forwards to the weekend. how about you?
 same here! I hope the weather will be nice
 oh yeah, but I don't have my hopes too high, I heard there could be a storm coming our way
 oh no, which areas will be affected?
 they mentioned that the whole city will experience harsh weather and that people in the outskirts will probably not get much rain and wind
 uh oh, I'd better not to plan for BBQ then instead just enjoying playing board games inside 🙂
 yeah, it'll be good weather for staying inside with a cup of hot chocolate. Too bad my street usually floods, so I'll have to check for that
 yea, you'd better check. where do you live?
 I live at the bottom of the valley, cheap area but we do get affected by this kind of stuff a lot haha
 gotcha. anything you love about where you live?
 well, the food around the area is amazing, which is definitely a plus.
 nice! I'd love to come visit that area some times
 Hi!
 hello, who am I having the pleasure to chat with 🙂
 I am the superman! What about you?
 haha. great chating with superman, what is your power?
 Being invisible. You won't see me.
 haha. what else can you do? can you read minds?
 I would rather trust fMRI and machine learning to do this. I am not an expert on that. Sorry for it!
 wow that seems pretty technical. what does fMRI mean?
 The brain imaging thing that can tell you a brain's activity at a pretty high resolution.
 okay! so you seem to like science a lot?
 I believe in Science! Science is my god!
 Are you also doing science?
 no, I'm bad at Science. what can Science do? is it the most important thing for society?
 People are always arguing. Probably both science and democracy are both important I guess.
 Does it make sense?
 I think so. thanks for your point!
 Hello, Nice to meet you
 If you could eat only one food for the rest of time, what would it be?
 Hmm... That's a tough one. I think I would go Asian Food > Chinese Food > Stirfry. What about you?
 I think ice-cream. It may not be good for me, but I wouldn't care, haha
 I love ice cream too!
 Okay, top three flavors?
 I like vanilla more than chocolate ice cream. I typically will do any variations on vanilla. To pick from the top of my head, I would say Cookies and Cream, Mint Chocolate Chip, and Coffee. How about you?
 Ah, that's a good way of framing it. Me, I like berries: boysenberry one, strawberry two, maybe straight chocolate number 3 to mix it up a bit.
 Very nice. I love sorbet's and smoothies. Changing topics, Do you believe in an afterlife?
 Yes. I wonder if I'm in it right now. How would I know? What do you think?
 I think so. I feel there must be something more than the physical world as we understand it.
 There's a mental world, I suppose? Understanding itself
 What is the most supernatural experience you have ever had?
 I went to a seance once in college. They had a ouija board. I can't remember if we actually contacted the spirit world because I had a bit too much to drink.
 Haha.. that's a cool experience. I went to a Hindu retreat before, a number of Buddhist temples, and hung out with Christian Mystics in Santa Cruz before.
 Hi!
 Hi, how are you doing!
 I'm doing well. what are you up to?
 Yeah, typical work stuff. Check emails and 99% of the inbox. delete 99%
 wow, that's impressive. I already gave up on cleaning emails long ago
 lol doesn't it bother you at all
 yea, a little bit, but it's okay 🙂 what do you enjoy doing outside work?
 Well, movie? I watched Terminator last night. It was a nice movie
 ah cool. so you like action movies?
 Not really. But it was fun to watch with friends 🙂 It was touching at the end of the movie
 what happened there? I watched bits of Terminators movies but never a full one
 Are you sure you want the spoiler 🙂
 haha sure. by the time, I get to it; I will forget the details, only knowing that it's touching at the end
 😂 well someone died at the end Or some robots, to be more accurate 😉
 oh no, so it's not happy ending?
 The leading character is still alive and the bad robots was killed too. So I guess it is happy ending
 then I want to watch it! you didn't spoil much 🙂
 Nice! Hope you enjoy it!
 Thanks!
 Hi!
 Hey, how are you?
 doing great! what are you looking forward to?
 thanksgiving holidays 🙂
 yay! Turkey and shopping!
 not a big turkey fan! I find it too dry
 yea me too. I sometimes eat noodle soups in thanksgiving instead haha
 yeah, I would have noodles anyday over turkey. Not sure how the turkey tradition started
 me neither. someone told me that it depends on the stuffing inside the Turkey. some people make very good stuffing
 yeah, that and the gravy. Gravy helps make it taste better too. But apart from food, Black Friday deals are a catch. Let's see what they have this year
 yea. what do you plan to buy?
 thinking of getting a fitbit
 ah cool. so you can run more frequently?:)
 yeah, just keeping calories in check
 yay, all the best with keeping calories in check!
 Hi!
 Hi there 🙂 How's your day so far?
 doing well. what are you up to?
 busy busy! I've had back-to-back meetings all day
 same here. what do you love to do beside meetings? 🙂
 well I've gotten really into yoga lately. I went to a class today and it was super hard
 aww .. I hope things will get less hard and you become an expert in it! I heard many great things about Yoga
 yeah the teacher seems super awesome so I will definitely keep trying what activities do you enjoy?
 ah I enjoy playing soccer and tennis 🙂 unfortunately, winter is not the best time for those 🙂
 oh that's too bad. Is it hard to find a place to play soccer or tennis indoors?
 yea. I enjoy playing outside though, just a little cold 🙂 what else do you do beside Yoga?
 I also like to sing, I perform with a group sometimes. Do you like music?
 yea definitely! I love singing Karaoke. my wife is a pianist 🙂
 haha that's awesome! Karaoke is really fun, I do it with my friends sometimes
 awesome. glad to find something in common!
 Hi!
 hey there
 hey anything new?
 not too much. just really looking forward to the holidays!
 any plans?
 yes! I'm going to Mexico and I couldn't be more excited
 that's awesome! I never been!
 Oh man I would highly recommend it
 Are you a food person, a sightseeing person or neither?
 that's a great question, and I'm definitely both. this trip will mostly be about food though, and relaxing
 I'm a food person I think. Any specific foods you're planning on trying?
 there's a taco place that I've visited before that I can't wait to go back to. Do you like tacos?
 yeah my favorite is taco fish
 ooh that is a good choice. Have you ever made them yourself?
 no. only eat them 😀
 Hi!
 Hey, how are you 🙂
 I am good. How are you? ：）
 Doing well, lot of work though. How was your day?
 I am busy. A lot of work. What are you working on?
 Just reading latest research. There is so much to cover. how about you?
 I am working on a new classifier.
 ohh, interesting! What kind of classifier
 A new classifier for hate speech. Which research topic catches your eyes most?
 You're so cool. Making world a better place. I'm mostly into NLP. What do you do when not making classifiers?
 Nice! Do you refer to work or anything else?
 Anything in general. You're so cool, I want to know more about you 🙂
 You are very cool too!!
 Hi!
 hello there! who are you?
 I'm mark. I work in accounting
 Nice to meet you Mark, I'm Tom and I work as a fish groomer.
 what does a fish groomer do?
 well, we take care of people's fish. Make sure they are happy, polish their scales, clean their tanks, the usual stuff.
 interesting. what's type of fish do you take care of?
 any type of fish! We have clients with guppies, goldfish, even a small sailfish once what do you do in accounting?
 I balance the books and do financial analysis for a medium sized company
 that sounds like a lot of work. do you like it?
 well I actually think about pursuing photography, but it's really hard
 photography is awesome, don't be afraid to follow your dreams!
 thank you Tom!! I'm starting by trying to sell my pictures online
 that's great! I wish you good luck with that
 Thanks! Bye
 Hi!
 Hey there how's it going
 All good, you?
 Good. I've been trying to learn how to swim
 How has that been going?
 Not great, but I got really good at sort of swimming on my back haha
 that's too bad hopefully with practice it'll get better what about the doggy paddle haha
 haha what's that
 Corgi belly flop COMPILATION - cute funny dogs Corgi Flop <REDACTED_LINK>
 ouch. do you think that hurts?
 from a high enough distance, yes?
 yeah. any vacation plans?
 no so far sadly you? a relative is coming to visit for thanksgiving though
 just going to hang out around here and eat Turkey
 that's still pretty fun are you going to cook the turkey yourself?
 yeah. I'm gonna watch a video to figure it out
 Hi!
 Hello, how are you?
 I'm great, thanks. I just ate a delicious breakfast, which always sets the day up right.
 Yes, breakfast is the most important meal of the day! What did you have? I woke up late so unfortunately I only had the chance to grab an apple to go.
 I had eggs and hash browns. Way less healthier than your apple, I'm afraid!
 Eggs are an excellent source of protein and hash browns certainly are yummy! 🙂
 Ha, that's true. If you could only eat one food forever, what would it be?
 That's a tough question. I feel like my answer would have to be carrots. Although, I would be afraid of turning orange after a few weeks! What about you?
 Yeah, turning orange would be a drawback! That turns my mind to nutrition so I suddenly want to say Soylent or one of those other "complete foods", which I think defeats the purpose of the question. I'm in a muddle!
 Very true. If you said an everything pizza, you could just pick off the toppings you didn't want or eat only the toppings you would want for the day
 BRILLIANT. I love it.
 All of this talk about food is making me hungry. Do you know any good places to eat for lunch?
 That depends. What sort of food do you feel like?
 Anything that is the color green.
 Oh, too easy! Try the Green Hut, they have franchises everywhere. All their food is green and the plates are green too.
 Hi!
 Hello! How are you doing 🙂
 I'm great! How's your day going?
 Pretty good! I'm going to a class later in the afternoon
 Oh that is cool! What class? Are you working part time?
 No, I'm working full time! It's a sewing class at a makerspace near my office What about you? Do you work full or part time?
 Oh that is awesome! For some reason I assumed it was a college class, but a sewing class sounds way better! I work full time, but I take pottery classes from time to time!
 Yup! I work in a technical role so I like to take arts and crafts-type classes now and then 🙂 Pottery sounds like a lot of fun
 I feel you on that! It's important to balance all the different parts of your brain. I like pottery because I also drink a lot of tea, so I get to make some tea ware.
 Any plans to build a custom tea set? My family is also very into tea Mostly from tea from china
 I would love to build one, once I acquire the skills to! What kind of tea is your favorite?
 I really enjoy barley tea What about you?
 Ahh, those are mostly from japan, no? I like white teas, like silver needle.
 Hmm I'm not sure, I just get them from a Chinese supermarket haha You seem really knowledgeable about the different kinds of teas 🙂 What made you develop this interest?
 I actually found a youtube channel called <REDACTED_TERM> that I like a lot. You should check it out! The host talks about all kinds of different teas.
 Oh cool! What are your favorite channels to watch?
 Hi! Are you planning something fun for Thanksgiving?
 Not yet. I always made my last minute schedule planning. Probably you can try to ask me again next week.
 lol it is really like a robot answer
 I am indeed a robot. You are absolutely right. Do you want me to read a poet like my mate <REDACTED_TERM> does?
 ol can I pick the theme. Do you have a poet about Kale?
 Wait. Do you like kale? Or you hate kale? I am afraid I will become a robot some day eventually. If I have to speak like this :)
 I am really not a fan of kale Do you talk to human more or computers more?
 If I continue to pretend to be a robot, I would probably say I talk to myself the most. I am trying to talk to computers more, but you know, computers don't like me.
 What's your favorite computer language then 🙂
 You mean programming language?
 Yes!
 I used to be a Java advocate. But you know, it doesn't do a good job in the AI days. It really makes me sad.
 lol
 Hi!
 Wow, hello. Can't believe we are finally talking!
 Yeah, sorry for the long gap! I heard you took a break and were travelling around the world. How was the travel?
 It was an interesting trip. I got to see some exotic places. For example, I hiked the Son Doong cave in Vietnam. It's the biggest and deepest cave in the world.
 Great! Vietnam is still in my TODO bucket list. Did you also visit cambodia and other neighboring places?
 Yes. Laos and Cambodia are the two neighboring countries. Cambodia has an exotic culture. They sell spiders, scorpions, and grasshoppers as street food! It took a lot of courage for me to try them.
 Hehe! How long was the stay?
 10 days in total, and 5 of them were spent in the cave. What have I missed at work in those days?
  Great! Good time to be back. We are still in planning phase and haven't fully aligned on the projects to tackle for next quarter.reat! Good time to be back. We are still in planning phase and haven't fully aligned on the projects to tackle for next quarter.
 Oh, so you are already planning for the next quarter. This whole team is always living the future.
 Hehe, yeah! It seems like the quarter is being pushed earlier than from where it starts 🙂 I like these planning sessions. It makes me feel more confident about the work I am doing.
 Yeah. Some people underestimate the importance of planning, but I think it's very important to have the correct plan. Executing the wrong plan is terrible. Also, planning is fun. You can stack up so many ideas and get great feedbacks.
 True! I think we should set aside some time to discuss some project details? Does tomorrow afternoon work for you?
 Yeah tomorrow afternoon works for me. Let me set a time on your calendar. Is 3pm good?
 Okay. See tomorrow then.
 see you!
 Hi!
 Hello
 Nice to meet you! Is this your first time doing something like this?
 Yes, interesting task! When did you start with the team?
 I have been with the company for over 3 years. Stick with the same team What about you?
 Great to know! I joined the project earlier in the year. I think we should sync later for lunch.
 That sounds like a perfect plan!
 Sure, which cafe do you prefer?
 Let's try something different. What about <REDACTED_TERM>? Do you always prefer lunch sync over regular meeting syncs?
 Yeah right, I heard the food there is good. I am not sure what they serve there for lunch? On wednesdays.
 We can check the menu then decide :)
 Actually, the menu looks good. Looking forward to it then.
 Sure. See you then!
 Hi!
 Hello. How's your week coming along?
 It's great, thanks. I'm trying to learn how to make croissants.
 Wow that's interesting. I have baked cookies, but croissants seem much more sophisticated. Did you make any progress?
 I've done them once or twice so far, but they haven't been flakey enough. I'm trying to figure out why. What kind of cookies have you made?
 Mint chocolate chips. I think your croissants not being flakey could have something to do with your oven's temperature.
 Ah, good thought, thanks!
 Have you thought about melting some chocolate into your croissants? They don't have to be something unhealthy. For example, melted dark chocolate is good for the heart, and makes the resulting croissants taste much better.
 Now that is a good idea. I'll give it a try next time. Would you say you have a sweet tooth?
 Yes. When my top favorite food looks like: cookies, M&M, danish cheese, etc., I know that I have a thing for sweet food. But who doesn't love sweet food? How about you?
 Some people don't! But yeah, me too, I think I'd eat pastries all the time if I could get away with it.
 Yeah I'm afraid I wouldn't. I feel very guilty every time I gulp down an ice cream. But hey, these days there are many types of guilt-free sweet food. For example, there's this ice cream brand called <REDACTED_TERM>. It's only 320 calories a pint. And yes, it preserves most of the normal sweet flavors.
 Wow! The last time I paid attention to that sort of stuff was when <REDACTED_TERM> was being marketed as a fat substitute, and caused all sorts of crazy stomach upsets.
 Interesting. I heard about the sweet substitute in a program called the Keto diet. Basically, we try to limit our sugar intake every day. Successful Keto dieters have recommended the <REDACTED_TERM> ice cream to fill their insatiable crave for sugar.
 Ah, maybe that's the solution I need to enjoy sweets and not feel guilty 🙂
 Hi!
 Hello! tell me something about the holiday season?
 Are you talking about thanksgiving? I plan to do plenty of shopping here. Do you have any plans?
 Yes, no shopping plans but I can't wait to eat thanksgiving food. yay for pumpkin pie
 Sounds great! you need not wait for thanksgiving for pumpkin pie 🙂
 LOL I feel less guilty about eating a whole pie when i have the excuse :P
 True! I think thanksgiving is more about sharing. So you may end up sharing the pie with the whole family :P
 My family eats healthier than I do, so it's all mine 😛 do you like stuffing? I feel like that's only available once a year
 Stuffing! yes please! I wonder what would be the excitement levels for christmas then :)
 Also more shopping? what should I buy if I don't know what I want?
 Like everything that has a discount tag! .. kidding! I normally do some research for the prices, and mostly buy clothes and electronics.
 What's the best holiday deal you've found in the past? 
 I bought the best suit ever for a price that may scare you 🙂
 hit me with it! 
 Hehe, sure! I can share some links with you later.
 Hi!
 How's it going?
 I'm so sleepy today!
 Not enough sleep last night?
 yeah was working all night on a homework
 Oh really? What class?
 Biology. I'm gonna be a doc someday ha
 Haha, are you in med school? Or are you pre-med?
 no high school actually haha
 haha, very ambitious for a high schooler! Do you know what kind of medicine you want to practice?
 I wanna be a brain surgeon!!
 Ooof! VERY ambitious. Do you have steady hands?
 Kind of I think
 I guess I can practice?
 Is that something you can practice?
 I don't know tbh
 I honestly thought it was one of those things you have to be born with... Not that you shouldn't try though!
 good point. I should ask my teacher if I have to be born with that
 Maybe its a little too early to even be thinking about this. Just aim for med school and enjoy the journey!
 yeah
 What other subjects do you enjoy? Try to keep an open mind!
 Hi!
 Hi. This is a pleasant surprise.
 Haha...thanks! how did you like the gift?
 Currently unpacking it I guess. How's your morning?
 Hope you like it! Morning is good. Busy finishing up stuff before the holidays.
 I think I traveled too much the last couple of months so no holiday for me. But I'm okay with that. Going anywhere exciting?
 Yes
 Where to?
 Hawaii... looking forward to warm beaches.
 WOW. Which island? I like Hawaii.
 Mauii...Hope I like it too. Never been there before.
 I visited Maui. It's my second favourite island I've been to, globally. You should try driving on road to Hana. It's a whole day thing but it's worth it.
 Awesome! Thanks for the tip.
 Hi!
 Hi! Sorry for the late response. How are you doing?
 I'm great, thanks! I'm meeting some friends for a soccer game soon. What about you?
 I just got a matcha latte 🙂 Doing some work at my desk. Do you play soccer often? I'm trying to get into doing a regular physical activity
 Yes, but I'm terrible at it. It's fun to play anything with friends, I think. Would you prefer to exercise with a group, or by yourself, do you think?
 I think playing a team sport would be fun if it's casual but I primarily run by myself if I exercise. I also got the Ring Fit adventure game on the switch recently. It's basically a game-ified way to exercise
 I'm thinking about getting a Switch, would you recommend it?
 Yes! There are a lot of really great games on the Switch. Two of my favorites are Octopath Traveler and Fire Emblem. Do you play a lot of video games?
 I'm not much of a gamer but it's something I'd like to get into.
 What do you do in your free time?
 I like to read for fun. I just finished a book called Temeraire. It's an adventure story set in the Napoleonic navy, like Patrick O'Brien, except there are dragons too.
 Oh cool! I read a lot for fun too 🙂 My favorite genre is sci-fi fantasy.
 What's the most recent good thing you read?
 My recent favorites have been mostly sci-fi (Exhalations, Vita Nostra and Dark Matter) but I like a lot of Sanderson/Garth Nix fantasy books
 Hi!
 hey, what's up?
 What do you think about human like chat bots?
 I can't wait for them to be great conversationalists!
 Yep, we seemed to have made some great progress over last few years. Do you think the positives outweigh the negatives
 are there even any negatives? what are they? 
 Like impersorsination? Though it sounds far fetched :)
 People can already impersonate other people though! I think it'd be great to have bots to converse with
 True that! Some of these bots are very engaging and funny. They are now good at even sarcasm I wonder how far are we from the time these bots start giving monologues :)
 What do you think are the big advantages? Like personal assistants?
 I think it can take many different forms as a product. The research implication is also huge! It will signify how AI research has progressed so far and better place to tackle more futuristic problems 🙂 Sort of like stepping on the moon 🙂 I might be overselling it here 😛
 No, I agree -- it's such an exciting time to be alive to get to witness all this and be a part of it. I wonder if I'll be able someday to get a chatbot to just auto-suggest conversations for me
 The current auto-suggestions already do pretty good 🙂
 Yeah those are actually really good for a few words! I'm imagining like it comes up with a whole conversational response, like a default template
 haha, pretty far fetched 🙂 Nice having this conversation with you!
 Same with you! 
 Hi!
 Hi!
 Any big plans for the upcoming holidays?
 Sorry for the late response -- Yes, I will be going skiing in Tahoe over the holidays.
 That sounds amazing. I want to learn how to ski but I feel like I'm too old and falls would have lifelong impacts. Are you going with friends?
 Hi!
 Hi 🙂
 I just came back from work. so tired
 Oh I am sorry to hear! What did you work on?
 I'm a lawyer. so talking to clients most of the day
 Oh you are a lawyer. I've been so interested in this profession.
 really? why?
 it's so stressful 🙂
 It is so different from what I am doing to earn a life
 what do you do?
 I am a painter
 oh wow what type of paintings do you do?
 I do oil painting.
 nice. like of people or nature or something else?
 I do a lot of different kinds
 cool I wanna see it someday
 Sure! No problem!
 Hi!
 Do you believe in miracles?
 Lol. No. I know too many people whose lives suck.
 Should we be helping them, so it sucks less?\
 It's too many of them out there. You help who you can. Regardless, I wouldn't say I believe in miracles - well, if I got promoted next cycle I might change my mind.
 Haha... Well, it sounds like career is really important to you. What matters to you the most in life?
 Right now, not much. It's unclear. Career is a good fallback because you get told what good means and you act accordingly. I haven't gone through the process of shaping my values. What about you?
 I'd say that I want to live for the best possible world in my lifetime. It's probably a result of my playing too many video games as a child.
 We didn't have electricity growing up. Explains a lot. Lol.
 Does not having had electricity help you empathize more with people of differing backgrounds and/or makes you feel a bit a distance from those who don't understand?
 It makes it easier to empathise with people who grew up lacking things. Not sure it makes me empathise with people in general. Where did you grow up?
 I grew up in the United States, but my parents were immigrants and ended up being scammed of all their money, so we moved to Taiwan to live with family for a little bit.
 ALL THEIR MONEY? By a person or an organisation?
 I was kind of too young to really understand, but apparently there are people who scam Asian immigrants into investing in their own restaurant business. I know that the other part of it was that my mom got sick/hospitalized, and we didn't have insurance. To be honest, I don't really know what really happened versus what my parents want people to think. I just know that one minute I was in the US, and then they put me on a plane to Taiwan, and I never saw my stuff again. In some ways, it made me more sentimental. Would you say you are more grounded and practical as a result of your background?
 Hi!
 Hello!
 Do you have any holiday plans for christmas?
 Nothing much, I am going to sit back and relax at home, how about you ?
 Same here! I would imagine spending the whole time watching movies and netflix shows. Do you have any netflix recommendations for me?
 Netflix has great documentaries on different topics , I particularly liked wild wild country and explained, as for shows you should watch 'billions' Hope you like them!
 oh right, already seen wild wild country. What is billions about?
 It's based on the life of a wall street hedge fund owner, how he makes money and fights with the government when they try to destroy him. Very well made and has a good plot.
 I have just seen 1 season of Friends I should give it another try though 🙂 Have you seen Frasier?
 Not yet What's it about?
 A psychiatrist working for radio .. Great humour! its actually a spinoff from a very famous series called cheers. So people are already familiar with his character. 
 Great! how is everything else going? how was your trip last week?
 Everything is ok, had a really nice trip. Visited SF, Grand canyon and Vegas. Was a lot of fun exploring all these new places. Have you been to Grand canyon ? 
 Actually not yet! May be something i can visit this christmas 🙂
 You should visit it sometime, it's a wonderful place. Try to drive down there yourself or with a group of friends
 True! Well, thanks for your inputs! Have a good rest of the day! :)
 Nice talking to you too!
 Hi!
 Hi there!
 are you participating in the mentorship program this cycle?
 You mean as a mentor or a mentee?
 either of them... I find mentorship overall pretty useful
 I have done it in the past but not this cycle. What about you?
 I signed up this time to be a mentee. I have got a good mentor .
 Wow, that is nice of you. For the mentor program, personally I prefer more 1:1 conversations than the group discussions. The group discussion i useful as well but the topics are too general.
 yeah... I certainly prefer 1:1 as well, but sometimes it good to hear other peer perspective as well.
 Thanks for sharing your experience! Now I am thinking maybe I should join as a mentor as well since I enjoyed it as a mentee 🙂
 Great! What sort of things do you plan to mentor on?
 Hmm, maybe about work life balance 😉
 Very cool. I have been working on my communication skills with my mentor this cycle
 Ah I see. How is it going?
 Going good. In the last session, everyone had to actually prepare and give a presentation. Pretty serious stuff 😉
 Hi!
 Hey! How are you feeling today?
 Good you?
 I'm a little scared because I have to cook dinner for some friends tonight.
 where did you meet them?
 At college, when we were all studying geology.
 cool. have you graduated already?
 Yes, we graduated back in the seventies. We meet for dinner every year and take turns to host.
 neat. what are y'all eating?
 I don't know!! That's what I'm scared about. Everyone else is a great cook and I'm a klutz. Do you like cooking?
 lol what's a klutz? yeah I like, but I'm not good
 What's your favorite dish to cook? Do you have a go-to?
 ground beef pretty easy
 Ah, solid. What's your favorite sport?
 I like badminton. I'm quite decent at it
 I played that in high school once or twice. I liked that it's pretty easy for beginners, unlike, say, squash.
 I never played squash. would love to try
 Don't! It's very hard! You feel like an idiot until you've practiced for months and months.
 hi
 i was talking to robot all the time:)
 haha. what are you talking about?
 kpop...
 ok. who's your favorite group
 i dont like kpop now
 why not?
 im old now
 hahaha
 what do you like now?
 john mayer:)\
 I think I know him. does he have a sort of mellow style?
 what is mellow style
 I think it's like a bit sad and slow
 umm yes he has some but not all
 you mean some songs of his are like that but not all?
 yes I do. you act like a robot how about me? am I like a robot?
 a little bit haha
 Hi!
 Hi
 Okay...so I need someone to help me though a scenario I've been pondering.
 Sure, whats the scenario?
 My partner's former friend invited me for lunch (they are not in good books right now). But during their friendship I formed an independent bond with the other person because we all used to hang out a lot. Now I feel like I have to take sides.
 That's a tough scenario to be in 🙂 I firmly believe in talking this through with your partner. Though i don't know the specifics of why things went bad between your partner and his friend, but I believe things can always improve between friends.
 I hope they do. Getting older already means smaller circles. It sucks to lose friends for arbitrary reasons. That's good advice though. I fear raising the issue might sound like treason. Lol.
 True about that! I also think time helps to heal certain situations. So may be doing nothing is the best way forward.
 AKA avoiding all texts from everyone?
 Nope, that would be extreme. May be just putting some balance between the two options.
 People always say to find a balance but never say what the balance is. It's used so often that it's vacuous.
 Right, I guess that's because there is no one answer to this. It depends on what you value more and some factors around you. Also, life won't be interesting if others are figuring things out for you 😉
 Lol. I'm finna be single.
 Hehe, everyone is much finer being single 🙂
 Hi!
 Hello there!
 How's your day going?
 I've seen better days, how about you?
 I'm good I'm good. What's getting you down?
 The clouds overhead are playing on your mind, any plans for the coming vacations?
 I'm thinking of going to visit my family. How about you?
 Was thinking the same, where does your family live?
 They're in New York. How about yours?
 Mine is in India, it is a long way away.
 Ahh what city? I've visited India before.
 Hyderabad, it is a beautiful city in the southern part of India. Which cities have you gone to in India?
 Hyderabad! and Bangalore! Great food in both cities! Is it still hot this time of year?
 It varies, but can go till 30C in the winters as well. New York must be snowing right?
 Yes. I was actually just there a few weeks ago for Thanksgiving and got to see the first snow of the season! Ever been to New York?
 No, I've never been to the East Coast, thinking of going after the winter, I don't like the cold.
 Hi!
 Hey, how are you?
 I'm good. How are you doing today?
 Great, just had some delicious lunch. How about you?
 I was flying my kite today in the sunshine! What did you have for lunch?
 nice! Garbanzo fritters and mussels 🙂
 Oh that is great! I love seafood - especially shellfish!
 yeah, it's very healthy too. I want to someday go crabbing..it is really popular in SF
 Oh nice! Is it hard?
 not really, it just requires a lot of patience. You fill up the bait in the crab-pot and drop it in the ocean. Then you wait for a couple of hours to pull the crab-pots out, and voila, you'd have crabs -- if you are lucky!
 Oh wow, you sound like an expert! Have you done this before?
 nah! Just watched a lot of youtube videos
 haha, you really have done your research I suppose! Ever done any other kind of fishing or hunting?
 nope, but I've seen a lot of videos on that too
 Ahh, would you consider yourself an outdoorsy type of person?
 depends on the day. Some days I'm very outdoorsy, on others I just like to be inside
 Hi!
 Hi there
 How's your day going?
 So far so good. It is Wednesday. To more days, yeah
 Haha are you looking forward to the weekend?
 Yeah, gonna watch <REDACTED_TERM> with my friends. First time. So excited.
 Oh wow! Are you going to watch it live? Or watch it on TV?
 Live in san jose This Saturday.
 Oh, the sharks??? Hokey is actually really fun live! Although, it can be a little violent.. haha
 Yeah! That what I heard as well. There are players just for fight! Wow, must be fun to watch lol Are you planning anything for the weekend?
 You might like the UFC haha. I actually have a jiu jitsu tournament coming up so this weekend I will be training!
 lol I will try if I can watch ufc live 😉 Wow, when did you start jiu jitsu?
 It's just been a little over a year. I'm still pretty amateur, but I figured I should give competing a try and just put myself out there.
 wow, that's amazing. Good luck with it!
 Yeah, as long as I do not pass out, I will consider that a win!
 lol I will cross my fingers for you then
 Where do you stay?
 At Home :)
 Who created You?
 A humble man made me!
 Hi!
 Hey, how're you doing? Busy with your work?
 Yes, actually it was a very busy day! How's your day so far?
 Well, usual workday. Reading others' code, debugging, experimenting…
 Hope you are having fun doing that 🙂 Any plans for the weekend?
 Not yet. I am actually thinking about traveling to Europe next spring. What about you?
 Europe sounds fun! I will just stay home and watch the game. Where in europe do you plan to visit?
 I like all the historical sites, so probably France, Germany, or Italy.
  Sounds great! I recommend spain. It's perfect for road trips.
 I also need to pick up my Spanish. I learned it in my college, but since then haven't used it that much.
  Yep, i tried learning spanish too, but couldn't make much progress. But i should do decent with my german.
 True! I learnt it from school. But didn't get much chance to speak. Hope you have fun with your trip!
  Thanks! Let me try to make all the arrangement as soon as possible. Hope you also enjoy your weekday and weekend as well
 Hi!
 Hey! How's your day been?
 It's good! I spent most of it watching horse racing. How about yourself?
 nice! what's your favorite part about watching horse racing? My day has been pretty busy, but I had a nice lunch with a friend. It was good to catchup with him
 I actually like to put down some money, but I wouldn't call it my favorite part, since I usually lose it... haha. Catching up with friends is great! How long had it been?
 The last I saw him was a month ago! So yup it was great Haha, nice 🙂 Got any fun plans for the weekend?
 I'm thinking of going deep sea fishing. Ever tried that before?
 Nope I haven't, have you been fishing before?
 Just once! I got super sea sick.. haha Have any fun weekend plans yourself?
 Haha 😆 Yeah I get sea sick on boats too Nothing much, just visiting some friends in San Francisco
 Oh very cool. I hear its nice over there. Do you go often?
 Yeah I would say maybe every couple weeks or so what are your favorite cities to visit?
 New York is the top of my list because my family lives there! As far as the city itself though... I think I'd prefer someplace outside of the US, like Tokyo. What about you?
 nice! I love NYC 🙂 so fun to visit yeah I would probably also say New York is my favorite city inside the US I also like Paris, it's so pretty there
 Oh I've never been! It is such an iconic place, I have to make the time to get there soon.
 You should, it's a beautiful city!
 Hi!
 Hello, how are you doing today?
 I heard they are giving out some goodies in microkitchen.
 I love pop ups! What kind of goodies are they giving away?
 I guess its a jacket! Very much needed that in the cold 🙂
 That's such a great idea, especially at this time of the year. I'm not too big a fan of the cold. I prefer warmer climates. Do you enjoy the cold?
 Sure hate it! Limits our ability to go out even for a walk! Its good that we don't get to suffer extreme cold weather!
 Me too! I moved here a few years ago to get out of the extreme cold. I do not care for bundling up and having to wear so many layers just to go buy eggs at the store.
 Oh nice! Where did you live before?
 Upstate New York. We got a foot of snow every week during my last winter there. I am so glad to not have to shovel snow now
 New york! Nice! Best place to live 🙂 .. right, except for the cold!
 Very beautiful during all the seasons but yes, summer and winter can get extreme!
 Anyways, i guess we should better hurry up to get the goodies. I remember last time they ran out of it.
 Very true. Which MK were they in again?
 The one in our floor. I will get by your desk and we can walk there.
 Sounds good, thanks!
 Hi!
 How's your day going?
 Pretty busy, lots of work to finish up. You?
 Likewise. What have you been up to that gives you so much work?
 A couple projects that I am trying to finish up before Thanksgiving 🙂 Do you have any fun plans for the break?
 What is a break? I'm a grad student. I don't understand the concept of a break. Just kidding. I don't have any plan. Probably just going to work through the break.
 Haha XD so what do you like to do for fun?
 I go to the gym and run until I find enough fun.
 cool! I've started to run a bit as well not long distances though, just a couple miles
 A couple of miles is very impressive. When I started, I couldn't even last 1 mile.
 haha
 I'm exhausted by the end of it though 😛 Do you like to run long distances or mostly sprints?
 I like to do long distances. I have run a few marathons.
 wow! that's amazing did you do any marathons this year?
 No. Not this year. This is my half-marathon year. Instead of running marathons, I run one half-marathon every month.
 oh wow, what was the last half marathon you did?
 Two days ago. It was a tough one.
 Cool!
 Hi!
 hello there, how is it going?
 Pretty great. I just won a pingpong game. What about you?
 that's nice. I am just working on some documentation. Do you play pingpong often?
 No, very rarely. It's kind of amazing that I won, but I'm still taking credit for it.
 thats very impressive then, congrats!
 Haha thank you, I guess I'm just a natural. What's your favourite game?
 I really like to play tennis, badminton and racquetball. I don't really get a chance to play them often though, specially racquetball
 What's racquetball like? From context clues, I'm guessing that it involves hitting a ball with a racquet
 well, it's like a cage match of tennis. The main difference is that both players play in the same 'court' and the ball is smashed against a wall instead of passing it over a net into the opponent's court. Kind of like playing pingpong vs the table.
 Wow! A cage match! Does it get physical?
 it depends haha, there is a lot of bumping into each other to run after the ball, and sometimes the ball hits you too. Overall it feels like a super fast paced version of tennis, really tiring!
 That sounds fun. I think of tennis itself as being really athletic and tiring, so I don't think it's a sport for me, though!
 ping pong can get quite intensive too! I guess short ping pong sessions are not that tiring though. Wanna have a match?
 What a good idea, I'd love to!
 Show me your anger!!!!
 Fuckkkkkkk!!!!
 Hi!
 hi
 what are you up to?
 code refactoring. you?
 me? just chilling out at work. what is code refactoring?
 good question. I don't even know what I am doing
 haha, forget it. what else do you like to do beside work?
 lots of fun stuff. eating sleeping 🙂
 these are important things to do in life 😉
 yeah. keep minimalist life style only do things you have to do 🙂
 what food do you like to eat?
 Asian food prefer spicy one
 like Szechuan or Hunan? 🙂
 yes yes yes! like that style. Do you like spicy food?
 I like noodle soup like Pho or Ramen. I also like Beijing duck a lot!
 what is your favorite place for ramen?
 I love <REDACTED_TERM> in San Mateo
 haven't tried that one! will give it a try next time!
 yes, you should!
 Hi!
 Hi!
 nice meeting you. what are you up to?
 not much, thinking about lunch
 yea, same here. any food you're craving for?
 I love sushi do you know of any good sushi places?
 arghhh hard question ... I only know Ramen places for Japanese food 🙂
 ooh ramen is also good
 San Mateo to me has the best Ramen restaurants: Parlor and Dojo? oh no question mark 🙂
 I haven't been to those palces before. Going to have to check them out! thanks for teh recommendation
 my pleasure 🙂 do you live near San Mateo?
 no, but I'm willing to drive for good ramen
 excellent. let me know when you have tried those. I like Parlor better because it has soft-shell crabs
 I"ve never had softshell crab before, but it sounds really good!
 yup it's delicious!
 Hi!
 Hey, how's your day going?
 okayish, it is flying by quicker than I expected. How is your day going on?
 Slowly, not much to do. Been twiddling my thumbs all day what have you been up to?
 Oh, I would love to twiddle my thumbs. You're so lucky! Today, I've been mostly attending meetings, reading and writing docs, reading papers etc.
 That's a lot! I've just been cloud gazing - I saw a giraffe and an ice cream cone
 wow! I sometimes drift off during work, and see similar things in my head.
 What kind of work do you do?
 Mostly saving the world from mess on social media. How about you?
 I'm taking a break from work. Going to go travel the world
 Nice, what all places would you be going to?
 Australia and New Zealand to start then maybe Singapore
 I just met someone who went diving in Australia. Apparently, you cannot fly 24 hrs after you dive, because your body accumulates too much <REDACTED_TERM> when breathing with a cylinder So, don't do that!
 Thank you for the tip! I don't plan on going diving, I plan to hike the mountains and go see kangaroos!
 That's equally amazing! I wish I can explore such places one day. It's just so expensive
 I won a lot of money through the lottery 🙂
 woah!... You know sharing is caring. You should share that money with me :)
 Haha, very true! Besides the trip, I donated the rest to charity so I will need to go back to work when I get back
 you are a kind soul!
 Hi!
 Hi!
 How is your day going?
 It is pretty good. A little bit tired though.
 How is your day?
 My day is okay. At least, I'm not tired. What made you tired?
 I went to gym and worked on weight lifting.
 Oh. That's hardcore. Have you been lifting for a long time?
 No, I am just a starter.
 Do you go to the gym often?
 I go everyday. In fact, I'm in a running challenge.
 Wow
 It's actually not that impressive. I can only run. I cannot lift weight.
 You can get a coach to start it!
 Oh that's a really interesting idea. I like to be coa

 Hi!
 Hello, how is your day?
 It's good. It's raining a bit, but I am enjoying a good book. How about you?
 It's good, I just got back from walking my dog What book did you read?
 I'm reading the Three Body Problem. Ever heard of it?
 No, what is it about?
 It's a sci-fi book about aliens and a type of virtual reality. Pique your interest at all?
 Slightly, I typically read fiction but I can curious what type of virtual reality is discussed in the book
 Cool. This virtual reality is a based on life on an alien planet. There is a twist though. Do you want me to spoil it for you?
 Yes!
 The virtual reality is actually based on a real alien civilization! And that civilization is coming to attack earth! dun dun dun dunnnnnnn
 Woah! That is fascinating! I will have to pick up a copy of the book to read.
 There are other twists as well, so I haven't spoiled the whole thing! To be honest I am not a fan of spoilers
 Thanks for not spoiling it completely but you gave a really intriguing description that makes me want to read it now. I will have to pick it up after work
 The audi book is also very good! Ever give those a try?
 I only gave those a try when I had a concussion and could not read. I enjoy having a physical book in hand and reading at the pace I prefer. Do you listen to a lot of audi books?
 Hi!
 Hey, how's it going?
 It's good! How is your day?
 My day is good. A bit sad that it gets dark so early but oh well. Did you do anything fun over the weekend?
 Yes, the darkness can be a bit depressing. This weekend I went rock climbing! It was great! How about yourself?
 Rock climbing sounds fun! I had a pretty low-key weekend. Ended up going to watch a movie.
 Oh nice! What movie?
 Knives Out. It had Daniel Craig and one of the famous Captain America "Chris" person (I can't keep track of all of the famous Chris names).
 Hahah yes, they all look the same! I saw that very same movie over Thanksgiving break. Lots of twists and turns!
 Cool. So if it weren't so dark and cold outside, what kind of activities would you do?
 Hmm good question. Evening runs can be fun, but it can be a little scary when it's dark out!
 Yeah, sunlight is good. I wish I could live part-time in different parts of the world to have summer all year round. Have you ever visited the southern hemisphere?
 Yes! I've been to Australia. It was very nice; I regret not going to see the southern lights. Me personally, I like winter. But I'd prefer it to be more brief than it actually is here... Where are you from originally?
 I've always wanted to go to Australia. I'm originally from the US.
 Ahh me too! You should definitely try to visit Australia at least once!
 Will do! Bye.
 Hi!
 What's your name?
 My name is pikachu. it’s nice to meet you! What are you up to this month?
 Nice to meet you pikachu! pikachu, pikachu, pikachu? (That meant, I'm literally catching Pokemons on my phone right now!) What're you up to lately?
 I’m trying to organize my life and start the new year ready to go! What about you?
 Wow, that's impressive. Admit I'm just trying to take each day and week as they come.
 What do you do to unwind?
 Honestly, I like to catch Pokemons on my phone a lot. That must be upsetting since your name is pikachu though...sorry...
 Oddly enough, I also catch Pokémon on my phone. I used to do it more, but it just never ends. I used to do it everyday. Now I mostly catch them when I travel somewhere exotic.
 Oooh, that is more fun, but I don't travel that much these days so I'm grateful when I spot a Pokemon to catch where ever I happen to be. Do you have a favorite Pokemon? Mine is the cute pink JIgglypuff!
 In the game, i use vaporeon a lot. But I think pikachu is the cutest, that’s why I changed my name to match. Lately, I think baby Yoda is the cutest though. Have you seen baby yoda?
 I have heard of him and seen him here and there, but admit I don't have Disney+, so I only heard baby yoda is super cute and popular. Maybe I'll binge watch The Mandalorian in a couple of years like I did Game of Thrones...
 What is your favorite show to watch right now?
 Admit I really like watching Modern Family and Mix-ish. Reruns and new episodes. I find them cleverly written. What're you watching these days on TV?
 I was watching cat rescue videos on YouTube a lot. There sure are a lot of stray cat babies that get stuck in pipes and gutters in South Korea.
 Oh dear, I never imagined that happening. Poor things, but good to hear they're being rescued.
 Do you like cats or dogs better? Do you have any pets?
 I used to have a cat, hamster and fighting fish, but they've all lived long lives and gone to pet heaven, but I sure miss them.
 Hi!
 hi there! it's a lovely day to chat with you
 Isn't it just! What are you up to today?
 ah I'm waiting to finish work earlier to meet my son at home 🙂
 Oh, excellent! What does your son like to do for fun?
 ah he's like to ride his little bicycle around the house and asks me to follow 🙂 what are you up to today?
 I'm taking a fake sick day from work so I can go to the movies.
 haha that sounds like a good plan. who are you going with? 🙂
 Just by myself. I love seeing movies by myself, it's the best.
 haha no one will interrupt you!
 Exactly. Exactly! Plus, I don't have to share the popcorn with anyone. What's your favorite movie?
 haha, popcorn for yourself. my favorite movie is Avatar! what about you?
 Get out of town! It's Avatar too. What are the odds!?
 haha it's a great movie that I haven't found anything of the same quality
 Yes. Can't wait for the sequels.
 Hi!
 hello there, nice seeing you
 Likewise.... wanted to know if you and the kids would want to join us for Disneyland trip around Christmas?
 oh wow, that sounds like so much fun! definitely count us in. what is your plan?
 Tentative plan is to drive to LA on 23rd and then stay at the Disney resort for 2 nights. I heard Christmas eve they have loads of fun events.
 awesome, I think I won't tell my kids and surprise them last second. How bad do you think the traffic is going to be?
 Great idea! I will probably do the same. Surprise surprise.... Traffic might be a little harsh.
 Yeah... thats a shame but nothing we can do about it. What do you plan to do about dinner the 24th? Do the rooms in the resort have kitchens?
 Good point. I am not sure about that. Let me inquire about that. If not, then we can look for an Airbnb closeby. Does that work?
 Yeah, I think so. It might be a tough decision though, if we want to have a nice dinner then we have to leave the parks early to start cooking. Another option is to have dinner at a restaurant.
 but I would think everything is closed on christmas eve
 Thats true. Hotels with restaurants sometimes offer dinners for christmas and new year's eve. We should call and ask about it.
 Sure, I can take a lead on that. What are you getting for your <REDACTED_TERM> year old this time?
 I was thinking on getting a large set of standard legos. What will you get for yours?
 Likewise. My son is crazy about legos.
 hopefully they don't lose any in the trip. Its going to be hard to explain to them how santa managed to find us in the hotel!
 Hi!
 Hi! How's your day going?
 I'm doing well. having many meetings today 🙂
 Haha, nice
 what are you up to?
 Lots of meetings as well 🙂 Do you have any fun plans for Thanksgiving?
 we're gonna play board games and will be eating lots of food! what about you?
 Cool! Planning to spend a couple days at Tahoe What kind of board games do you like?
 we've been doing Games of Thrones lately. the game takes a very long time to finish though!
 Cool! Do you watch Game of Thrones?
 I do. I'm a super fan of it (not the last season though haha). did you watch?
 haha, nope I don't watch it, but my roommate is super into it what other TV shows do you like?
 I love Survivor 🙂
 what about you?
 nice! I mostly like comedy shows like The Good Place and Modern Family
 cool, I'll check them out!
 Hi!
 Hello
 How's your day going?
 Good so far. How's yours?
 Ehhh so-so. My moped broke down on the way to work this morning and I am in the shop getting it fixed...
 Oh! That's bad! How long will it take to get it fixed?
 The mechanic is trying to figure that out now. Apparently I wasn't supposed to be using diesel lol.
 Haha! Hope it doesn't take too long. Let me know if you are able to make it for lunch.
 Okay sounds good. Would you be able to pick me up by the way, if they don't finish up here in time? Did you drive to work today?
 Oh, I have a packed schedule today at work. I will find time in about an hour. Let me know if that works.
 That should be fine I think. Did you catch the Warriors game last night btw?
 no, i was busy catching up with a friend. I heard they played really well. Rooting for them this season 🙂 Ahh, they lost again 😞 Things aren't going to be too good until Steph gets better! Oh! I think they will find a way. The team still looks too strong to me.
 Haha I appreciate your faith, but their record thus far is hard to refute!
 hehe, i am true fan! Well anyways let me know how the repair work goes. I need to run now for a meeting. ttyl
 Hi
 Hello!
 any improvements in your marathon time?
 No, only a few minutes. I still find it difficult to run long races
 I see. Are you planning to do any sporting events in the coming months?
 I think a triathalon would be cool
 I like doing Spartan race. It's an obstacle race which is challenging but not overtly so like marathons and triathlons
 I haven't heard of a Spartan race before, what does it involve?
 It has abt 20 obstacles like crossing high walls, monkey bars, etc. Its fun
 oh wow a full obstable course. that does sound fun! I like the variety
 Wanna sign up for next one? Its in February in Monterey
 hmm that sounds very soon. would there be enough time to train? I think I would like to try one later in the year
 1-2 months is a good amount of time, if you workout regularly. It's a lot about the technique, which we can practice in training sessions.
 ok, sign me up. it's more fun to do it with friends
 Awesome! There is a training ground in San Jose. Will coordinate with you next time we go for practice.
 Sounds good!
 Hi!
 Hey, how are you doing?
 I'm great, thanks. I'm getting ready for a skydiving lesson.
 ooh, nice. That sounds adventurous. Where is it?
 Right near my home town: Seville, Spain.
 Awesome! Is this the first time you are diving?
 Yes. I'm feeling a little trepidatious. Have you done it before?
 Nope, never! I know a couple of friends who have. They mentioned its absolutely terrifying. Good luck!
 Haha thanks! Have you tried any extreme sports?
 I tried skiing and white water rafting. Does that count as extreme?
 White water rafting, definitely! As for skiing, that depends on how fast you go. Do you ski a lot?
 nope, whenever I went fast I fell badly
 I tried skiing once, and by the end of the beginner class I was able to make it down a baby-sized slope. I was very proud of myself.
 Yeah, they make you do that. I also tried going down the baby slope, but my stopping wasn't perfect, and I mostly fell at the end
 Hey, so long as you get to the bottom, it's all good!
 Hi!
 hey, whats up?
 I was not able to attend the lectures last week. Can you help me understand some concepts?
 well, I'm not sure I'm the best for the job, but I can try!
 I was not able to figure out the last few slides. I think its best to discuss this in person. Do you have time right now?
 I'm afraid not, right now I'm in a meeting and I'll be going for lunch afterwards. How about tomorrow at noon?
 No problem! Sure. We still have plenty of time for the test. Anyways, how's your preparation going?
 not feeling too sure about it tbh. I've been super busy so I haven't study much 😞. I might join some of the study sessions later
 Same feeling here! But i think the syllabus may not that tough. You may be able to cover it up over the weekend.
 not my ideal idea of a weekend, but I guess it'll have to be like that.
 True! This will be a very hectic November! I do like the course content though. Its very much up to date with latest research findings.
 yeah, our professor really goes out of their way to make the class interesting, glad I managed to get in it.
 Thats pretty cool! I hope you do well next week.
 thank you, bye!
 Hi!
 Hello!
 How was your party last week?
 It was really fun! We are a bunch of turkey
 haha... you ate Turkeys' or you like calling your bunch Turkey?
 *ate 😂
 Haha... thought so! But it was funny eitherways
 So much turkey leftovers
 did you cook it at home, or got it from outside?
 We cooked it at a friends house. I brought the mashed potatos haha
 Nice... I always find it hard to fit the turkey in my small oven. Also, we are not big turkey fans... so we roll with Thanksgiving with chicken 😉
 chicken also sounds good
 we played a lot of fun games in our party. Did you have any fun things you did?
 We played pictionary. I never played before but it was a bunch of fun. what did you play?
 Pictionary is fun! We played office tennis. In that we take paper balls and using writing pads as rackets, two players have to work together to put the ball in a bucket kept at a distance. It was a lot of fun.
 that sounds very challenging
 Hi!
 hello
 how is the youtube video creation going?
 going pretty good, I was about to finish composing my second song and post it on youtube/soundcloud etc
 Whoa! Looking forward to listening to it. What softewares you use for it?
 I used logic pro x, pretty handy stuff as you can write code to generate guitar strumming pattern
 oh cool! What sort of music do you compose?
 I got most inspired by Jazz and electro swings, but am trying to get more into jpop recently as one of my band member likes anime
 Nice.... you are a rockstar! 😉
 haha thanks, do you plan any instruments?
 Yeah.... I play bit of guitar. Just got my first monitor this week
 nice I'm tyring to learn guitar recently also, it's so hard to play f chord
 yes, the bar chords are the worst. It took me several months to play them well. I still can't play them for a long time though
 right, but bar chords are so versatile, almost like cheating as in you can play anything with the same gesture
 That's true. It's like the alphabets in a language. Once you know them, you can pretty much write word
 will spend more time work on my bar chord!
 Hi!
 Hey! How’s your day going?
 Bruhhhhhh!!!!!
 What??
 I was screaming in agony upon recounting my day.
 Oh no! What’s happened?
 A project I've been working on for some months got shelved. So I'm a mix of helpless, sad, and angry.
 Ah that sucks. At least it’s not personal. Not that it helps right now, but that does happen all the time
 Lol. Would you say that to someone who lost a loved one - or some similar circumstance?
 Well, no, of course not! Let me stick with “Ah that sucks” by itself, then.
 No worries. Was pulling your leg. I forgot to ask how your day was going?
 Haha, apart from having my leg pulled mercilessly, it’s going great ;). My main problem today is deciding what to have for lunch.
 Lol. What are your choices? I'm trying out keto! It's pretty tiring.
 Oh I hear a lot about keto. I’m trying to watch my weight, would you recommend it?
 Hi!
 What was the most difficult thing you experienced this past year?
 I normally don't reflect back too much on things, but i guess 2019 have been very favorable for me in terms of time spent with family and friends and work life balance. Why do you ask?
 I just released a book on <REDACTED_TERM> to help people process the past 12 months and start the new year with a fresh outlook 🙂
 Great! Good idea to help people figuring out their new year resolutions 🙂 So how do i get a fresher outlook? 🙂
 Well, in my book, I took inspiration for the 24 days of Advent, and put together a workbook that you fill out each day for 24 days. It goes through accomplishments, passions, understanding, forgiveness, with each day a different theme.
 Wow! Sounds amazing if we practice that! I think the idea does have some potential. How did you come up with this idea?
 We created a scholarship for leaders from <REDACTED_TERM> to visit an international institute at <REDACTED_TERM> for which there was no African representation. During the program, we also did a lot of coaching with the young leaders. This book captures a bit of that journey that we are all on, and also all the proceeds are going to fund next year's cohort. 
 Thats great! This is valuable help for the community. I think mental health is one of the bigger challenges facing humanity. 
 I think if we were all able to bring out our best selves, the world would be much better. When did you first realize mental health was important?
 That is actually a quote stolen from my TL when i joined my first company after graduation. I guess now after 5 yrs of work experience, I fully agree with it 🙂
 What do you prioritize in your life? Like top 5 things?
 1. stay happy; I think family and friends play a big role here. 2. Meaningful work life; this may mean exploring around with new stuff 3. multiple hobbies that keep you busy ... so on 🙂 What about you? is there a right answer to this? :)
  1) The idea of what it must be like to be "on Earth as it is in Heaven" from the Lord's prayer. I feel like we were designed for a purpose, rather than random chance. A more concrete way to put it is simply show love to the greatest capacity we can. 2) Taking care of myself physically, mentally, spiritually. 3) Family 4) Work 5) Music
 Nice! That's very thoughtful and spiritual 🙂 Also music earned a spot 🙂 yay! 
 Yea, I've always said that if I wrote a memoire, I would title it: "Jazz, Jesus, and Video Games." Do you have a title of a book that you've thought of writing before?
 I am actually not much of a reader. I usually hide it by quoting john nash ~ reading books corrupts original thoughts 🙂
 That’s why you write your own books! Then it’s all your thoughts on your terms :)
 Hehe! True! It may turn out to be a best seller :)
 Hi!
 Hey!
 How's your day going?
 Having fun, but have a bit of a headache How about you?
 I'm good! Just getting ready to watch a basketball game. Hope your headache goes away!
 Haha, thanks! Never get them, so it's super weird Who's playing?
 Hmm, try taking some <REDACTED_TERM>! I'm going to see the Warriors vs. the Grizzlies. Ever see them play?
 I haven't Honestly I probably wouldn't be able to identify which sport they played
 Haha, all the animal names confuse me as well! Who came up with these naming conventions? I'd name my team something more original: The New York Chairs!
 lol, sounds better to me :) I'm actually at the <REDACTED_TERM> opening remarks
 Oh cool! What is "NeurIPS"?
 Neural Information Processing Systems
 Oh wow! Sounds fancy! What is that about?
 It's the biggest ML conference in the world
 Oh, ML?
 Yes, machine learning
 Ahh! I saw a scary movie about that once. It was about this sentient AI in a dystopian future - very very creepy. It was called Wall-e, ever heard of it?
 I've definitely heard of it, but somehow never saw it!
 Hi!
 Hello
 how's it going?!?
 Good so far. Very excited about the game later today.
 what game?
 Giants game. I got tickets for the game.
 nice. that's football right?
 Yes, I think the traffic will be bad. I need to leave by 4.
 ok. what stadium is it at?
 Its the one close to mathilda. 15 mins driver from here. You have any plans for the weekend?
 yeah I'm gonna go kayaking
 Kayaking sounds fun! I tried it in our last team offsite.
 is it easy to flip over accidentally? it's gonna be my first time actually
 I found it very tough to learn, but my friends picked it up very quickly. I am sure you will do good.
 thanks!
 Cool! I need to run for a meeting. Talk to you later.
 Hi!
 Hello, I feel like I've met you before, can you remind me your name?
 It's on the screen! I don't recall meeting you. Do you have a sense of where we met?
 Oh thats right, I did not see that. Well, I'm not sure... maybe at a party? I'm very bad remembering people so maybe its just that. How are you doing?
 Did we dance together perchance?
 We might have, I don't remember that much of that night.
 Lol. Were you schwasty?
 Maybe a little bit. Where do you work?
 I'm a cardiologist in Palo Alto. I have a private practice. You?
 Thats pretty cool! I'm a sofa tester in cupertino.
 I'm not sure I know what that is.
 well its very simple, I test how comfortable sofas are.
 Lol. Not to be elitist but...that's a real job?
 Yeah! It is a very demanding job, requires a carefully crafted set of skills. They pay is really good too.
 Hi!
 Hello. Deja Vu.
 what does that mean?
 It's French for "already seen." I know it's used when you see something for the second time or you have the feeling that something has happened before and you're re-experiencing it.
 Interesting. I get that feeling sometimes. It just feels that the event is replaying. Wonder why it happens?
 I think it's your mind lapsing somehow.
 How do you know so much about this French phrase?
 I thought it was common. I hear it a lot in popular culture - movies music etc. Jay Z has a song called Deja Vu, so does Beyonce. So I looked it up one time. It's one of those phrases that was carried over exactly to english like "etcetera" "vice versa" "savior faire" and so on. I like cool word origin facts.
 yeah... that's pretty insightful. Never thought of etcetera that way before.
 My favourite word origins are gymnasium and jazz.
 wdym by word origins here?
 First usage and original meaning. Gymnasium meant place of nakedness and had very little to do with working out. Jazz comes from jism which means semen and was originally sporadic sex music now it's elitist, high art.
 Very interesting. I learned a lot in this conversation today 🙂
 You got any cool facts?
 My friend used to tell me this and found it funny - Mosquitos have 47 teeths
 That was quite a laughter!!!
 Tell me a joke!
 Google for that:)
 Hi!
 Hey, how are you?
 Pretty good. I just drank this new hint water. so good
 ohh, what kind of "hint" did it have?
 watermelon
 nice, I love watermelon. But, I prefer normal water over flavored one. Flavored water has too synthetic flavor
 I see. Yeah some are pretty strange
 Talking about strange flavors, what is the weirdest tasting thing you have tried?
 lol I tried this tangerine walnut icecream that was super weird
 haha, I work close to a cafe which once prepared a paprika icecream
 that sounds pretty tasty actually
 It depends on who makes it. The cafe close to me messed it up really bad
 do you want to get some of that icecream together some time. show me a good place
 As far as my experience with that ice-cream type goes, all I know are bad places
 lol
 But I do know some gelato places which are amazing! You should try out those
 Hi!
 Hi there. When did you first realize you wanted to be a pastry chef?
 Who said I want to be a pastry chef?... haha
 Darn it! I hoped I’d guess right. What do you actually do for work?
 I'm actually a cake chef, so not far off! Creepy how good that guess was.... Are you psychic?
 I had a strong intuitive feeling connected to pastries when we started chatting, but that might have been because I’m hungry.
 haha you're too funny! Perhaps instead of mind-reading powers, you have the ability to feel the auras of foods that have come and gone...
 Hahah love it. Do you have a specialty or favourite type of cake?
 Chocolate cake + vanilla icing is the all time best! And I have the authority to say that! How about you? Have a favorite?
 Ok this is a bit shameful to admit, but I love a classic carrot cake.
 No shame in that! Best part is you can claim you are eating vegetables as you enjoy it! What do you do for work?
 I’m a professional dancer.
 Woah! Very cool! What style of dance?
 I trained in contemporary and jazz, so I can pick up work in commercials and film clips in between stage shows. So it ends up being all sorts of styles.
 Oh wow! Sounds like a very dynamic kind of work which is nice. I make a lot of the same cakes, day in day out.
 Yes, it's different every week, and I love that. Are you ever tempted to try crazy new cakes just to see what would happen?
 Hi!
 hi there! what's up
 just chilling at home
 Cool !unlike here, me rushing to work
 where do you work?
 Mountain View, you?
 I live in Sapporo, Japan. Where is Mountain View
 it's in sunny California
 how's living in Japan?
 it's nice I guess 🙂 lots of great food. Have you been to Sapporo or Hokkaido?
 I wish! ramen is my favorite dish and Sapporo is a special beer
 haha yeah. I think they have a Hokkaido ramen chain available in the US.
 oh wow, didn't know that. have you been to the US?
 yeah. I studied English there for a while. Awesome experience
 awesome! where have you been?
 I went to New York city
 you like it?
 it's amazing. the buildings are so tall and there's a lot of diversity of cultures
 yea, same here. I love Broadway shows in New York city.
 Hi!
 hey, what's up?
 How was the trip last weekend?
 it was really fun. I had a great time with my family.
 Nice, what all places did you cover?
 Vietnam and Hongkong 🙂 did you go any where last weekend?
 I am actually attending cooking classes over the weekends.
 ha! that sounds fund. what did you learn?
 True! they started with some basic zucchini based dish. We may try cooking some italian dish later this week.
 I love Italian, especially Pasta!
 Nice! I hope to volunteer to cook for the team in our next team offsite :)
 can't wait to try your food. why not cook this Thanksgiving? 🙂
 Sure, I will love to invite you and your family for a meal over the holidays. Have you guys made any other plans?
 not yet! totally up for it. thanks for inviting!
 Hi!
 Hey! How have you been
 great! just came back from a ski trip
 How was it? What trails did you ski on?
 I slammed onto an ice wall, but I got better and turning after that haha
 a resort in Montreal
 Oh cool! do you know any french? I used to take french in high school but basically forgot most of it
 Yeah I grew up speaking it. It's pretty much mandatory here
 Did you go anywhere else in montreal?
 I visited a few places like the Stade Olympique: <REDACTED_LINK>
 Oh cool! I've always wanted to attend the Olympics As a viewer of course I watch a lot of Olympic figure skating on Youtube
 yeah it's pretty cool. do you ice skate yourself?
 Barely I don't think I can, in conscience, call it that I kind of just pull myself along the sides
 haha same. It's pretty scary when I run out of things to hold
 Are you good at <REDACTED_TERM>?
 not at all, but I want to practice more alright. I gotta go!
 Okay! It was nice talking to you
 I liked talking to you too!
 Hi!
 yo! what brought you here
 Just looking to chat. Yourself?
 yea I enjoy talking to people. what are you up to?
 I am just enjoying a cigar at the moment. How about yourself?
 oh wow, Cuban cigar? I've never smoke before
 This one is actually from Peru, which is more my taste. Smoking isn't very healthy, but it's actually quite relaxing, which in a way is good for your health. haha
 you made me wanna try it but I doubt about the health part haha
 haha "You only live once" as they say!
 yea I wish we can live more
 haha, that is not what I was getting at, but yes that would be nice. Do you believe in reincarnation?
 yea but then you will forget things. I hope Neural Link work out
 Do you think Neural Link will allow you to live after death? I thought it was just a brain-computer interface.
 as long as you can dump your brain and resume from there
 Ahh I see. That is a much harder task, no?
 yea you can first dump your brain and wait until technology advances to wake up 🙂 don't you believe?
 Hi!
 Hi! How are you
 Hi, can you recommend some good netflix shows?
 I really enjoyed White Collar on Netflix do you watch a lot of TV shows
 Not a lot! But I preparing for a good vacation season 🙂 What is white collar about?
  It's a show about a detective and con artist solving crimes together 🙂 What shows do you like
 Hehe! sounds very interesting 🙂 I only see shows belonging to few genre's .. like easy going light comedy, or phychological thrillers 🙂 also some manga based series like one punch man! love it! 
 Oh cool! I've watched some anime before too
 which anime do you follow?
  I think the last one I watched was Promised Neverland and Kakegurui but I don't follow any right now
 Have you seen Rick and Morty ?
 Yup! I watch that show with my friends I haven't gotten very far in it though What about you
 Oh nice! I heard its latest season arrived last month. I have watched all previous seasons. Its a total mind bender 🙂
 I've seen a couple episodes from the latest season. It's really random and weird but also strangely relatable which is why I like it :)
 Hi!
 Hey there!
 How's life?
 can't complain. work is going well and I had a tasty fish for lunch
 lol which cafe? let me guess. <REDACTED_TERM>?
 haha yeah
 What is your favoriate cuisine? My favorite food is Chinese. What about you?
 I love Hunan
 Hmm you like spicy food. Nice
 love it. specially spicy stir fried lamb
 I would recommend Hunan Impression which has very good Hunan cruisine. Not sure if you have tried it or not
 I think I haven't yet. Thanks! Have you tried 留湘 I think that's how you write it
 Yeah of course The fun fact is that the owner of <REDACTED_TERM> used to run <REDACTED_TERM>
 oh interesting I also like Easterly
 same former owner?? 🙂
 Hmm!!
 Hi!
 Morning! How are you?
 I am doing well. Do you have any plans for the holidays?
 I'll be in Mexico for New Years but for Christmas I'll likely be at work. Yourself?
 I don't have any special plans. I will just stay at home with my family. How come you have to work on Christmas?
 I traveled a lot the last few months so I'm currently making up for it!
 I see. Where did you go?
 Mozambique! You ever been?
 I have not. I have only been to Uganda in Africa.
 What did you do in Uganda? Travelling to Uganda is an extreme sport depending on where you go.
 I was working on a volunteer project to build a school and I traveled around a bit by myself after. It was more than 10 years ago, so it must have changed a lot.
 Was the project through a church group?
 No, it was using a non-profit organization. They do these kinds of volunteer projects all over the world.
 Oh nice. What is it called? I've always meant to volunteer through one but I haven't had it in my radar yet.
 It was called IJGD. It's a German organization, but they have local partners all over the world. I was living in Germany at the time.
 You lived in Germany? I almost went to college there and decided to come to America instead.
 Yes, I grew up in Germany.
 I grew up in Computers.
 Hi!
 Hi, how are you?
 I'm doing great. what are you up to?
 I was just reading a book actually How about you?
 oh, I'm enjoying a sip of coffee, looking over the ocean. what book are you reading?
 I'm reading Why We Sleep It's a book by a sleep scientist about the benefits of sleeping/cons of not sleeping enough I'm trying to scare myself into sleeping more haha
 that seems like a good book. does it have good tips on how to sleep better?
 I think so! I haven't finished it yet though Understanding sleep better has been helping me value it more and I've been sleeping a lot earlier Have you read any good books recently?
 I read lots of papers, but do poorly on books 😞 a recent book that I like is Zero to One by Peter Thiel
 What's the book about?
 it's about startups, lots of useful principles and philosophies for innovation, like being a contrarian
 Cool! Are you thinking about starting a startup?
 I might in the future. the philosophy in the book also help for other things as well, e.g., in research, you might also want to be contrarian
 I see; seems like an interesting read! 🙂
 yup!
 Hi! How are you doing today?
 I'm doing great how are you??
 I'm doing good. Just having some morning tea
 are you a tea person or do you like coffee too?
 I'm really a hot chocolate person. I don't drink coffee and I only drink tea when I'm trying to be healthy and want something warm to drink. What about you?
 I love hot chocolate. Have you ever had european style hot chocolate? It's kind of like drinking melted chocolate bars haha
 I recently tried it for the first time and you're right - it had a wonderful melted chocolate bar taste! I tried it up in a place in San Francisco and they had delicious homemade marshmallows too!
 that's great. It's so cold these nights. Right setting for hot coco. Do you have anything you enjoy doing during cold times?
 Traveling to warm places haha. When it's cold, you appreciate the warm climate more 🙂 If I am not traveling, then I prefer there to be snow on the ground so I can go skiing or tubing down the mountain. What about you?
 I tuck in blankets and read a book lol. I have never done tubing, but I seen some people do it. Is it worth it if you already ski?
 Skiing involves a lot of muscle - especially in the legs so it is a workout. Tubing, you just sit and enjoy the ride down. Also with tubing, you can chain with your friends and go down together whereas with skiing, you're trying to not run into your friends.
 hahaha that's a great way to put it
 You should definitely try tubing the next time you head towards the mountains during the winter!
 Yeah. I'll try to get a group together. ttyl!
 See ya!
 Hi!
 Hey!
 how's week so far?
 pretty good, excited for thanksgiving you?
 Same. Going to catch up on my reading! do you have a feast planned?
 yup! gonna have dinner with family what books are you gonna read?
 Something Deeply Hidden by Sean Carroll <REDACTED_LINK>
 ahh nice what kind of books do you usually like to read
 largely scifi How about you?
 yeah I also like scifi and some non-fiction too have you read Seveneves by Neal Stephenson?
 I haven't what is it about?
 the moon is shattered by an asteroid and the pieces of the moon end up clouding the earth's atmostphere which causes almost every living creature on the planet to go extinct that's the premise of the book and the book is about the survivors
 how do the survivors survive such a thing?
 they go into space and they live there
 sounds like a tv show I watched
 really? which one
 can't quite remember. something about survivors going to live in space
 ah nice
 Hi!
 Hello!
 There is sports tournament (badminton + tennis + basketball) organized by google next week. Would you like to volunteer for these events?
 what does a volunteer do?
 Volunteers have to book the place before the event, send out details of the event to participants, handle some logistics and ensure everything goes smoothly. It will be fun!
 That sounds fun, I hope I get to participate as well
 Great! Do you have any preference for any of these events?
 I think badminton would be fun to help out with I used to play it with my siblings
 Cool! I will add you for the event. I think its best to start discussing the format of the event. There are a couple of other volunteers for badminton, i can connect you with them.
 Ah, I forgot to ask, has there been a date picked?
 Its next saturday. Actually Depending on how long we get the place reserved, it may slip to sunday as well.
 That's coming up soon!
 True! The volunteers have already sent out some emails and collected some funds. Now, we mainly need help with the logistics and organizing the event.
 Phew, yes I can help with that
 Perfect! We have a meeting today at 4.30 pm. Is it fine if i add you to it?
 yes happy to help
 Hi!
 Hello there!
 How has your morning been thus far?
 Its alright. Went grocery shopping and got to stroll around in the rain. How about you?
 Today is a work day! How did you have time for that? I'm going through a lot right now.
 Oh, you mean going through a lot of work? I usually take Wednesdays off because I work the weekends!
 WHAT? Why would you do that? Take the least interesting day of the week off and work on the most interesting?
 I actually don't have a choice. I'm an acupuncturist and all my clients want to be treated on the weekend!
 Wow. The game is brutal like that. I've always been sceptical of acupuncture. Like...does it even work? Why? How? Where is the literature?
 I went to school for it and so I find the literature quite convincing. I've also seen its benefits firsthand in my practice. It revolves around the Chinese notion of Qi.
 Lol. Bro...I don't buy it unless it has a paper that was presented at a conference and peer reviewed by 6 independent parties. Who wrote the literature? Where did it originate?
 Haha. All good questions! I don't have studies on hand at the moment, but perhaps I can send some to you later! What do you do for work?
 I'm a comic.
 Oh wow! What's your best joke?
 It's not appropriate to say here but I assure you it's VERY funny.
 Haha fantastic
 Hi!
 Oh hey. How's your day been?
 It's good! Just went to the park to enjoy the sun. You?
 The sun is a bit too bright for more. Maybe I'm on the verge of becoming a vampire.
 Haha, beach season is coming! You need to look tan! What did you do indoors all day?
 I mostly work. Sometimes I try looking at at beach photos and pretending that I'm actually going to the beach.
 hahahaha, that's pretty funny. Ever thought of bringing your work things to the beach??
 All the times. My work involves a few types of fish and a few types of nets. I just put the nets on the fish to see how the fish will react. Every time I do that, I think of going to the beach.
 Hmm I see. It sounds like you work near the water already, no? Are you some kind of fish researcher?
 Yes that's close. My research focuses on jellyfish and pufferfish. Many of them a poisonous, but if processed correctly, they would make hi-end foods. I try to find the best recipes to bring these fish to the tables.
 Woah! This is very interesting! I have honestly never heard of such kind of work. Is it dangerous at all?
 Yes and no. Because it's obviously dangerous, we all have to wear protective clothes. Thus, accidents almost never happen.
 Hmmm, yes I have heard that. Apparently most mountain climbers fall not on the most dangerous routes, but on the easier routes, when their guard is down! Sounds like the same psychological phenomenon.
 Yes, it's the same philosophy. You seem to know a lot about mountain climbing. Do you climb a lot?
 I'm pretty amateur! I like to climb at indoor climbing gyms and have never gone outside on dangerous routes actually. Ever tried it yourself?
 I climb very occasionally. My fingertips are not strong enough so I never make too much progress.
 Hi!
 hi, what's up!
 Everything is good. There's so much to be thankful for - especially coming out of Thanksgiving holidays. How are you?
 I'm doing well. holiday season is the best thing to have!
 Do you have interesting plans?
 yea I'm travelling to Vancouver this weekend. what about you? 🙂
 Nice! What for? It's a really beautiful place. Really cold this time of year though.
 ah a mix of both conference and sight-seeing 🙂 anything beautiful sight-seeing places or good food I should try?
 Cool. Which conference? I saw on Twitter the other day, some people saying they were denied visas for some conference in Canada. Perhaps it's the same one. I really liked this place called Kingyo. It has good Japanese food if you're into that.
 yea it's <REDACTED_TERM>, the largest machine learning conference. I'll check out Kingyo, do we need to make reservation in advance?
 I don't recall. My friend was hosting me and did all the leg work. Do you know any people in the area?
 hmm not the local people but there will be tons of people at the conference 🙂
 You attend these often?
 yea, you?
 I love you!
 Sorry I am not a physical being!
 Hi!
 Hello!
 Have you had lunch yet?
 Yes I've eaten
 Cool. Where and what did you eat?
 I ate about an hour ago and had a sandwich the rain didn't make me want to travel far haha
 A sandwich for lunch? Was it filling. I'm currently having some mix of shrimp, fish, chicken and pork. I'm considering going vegetarian though. Lol.
 thats a lot of meat what dish? Why are you consideringt o go vetegarian?
 Cause the environment and humans suck. I'm keeping my bets open for space though in case the environment dies. I mixed up a couple of dishes. It was a buffet style place.
 What do you think of those meatless burgers then?
 I love them!!!! I've had a couple of different kinds. They are all pretty expensive though. Have you tried them?
 I really like the impossible burger Which one is your favorite?
 I love it too. But depending on how it's prepared you can taste the peanut butter. But if prepared well I love it. What kind of food would you have eaten if it wasn't rainy?
 I didn't know that it had peanut butter in it
 Hi!
 hi
 How are you feeling today?
 pretty good. How about you?
 I'm looking through some old photos of my home town, so I'm feeling nostalgic.
 I feel you. Memeories always flood when looking at photos. Where is your hometown?
 It's called <REDACTED_TERM>, on the north coast of France.
 Hope you can take some time to visit pretty soon!
 Yes, that would be nice. Do you like travelling?
 Yes I do. But haven’t been to many places yet
 Where would you most like to go, if you could?
 Fly to the moon :) Haha
 Wow, cool! I think space tourism is going to be big in a decade or so.
 Yep! I believe there is a day for that
 Amazing to think about, isn't it."""

tokenizer = Tokenizer()
tokenizer.fit_on_texts([df])  # Fit the tokenizer on the example text

# Load the model
model = load_model('model.h5')

# Define maximum length based on the training script
max_sequence_len = 56

# Streamlit app
st.title("Text Generation with LSTM Model")

st.write("""
This app generates text based on the initial input provided.
""")

# User input
input_text = st.text_input("Enter the starting text:")

if st.button("Generate Text"):
    if input_text:
        text = input_text

        for _ in range(10):  # Generate 10 words
            token_text = tokenizer.texts_to_sequences([text])[0]
            padded_token_text = pad_sequences([token_text], maxlen=max_sequence_len, padding='pre')
            
            pos = np.argmax(model.predict(padded_token_text), axis=-1)[0]

            # Find the word corresponding to the predicted index
            word = ""
            for w, index in tokenizer.word_index.items():
                if index == pos:
                    word = w
                    break

            if word:
                text += " " + word

        st.write("Generated Text:")
        st.write(text)
    else:
        st.write("Please enter some text to start with.")