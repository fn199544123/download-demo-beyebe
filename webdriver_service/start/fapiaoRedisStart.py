import sys
sys.path.append("/")
from webdriver_service.factory.fapiaoImpl import fapiaoImpl
from webdriver_service.pipeline.redisPipe import getMission

if __name__ == '__main__':
    redisKey = 'lst_fapiao'
    # 2
    fpdm = "4403181130"
    fphm = "27671246"
    kprq = "20180920"
    kjje = "351.69"
    while True:
        getMission(redisKey, fapiaoImpl, 5)
