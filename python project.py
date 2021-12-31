import mysql.connector as mc
a=mc.connect(host='localhost',user='root',passwd='1234',database='project',auth_plugin='mysql_native_password')
from IPython.display import Image # used to import image from folders
# module is used to play background music
import pygame
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\vishnu\OneDrive\Desktop\python project\audio\Bgmi.mp3")
pygame.mixer.music.play()
import pyttsx3
engine=pyttsx3.init()# starts the engine of pyttsx3 module
voices=engine.getProperty('voices')  # giving property to voices variable from engine
engine.setProperty('voice', voices[1].id)  # seting female voice to the voice assisant
engine. setProperty("rate", 150)
from tabulate import tabulate
import matplotlib.pyplot as plt
import speech_recognition as sr
# collect the required data from the database
def collect(b,u1):
    u=a.cursor()
    c=u.execute(b,(u1,))
    d=u.fetchone()
    e=d[0]
    return e

# speaks the text given to function
def speak(s):
    engine.say(s)
    engine.runAndWait()
# this function round off the float values
def round1(n):
    if n>(n+0.5):
        return n+1
    else:
        return n
    
def listen():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('speak anything')
        audio=r.listen(source,timeout=4)
        try:
            text=r.recognize_google(audio)
            return text
        except:
            print('voice is not recoginized')

display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\bgmi.jpeg",width=500,height=700))
speak('good morning friend, i am saara your voice assistant.')    
ch = 'y'
speak('please enter user id')
u1=int(input('enter user id :'))
while ch == 'y' or ch =='yes':
    speak('please enter password')
    u2=input('enter password :')
    e=collect('select password from user where user_id =%s',u1)
    if u2 == e:
        u=collect('select name from detail where user_id =%s',u1)
        speak('hi {} , what i can do for you?'.format(u))
        a1=listen()
        while 'no' not in a1:
            if a1 in ['how can i use','who are you','what is your name']:
                display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\sara.jpeg",width=300,height=300))
                speak('i am saara the voice assistant for battle ground mobile india ,I will help you to know your details in the game')
                
            elif a1 in ['tell  my details','display my profile']:
                print('The details about you is given below, if any doubts refer me')
                speak('The details about you is given below, if any doubts refer me')
                print()
                c1=collect('select c_season from detail where user_id =%s',u1)
                c2=collect('select f_d from detail where user_id =%s',u1)
                c3=collect('select title from d_extra where user_id =%s',u1)
                c4=collect('select archi1 from d_extra where user_id =%s',u1)
                c5=collect('select archi2 from d_extra where user_id =%s',u1)
                c6=collect('select archi3 from d_extra where user_id =%s',u1)
                l=[['user name :',u,' ','Title :',c3],['user id :',u1,' ','Achievement 1 :',c4],['f/d :',c2,' ','Achievement 2 :',c5],['','',' ','Achievement 3 :',c6]]
                print(tabulate(l,tablefmt='grid'))
                print('Current Season Rank :')
                if c1 =='bronze1':
                    display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\B1.jpeg",width=200,height=300))
                elif c1=='silver1':
                    display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\S1.jpeg",width=200,height=300))
                elif c1=='gold1':
                    display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\G1.jpeg",width=200,height=300))
                elif c1=='platinum1':
                    display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\P1.jpeg",width=200,height=300))
                elif c1=='diamond1':
                    display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\D1.jpeg",width=200,height=300))
                elif c1=='crown1':
                    display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\C1.jpeg",width=200,height=300))
                elif c1=='ace1':
                    display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\A1.jpeg",width=200,height=300))
                else:
                    display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\CR1.jpeg",width=200,height=300))
                
            elif a1 in ['tell me the events','show events',]:
                speak('the on going events in this curren season C1S3 M6 royal pass are :')
                print('1. MYTHIC WINTER (M6 Royal Pass)')
                speak(' MYTHIC WINTER (M6 Royal Pass)')
                print('2. Squid Game Mode')
                speak('Squid Game Mode')
                print('3. Mirror World Mode')
                speak('Mirror World Mode')
                print('4. Avalanche X-Suit')
                speak('Avalanche X-Suit')
                print('5. Coupon Exchange Event')
                speak('Coupon Exchange Event')
                print()
                speak('I can help you to explain the events ,shall I')
                a2=int(input('enter the event option :'))
                while a2 in range(1,6):
                    if a2 ==1:
                        print()
                        print('MYTHIC WINTER (M6 Royal Pass)')
                        print()
                        display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\m6.jpeg",width=400,height=600))
                        print()
                        print('The current royale pass will be valid till December 20, 2021')
                        print('After the given date, players can enjoy the next royale pass')
                        speak('The current royale pass will be valid till December 20, 2021. After the given date, players can enjoy the next royale pass')
                        print('the players can enjoy this royal pass by playing and collecting the royal pass gifts')
                        speak('the players can enjoy this royal pass by playing and collecting the royal pass gifts')
                    elif a2 ==2:
                        print()
                        print('Squid Game Mode')
                        print()
                        display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\SG.jpeg",width=400,height=600))
                        print()
                        print('The Squid Game mode starts from December 21, 2021')
                        speak('The Squid Game mode starts from December 21, 2021')
                        print('the players can experience the squid game in the BGMI.')
                        speak('the players can experience the squid game in the BGMI.')
                    elif a2 ==3:
                        print()
                        print('Mirror World Mode')
                        print()
                        print()
                        display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\MW.jpeg",width=400,height=600))
                        print()
                        print('The Mirror World mode starts from december 21, 2021')
                        speak('The Mirror World mode starts from december 21, 2021')
                        print('the colabration of Bgmi and Arcane where you can experince the Arcane characters in Playground.')
                        speak('the colabration of Bgmi and Arcane where you can experince the Arcane characters in Playground.')
                    elif a2==4:
                        print()
                        print('Avalanche X-Suit')
                        print()
                        print()
                        display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\AX.jpeg",width=400,height=600))
                        print()
                        print('The Christmas Gift for all bgmi users is here, Avalanche X-suit')
                        speak('The Christmas Gift for all bgmi users is here, Avalanche X-suit')
                        print('the event starts from december 25, 2021')
                        speak('the event starts from december 25, 2021')
                        print('Players be ready to obtain Avalanche the snow Guardian')
                        speak('Players be ready to obtain Avalanche the snow Guardian')
                    else:
                        print()
                        print('Coupon Exchange Event')
                        print()
                        print()
                        display(Image(filename=r"C:\Users\vishnu\OneDrive\Desktop\python project\pictures\CE.jpeg",width=400,height=600))
                        print()
                        print('After 1.8 update, Users can exchange the coupons in given phase')
                        speak('After 1.8 update, Users can exchange the coupons in given phase')
                        print('The number of crap used is reduced, from 1.8 update')
                        speak('The number of crap used is reduced, from 1.8 update')
                        print('Enjoy the new Update Byeee')
                        speak('Enjoy the new Update Byeee')
                    print('-'*100)
                    a2=int(input('enter the event option :'))
            elif a1 in ['improvement in FD','target fd']:
                speak('Hi {} ,i will help you to improve your Target finish Rate :'.format(u))
                f_d=collect('select f_d from f_d where user_id =%s',u1)
                f_d1=collect('select f_d1 from f_d where user_id =%s',u1)
                f_d2=collect('select f_d2 from f_d where user_id =%s',u1)
                f_d3=collect('select f_d3 from f_d where user_id =%s',u1)
                n=collect('select Matches from f_d where user_id =%s',u1)
                a1=[n-3,n-2,n-1,n]
                b1=[f_d,f_d1,f_d2,f_d3]
                plt.plot(a1,b1,linestyle='-')
                plt.title('no of Matches VS F_D')
                plt.xlabel('No. of Matches')
                plt.ylabel('Finish Rate')
                plt.show()
                td=float(input('Enter the Target Finish Rate :'))
                k=int(round1(td-f_d3))
                print('To achieve the given target, you should take {} kills per match'.format(k))
                speak('To achieve the given target, you should take {} kills per match'.format(k))
                break
            else:
                print('Question Not Recognized')
                pass
            print()
            print('-'*100)
            print() 
            a1=listen()
        break
    else:
        speak('your password is incorrect')
        print('password incorrect !!')
        speak('do you want to re-enter your password')
        ch=input('do you want to re-enter password(y/n) :')

enter user id :1234567890
enter password :kum@1
speak anything

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
The details about you is given below, if any doubts refer me

+-------------+------------+--+-----------------+----------------+
| user name : | Price Odin |  | Title :         | Weapon Master  |
+-------------+------------+--+-----------------+----------------+
| user id :   | 1234567890 |  | Achievement 1 : | OverAchiver    |
+-------------+------------+--+-----------------+----------------+
| f/d :       | 1.02       |  | Achievement 2 : | Skull Buster V |
+-------------+------------+--+-----------------+----------------+
|             |            |  | Achievement 3 : | Elite Master   |
+-------------+------------+--+-----------------+----------------+
Current Season Rank :

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
1. MYTHIC WINTER (M6 Royal Pass)
2. Squid Game Mode
3. Mirror World Mode
4. Avalanche X-Suit
5. Coupon Exchange Event

enter the event option :1

MYTHIC WINTER (M6 Royal Pass)


The current royale pass will be valid till December 20, 2021
After the given date, players can enjoy the next royale pass
the players can enjoy this royal pass by playing and collecting the royal pass gifts
----------------------------------------------------------------------------------------------------
enter the event option :6

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything
Question Not Recognized

----------------------------------------------------------------------------------------------------

speak anything

Enter the Target Finish Rate :6
To achieve the given target, you should take 5 kills per match
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print('speak anything')
    audio=r.listen(source,timeout=2)
    try:
        text=r.recognize_google(audio)
        print(text)
    except:
        print('voice is not recoginized')
speak anything
hello
 
