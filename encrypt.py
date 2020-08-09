import os,sys,time
import compileall

def jalan(z):
    for e in z +'\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(00000.01)


os.system('clear')
jalan("\033[1;36m#*"*22)
print ("\033[1;32mAuthor    \033[1;31m:\033[1;33m Hydra NET")
time.sleep(0.3)
print ("\033[1;32mGithub    \033[1;31m:\033[1;33m hydra20")
time.sleep(0.3)
print ("\033[1;32mInstagram \033[1;31m:\033[1;33m hydranet2020")
time.sleep(0.3)
jalan("\033[1;36m#*"*22)
print ("")
tool_list = str(raw_input(" \033[1;36mType the path for the tool: "))
compileall.compile_file(tool_list)
jalan('\033[31;1mEncryption successful')
jalan("\033[1;31mSubscribe \033[1;37mto my channel to learn more")
time.sleep(0.7)
os.system('xdg-open https://www.youtube.com/c/hydranet2')
