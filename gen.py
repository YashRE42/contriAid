from sh import git
import pprint
import subprocess
import re
import curses
# subprocess.run(["cd", "../zulip/"])
# subprocess.run(["cd", "../"])
commitReg = re.compile(r'(commit \S{40})')
cmd = "git clone"
url = "https://github.com/zulip/zulip.git"
cmd = cmd + " " + url
subprocess.run(cmd.split(" "))

cmd = "git --no-pager log"
repo = "zulip"

process = subprocess.Popen(cmd.split(" "), cwd=("../"+repo), stdout=subprocess.PIPE)
stdout = process.communicate()[0]
commitSHAs = commitReg.findall(str(stdout))
pprint.pprint(len(commitReg.findall(str(stdout))))
# print("stdout:{}".format(stdout))
# log = subprocess.check_output(('grep', 'process_name'), stdin=log_pipe.stdout)
length = 0
import os
if not os.path.exists('workbase'):
    os.makedirs('workbase')
for SHA in commitSHAs:
    length = length + 1
    with open("./workbase/" + str(length) + ".txt",'w',encoding = 'utf-8') as f:
        cmd = "git show " + SHA[7::]
        repo = "zulip"
        process = subprocess.Popen(cmd.split(" "), cwd=("../"+repo), stdout=subprocess.PIPE)
        stdout = process.communicate()[0]
        try:
            f.write(stdout.decode('UTF-8'))
        except Exception as e:
            print("\nsomething broke here\n")
            pass