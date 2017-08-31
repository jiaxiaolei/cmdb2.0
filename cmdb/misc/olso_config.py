# -*- coding:utf-8 -*-

from tornado.options import parse_command_line

class ConfigOpts(object):  
  
    def __call__(self, ...):  
  
        opts = [  
            MultiStrOpt('config-file',  
                    ...),  
            StrOpt('config-dir',  
                   ...),  
        ]  
  
        self.register_cli_opts(opts)  


def main():
    pass

if __name__ == '__main__':
    parse_command_line()
   
    main()

