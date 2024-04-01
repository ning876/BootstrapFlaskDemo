import os
import yaml
from dotenv import load_dotenv
import logging
from datetime import datetime
load_dotenv()

env=os.environ.get('env','local')
basedir=os.environ.get('basedir',os.path.abspath(os.path.dirname(__file__)))

def get_container_id():
    try:
        cmd='cat /proc/self/cgroup'
        output=os.popen(cmd)
        resets=output.readlines()
        container_message=resets[-1]
        container_id=container_message.strip().split('/')[-1][:8]
    except Exception as e:
        import traceback
        print('Fail to get container id')
        traceback.print_exc()
        container_id='Local-ID'
    return container_id

CONTAINER_ID=get_container_id()

LOG_Name="test-program-%s-%s.log"
LOG_FILE_NAME=LOG_Name % (CONTAINER_ID,datetime.strftime(datetime.now(),'%Y-%m-%d'))
LOG_DIR=os.path.join(os.getenv('basedir',basedir),os.getenv('log_dir','log'))

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

cfg_path=os.path.join(basedir,'cfg','config.yaml')
cfg=yaml.load(open(cfg_path,'r'),Loader=yaml.FullLoader)





