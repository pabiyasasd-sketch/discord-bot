import discord
from discord.ext import commands
from botLogic import flip_coin, gen_pass, gen_emoji

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def bye(ctx):
    await ctx.send("\U0001f642")

@bot.command()
async def pwgen(ctx):
    password = gen_pass(10)  # Generate a 10-character password
    await ctx.send(f"Generated password: {password}")

@bot.command()
async def cflip(ctx):
    result = flip_coin()  # Flip a coin
    await ctx.send(f"The coin landed on: {result}")

@bot.command()
async def emoji(ctx):
    emoji = gen_emoji()  # Generate a random emoji
    await ctx.send(emoji)

@bot.command()
async def ten_emoji(ctx):
    emojis = [gen_emoji() for _ in range(10)]  # Generate a list of 10 random emojis
    await ctx.send(' '.join(emojis))

@bot.command()
async def heh(ctx, count: int = 5):
    await ctx.send("he" * count)

@bot.command()
async def lol(ctx, count: int = 5):
    await ctx.send("LO" * count)

@bot.command()
async def cat(ctx):
    # Send a cat picture from the local directory
    with open('img2/cat.jpg', 'rb') as f:
        picture = discord.File(f)
    # Send the picture to the channel
    await ctx.send(file=picture)

@bot.command()
async def mem(ctx):
    # Send a meme picture from the local directory
    memes = os.listdir('img')
    with open(random.choice([f'img/{meme}' for meme in memes]), 'rb') as f:
        picture = discord.File(f)
    # Send the picture to the channel
    await ctx.send(file=picture)

@bot.command('duck')
async def duck(ctx):
    # Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def cmds(ctx):
    # Help command that lists all available commands and their descriptions
    help_message = """
    **Available Commands:**
    - `$hello`: Greet the bot.
    - `$bye`: Say goodbye to the bot.
    - `$pwgen`: Generate a random password.
    - `$cflip`: Flip a coin and get the result.
    - `$emoji`: Get a random emoji.
    - `$ten_emoji`: Get a string of 10 random emojis.
    - `$heh [count]`: Get a string of "he" repeated [count] times (default is 5).
    - `$lol [count]`: Get a string of "LO" repeated [count] times (default is 5).
    - `$cat`: Get a cat picture from the local directory.
    - `$mem`: Get a random meme picture from the local directory.
    - `$duck`: Get a random duck image URL from an API.
    - `$tips [topic]`: Get tips on a specific topic (available topics: 'sampah', 'air').
    - `$apa [topic]`: Get a brief explanation of a topic (available topics: 'reduce', 'reuse', 'recycle', 'sampah', 'air', 'daur ulang', 'konservasi').
    """
    await ctx.send(help_message)

# Others stuff that are off-topic
@bot.command()
async def tips(ctx, topic: str = None):
    if topic == "sampah":
        tips_message_s = """
        **Tips untuk Mengurangi Sampah:**
        1. Gunakan tas, botol, dan wadah yang dapat digunakan kembali.
        2. Hindari plastik sekali pakai.
        3. Buat kompos dari sisa makanan dan sampah kebun.
        4. Daur ulang dengan benar dan dukung program daur ulang.
        5. Beli dalam jumlah besar untuk mengurangi sampah kemasan.
        6. Sumbangkan atau gunakan kembali barang-barang daripada membuangnya.
        7. Dukung perusahaan yang memprioritaskan keberlanjutan.
        """
        await ctx.send(tips_message_s)
    elif topic == "air":
        tips_message_a = """
        **Tips untuk Mengurangi Penggunaan Air:**
        1. Matikan keran saat menyikat gigi atau mencuci tangan.
        2. Perbaiki keran yang bocor untuk mencegah pemborosan air.
        3. Gunakan shower daripada bathtub untuk mandi, dan batasi waktu mandi.
        4. Gunakan mesin cuci dan pencuci piring hanya saat penuh untuk menghemat air.
        5. Kumpulkan air hujan untuk menyiram tanaman.
        6. Pilih tanaman yang tahan kekeringan untuk taman Anda.
        7. Dukung kebijakan dan inisiatif yang mempromosikan konservasi air.
        """
        await ctx.send(tips_message_a)
    else:
        await ctx.send("Maaf, saya tidak memiliki tips untuk topik tersebut. Silakan pilih antara 'sampah' atau 'air'.")

@bot.command()
async def apa(ctx, *, topic: str):
    if topic.lower() == "reduce":
        await ctx.send("Reduce berarti mengurangi penggunaan sumber daya dan produksi limbah.")
    elif topic.lower() == "reuse":
        await ctx.send("Reuse berarti menggunakan kembali barang-barang untuk mengurangi limbah.")
    elif topic.lower() == "recycle":
        await ctx.send("Recycle berarti mengolah kembali bahan-bahan bekas menjadi produk baru untuk mengurangi limbah.")
    elif topic.lower() == "sampah":
        await ctx.send("Sampah adalah bahan atau benda yang dibuang karena sudah tidak digunakan atau tidak diinginkan lagi.")
    elif topic.lower() == "air":
        await ctx.send("Air adalah zat cair yang sangat penting untuk kehidupan, digunakan untuk minum, memasak, membersihkan, dan banyak lagi.")
    elif topic.lower() == "daur ulang":
        await ctx.send("Daur ulang adalah proses mengubah limbah menjadi bahan baru untuk digunakan kembali, membantu mengurangi penggunaan sumber daya alam.")
    elif topic.lower() == "konservasi":
        await ctx.send("Konservasi adalah upaya untuk melindungi dan melestarikan sumber daya alam, lingkungan, dan keanekaragaman hayati untuk generasi mendatang.")
    else:
        await ctx.send("Maaf, saya tidak memiliki informasi tentang topik tersebut. Silakan tanyakan tentang 'reduce', 'reuse', 'recycle', 'sampah', 'air', 'daur ulang', atau 'konservasi'.")


bot.run("*** no ***")
