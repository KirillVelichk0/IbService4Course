from prime_numbers import generate_prime_numbers
from RSA import Rsa


def CreateShadowedVote(userVote: int, minShadowNum: int, openKey: tuple) -> int:
    shadowNum = 0
    while shadowNum < minShadowNum:
        shadowNum = generate_prime_numbers(256)
        print(shadowNum)
    shadowedVote = userVote * shadowNum
    return pow(shadowedVote, int(openKey[0]), int(openKey[1]))


def ExtractRealVotes(shadowedVotes: list, closeKey: tuple) -> list:
    svm = 1
    for vote in shadowedVotes:
        svm = svm * int(vote)
    deciphered = pow(svm, int(closeKey[0]), int(closeKey[1]))
    result = [0, 0, 0]  # votes count
    while deciphered % 2 == 0:
        deciphered = deciphered // 2
        result[1] = result[1] + 1
    while deciphered % 3 == 0:
        deciphered = deciphered // 3
        result[2] = result[2] + 1
    result[0] = len(shadowedVotes) - result[1] - result[2]
    return result
