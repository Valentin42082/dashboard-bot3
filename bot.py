import discord
from flask import Flask
import threading
import os

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Client(intents=intents)
app = Flask(__name__)

stats = {}

@app.route("/")
def dashboard():

    top = sorted(stats.values(), key=lambda x: x["xp"], reverse=True)[:10]

    html = """
    <h1>🏆 Leaderboard Discord</h1>
    """

    for i,user in enumerate(top,1):
        html += f"""
        <div>
        #{i}
        <img src="{user['avatar']}" width="40" style="border-radius:50%">
        {user['name']} — {user['xp']} XP — {user['messages']} messages
        </div>
        """

    return html


@bot.event
async def on_message(message):

    if message.author.bot:
        return

    uid = str(message.author.id)

    if uid not in stats:
        stats[uid] = {
            "name": message.author.name,
            "xp": 0,
            "messages": 0,
            "avatar": message.author.display_avatar.url
        }

    stats[uid]["xp"] += 5
    stats[uid]["messages"] += 1


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


threading.Thread(target=run_web).start()

bot.run("TON_TOKEN_DISCORD")
