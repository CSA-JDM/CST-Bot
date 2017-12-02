import discord
import time
from random import randint


def b(num):
    return chr(num)


def a(char):
    return ord(str(char))


# TIME VARIABLES
minute = 60
hour = 60 * minute
day = 24 * hour

client = discord.Client()


@client.event
async def on_ready():
    global start
    start = time.time()
    print("Username: %s\nID: %s\nOpened Since: %s\n" % (client.user.name, client.user.id, time.asctime()))


@client.event
async def on_message(msg):
    if msg.content.startswith("!calc"):
        print(time.asctime() + ": " + msg.author.name + ": " + msg.content)
        result = eval(msg.content[6:])
        print(str(result))
        await client.send_message(msg.channel, str(result))
    elif msg.content.startswith('!roll'):
        print(time.asctime() + ": " + msg.author.name + ": " + msg.content)
        print(roll(msg) + "\n")
        await client.send_message(msg.channel, roll(msg))
    elif msg.content.startswith("!uptime"):
        print(time.asctime() + ": " + msg.author.name + ": " + msg.content)
        uptime = time.time() - start
        upday = int(uptime // day)
        uphour = int((uptime % day) // hour)
        upminute = int((uptime % hour) // minute)
        upsecond = int((uptime % minute) // 1)
        print("Live for " + ("{}:{}:{}:{} (d:h:m:s)".format(upday, uphour, upminute, upsecond) if uptime > day else (
            "{}:{}:{} (h:m:s)".format(uphour, upminute, upsecond) if uptime > hour else (
                "{}:{} (m:s)".format(upminute, upsecond) if uptime > minute else "{} seconds\n".format(upsecond)))))
        await client.send_message(msg.channel, "live for " + (
            "{}:{}:{}:{} (d:h:m:s)".format(upday, uphour, upminute, upsecond) if uptime > day else (
                "{}:{}:{} (h:m:s)".format(uphour, upminute, upsecond) if uptime > hour else (
                    "{}:{} (m:s)".format(upminute, upsecond) if uptime > minute else "{} seconds".format(upsecond)))))
    elif msg.content.startswith("!calc"):
        expression = msg.content[6:].lower()
        print(str(msg.content))
        for x in expression:
            if str(x) not in "0123456789abcdefintx+-=<>~^*/%&|()[].,\"' \r\n\x00":
                await client.send_message(msg.channel,
                                          "Characters allowed are 0123456789abcdefintx+-=<>~^*/%&|()[].,\"' and spaces")
                return
        try:
            result = eval(expression)
            print(result)
            await client.send_message(msg.channel, str(result))
        except:
            await client.send_message(msg.channel, "Well shoot")
    elif msg.content.startswith('!fibonacci'):
        print(time.asctime() + ": " + msg.author.name + ": " + msg.content)
        try:
            tostop = int(msg.content[11:])
            a, b = 0, 1
            allb = []
            while b < tostop:
                allb.append(b)
                a, b = b, a + b
            print(allb)
            await client.send_message(msg.channel, allb)
        except ValueError:
            print("An error occurred; please try again. (Ex. !fibonacci 1)")


def roll(msg):
    dcount = sum([1 for x in msg.content.lower()[6:] if x == 'd'])
    if dcount == 1:
        try:
            splitted = msg.content.lower()[6:].split('d')
            if splitted[0] != '' and type(int(splitted[0])) is int and type(int(splitted[1])) is int:
                roll = [randint(1, int(splitted[1])) for x in range(int(splitted[0]))]
                return msg.author.name + ", rolling " + splitted[1] + " sided dice " + splitted[0].rstrip() + (
                    " time: " if int(splitted[0]) == 1 else " times: ") + "\n" + str(sum(roll)) + " (" + '+'.join(
                        [str(x) for x in roll]) + ")"
            elif splitted[0] == '' and type(int(splitted[1])) is int:
                return msg.author.name + ", rolling " + splitted[1] + " sided dice 1 time: " + str(
                    randint(1, int(splitted[1])))
            else:
                return "Format incorrect"
        except:
            return "Something happened..."
    else:
        return msg.author.name + ", rolling 6 sided dice 1 time: " + str(randint(1, 6))


token = "Mzg1OTMwMTc5NjY4ODY5MTIw.DQInkA.loqfn2gG9JK57S1HvTGAq4FqIlk"

client.run(token)
