from aiogram import types, Bot


async def set_default_commands(bot: Bot):
    await bot.set_my_default_administrator_rights(
        types.ChatAdministratorRights(
            can_delete_messages=True,
            can_edit_messages=True,
            can_invite_users=True,
            can_restrict_members=True,
            can_post_messages=True,
            can_manage_chat=True,
            is_anonymous=False,
            can_delete_stories=False,
            can_edit_stories=False,
            can_post_stories=False,
            can_change_info=False,
            can_promote_members=False,
            can_manage_video_chats=False,
            can_manage_topics=False,
            can_pin_messages=True,
        )
    )
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Botni ishga tushurish"),
            types.BotCommand(command="help", description="Yordam"),
        ]
    )
