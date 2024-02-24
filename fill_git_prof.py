import os
import subprocess
import argparse
from datetime import datetime
from itertools import cycle
import glob

def list_files(project_loc):
    # files = glob.glob(project_loc+"/**/*")
    files = glob.glob("**/*", recursive=True)
    return files


def generate_date_till_today(start_date):
    start_date = datetime.strptime(start_date, "%d-%m-%Y").date()
    end_date = datetime.now().date()
    dates_lst = [d for d in range((end_date-start_date).days+1)]
    return dates_lst

def git_commit(file, day):
    print(file)
    commnd1 = f'git add {file}'
    commnd2 = f'git commit --date "{day} day ago" --message "committed file {file}" --allow-empty'
    subprocess.run(commnd1, shell=True)
    subprocess.run(commnd2, shell=True)    
    return

if __name__== "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-r", "--repo", help="path of repo")
    parser.add_argument("-d", "--date", help="start date for operation",\
                        default=datetime.today().strftime('%d-%m-%Y'))
    args=vars(parser.parse_args())
    project_loc=args['repo']
    os.chdir(project_loc)
    print(os.getcwd())
    start_date=args['date']
    date_lst=generate_date_till_today(start_date)
    files=list_files(project_loc)
    max_len = max(len(date_lst), len(files))
    cycler_l1=cycle(date_lst)
    cycler_l2=cycle(files)
    res_list = [(i, next(cycler_l1), next(cycler_l2)) for i in range(max_len)]

    for i,day_ptr, file in res_list:
        print(f"[{i}]: uploading file {file} {day_ptr} days ago")
        git_commit(file, day_ptr)


