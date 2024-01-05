import discord
from discord.ext import commands , tasks
from yapayzeka import mesajlas
import asyncio
import random
from ceviri import cevir
from ceviri import cevirtr
from googlesearch import search
from datetime import datetime
import requests
import html
import json
import pyodbc

TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Bot = commands.Bot(command_prefix='-', intents=discord.Intents.all())
top_command_used = False
hatirlaticilar = []
weekly_activity = {}
user_xp = {}
quiz_active = False

RIOT_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


@Bot.command()
async def lol_west(ctx, username):
    summoner_api_url = f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}"
    headers = {
        "X-Riot-Token": RIOT_API_KEY
    }
    summoner_response = requests.get(summoner_api_url, headers=headers)

    if summoner_response.status_code == 200:
        summoner_data = summoner_response.json()
        summoner_id = summoner_data["id"]
        
        level = summoner_data["summonerLevel"]
        
        ranked_api_url = f"https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
        ranked_response = requests.get(ranked_api_url, headers=headers)

        if ranked_response.status_code == 200:
            ranked_data = ranked_response.json()
            if ranked_data:
                rank_info = ranked_data[0] 
                rank = rank_info["tier"] + " " + rank_info["rank"]
                wins = rank_info["wins"]
                losses = rank_info["losses"]
                win_rate = f"{(wins / (wins + losses)) * 100:.2f}%"
                tft_api_url = f"https://euw1.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}"
                tft_response = requests.get(tft_api_url, headers=headers)

                if tft_response.status_code == 200:
                    tft_data = tft_response.json()
                    if tft_data:
                        tft_rank_info = tft_data[0]  
                        tft_rank = tft_rank_info["tier"] + " " + tft_rank_info["rank"]
                        embed = discord.Embed(title=f"**Performans**", color=0x808080) 
                        embed.set_author(name=username, icon_url=f"https://cdn.communitydragon.org/latest/profile-icon/{summoner_data['profileIconId']}")
                        embed.add_field(name="**Level**", value=level, inline=True)
                        embed.add_field(name="**Rank**", value=rank, inline=True)
                        embed.add_field(name="**TFT Rank**", value=tft_rank, inline=True)
                        embed.add_field(name="**Win Rate**", value=win_rate, inline=True)

                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("TFT sıralama bilgisi yok.")
                else:
                    await ctx.send("TFT sıralama bilgisi alınamadı.")
            else:
                embed = discord.Embed(title=f"Kullanıcı Bilgileri - {username}", color=0x808080) 
                embed.set_author(name=username, icon_url=f"https://cdn.communitydragon.org/latest/profile-icon/{summoner_data['profileIconId']}")
                embed.add_field(name="**Level**", value=level, inline=True)
                embed.add_field(name="**Rank**", value="UnRanked", inline=True)
                embed.add_field(name="**TFT Rank**", value="UnRanked", inline=True)
                await ctx.send(embed=embed)
        else:
            await ctx.send(f"Kullanıcı adı: {username}\nLevel: {level}\nLoL sıralama bilgisi alınamadı.")
    else:
        await ctx.send("Kullanıcı bulunamadı veya bir hata oluştu.")




@Bot.command()
async def lol_tr(ctx, username):
    summoner_api_url = f"https://tr1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}"
    headers = {
        "X-Riot-Token": RIOT_API_KEY
    }
    summoner_response = requests.get(summoner_api_url, headers=headers)

    if summoner_response.status_code == 200:
        summoner_data = summoner_response.json()
        summoner_id = summoner_data["id"]
        level = summoner_data["summonerLevel"]
        ranked_api_url = f"https://tr1.api.riotgames.com/lol/league/v4/entries/by-summoner/{summoner_id}"
        ranked_response = requests.get(ranked_api_url, headers=headers)

        if ranked_response.status_code == 200:
            ranked_data = ranked_response.json()
            if ranked_data:
                rank_info = ranked_data[0] 
                rank = rank_info["tier"] + " " + rank_info["rank"]
                wins = rank_info["wins"]
                losses = rank_info["losses"]
                win_rate = f"{(wins / (wins + losses)) * 100:.2f}%"
                tft_api_url = f"https://tr1.api.riotgames.com/tft/league/v1/entries/by-summoner/{summoner_id}"
                tft_response = requests.get(tft_api_url, headers=headers)

                if tft_response.status_code == 200:
                    tft_data = tft_response.json()
                    if tft_data:
                        tft_rank_info = tft_data[0]  
                        tft_rank = tft_rank_info["tier"] + " " + tft_rank_info["rank"]
                        embed = discord.Embed(title=f"**Performans**", color=0x808080) 
                        embed.set_author(name=username, icon_url=f"https://cdn.communitydragon.org/latest/profile-icon/{summoner_data['profileIconId']}")
                        embed.add_field(name="**Level**", value=level, inline=True)
                        embed.add_field(name="**Rank**", value=rank, inline=True)
                        embed.add_field(name="**TFT Rank**", value=tft_rank, inline=True)
                        embed.add_field(name="**Win Rate**", value=win_rate, inline=True)

                        await ctx.send(embed=embed)
                    else:
                        await ctx.send("TFT sıralama bilgisi yok.")
                else:
                    await ctx.send("TFT sıralama bilgisi alınamadı.")
            else:
                embed = discord.Embed(title=f"Kullanıcı Bilgileri - {username}", color=0x808080) 
                embed.set_author(name=username, icon_url=f"https://cdn.communitydragon.org/latest/profile-icon/{summoner_data['profileIconId']}")
                embed.add_field(name="**Level**", value=level, inline=True)
                embed.add_field(name="**Rank**", value="UnRanked", inline=True)
                embed.add_field(name="**TFT Rank**", value="UnRanked", inline=True)

                await ctx.send(embed=embed)
        else:
            await ctx.send(f"Kullanıcı adı: {username}\nLevel: {level}\nLoL sıralama bilgisi alınamadı.")
    else:
        await ctx.send("Kullanıcı bulunamadı veya bir hata oluştu.")


# KULLANICIYA AİT PROFİL RESMİNİ GÖSTERİR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@Bot.command()
async def profilresmi(ctx, user: discord.User):
    if user.avatar:
        avatar_url = user.avatar.with_format("png")
    else:
        avatar_url = user.default_avatar.with_format("png")
    await ctx.send(avatar_url)


# Veritabanı bağlantısını açar ve cursor oluşturur <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def open_connection():
    
    cnxn = pyodbc.connect("Driver={SQL Server};Server=XXXXXX\XXXXXX;Database=XXXX;Trusted_Connection=yes;")
    cursor = cnxn.cursor()
    return cnxn, cursor

# Veritabanı bağlantısını kapatır  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def close_connection(connection):
    try:
        connection.close()
    except Exception as e:
        print(f"Hata: {e}")

# Kullanıcıyı veritabanına eklemek için <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def add_user_to_database(discord_user_id):
    conn, cursor = open_connection()
    cursor.execute(f"INSERT INTO UserXP (DiscordUserID, XP) VALUES ('{discord_user_id}', 0);")
    conn.commit()
    close_connection(conn)

# Kullanıcının XP puanını güncellemek için <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def update_user_xp(discord_user_id, xp_earned):
    conn, cursor = open_connection()
    cursor.execute(f"UPDATE UserXP SET XP = XP + {xp_earned} WHERE DiscordUserID = '{discord_user_id}';")
    conn.commit()
    close_connection(conn)
    
    
    
# Kullanıcının veritabanında olup olmadığını kontrol etmek için <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def is_user_in_database(discord_user_id):
    conn, cursor = open_connection()
    cursor.execute(f"SELECT COUNT(*) FROM UserXP WHERE DiscordUserID = '{discord_user_id}';")
    count = cursor.fetchone()[0]
    close_connection(conn)
    return count > 0


#XP TABLOSUNU AÇAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@Bot.command()
async def xp(ctx):
    global user_xp
    conn, cursor = open_connection()
    cursor.execute("SELECT TOP 10 DiscordUserID, XP FROM UserXP ORDER BY XP DESC;")
    xp_data = cursor.fetchall()
    close_connection(conn)

    xp_table = []
    for i, (user_id, xp) in enumerate(xp_data):
        member = ctx.guild.get_member(int(user_id))
        if member:
            xp_table.append(f"{i + 1}. {member.mention}: {xp} puan")

    if xp_table:
        xp_table = "\n".join(xp_table)
        xp_embed = discord.Embed(title="** TOP 10 Sıralama **", description=xp_table, color=0xbfc0c0) 
        await ctx.send(embed=xp_embed)
    else:
        await ctx.send("Sıralama bulunamadı.")


# QUİZ  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
@Bot.command()
async def quiz(ctx):
    global user_xp
    global quiz_active
    if quiz_active:
        embed = discord.Embed(title="** HEY **", description="**Şu anda bir yarışma devam ediyor.**", color=0xbfc0c0)
        await ctx.send(embed=embed)
        return
    quiz_active = True
    response = requests.get("https://opentdb.com/api.php?amount=1&type=multiple")
    data = json.loads(response.text)
    question_data = data['results'][0]
    question = cevirtr(html.unescape(question_data['question']))  
    correct_answer = cevirtr(html.unescape(question_data['correct_answer'])) 
    incorrect_answers = [cevirtr(html.unescape(answer)) for answer in question_data['incorrect_answers']] 
    answers = [correct_answer] + incorrect_answers
    random.shuffle(answers)
    formatted_answers = [f"{chr(65 + i)}- {answer}" for i, answer in enumerate(answers)]
    question_text = f"{question}\n\n" + "\n".join(formatted_answers)
    embed = discord.Embed(title="Savitar Quiz  (**BİRDEN ÇOK CEVABA TIKLAMAK YASAKTIR**)", description=question_text, color=0x3498db)
    message = await ctx.send(embed=embed)
    for i in range(len(answers)):
        await message.add_reaction(chr(127462 + i))
        
    await asyncio.sleep(12) 
    message = await ctx.fetch_message(message.id)  
    reactions = message.reactions
    correct_reaction = reactions[answers.index(correct_answer)]
    users = []
    async for user in correct_reaction.users():
        if not user.bot:
            users.append(user)

    if len(users) > 1:
        warning_message = "Birden fazla emojiye tıklamayın! Sadece bir emojiye tıklayabilirsiniz."
        await ctx.send(warning_message)
    else:
        if users:
            await ctx.send(f'Tebrikler: {", ".join([user.mention for user in users])} Doğru Cevap: {correct_answer}')
            for user in users:
                user_id = str(user.id)
                if not is_user_in_database(user_id):
                    add_user_to_database(user_id)
                update_user_xp(user_id, 25)
        else:
            await ctx.send(f'Kimse doğru cevap vermedi. Cevap: {correct_answer}')

    quiz_active = False



#KULLANICININ XPSİNİ SIFIRLAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
@commands.has_permissions(administrator=True)
async def sifirla_xp(ctx, member: discord.Member):
    conn, cursor = open_connection()
    discord_user_id = str(member.id)
    sql_command = f"UPDATE UserXP SET XP = 0 WHERE DiscordUserID = '{discord_user_id}';"
    cursor.execute(sql_command)
    conn.commit()
    close_connection(conn)

    await ctx.send(f"{member.mention}'in XP'si sıfırlandı.")


#QUİZ TABLOSUNDAKİ XPLERİ SIFIRLAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@Bot.command()
@commands.has_permissions(administrator=True)
async def reset_xp_table(ctx):
    conn, cursor = open_connection()
    sql_command = "UPDATE UserXP SET XP = 0;"
    cursor.execute(sql_command)
    conn.commit()
    close_connection(conn)   
    await ctx.send(f"**XP TABLOSU SIFIRLANDI**")    

#QUİZ XP VERİR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@Bot.command()
@commands.has_permissions(administrator=True)
async def xp_ver(ctx, member: discord.Member, xp_amount: int):
    user_id = str(member.id)
    conn, cursor = open_connection()
    cursor.execute(f"SELECT XP FROM UserXP WHERE DiscordUserID = '{user_id}';")
    current_xp_row = cursor.fetchone()

    if current_xp_row:
        current_xp = current_xp_row[0] 
        new_xp = current_xp + xp_amount
        cursor.execute(f"UPDATE UserXP SET XP = {new_xp} WHERE DiscordUserID = '{user_id}';")
        conn.commit()
    else:
        cursor.execute(f"INSERT INTO UserXP (DiscordUserID, XP) VALUES ('{user_id}', {xp_amount});")
        conn.commit()
    close_connection(conn)
    await ctx.send(f"{member.mention} adlı kullanıcıya {xp_amount} XP verildi.")




# QUIZ XP SİLER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@Bot.command()
@commands.has_permissions(administrator=True)
async def xp_sil(ctx, member: discord.Member, xp_amount: int):
    user_id = str(member.id)
    conn, cursor = open_connection()
    cursor.execute(f"SELECT XP FROM UserXP WHERE DiscordUserID = '{user_id}';")
    current_xp_row = cursor.fetchone()

    if current_xp_row:
        current_xp = current_xp_row[0] 
        if xp_amount > current_xp:
            await ctx.send(f"{member.mention} adlı kullanıcının mevcut XP'si {current_xp} ve silinmek istenen XP miktarı daha fazla.")
        else:
            new_xp = current_xp - xp_amount
            cursor.execute(f"UPDATE UserXP SET XP = {new_xp} WHERE DiscordUserID = '{user_id}';")
            conn.commit()

            await ctx.send(f"{xp_amount} XP, {member.mention} adlı kullanıcıdan silindi. Yeni XP miktarı: {new_xp}")
    else:
        await ctx.send(f"{member.mention} adlı kullanıcı veritabanında kayıtlı değil.")
    close_connection(conn)


#BAĞLANTI KONTROL <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def connect(ctx):
    embed = discord.Embed(description="**Bağlantı tamamlandı. Beni kullanman için seni bekliyorum. Yapay zeka modeli olarak sınırsız bilgiye sahibim.**",color=0xCCCCCC)
    
    await ctx.send(embed=embed)



#ÇEKİLİŞ OLUŞTURUR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
@commands.has_permissions(administrator=True)
async def cekilis_olustur(ctx, duration: str, *, prize: str):
    giveaway_channel = ctx.channel
    duration_in_seconds = convert_to_seconds(duration)
    if duration_in_seconds is None:
        await ctx.send("Geçersiz süre formatı. Örnek: 2s (2 saniye), 5m (5 dakika), 1h (1 saat), 3d (3 gün)")
        return

    embed = discord.Embed(title="Çekiliş", description=f"{prize}", color=discord.Color.gold())
    embed.add_field(name="Katılım", value="Katılmak için 🎉 tepkisine tıklayın!", inline=False)
    embed.set_footer(text=f"Çekiliş süresi: {duration}")
    
    giveaway_msg = await giveaway_channel.send(embed=embed)
    await giveaway_msg.add_reaction("🎉")

    await asyncio.sleep(duration_in_seconds)

    giveaway_msg = await giveaway_channel.fetch_message(giveaway_msg.id)
    users = [user async for user in giveaway_msg.reactions[0].users() if not user.bot]

    if users:
        winner = random.choice(users)
        await giveaway_channel.send(f"🎉 {winner.mention} kazandı! Tebrikler!")
    else:
        await giveaway_channel.send("Üzgünüz, kimse çekilişe katılmadı.")

def convert_to_seconds(duration):
    try:
        time_unit = duration[-1]
        time_value = int(duration[:-1])
        if time_unit == 's':
            return time_value
        elif time_unit == 'm':
            return time_value * 60
        elif time_unit == 'h':
            return time_value * 3600
        elif time_unit == 'd':
            return time_value * 86400
        else:
            return None
    except ValueError:
        return None

#BOT ÇALIŞMAYA BAŞLADIĞINDA YAPILACAK VE BAŞLATILACAK FONKSİYONLAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name=" -yardım | Sizi")
    await Bot.change_presence(activity=activity)
    hatirlaticilari_kontrol_et.start()


#HATIRLATICI OLUŞTURUR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@Bot.command()
@commands.has_permissions(administrator=True)
async def hatırlat(ctx, saat, *, mesaj):
    try:
        saat = datetime.strptime(saat, '%H:%M')
        hatirlaticilar.append((saat, mesaj, ctx.author, ctx.guild))
        embed = discord.Embed(description=f"**Hatırlatma saat: {saat.strftime('%H:%M')} - Mesaj: {mesaj}**",color=0xCCCCCC)
        
        await ctx.send(embed = embed)
    except ValueError:
        embed = discord.Embed(description="**Geçersiz saat formatı. Saati 'saat:dakika' formatında girin, örneğin: -hatirlat 12:30 hatırlatma_mesajı**",color=0xCCCCCC)
        await ctx.send()

#HATIRLATICILARI KONTROL EDER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@tasks.loop(minutes=1)
async def hatirlaticilari_kontrol_et():
    now = datetime.now()
    for hatirlatma in hatirlaticilar:
        saat, mesaj, kullanici, sunucu = hatirlatma
        if now.hour == saat.hour and now.minute == saat.minute:
            kanal = sunucu.get_channel(769850792429486090) 
            embed = discord.Embed(description=f"**{kullanici.mention}, hatırlatma: {mesaj}**",color=0xCCCCCC)    
            await kanal.send(embed = embed)


#LEADERBOARD TABLOSUNU SIFIRLAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def top_sıfırla(ctx):
    conn, cursor = open_connection()
    cursor.execute("UPDATE Leaderboard SET Points = 0, Level = 0;")
    conn.commit()
    close_connection(conn)
    
    await ctx.send("Leaderboard puanları sıfırlandı.")


#LEADERBOARD TOP 10 TABLOSUNU GÖSTERİR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def top(ctx):
    conn, cursor = open_connection()
    cursor.execute("SELECT TOP 10 DiscordUserID, Points, Level FROM Leaderboard ORDER BY Points DESC;") 
    leaderboard_data = cursor.fetchall()
    close_connection(conn)

    max_name_length = 20  
    max_score_length = 10  

    leaderboard_text = []
    for i, (user_id, points, level) in enumerate(leaderboard_data, start=1):
        member = ctx.guild.get_member(int(user_id))
        if member:
            username = member.display_name.ljust(max_name_length)
            score = f"{points} puan | Level {level}".rjust(max_score_length)
            leaderboard_text.append(f"{username} : {score}")
    if leaderboard_text:
        leaderboard_text = "\n".join(leaderboard_text)
        embed = discord.Embed(title="🏆 TOP 10 Sıralama 🏆", description=leaderboard_text, color=0xFFD700)
        embed.set_footer(text="Leaderboard by SAVITAR")
        await ctx.send(embed=embed)
    else:
        await ctx.send("Sıralama bulunamadı.")
        
     
def update_user_points(discord_user_id, points):
    conn, cursor = open_connection()
    cursor.execute(f"UPDATE Leaderboard SET Points = {points} WHERE DiscordUserID = '{discord_user_id}';")
    conn.commit()
    close_connection(conn)       


# leaderBoard Tablosundaki bir Kullanıcının puanını günceller <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
@commands.has_permissions(administrator=True)
async def guncelle_top_puan(ctx, member: discord.Member, points: int):
    user_id = str(member.id)
    update_user_points(user_id, points)
    await ctx.send(f"{member.mention} kullanıcısının puanı {points} olarak güncellendi.")


# AKTİVİTE SIFIRLAR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def resetactivity(ctx):
    if ctx.message.author.id == 324902488769822722:
        global weekly_activity
        weekly_activity = {}
        await ctx.send("Haftalık aktiflik sıfırlanmıştır.")
    else:
        await ctx.send("Bu komutu kullanma izniniz yok.")


# YAZILAN MESAJLARI DİNLEME EVENTİ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.event
async def on_message(message: discord.Message):
    kufurler = [""]
    if any(kufur in message.content for kufur in kufurler):
        await message.delete()
        embed = discord.Embed(description=f"**{message.author.mention}, Küfür etmeyelim !**",color=0xCCCCCC)
        await message.channel.send(embed=embed)

    author = message.author
    if not author.bot:
        if author.id not in weekly_activity:
            weekly_activity[author.id] = 1
        else:
            weekly_activity[author.id] += 1

        user_id = str(message.author.id)
        xp_earned = 0.2  

        conn, cursor = open_connection()
        cursor.execute(f"SELECT Points, Level FROM Leaderboard WHERE DiscordUserID = '{user_id}';")
        user_data = cursor.fetchone()

        if user_data:
            current_points = user_data[0]
            current_level = user_data[1]
            new_points = current_points + xp_earned
            new_level = current_level or 0

            required_points = new_level * 20
            while new_points >= required_points:
                new_level += 1
                required_points += new_level * 20
                user = await Bot.fetch_user(message.author.id)
                user_avatar = user.avatar.url  
                embed = discord.Embed(
                    title=f"Tebrikler {message.author.display_name}!",
                    description=f"Level UP - SEVİYE {new_level}",
                    color=0x00ff00
                )
                embed.set_thumbnail(url=user_avatar)
                await message.channel.send(embed=embed)
            cursor.execute(f"UPDATE Leaderboard SET Points = {new_points}, Level = {new_level} WHERE DiscordUserID = '{user_id}';")
            conn.commit()
        else:
            cursor.execute(f"INSERT INTO Leaderboard (DiscordUserID, Points, Level) VALUES ('{user_id}', {xp_earned}, 1);")
            conn.commit()

        close_connection(conn)

    await Bot.process_commands(message)


# HATALI KOMUT - HATA BİLGİSİ - YETKİSİZ KOMUT UYARILARI <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description="**Bu komutu kullanmak için yetkin yok kurcalama**",color=0xCCCCCC)
        await ctx.send(embed = embed)
    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(description="**Böyle bir komut kullanma şekli yok :) -yardım yaz bak **",color=0xCCCCCC)
        await ctx.send(embed = embed)
    else:
        print(f"Bilinmeyen Hata: {error}")
        embed = discord.Embed(description="**Bilinmeyen Hata ! Böyle bir hata alıyorsan Yaratıcıma danış**",color=0xCCCCCC)
        await ctx.send(embed = embed)

# SUNUCUYA GİRİŞ VE ÇIKIŞ KONTROLÜ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.event
async def on_member_join(member):
    welcome_channel = member.guild.system_channel  
    if welcome_channel is not None:
        welcome_message = f'{member.mention}! Çöplüğümüze hoşgeldin.'
        await welcome_channel.send(welcome_message)

@Bot.event
async def on_member_remove(member):
    goodbye_channel = member.guild.system_channel  
    if goodbye_channel is not None:
        goodbye_message = f'{member.display_name} sunucudan ayrıldı.'
        await goodbye_channel.send(goodbye_message)


#YAPAY ZEKA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@Bot.command()
async def savitar(ctx): 
    soru = ctx.message.content.replace("-savitar", "").strip()
    cevap = mesajlas(soru)
    if not cevap:
        await ctx.send("Üzgünüm, bir hata oluştu veya bu soruya cevap veremiyorum.")
        return
    if len(cevap) > 2000:
        cevap_parcalar = [cevap[i:i+2000] for i in range(0, len(cevap), 2000)]
        for parca in cevap_parcalar:
            embed = discord.Embed(description=f"**{parca}**",color=0xCCCCCC)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description=f"**{cevap}**",color=0xCCCCCC)
        await ctx.send(embed = embed)



#KULLANICIYI AT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@Bot.command()
@commands.has_permissions(administrator=True)
async def at(ctx, member: discord.Member):
    await member.kick()
    await ctx.send(f"{member} sunucudan atıldı!")



#SUSTUR <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
@commands.has_permissions(administrator=True)
async def sustur(ctx, member: discord.Member, *args):
    sure = None
    zaman_birimi = "saniye" 
    for i in range(len(args)):
        if args[i].isdigit():
            sure = int(args[i])
            if i + 1 < len(args):
                if args[i + 1].lower() == "dakika":
                    zaman_birimi = "dakika"
                elif args[i + 1].lower() == "saat":
                    zaman_birimi = "saat"
            break
    if sure is None:
        await ctx.send("Süre belirtilmedi. Örnek: -sustur @Kullanıcı 10 saniye")
        return
    if zaman_birimi == "dakika":
        sure *= 60  
    elif zaman_birimi == "saat":
        sure *= 3600  
    x = "saniye"
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        embed = discord.Embed(description="**Muted rolü sunucuda bulunamadı. Lütfen önce Muted rolünü oluşturun.**",color=0xCCCCCC)
        await ctx.send(embed = embed)
        return
    await member.add_roles(muted_role)
    embed = discord.Embed(description=f"**{member.mention} {sure} {x} boyunca susturuldu.**",color=0xCCCCCC)
    await ctx.send(embed = embed)
    await asyncio.sleep(sure)
    await member.remove_roles(muted_role)
    embed = discord.Embed(description=f"**{member.mention} artık susturulmuyor.**",color=0xCCCCCC)
    await ctx.send(embed = embed)


#SUSTURMAYI KALDIRMA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
@commands.has_permissions(administrator=True)
async def susturmayıkaldır(ctx, member: discord.Member):
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        await ctx.send("Muted rolü sunucuda bulunamadı. Lütfen önce Muted rolünü oluşturun.")
        return
    if muted_role in member.roles:
        await member.remove_roles(muted_role)
        embed = discord.Embed(description=f"**{member.mention} artık susturulmuyor.**",color=0xCCCCCC)
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(description=f"**{member.mention} zaten susturulmamış.**",color=0xCCCCCC)
        await ctx.send(embed = embed)




#MESAJLARI SİL <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@Bot.command()
async def sil(ctx, miktar: int):
    if miktar <= 0:
        embed = discord.Embed(description="**Geçersiz miktar. Pozitif bir tam sayı belirtmelisiniz.**",color=0xCCCCCC)
        await ctx.send(embed = embed)
        return
    deleted = await ctx.channel.purge(limit=miktar + 1)  
    embed = discord.Embed(description=f"**{len(deleted) - 1} mesaj silindi.**",color=0xCCCCCC)
    await ctx.send(embed = embed) 


# iq ölçer <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


@Bot.command()
async def iq(ctx):
    zeka = random.randint(70,160)
    embed = discord.Embed(description=f"**{zeka} iq'ya sahip **",color=0xCCCCCC)
    await ctx.send(embed = embed)
    
    
#İngilizce Çeviri <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< <<<<<<<<<<<< <  
    
    
@Bot.command()
async def cevir_en(ctx, *, metin):
    ceviri = cevir(metin)
    embed = discord.Embed(description=f"**Çeviri: {ceviri}**",color=0xCCCCCC)
    await ctx.send(embed = embed)


#Türkçe Çeviri <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def cevir_tr(ctx, *, metin):
    ceviri = cevirtr(metin)
    embed = discord.Embed(description=f"**Çeviri: {ceviri}**",color=0xCCCCCC)
    await ctx.send(embed = embed)

# YARDIM Komutu <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def yardım(ctx):
    komutlar = [
        {"Komut": "-savitar [soru]" , "Amaç": "Yapay Zekaya Soru Sormak"},
        {"Komut": "-profilresmi [@Kullanıcı]" , "Amaç": "Kullanıcının profil resmini tam boy gösterir"},
        {"Komut": "-connect", "Amaç": "Botun bağlantısını kontrol etmek"},
        {"Komut": "-at @Kullanıcı", "Amaç": "Belirtilen kullanıcıyı sunucudan atmak"},
        {"Komut": "-sustur @Kullanıcı [süre dakika/saat]", "Amaç": "Belirtilen kullanıcıyı belirtilen süre boyunca susturmak"},
        {"Komut": "-susturmayıkaldır @Kullanıcı", "Amaç": "Belirtilen kullanıcının susturmasını kaldırmak"},
        {"Komut": "-sil [mesaj sayısı]", "Amaç": "Belirtilen sayıda mesajı silmek"},
        {"Komut": "-iq", "Amaç": "Rastgele bir IQ seviyesi göstermek"},
        {"Komut": "-cevir_en [metin]", "Amaç": "Metni İngilizce'ye çevirmek"},
        {"Komut": "-cevir_tr [metin]", "Amaç": "Metni Türkçe'ye çevirmek"},
        {"Komut": "-dizi", "Amaç": "Dünyadaki Her diziyi ücretsiz yayımlayan dizi linkini atar"},
        {"Komut": "-maclinkleri", "Amaç": "Ücretsiz Maç Yayını veren Siteleri getirir"},
        {"Komut": "-maclinki_ekle [link]", "Amaç": "Veritabanına maç linki ekler ve saklar"},
        {"Komut": "-hatırlat XX:YY [mesaj]", "Amaç": "BELİRTİLEN SAAT İÇİN HATIRLATMA EKLER"},
        {"Komut": "-top", "Amaç": "En Aktif TOP 10 Üye görüntülenir"},
        {"Komut": "-top_sıfırla", "Amaç": "TOP Leaderboard tablosundaki LEVEL ve PUANLARI sıfırlar !"},
        {"Komut": "-fıkra", "Amaç": "Random +1000 fıkra arşivinden fıkra getirir"},
        {"Komut": "-quiz", "Amaç": "Savitar quiz Yarışmasını Başlatır"},
        {"Komut": "-xp", "Amaç": "Savitar quiz XP Tablosunu görüntüler"},
        {"Komut": "-xp_sil @Kullanıcı Miktar", "Amaç": "Kullanıcının xp sini siler"},
        {"Komut": "-xp_ver @Kullanıcı Miktar", "Amaç": "Kullanıcıya xp ekler"},
        {"Komut": "-sifirla_xp @Kullanıcı", "Amaç": "Kullanıcının xp'sini sıfırlar "},   
        {"Komut": "-reset_xp_table", "Amaç": "XP TABLOSUNU SIFIRLAR "},
        {"Komut": "-lol_west [Hesap Adı]", "Amaç": "West Hesap Bilgilerini Getirir "},
        {"Komut": "-lol_tr [Hesap Adı]", "Amaç": "TR Hesap Bilgilerini Getirir"},
        
    ]

    yardim_mesaji = "İşte mevcut komutlar ve amaçları:"
    for komut in komutlar:
        yardim_mesaji += f"\n**{komut['Komut']}** - {komut['Amaç']}"

    embed = discord.Embed(title="Komutlar Listesi", description=yardim_mesaji, color=0x3498db)
    await ctx.send(embed=embed)


#DiziPal güncel link <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def dizi(ctx):
    arama_terimi = "dizipal"  
    link = None
    for sonuc in search(arama_terimi, num_results=1):
        link = sonuc
        break
    if link:
        embed = discord.Embed(description=f"**İşte 'dizipal' için Google'da bulduğum ilk sonucun bağlantısı:\n{link}**",color=0xCCCCCC)
        await ctx.send(embed = embed)
    else:
        embed = discord.Embed(description="**Üzgünüm, herhangi bir sonuç bulunamadı.**",color=0xCCCCCC)
        await ctx.send(embed = embed)


#MACKLİNKİ TABLOSUNU GÖSTER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def maclinkleri(ctx):
    conn, cursor = open_connection()
    cursor.execute("SELECT Link FROM Maclinkleri;")
    links = cursor.fetchall()
    close_connection(conn)

    if links:
        link_mesaji = "\n".join(link[0] for link in links)
        embed = discord.Embed(description=f"**{link_mesaji}**", color=0xCCCCCC)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Henüz maç linki eklenmemiş.")


#MACLİNKİ EKLE <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def maclinki_ekle(ctx, link: str):
    conn, cursor = open_connection()
    cursor.execute(f"INSERT INTO Maclinkleri (Link) VALUES ('{link}');")
    conn.commit()
    close_connection(conn)
    await ctx.send(f"Başarıyla yeni bir link eklediniz: {link}")
    conn, cursor = open_connection()
    cursor.execute("SELECT Link FROM Maclinkleri;")
    links = cursor.fetchall()
    close_connection(conn)
    if links:
        updated_link_mesaji = "\n".join(link[0] for link in links)
        embed = discord.Embed(description=f"**{updated_link_mesaji}**", color=0xCCCCCC)
        await ctx.send(embed=embed)




#FIKRA <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

@Bot.command()
async def fıkra(ctx):
    try:
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        if response.status_code == 200:
            data = response.json()
            joke = data["joke"]
            embed = discord.Embed(description=f"**{cevirtr(joke)}**",color=0xCCCCCC)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Üzgünüm, fıkra alınamadı.")
    except Exception as e:
        print(e)
        await ctx.send("Fıkra alınırken bir hata oluştu.")



Bot.run(TOKEN)

