from conf import setting


class BasePlugin(object):
    def __init__(self, host_name=''):
        self.mode_list = ['agent', 'salt', 'ssh']
        # if hasattr(setting, 'MODE'):
        #     self.mode = setting.MODE
        # else:
        #     self.mode = 'agent'
        self.mode = setting.MODE if hasattr(setting, 'MODE') else 'agent'
        self.host_name = host_name

    def salt(self, cmd):
        import salt.client
        local = salt.client.LocalClient()
        result = local.cmd(self.host_name, 'cmd.run', [cmd])
        return result[self.host_name]

    def agent(self, cmd):
        import subprocess
        output = subprocess.getoutput(cmd)
        return output

    def execute(self):
        return self.linux()

    def linux(self):
        raise Exception('You must complete linux method.')
