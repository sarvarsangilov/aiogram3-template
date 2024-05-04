import environs

env = environs.Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list('ADMINS')
IP = env.str('IP')
