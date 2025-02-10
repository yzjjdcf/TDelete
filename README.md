# TDelete - Telegram Account Cleaner

TDelete is a simple Telegram cleanup tool designed to delete conversations with deactivated users. It connects to Telegram via the provided API credentials and allows users to remove chats with deactivated accounts automatically. The tool also supports SOCKS5 proxies, making it suitable for use in restricted network environments.

For the Chinese version of this README, please refer to [README-zh.md](README-zh.md).

## Features
- Logs into your Telegram account using the provided API ID, API Hash, and phone number.
- Supports SOCKS5 proxy configuration for network flexibility.
- Automatically checks all dialogs and deletes those involving deactivated users.
- Displays a real-time log of actions in a scrolling text box for easy tracking.

## Installation and Usage

### 1. Download the Executable

- Download the latest `TDelete.exe` from the **Releases** section of this repository.
- No installation required! Simply download and run the `.exe` file.

### 2. Run the Program

1. Launch `TDelete.exe`.
2. The GUI will open. Enter the following details:
   - **API ID**: Your Telegram API ID.
   - **API Hash**: Your Telegram API Hash.
   - **Phone Number**: The phone number associated with your Telegram account.
   - **Proxy Address (optional)**: The SOCKS5 proxy address (if you're using a proxy).
   - **Proxy Port (optional)**: The SOCKS5 proxy port.

3. Once all fields are filled, click **"Start Cleaning"** to begin the cleanup process.
   - The tool will scan your Telegram dialogs and automatically delete conversations with deactivated users.
   - The progress and log information will be displayed in real-time in the GUI.

## Notes

- Please ensure that your Telegram account and provided API credentials are correct before running the program.
- If you encounter issues with the proxy connection, double-check your proxy settings.
- The program will scan all dialogs and remove conversations with deactivated users. This operation is irreversible, so please use it carefully.

## License

This project is licensed under the [MIT License](LICENSE).
