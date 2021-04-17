RconDiscordBot
==============
在discord輸入指令傳送到mc server終端  
Example:  
![image](https://cdn.discordapp.com/attachments/800020585286860800/832956985644417054/unknown.png)  
  
配置:
-------

1.  打開server.properties  
    * enable-rcon=true
    * rcon_port = `你的port`  
    * rcon_password = `你的密碼`  

2.  運行一次RconDiscordBot.py 生成設定檔  
3.  打開RconDiscordBot_config.json:
    * `TOKEN` = Bot's token  
    * `PREFIX` = 指令前綴  
    * `IP` = server ip  
    * `rcon_pw` = rcon_password    
    * `rcon_port` = rcon_port  
    * `server_path` = 伺服器啟動檔路徑 ex: D:\server\start.bat  
    * `console_channel` = Discord頻道ID  

使用方式:  
--------
運行RconDiscordBot.py同時會自動嘗試啟動伺服器   
`--start`: 啟動伺服器，若伺服器正在運行則顯示已在線  
`--加上任意指令`: 將指令直接傳送到伺服器終端，並返回結果  
Ex: 
  ```bash
  --whitelist Steve  
  ```
  ```bash
  --op Steve  
  ```
  ```bash
  --time set day
  ```
