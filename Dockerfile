from debian

run apt update
run apt install -y git python3 python3-venv

entrypoint git clone https://github.com/Nordick-24/Telegram-Transalte.git; export TELEGRAM_key="paste token here"; cd Telegram-Transalte; bash install.sh

