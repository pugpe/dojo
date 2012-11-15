# coding: utf-8
# problem

def jogo(jogador1, jogador2):

    jogadores = ((jogador1, jogador2), 
        (jogador2, jogador1))
    ret = "Uhhhh" 


    if ('lagarto', 'spock') in jogadores:
        ret = 'lagarto envenena spock'

    elif ('pedra', 'tesoura') in jogadores:
        ret = 'pedra esmaga tesoura'

    elif ('pedra', 'lagarto') in jogadores: 
        ret = 'pedra esmaga lagarto' 

    elif ('tesoura', 'papel') in jogadores:
        ret = 'tesoura corta papel'

    elif ('spock', 'tesoura') in jogadores:
        ret = 'spock esmaga tesoura'
    
    elif ('spock', 'pedra') in jogadores:
        ret = 'spock vaporiza pedra'

    elif ('lagarto', 'papel') in jogadores:
        ret = 'lagarto come papel'

    return ret



  

    # if (jogador1 == 'pedra' 
    #     and jogador2 == 'tesoura'):
    #     return 'pedra esmaga tesoura'
    # elif (jogador1 == 'pedra'
    #     and jogador2 == 'lagarto'):
    #     return 'pedra esmaga lagarto'
    # elif (jogador1 == 'lagarto'
    #     and jogador2 == 'spock'):
    #     return 'lagarto envenena spock'
    # else:
    #     return 'Uhhhh'