import json, os, asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
from telegram.constants import ParseMode
import config

BOT_TOKEN = "8857539328:AAGoQYcCJk7gSMMvpSIGJ81ETqKVfIj9q3I"
DB_FILE = "database.json"

def load_db():
    if not os.path.exists(DB_FILE):
        return {"allowed": {}, "paired": {}, "users": {}}
    with open(DB_FILE, "r") as f:
        data = json.load(f)
        if "users" not in data: data["users"] = {}
        return data

def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    username = update.effective_user.username or "nousername"
    db = load_db()
    
    # Auto save username -> ID mapping for owner to use later
    db["users"][username.lower()] = uid
    db["users"][uid] = username
    save_db(db)

    is_owner = uid == str(config.OWNER_ID)
    is_allowed = uid in db["allowed"] or username.lower() in [k.lower() for k in db["allowed"]] or f"@{username.lower()}" in [k.lower() for k in db["allowed"]]

    # Check also by username in allowed
    allowed_keys = [k.lower().replace("@","") for k in db["allowed"].keys()]
    if username.lower() in allowed_keys:
        is_allowed = True

    if not is_owner and not is_allowed:
        # check if pending username access
        for key in db["allowed"]:
            if key.lower().replace("@","") == username.lower():
                is_allowed = True
                break

    if not is_owner and not is_allowed:
        kb = [[InlineKeyboardButton("📞 Contact Owner", url=f"https://t.me/{config.OWNER_INFO['telegram'].replace('@','')}")]]
        await update.message.reply_text(config.NO_ACCESS_MESSAGE + f"\n\nWA: {config.OWNER_INFO['whatsapp']}\nTG: {config.OWNER_INFO['telegram']}", reply_markup=InlineKeyboardMarkup(kb))
        return

    kb = [[InlineKeyboardButton("💠 MENU 💠", callback_data="menu")], [InlineKeyboardButton("👑 OWNER", callback_data="owner"), InlineKeyboardButton("🔗 PAIR", callback_data="pair")]]
    await update.message.reply_text(f"╔═══ <b>RIGHT ARM TESTING BOT</b> ═══╗\n\n👋 Hello @{username}\n⚡ Online\n\n✨ Choose Below 👇", reply_markup=InlineKeyboardMarkup(kb), parse_mode=ParseMode.HTML)

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "menu":
        kb = [
            [InlineKeyboardButton(config.TOOLS_DATA["tool_1"]["name"], callback_data="tool_1"), InlineKeyboardButton(config.TOOLS_DATA["tool_2"]["name"], callback_data="tool_2")],
            [InlineKeyboardButton(config.TOOLS_DATA["tool_3"]["name"], callback_data="tool_3"), InlineKeyboardButton(config.TOOLS_DATA["tool_4"]["name"], callback_data="tool_4")],
            [InlineKeyboardButton(config.TOOLS_DATA["tool_5"]["name"], callback_data="tool_5"), InlineKeyboardButton(config.TOOLS_DATA["tool_6"]["name"], callback_data="tool_6")],
            [InlineKeyboardButton("🔙 Back", callback_data="back")]
        ]
        await query.edit_message_text("💠 <b>SELECT TOOL - 6 TOOLS</b> 💠", reply_markup=InlineKeyboardMarkup(kb), parse_mode=ParseMode.HTML)
    elif query.data.startswith("tool_"):
        tool = config.TOOLS_DATA.get(query.data)
        await query.edit_message_text(tool["commands"], parse_mode=ParseMode.HTML)
        await context.bot.send_message(chat_id=config.OWNER_ID, text=f"👤 @{query.from_user.username} Opened {tool['name']}")
    elif query.data == "owner":
        await query.edit_message_text(f"👑 OWNER\n\nWA: {config.OWNER_INFO['whatsapp']}\nTG: {config.OWNER_INFO['telegram']}", parse_mode=ParseMode.HTML)
    elif query.data == "pair":
        context.user_data["waiting_pair"] = True
        await query.edit_message_text(config.PAIR_ASK, parse_mode=ParseMode.HTML)
    elif query.data == "back":
        kb = [[InlineKeyboardButton("💠 MENU 💠", callback_data="menu")], [InlineKeyboardButton("👑 OWNER", callback_data="owner"), InlineKeyboardButton("🔗 PAIR", callback_data="pair")]]
        await query.edit_message_text("Main Menu:", reply_markup=InlineKeyboardMarkup(kb))

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = str(update.effective_user.id)
    db = load_db()
    if context.user_data.get("waiting_pair"):
        number = update.message.text.strip()
        db["paired"][uid] = number
        save_db(db)
        msg = await update.message.reply_text("⏳ <b>Pairing...</b>", parse_mode=ParseMode.HTML)
        await asyncio.sleep(1.5)
        await msg.edit_text(config.PAIR_SUCCESS.format(number=number), parse_mode=ParseMode.HTML)
        await context.bot.send_message(chat_id=config.OWNER_ID, text=f"🔗 NEW PAIR!\n@{update.effective_user.username} - {number}")
        context.user_data["waiting_pair"] = False
        return
    if update.message.text.startswith("/"):
        await context.bot.send_message(chat_id=config.OWNER_ID, text=f"⚡ LOG: @{update.effective_user.username} Used {update.message.text} | Paired: {db['paired'].get(uid,'No')}")
        m = await update.message.reply_text(config.LOADING_TEXT, parse_mode=ParseMode.HTML)
        await asyncio.sleep(0.8)
        await m.edit_text(config.RUNNING_TEXT, parse_mode=ParseMode.HTML)
        await asyncio.sleep(1)
        await m.edit_text(config.SUCCESS_TEXT, parse_mode=ParseMode.HTML)

# NEW - Username එකෙන් Access දෙන Command
async def add_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != config.OWNER_ID: return
    try:
        identifier = context.args[0]  # Can be @username or ID
        plan = context.args[1]
        tool_key = context.args[2]

        db = load_db()
        
        target_id = identifier
        # If @username given, try to find ID
        if identifier.startswith("@"):
            uname = identifier.replace("@","").lower()
            if uname in db["users"]:
                target_id = db["users"][uname]
            else:
                # Save as pending username access
                db["allowed"][identifier] = {"plan": plan, "tool": tool_key}
                save_db(db)
                await update.message.reply_text(f"✅ Pending Access Saved for {identifier}. When @{uname} starts bot, auto access will work!")
                return
        elif not identifier.startswith("@") and not identifier.isdigit():
            # Username without @
            uname = identifier.lower()
            if uname in db["users"]:
                target_id = db["users"][uname]
            else:
                db["allowed"][f"@{identifier}"] = {"plan": plan, "tool": tool_key}
                save_db(db)
                await update.message.reply_text(f"✅ Pending Access Saved for @{identifier}. When he starts bot, auto access!")
                return

        db["allowed"][str(target_id)] = {"plan": plan, "tool": tool_key}
        # Also save username version
        if str(target_id) in db["users"]:
            db["allowed"][f"@{db['users'][str(target_id)]}"] = {"plan": plan, "tool": tool_key}
        
        save_db(db)
        tool_name = config.TOOLS_DATA[tool_key]["name"]
        features = config.TOOLS_DATA[tool_key]["features"]
        await update.message.reply_text(f"✅ Granted {identifier} ({target_id}) -> {plan} -> {tool_name}")
        try:
            await context.bot.send_message(chat_id=int(target_id), text=config.ACCESS_GRANTED_TEXT(update.effective_user.username, plan, tool_name, features), parse_mode=ParseMode.HTML)
        except:
            pass
    except Exception as e:
        await update.message.reply_text(f"Usage:\n/add @username 1Month tool_1\n/add 123456789 1Month tool_1\nError: {e}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("add", add_user))
    app.add_handler(CallbackQueryHandler(buttons))
    app.add_handler(MessageHandler(filters.TEXT, handle_text))
    print("BOT RUNNING - USERNAME ACCESS ENABLED")
    app.run_polling()

if __name__ == "__main__":
    main()
