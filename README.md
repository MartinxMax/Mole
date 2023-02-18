  <div align="center">
 <img src="https://readme-typing-svg.herokuapp.com/?lines=Reverse_SHELL_connection_and_automatic_;webpage_backdoor_triggering---@Мартин.&font=Roboto" />
 <p align="center">
 <img title="Mole" src='https://img.shields.io/badge/Mole-1.0.0-brightgreen.svg' />
 <img title="Mole" src='https://img.shields.io/badge/LD_PRLOAD-Tool'/>
 <img title="Mole" src='https://img.shields.io/badge/Python-3.9-yellow.svg' />
  <img title="Mole" src='https://img.shields.io/badge/HackerTool-x' />
 <img title="Mole" src='https://img.shields.io/static/v1?label=Author&message=@Martin&color=red'/>
 <img title="Mole" src='https://img.shields.io/badge/-Linux-F16061?logo=linux&logoColor=000'/>
 </p>
  
 
  <img height="137px" src="https://github-readme-stats.vercel.app/api?username=MartinXMax&hide_title=true&hide_border=true&show_icons=trueline_height=21&text_color=000&icon_color=000&bg_color=0,ea6161,ffc64d,fffc4d,52fa5a&theme=graywhite" />
  
   
 <table>
  <tr>
      <th>Function</th>
  </tr>
  <tr>
    <th>LD_ PRLAOD function hijacking (Web hijacking)</th>
  </tr>
  <tr>
    <th>LD_ PRLAOD function hijacking (EXE executable hijacking)</th>
  </tr>
 </table>
</div>

## usage method

 * View help information

      ```#python3 Mole.py -h```

  ![图片名称](./PT/help.png)  
  
## Web remote command execution

1.Connect to the server,Because Flag is invisible to us, we need to bypass permission reading

![图片名称](./PT/readflag.png)  
![图片名称](./PT/empty.png)  

2.Upload a file to read Flag beyond authority

![图片名称](./PT/upload.png)  

3.After accessing the php page, our Flag is generated in the tmp directory

![图片名称](./PT/GetFlag.png)  

## Executable reverse shell

1.Generate malicious shared libraries
![图片名称](./PT/Create_SO.png)  
Complete the reverse connection IP and port

2.Compile the c file

``gcc Main.c -o Main``

_You can use the example in the ```Main.c``` file. This time the Printf function is hijacked. If you need to hijack other functions, please modify the code in ```Hijacking-source.c```_


![图片名称](./PT/Create_GCC_Main.png)  


3.Send the following files to the target: ```Loading.sh``` ```Main``` ```Hijacking-OutputNew.so```


_When the user runs ```. ./Loading.sh ```automatically loads the code. We can see that the printf function is hijacked and a reverse shell is opened_

![图片名称](./PT/RunMain.png)  
![图片名称](./PT/Getshell.png)  


