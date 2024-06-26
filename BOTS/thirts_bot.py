class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    # Class will check whether the user is admin or creator in group or not
    key='is_admin'
    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']

# To register filter, you need to use method add_custom_filter.
bot.add_custom_filter(IsAdmin())

# Now, you can use it in handler.
@bot.message_handler(is_admin=True)
def admin_of_group(message):
	bot.send_message(message.chat.id, 'You are admin of this group!')
