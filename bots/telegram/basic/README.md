# Telegram Bot POC

This project is a proof of concept for a Telegram bot implemented in Python 3 using a virtual environment (venv).

## Installation

1. Clone the repository:

    ```shell
    git clone https://github.com/your-username/poc.git
    cd /bot/telegram/basic/
    ```

2. Create and activate a virtual environment:

    ```shell
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:

    ```shell
    pip install -r requirements.txt
    ```

## Usage

To run the Telegram bot, execute the following command:


```mermaid
graph LR

Start --> Initialize_Bot
Initialize_Bot --> Register_Command_Handlers
Initialize_Bot --> Register_Message_Handler
Register_Command_Handlers --> Handle_Start_Command
Register_Message_Handler --> Handle_Text_Message
Handle_Start_Command --> Send_Greeting_Message
Handle_Text_Message --> Echo_Text_Back
Send_Greeting_Message --> End
Echo_Text_Back --> End
End --> Poll_For_Messages
Poll_For_Messages --> Handle_Command_or_Message
Handle_Command_or_Message --> Handle_Start_Command
Handle_Command_or_Message --> Handle_Text_Message
Handle_Start_Command --> Send_Greeting_Message
Handle_Text_Message --> Echo_Text_Back

```