FROM debian:buster

RUN apt-get update
RUN echo "Installing Python 3 [...]"
RUN apt-get install python3 -y
RUN echo "Installing Pip3 [...]"
RUN apt-get install python3-pip -y
RUN echo "Install Telegram-Bot API [...]"
RUN pip3 install pyTelegramBotAPI
RUN pip3 install pyyaml
RUN pip3 install argparse
ADD src/ /
#ENTRYPOINT nohup python3 /bot.py -d &
RUN chmod +x /start_bot.sh
ENTRYPOINT bash -c "/start_bot.sh &" && sleep 4 && tail -F /dev/null
