FROM registry.gitlab.com/william.dev.env/co_bot/co-bot-spanish
MAINTAINER William Galindez Arias

#RUN service postgresql start
RUN chmod +x home/ChatBotProject/co_bot/rasa_services.sh
RUN . home/venvBot/botEnv/bin/activate
#CMD source home/venvBot/botEnv/bin/activate && cd home/ChatBotProject/co_bot && rasa_services.sh
#CMD cd home/ChatBotProject/co_bot && rasa_services.sh 
CMD . home/venvBot/botEnv/bin/activate && service postgresql start && cd home/ChatBotProject/co_bot && ./rasa_services.sh


#CMD service postgresql start && source home/venvBot/botEnv/bin/activate && cd home/ChatBotProject/co_bot

#RUN chmod +x home/ChatBotProject/co_bot/rasa_services.sh
#ENTRYPOINT []
#CMD rasa_services.sh
