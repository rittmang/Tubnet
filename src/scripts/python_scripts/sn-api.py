from subnetting import do_stuff
import traceback
import sys
import zerorpc
#lasters=[]
class SNApi(object):
    def calc(self, s, u):
        """based on the input text, return the int result"""
        try:
            starters, enders = do_stuff(s,u)#use s,u,mode=1 and 2?
            starters.append('+')
            starters.append(enders)
            return starters
        except Exception as e:
            #print(traceback.format_exc())
            return traceback.format_exc()
    def echo(self, text):
        """echo any text"""
        return text

def parse_port():
    port = 4242
    try:
        port = int(sys.argv[1])
    except Exception as e:
        pass
    return '{}'.format(port)

def main():
    addr = 'tcp://127.0.0.1:' + parse_port()
    s = zerorpc.Server(SNApi())
    s.bind(addr)
    print('start running on {}'.format(addr))
    s.run()

if __name__ == '__main__':
    main()