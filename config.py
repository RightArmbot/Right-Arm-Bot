OWNER_ID = 123456789
OWNER_INFO = {"whatsapp": "94741895740", "telegram": "@ROMEOLDALPHA"}

NO_ACCESS_MESSAGE = """
╔══════════════════════╗
  ⚠️ ACCESS DENIED ⚠️
╚══════════════════════╝

🔒 You Don't Have Premium Access!

💎 Buy Premium to Unlock

🛠️ ALL TOOLS PRICING 🛠️
TOOL 1: 1M-2000 | 3M-5000 | 6M-10000 | 1Y-16000 | Lifetime-25000
TOOL 2: 1M-2000 | 3M-5000 | 6M-10000 | 1Y-16000 | Lifetime-25000
TOOL 3: 1M-3000 | 3M-6000 | 6M-12000 | 1Y-18000 | Lifetime-30000
TOOL 4: 1M-2500 | 3M-5500 | 6M-11000 | 1Y-17000 | Lifetime-28000
TOOL 5: 1M-4000 | 3M-7000 | 6M-13000 | 1Y-20000 | Lifetime-35000
TOOL 6 [PRO]: 1M-5000 | 3M-9000 | 6M-15000 | 1Y-25000 | Lifetime-40000

📩 Contact Owner
"""

def ACCESS_GRANTED_TEXT(username, plan, tool_name, features):
    return f"✅ ACCESS GRANTED ✅\n\n👤 User: @{username}\n⏳ Plan: {plan}\n🛠️ Tool: {tool_name}\n\n🔓 Features:\n{features}\n\nType /start"

TOOLS_DATA = {
    "tool_1": {"name": "🔥 TOOL 1 - BASIC", "features": "• Fast\n• 6 Commands\n• Support", "commands": "💠 TOOL 1 - 6 COMMANDS 💠\n\n🔹 /t1cmd1\n🔹 /t1cmd2\n🔹 /t1cmd3\n🔹 /t1cmd4\n🔹 /t1cmd5\n🔹 /t1cmd6"},
    "tool_2": {"name": "💎 TOOL 2", "features": "• Standard\n• 6 Commands", "commands": "💠 TOOL 2 - 6 COMMANDS 💠\n\n🔹 /t2cmd1\n🔹 /t2cmd2\n🔹 /t2cmd3\n🔹 /t2cmd4\n🔹 /t2cmd5\n🔹 /t2cmd6"},
    "tool_3": {"name": "⚡ TOOL 3", "features": "• Advanced\n• 6 Commands", "commands": "💠 TOOL 3 - 6 COMMANDS 💠\n\n🔹 /t3cmd1\n🔹 /t3cmd2\n🔹 /t3cmd3\n🔹 /t3cmd4\n🔹 /t3cmd5\n🔹 /t3cmd6"},
    "tool_4": {"name": "🚀 TOOL 4", "features": "• Ultra\n• 6 Commands", "commands": "💠 TOOL 4 - 6 COMMANDS 💠\n\n🔹 /t4cmd1\n🔹 /t4cmd2\n🔹 /t4cmd3\n🔹 /t4cmd4\n🔹 /t4cmd5\n🔹 /t4cmd6"},
    "tool_5": {"name": "👑 TOOL 5", "features": "• King\n• 6 Commands", "commands": "💠 TOOL 5 - 6 COMMANDS 💠\n\n🔹 /t5cmd1\n🔹 /t5cmd2\n🔹 /t5cmd3\n🔹 /t5cmd4\n🔹 /t5cmd5\n🔹 /t5cmd6"},
    "tool_6": {"name": "💥 TOOL 6 - PRO MAX [10]", "features": "• Pro Max\n• 10 Commands", "commands": "💠 TOOL 6 - 10 COMMANDS 💠\n\n🔹 /t6cmd1\n🔹 /t6cmd2\n🔹 /t6cmd3\n🔹 /t6cmd4\n🔹 /t6cmd5\n🔹 /t6cmd6\n🔹 /t6cmd7\n🔹 /t6cmd8\n🔹 /t6cmd9\n🔹 /t6cmd10"},
}

LOADING_TEXT = "⏳ <b>Loading...</b>"
RUNNING_TEXT = "⚡ <b>▓░░░░ 20%", "▓▓▓░░ 60%", "▓▓▓▓▓ 100% </b>"
SUCCESS_TEXT = "✅ <b>Successfully Sent!</b>"

PAIR_ASK = "🔗 <b>PAIR SYSTEM</b>\n\n📱 Send Country Code + Number\nEx: 94741895740"
PAIR_SUCCESS = "✅ <b>Paired!</b> Number: {number}"