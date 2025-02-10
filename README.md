# TDelete

For the Chinese version of this README, click [中文版本](./README-zh.md).

**TDelete** is a simple Telegram utility that helps users clean up their Telegram chats by automatically deleting conversations with deleted or inactive users.

## Features
- Automatically deletes conversations with deleted Telegram users.
- Can be used with a SOCKS5 proxy for privacy and security.

## How to Use

1. **Run `TDelete.exe`**: Launch the program by running the `TDelete.exe` file.

2. **Enter the Required Information**: A window will pop up, prompting you to input the following details:
   - **API ID**: Your Telegram API ID (explained below).
   - **API Hash**: Your Telegram API Hash (explained below).
   - **Phone Number**: The phone number associated with your Telegram account.
   - **Proxy Address (Optional)**: If you're using a proxy, enter the SOCKS5 proxy address.
   - **Proxy Port (Optional)**: Enter the SOCKS5 proxy port number.

3. **Start the Cleaning Process**: After filling in all the fields, click the **"Start Cleaning"** button.
   - The tool will scan your Telegram chats and automatically delete conversations with deleted users.
   - Progress and log information will be displayed in real-time within the interface.

## Getting API ID and API Hash

Before using this program, you need to obtain your **API ID** and **API Hash** from Telegram's developer platform. Here are the steps:

1. Visit [Telegram Developer Platform](https://my.telegram.org/auth).
2. Log in with your Telegram account.
3. Click on **API Development Tools**, then click **Create New Application**.
4. Fill in the application name and description, then click **Create application**.
5. After successful creation, you will be provided with your **API ID** and **API Hash**. Copy these and enter them into the program.

## Proxy Settings (Optional)

If you wish to use a **SOCKS5 proxy** for privacy, you can enter your proxy details in the respective fields in the application.

- **Proxy Address**: Enter the address of your SOCKS5 proxy server (e.g., `127.0.0.1`).
- **Proxy Port**: Enter the proxy server port number (e.g., `10808`).

## License

TDelete is open-source and available under the MIT License. Feel free to fork or contribute to the project!
