class Context(object):
    pass

def init(context):
    context.s2 = "000001.XSHE"
    context.stocks = [context.s2]
    context.init_cash = 10000

if __name__=='__main__':
    context = Context()
    init(context)
    print context.__dict__
