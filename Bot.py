from telegram.ext import Updater, MessageHandler,CommandHandler, Filters
from telegram import ChatAction

def ReadData():
    f = open("task_list.txt",'r')
    list = f.readlines()
    for i in range(0,len(list)):
        list[i]=list[i].replace("\n","")
    f.close()
    return list
def SaveToFile(list):
    f= open("task_list.txt",'w')
    for task in list:
        f.write(task + "\n")
    f.close()

def message(bot,update):
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    update.message.reply_text("I'm sorry, i understand only commands!")

def showTasks(bot, update):
    list=ReadData()
    bot.sendChatAction(update.message.chat_id, ChatAction.TYPING)
    if len(list)== 0:
        update.message.reply_text("Nothing to do here!")
    else:
        update.message.reply_text(list)

def newTask(bot,update,args):
    list=ReadData()
    arg=' '.join(args)
    list.append(arg)
    SaveToFile(list)

def removeTask(bot,update,args):
    list=ReadData()
    arg=' '.join(args)
    if arg in list:
        list.remove(arg)
        SaveToFile(list)
    else:
        update.message.reply_text("Nothing to do here!")


def removeAllTasks(bot,update,args):
    list=ReadData()
    arg = ' '.join(args)
    for object in list:
        if arg in object:
            list.remove(object)
    SaveToFile(list)


def main():
    updater = Updater("555762929:AAE7ZLNOkRtF_OjGwAPOKTEizhQRG-iFK18")
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text,message))

    dp.add_handler(CommandHandler("showTasks", showTasks))
    dp.add_handler(CommandHandler("newTask", newTask,pass_args=True))
    dp.add_handler(CommandHandler("removeTask", removeTask,pass_args=True))
    dp.add_handler(CommandHandler("removeAllTasks", removeAllTasks,pass_args=True))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()