# TDelete

**TDelete** 是一个简单的 Telegram 工具，帮助用户自动删除与已注销或非活跃用户的对话，便于管理 Telegram 聊天记录。

## 功能
- 自动删除与已注销 Telegram 用户的对话。
- 可以使用 SOCKS5 代理进行隐私保护和安全性提升。

## 使用方法

1. **运行 `TDelete.exe`**：启动程序，运行 `TDelete.exe` 文件。

2. **输入必要信息**：界面弹出后，请输入以下信息：
   - **API ID**：你的 Telegram API ID（后续步骤将说明如何获取）。
   - **API Hash**：你的 Telegram API Hash（后续步骤将说明如何获取）。
   - **手机号**：你 Telegram 账户绑定的手机号。
   - **代理地址（可选）**：如果使用代理，请输入 SOCKS5 代理地址。
   - **代理端口（可选）**：输入 SOCKS5 代理端口。

3. **开始清理**：填写完所有字段后，点击 **"开始清理"** 按钮开始清理过程。
   - 工具会扫描你的 Telegram 对话，并自动删除与已注销用户的对话。
   - 进度和日志信息将实时显示在界面中。

## 获取 API ID 和 API Hash

在使用本程序之前，你需要从 Telegram 的开发者平台获取 **API ID** 和 **API Hash**。以下是获取步骤：

1. 访问 [Telegram 开发者平台](https://my.telegram.org/auth)。
2. 使用你的 Telegram 账户登录。
3. 点击 **API Development Tools**，然后点击 **Create New Application**（创建新应用）。
4. 填写应用名称和描述，点击 **Create application**（创建应用）。
5. 成功创建后，你会看到 **API ID** 和 **API Hash**。将它们复制到程序中。

## 代理设置（可选）

如果你想通过 **SOCKS5 代理** 使用本程序，可以在程序中输入你的代理信息。

- **代理地址**：输入 SOCKS5 代理服务器地址（例如 `127.0.0.1`）。
- **代理端口**：输入 SOCKS5 代理端口号（例如 `10808`）。

## 许可证

TDelete 是开源项目，采用 MIT 许可证。欢迎 Fork 或贡献代码！
