Launch an EC2 instance in the AWS console

Name your instance 

select you Application and OS Images (Amazon Machine Image)

UBUNTU Imaga
64-bit (x86)

Instance Type: t3.micro

Key Pair - select existing or create. this is what allows you to connect remotely to your server

For the rest of initial config I recommend you check this video tutorial out

Connect to instance using SSH. 

Install zsh and ohmyzsh follow here -: https://vitux.com/ubuntu-zsh-shell/

1. sudo apt update && sudo apt dist-upgrade -y
2. sudo apt install build-essential curl file git
3. sudo apt install zsh
4. sudo apt install git-core curl fonts-powerline
5. sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

More configuration go to : sudo nano ~/.zshrc

install git
sudo apt-get update
sudo apt-get install git-all

Install BREW
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

clone repo 
git clone https://github.com/manuel-candelaria/ai_tool_search.git

isntall python - If not installed
check version: python3 --version
 install pip:
 sudo apt install python3-pip


install dependencies
Google and find best way to install







