# ================= EDIT HERE =================
OWNER_ID = 6528091494  # @userinfobot ගෙන් ගන්න ID එක
OWNER_INFO = {
    "whatsapp": "94741895740",
    "telegram": "@ROMEOLDALPHA"
}

# Premium නැති කෙනෙක්ට යන Message එක
NO_ACCESS_MESSAGE = """
╔══════════════════════════╗
   ⚠️  ACCESS DENIED  ⚠️
╚══════════════════════════╝

🔒 <b>You Don't Have Premium Access!</b>

💎 <b>Buy Premium to Unlock All Tools</b>

🛠️ <b>ALL TOOLS PRICING</b> 🛠️
━━━━━━━━━━━━━━━━━━━━
<b>TOOL 1:</b> 1M-2000 | 3M-5000 | 6M-10000 | 1Y-16000 | Lifetime-25000
<b>TOOL 2:</b> 1M-2000 | 3M-5000 | 6M-10000 | 1Y-16000 | Lifetime-25000
<b>TOOL 3:</b> 1M-3000 | 3M-6000 | 6M-12000 | 1Y-18000 | Lifetime-30000
<b>TOOL 4:</b> 1M-2500 | 3M-5500 | 6M-11000 | 1Y-17000 | Lifetime-28000
<b>TOOL 5:</b> 1M-4000 | 3M-7000 | 6M-13000 | 1Y-20000 | Lifetime-35000
<b>TOOL 6 [PRO]:</b> 1M-20000 | 3M-22000 | 6M-25000 | 1Y-36000 | Lifetime-40000
━━━━━━━━━━━━━━━━━━━━

📩 <b>Contact Owner to Buy</b>
"""

def ACCESS_GRANTED_TEXT(username, plan, tool_name, features):
    return f"""
╔══════════════════════════╗
   ✅ ACCESS GRANTED ✅
╚══════════════════════════╝

👤 <b>User:</b> @{username}
⏳ <b>Plan:</b> {plan}
🛠️ <b>Tool:</b> {tool_name}

🔓 <b>Unlocked Features:</b>
{features}

💠 Type /start to Begin
"""

# ================ TOOLS EDIT HERE ================
# Tool Name, Features, Commands ඔයාට ඕන විදියට වෙනස් කරන්න
TOOLS_DATA = {
    "tool_1": {"HIJACK": "🔥 TOOL 1 - BASIC", "features": "• ⚡ Super Fast Whatsapp Group Hijack\n• 🔧 6 Commands\n• 🎧 24/7 Support\n• 💎 Lifetime Updates", "commands": "💠 <b>TOOl - COMMANDS</b> 💠\n\n🔹 /t1cmd1 - Small Group\n🔹 /tdrzoo - Medium Group\n🔹 /tha - Fast Search\n🔹 /shsh - Bypass Number\n🔹 /metaowa - Destroy\n🔹 /help - Help"},
    "tool_2": {"BUG": "💎 TOOL 2 - STANDARD", "features": "• Victims Crasher\n• 6 Pro Commands\n• Fast Server", "commands": "💠 <b>TOOL 2 - COMMANDS</b> 💠\n\n🔹 /cw\n🔹 /clonecw\n🔹 /bigbossbahirawa\n🔹 /senasuru\n🔹 /Eskoder\n🔹 /Metlsl"},
    "tool_3": {"DELAY": "⚡ TOOL 3 - ADVANCED", "features": "• Slow Down Or Delay Bugs\n• 6 Commands", "commands": "💠 <b>TOOL 3 - COMMANDS</b> 💠\n\n🔹 /frese\n🔹 /frese2\n🔹 /frezewa\n🔹 /freze2\n🔹 /amtomphisher\n🔹 /kileertel"},
    "tool_4": {"CRASH": "🚀 TOOL 4 - ULTRA", "features": "• Ultra Speed Whatsapp Crasher\n• 6 Commands", "commands": "💠 <b>TOOL 4 - COMMANDS</b> 💠\n\n🔹 /t4cmd1\n🔹 /t4cmd2\n🔹 /t4cmd3\n🔹 /t4cmd4\n🔹 /t4cmd5\n🔹 /t4cmd6"},
    "tool_5": {"BAND": "👑 TOOL 5 - KING", "features": "• Remove Any Whatsapp Account In 2 Minutes\n• 6 Commands", "commands": "💠 <b>TOOL 5 - COMMANDS</b> 💠\n\n🔹 /t5cmd1\n🔹 /t5cmd2\n🔹 /t5cmd3\n🔹 /t5cmd4\n🔹 /t5cmd5\n🔹 /t5cmd6"},
    "tool_6": {"ALL IN ONE": "💥 TOOL 6 - PRO MAX [10]", "features": "• 🔥 PRO MAX - 6 Tools - 500+ Commands\n• 👑 All Features Unlocked\n• ⚡ No Limits", "commands": "💠 <b>TOOL 6 - PRO MAX [10]</b> 💠\n\n🔹 /t6cmd1 - Ultimate Tool 1\n🔹 /t6cmd2 - Ultimate Tool 2\n🔹 /t6cmd3 - Ultimate Tool 3\n🔹 /t6cmd4 - Ultimate Tool 4\n🔹 /t6cmd5 - Ultimate Tool 5\n🔹 /t6cmd6 - Ultimate Tool 6\n🔹 /t6cmd7 - Ultimate Tool 7\n🔹 /t6cmd8 - Ultimate Tool 8\n🔹 /t6cmd9 - Ultimate Tool 9\n🔹 /t6cmd10 - Ultimate Tool 10"},
}

# Animation Texts - ඔයාට වෙනස් කරන්න පුලුවන්
LOADING_TEXT = "⏳ <b>Loading...</b>"
SUCCESS_TEXT = "✅ <b>Successfully Sent!</b>\n\n⚡ <b>Check Inbox</b>"
PAIR_ASK = "🔗 <b>PAIR SYSTEM</b>\n\n📱 <b>Send Your Number With Country Code</b>\n\nEx: <code>94746262683</code>"
PAIR_SUCCESS = "✅ <b>Successfully Paired!</b>\n\n📱 Number: <code>{number}</code>\n🔒 Secured"
