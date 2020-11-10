from pid import PidFile
from config import *
from handlers import *
from mailru_im_async_bot.bot import Bot
from mailru_im_async_bot.filter import Filter
from mailru_im_async_bot.handler import MessageHandler, BotButtonCommandHandler


bot = Bot(
    token=TOKEN, version=VERSION, name=NAME, poll_time_s=POLL_TIMEOUT_S, request_timeout_s=REQUEST_TIMEOUT_S,
    task_max_len=TASK_MAX_LEN, task_timeout_s=TASK_TIMEOUT_S
)

# Register your handlers here
# ---------------------------------------------------------------------

bot.dispatcher.add_handler(BotButtonCommandHandler(
                            callback=subscription,
                            filters=Filter.callback_data('subscription')
                        )
                    )
bot.dispatcher.add_handler(BotButtonCommandHandler(
                            callback=formal_reply,
                            filters=Filter.callback_data('formal_reply')
                        )
                    )
bot.dispatcher.add_handler(BotButtonCommandHandler(
                            callback=rand_photo,
                            filters=Filter.callback_data('rand_photo')
                        )
                    )
bot.dispatcher.add_handler(BotButtonCommandHandler(
                            callback=start,
                            filters=Filter.callback_data('main')
                        )
                    )
bot.dispatcher.add_handler(MessageHandler(
        callback=start
    )
)


with PidFile(NAME):
    try:
        loop.create_task(send_subscription(bot))
        loop.create_task(bot.start_polling())
        loop.run_forever()
    except KeyboardInterrupt:
        loop.create_task(bot.stop_polling())
        loop.close()
    finally:
        loop.close()
