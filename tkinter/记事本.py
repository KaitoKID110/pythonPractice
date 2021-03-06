import tkinter

win = tkinter.Tk()
win.title("记事本")
win.geometry("400x400+700+200")
win.resizable(0,0)
scroll = tkinter.Scrollbar()

#                       ,width = 50,height = 8      列数          行数
text = tkinter.Text(win)
#                    放在右侧        填充y轴
scroll.pack(side = tkinter.RIGHT,fill = tkinter.Y)
text.pack(side = tkinter.LEFT,fill = tkinter.BOTH)
#关联
scroll.config(command = text.yview)
text.config(yscrollcommand = scroll.set)
'''
str = """If there is anyone out there who still doubts that america is a place where all things are possible; who still wonders if the dream of our founders is alive in our time; who still questions the power of our democracy, tonight is your answer.it's the answer told by lines that stretched around schools and churches in numbers this nation has never seen; by people who waited three hours and four hours, many for the very first time in their lives, because they believed that this time must be different; that their voice could be that difference.

it's the answer spoken by young and old, rich and poor, democrat and republican, black, white, latino, asian, native american, gay, straight, disabled and not disabled - americans who sent a message to the world that we have never been a collection of red states and blue states: we are, and always will be, the united states of america.

it's the answer that led those who have been told for so long by so many to be cynical, and fearful, and doubtful of what we can achieve to put their hands on the arc of history and bend it once more toward the hope of a better day.

it's been a long time coming, but tonight, because of what we did on this day, in this election, at this defining moment, change has come to america.

ijust received a very gracious call from senator mccain. he fought long and hard in this campaign, and he's fought even longer and harder for the country he loves. he has endured sacrifices for america that most of us cannot begin to imagine, and we are better off for the service rendered by this brave and selfless leader. i congratulate him and governor palin for all they have achieved, and i look forward to working with them to renew this nation's promise in the months ahead.

iwant to thank my partner in this journey, a man who campaigned from his heart and spoke for the men and women he grew up with on the streets of scranton and rode with on that train home to delaware, the vice president-elect of the united states, joe biden.

iwould not be standing here tonight without the unyielding support of my best friend for the last sixteen years, the rock of our family and the love of my life, our nation's next first lady, michelle obama. sasha and malia, i love you both so much, and you have earned the new puppy that's coming with us to the white house. and while she's no longer with us, i know my grandmother is watching, along with the family that made me who i am. i miss them tonight, and know that my debt to them is beyond measure.

to my campaign manager david plouffe, my chief strategist david axelrod, and the best campaign team ever assembled in the history of politics - you made this happen, and i am forever grateful for what you've sacrificed to get it done.

but above all, i will never forget who this victory truly belongs to - it belongs to you.

iwas never the likeliest candidate for this office. we didn't start with much money or many endorsements. our campaign was not hatched in the halls of washington - it began in the backyards of des moines and the living rooms of concord and the front porches of charleston.

it was built by working men and women who dug into what little savings they had to give five dollars and ten dollars and twenty dollars to this cause. it grew strength from the young people who rejected the myth of their generation's apathy; who left their homes and their families for jobs that offered little pay and less sleep; from the not-so-young people who braved the bitter cold and scorching heat to knock on the doors of perfect strangers; from the millions of americans who volunteered, and organized, and proved that more than two centuries later, a government of the people, by the people and for the people has not perished from this earth. this is your victory.

iknow you didn't do this just to win an election and i know you didn't do it for me. you did it because you understand the enormity of the task that lies ahead. for even as we celebrate tonight, we know the challenges that tomorrow will bring are the greatest of our lifetime - two wars, a planet in peril, the worst financial crisis in a century. even as we stand here tonight, we know there are brave americans waking up in the deserts of iraq and the mountains of afghanistan to risk their lives for us. there are mothers and fathers who will lie awake after their children fall asleep and wonder how they'll make the mortgage, or pay their doctor's bills, or save enough for college. there is new energy to harness and new jobs to be created; new schools to build and threats to meet and alliances to repair.

the road ahead will be long. our climb will be steep. we may not get there in one year or even one term, but america - i have never been more hopeful than i am tonight that we will get there. i promise you - we as a people will get there.

there will be setbacks and false starts. there are many who won't agree with every decision or policy i make as president, and we know that government can't solve every problem. but i will always be honest with you about the challenges we face. i will listen to you, especially when we disagree. and above all, i will ask you join in the work of remaking this nation the only way it's been done in america for two-hundred and twenty-one years - block by block, brick by brick, calloused hand by calloused hand.

what began twenty-one months ago in the depths of winter must not end on this autumn night. this victory alone is not the change we seek - it is only the chance for us to make that change. and that cannot happen if we go back to the way things were. it cannot happen without you.

so let us summon a new spirit of patriotism; of service and responsibility where each of us resolves to pitch in and work harder and look after not only ourselves, but each other. let us remember that if this financial crisis taught us anything, it's that we cannot have a thriving wall street while main street suffers - in this country, we rise or fall as one nation; as one people.

let us resist the temptation to fall back on the same partisanship and pettiness and immaturity that has poisoned our politics for so long. let us remember that it was a man from this state who first carried the banner of the republican party to the white house - a party founded on the values of self-reliance, individual liberty, and national unity. those are values we all share, and while the democratic party has won a great victory tonight, we do so with a measure of humility and determination to heal the divides that have held back our progress. as lincoln said to a nation far more divided than ours, “we are not enemies, but friends…though passion may have strained it must not break our bonds of affection.” and to those americans whose support i have yet to earn - i may not have won your vote, but i hear your voices, i need your help, and i will be your president too.

and to all those watching tonight from beyond our shores, from parliaments and palaces to those who are huddled around radios in the forgotten corners of our world - our stories are singular, but our destiny is shared, and a new dawn of american leadership is at hand. to those who would tear this world down - we will defeat you. to those who seek peace and security - we support you. and to all those who have wondered if america's beacon still burns as bright - tonight we proved once more that the true strength of our nation comes not from our the might of our arms or the scale of our wealth, but from the enduring power of our ideals: democracy, liberty, opportunity, and unyielding hope.

for that is the true genius of america - that america can change. our union can be perfected. and what we have already achieved gives us hope for what we can and must achieve tomorrow.

this election had many firsts and many stories that will be told for generations. but one that's on my mind tonight is about a woman who cast her ballot in atlanta. she's a lot like the millions of others who stood in line to make their voice heard in this election except for one thing - ann nixon cooper is 106 years old.

she was born just a generation past slavery; a time when there were no cars on the road or planes in the sky; when someone like her couldn't vote for two reasons - because she was a woman and because of the color of her skin.

and tonight, i think about all that she's seen throughout her century in america - the heartache and the hope; the struggle and the progress; the times we were told that we can't, and the people who pressed on with that american creed: yes we can.

at a time when women's voices were silenced and their hopes dismissed, she lived to see them stand up and speak out and reach for the ballot. yes we can.

when there was despair in the dust bowl and depression across the land, she saw a nation conquer fear itself with a new deal, new jobs and a new sense of common purpose. yes we can.

when the bombs fell on our harbor and tyranny threatened the world, she was there to witness a generation rise to greatness and a democracy was saved. yes we can.

she was there for the buses in montgomery, the hoses in birmingham, a bridge in selma, and a preacher from atlanta who told a people that “we shall overcome.” yes we can.

aman touched down on the moon, a wall came down in berlin, a world was connected by our own science and imagination. and this year, in this election, she touched her finger to a screen, and cast her vote, because after 106 years in america, through the best of times and the darkest of hours, she knows how america can change. yes we can.

america, we have come so far. we have seen so much. but there is so much more to do. so tonight, let us ask ourselves - if our children should live to see the next century; if my daughters should be so lucky to live as long as ann nixon cooper, what change will they see? what progress will we have made?

this is our chance to answer that call. this is our moment. this is our time - to put our people back to work and open doors of opportunity for our kids; to restore prosperity and promote the cause of peace; to reclaim the american dream and reaffirm that fundamental truth - that out of many, we are one; that while we breathe, we hope, and where we are met with cynicism, and doubt, and those who tell us that we can't, we will respond with that timeless creed that sums up the spirit of a people:

yes we can. thank you, god bless you, and may god bless the united states of america.
"""
text.insert(tkinter.INSERT,str)
'''

def name():
    #布尔值变量
    b = False
    top = tkinter.Toplevel()
    top.title("询问")
    top.geometry("200x100+750+250")
    top.resizable(0, 0)
    e = tkinter.Variable()
    entry = tkinter.Entry(top, textvariable=e)
    entry.pack(side = tkinter.LEFT)
    e.set("")

    def func():
        global n,b
        name = e.get()
        n+=name

    button = tkinter.Button(top,text="完成",command=func)
    button.pack(side = tkinter.RIGHT)
    top.mainloop()

n = ""
#保存
path = r"C:\Users\Administrator\Desktop"
str = ""
def baocun():
    global n,str
    str = text.get("0.0",tkinter.END)
    name()
    name1 = n
    print(name1)
    with open(path+"\\"+name1+".txt","w",encoding="utf-8") as f:
        f.write(str)
        str = ""
        n = ""
'''
def dakai():
    global n
    name()
    name1 = n
    print(name1)
    with open(path+"\\"+name1+".txt","r",encoding="utf-8") as f:
        str = f.read()
        text.insert(tkinter.INSERT, str)
        n = ""
'''

#保存和退出
menubar = tkinter.Menu(win)
win.config(menu = menubar)
menu1 = tkinter.Menu(menubar,tearoff = False)
menu1.add_command(label = "保存",command = baocun)
'''
menu1.add_command(label = "打开",command = dakai)
'''
menu1.add_separator()
menu1.add_command(label = "退出",command =win.quit)
menubar.add_cascade(label = "文件",menu = menu1)

win.mainloop()